import re
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import Widget, Select, MultiWidget
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.forms.fields import EMPTY_VALUES

__all__ = ('SelectTimeWidget', 'SplitSelectDateTimeWidget')

# Attempt to match many time formats:
# Example: "12:34:56 P.M."  matches:
# ('12', '34', ':56', '56', 'P.M.', 'P', '.', 'M', '.')
# ('12', '34', ':56', '56', 'P.M.')
# Note that the colon ":" before seconds is optional, but only if seconds are omitted
time_pattern = r'(\d\d?):(\d\d)(:(\d\d))? *([aApP]\.?[mM]\.?)?$'

RE_TIME = re.compile(time_pattern)
# The following are just more readable ways to access re.matched groups:
HOURS = 0
MINUTES = 1
SECONDS = 3
MERIDIEM = 4

class SelectTimeWidget(Widget):
    """
    A Widget that splits time input into <select> elements.
    Allows form to show as 24hr: <hour>:<minute>:<second>, (default)
    or as 12hr: <hour>:<minute>:<second> <am|pm> 
    
    Also allows user-defined increments for minutes/seconds
    """
    hour_field = '%s_hour'
    minute_field = '%s_minute'
    second_field = '%s_second' 
    meridiem_field = '%s_meridiem'
    twelve_hr = False # Default to 24hr.
    
    def __init__(self, attrs=None, hour_step=None, minute_step=None, second_step=None):
        """
        hour_step, minute_step, second_step are optional step values for
        for the range of values for the associated select element
        twelve_hr: If True, forces the output to be in 12-hr format (rather than 24-hr)
        """
        self.attrs = attrs or {}
        
        if hour_step: self.hours = range(0,100,hour_step)
        else: self.hours = range(0,100) 

        if minute_step: self.minutes = range(0,60,minute_step)
        else: self.minutes = range(0,60)

        if second_step: self.seconds = range(0,60,second_step)
        else: self.seconds = range(0,60)

    def render(self, name, value, attrs=None):
        try: # try to get time values from a datetime.time object (value)
            hour_val, minute_val, second_val = value.hour, value.minute, value.second
        except AttributeError:
            hour_val = minute_val = second_val = 0
            if isinstance(value, basestring):
                match = RE_TIME.match(value)
                if match:
                    time_groups = match.groups();
                    hour_val = int(time_groups[HOURS])
                    minute_val = int(time_groups[MINUTES])
                    if time_groups[SECONDS] is None: second_val = 0
                    else: second_val = int(time_groups[SECONDS])
                    
                    # check to see if meridiem was passed in
                    if time_groups[MERIDIEM] is not None: self.meridiem_val = time_groups[MERIDIEM]
                    else: self.meridiem_val = None
                        
        output = []
        if 'id' in self.attrs: id_ = self.attrs['id']
        else: id_ = 'id_%s' % name

        # For times to get displayed correctly, the values MUST be converted to unicode
        # When Select builds a list of options, it checks against Unicode values
        hour_val = u"%.2d" % hour_val
        minute_val = u"%.2d" % minute_val
        second_val = u"%.2d" % second_val

        hour_choices = [("%.2d"%i, "%.2d"%i) for i in self.hours]
        local_attrs = self.build_attrs(id=self.hour_field % id_)
        select_html = Select(choices=hour_choices).render(self.hour_field % name, hour_val, local_attrs)
        output.append(select_html+" h")

        minute_choices = [("%.2d"%i, "%.2d"%i) for i in self.minutes]
        local_attrs['id'] = self.minute_field % id_
        select_html = Select(choices=minute_choices).render(self.minute_field % name, minute_val, local_attrs)
        output.append(select_html+" m")

        second_choices = [("%.2d"%i, "%.2d"%i) for i in self.seconds]
        local_attrs['id'] = self.second_field % id_
        select_html = Select(choices=second_choices).render(self.second_field % name, second_val, local_attrs)
        output.append(select_html+" s")
    
        return mark_safe(u'\n'.join(output))

    def id_for_label(self, id_): return '%s_hour' % id_
    id_for_label = classmethod(id_for_label)

    def value_from_datadict(self, data, files, name):
        # if there's not h:m:s data, assume zero:
        h = data.get(self.hour_field % name, 0) # hour
        m = data.get(self.minute_field % name, 0) # minute 
        s = data.get(self.second_field % name, 0) # second

        meridiem = data.get(self.meridiem_field % name, None)

        #NOTE: if meridiem is None, assume 24-hr
        if meridiem is not None:
            if meridiem.lower().startswith('p') and int(h) != 12:
                h = (int(h)+12)%24 
            elif meridiem.lower().startswith('a') and int(h) == 12:
                h = 0
        
        if (int(h) == 0 or h) and m and s:
            return '%s:%s:%s' % (h, m, s)

        return data.get(name, None)

class RangeWidget(Widget):
	def __init__(self, Min=0, Max=100, Step=1, Default=50, LabelBefore="", LabelAfter=""):
		self.min = Min
		self.max = Max
		self.step = Step
		self.default = Default
		self.labelBefore = LabelBefore
		self.labelAfter = LabelAfter
		self.attrs = {}

	def render(self, name, value, attrs=None):
		renderStr = '<div id="id_%s" class="divRangeHorizontal"> <span class="labelBeforeRange">%s</span> <input type="range" min="%s" max="%s" step="%s" value="%s" orient="horizontal" name="%s" class="rangeHorizontal"/> <span class="labelAfterRange">%s</span> </div>' % (name, str(self.labelBefore.encode('utf8')), str(self.min), str(self.max), str(self.step), str(self.default), name, str(self.labelAfter.encode('utf8')))
		return mark_safe(renderStr)