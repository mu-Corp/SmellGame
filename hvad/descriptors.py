import django
from django.db.models.fields import FieldDoesNotExist
from django.utils.translation import get_language
from hvad.utils import get_translation
if django.VERSION >= (1, 7):
    from django.apps import registry

class BaseDescriptor(object):
    """
    Base descriptor class with a helper to get the translations instance.
    """
    def __init__(self, opts):
        self.opts = opts
        self._NoTranslationError = type('NoTranslationError',
                                        (AttributeError, opts.translations_model.DoesNotExist),
                                        {})
    
    def translation(self, instance):
        cached = getattr(instance, self.opts.translations_cache, None)
        if cached is None:
            try:
                cached = get_translation(instance)
            except self.opts.translations_model.DoesNotExist:
                raise self._NoTranslationError('Accessing a translated field requires that '
                                               'the instance has a translation loaded, or a '
                                               'valid translation in current language (%s) '
                                               'loadable from the database' % get_language())
            setattr(instance, self.opts.translations_cache, cached)
        return cached


class TranslatedAttribute(BaseDescriptor):
    """
    Basic translated attribute descriptor.
    
    Proxies attributes from the shared instance to the translated instance.
    """
    def __init__(self, opts, name):
        self.name = name
        super(TranslatedAttribute, self).__init__(opts)
        
    def __get__(self, instance, instance_type=None):
        if not instance:
            if django.VERSION >= (1, 7) and not registry.apps.ready:
                raise AttributeError('Attribute not available until registry is ready.')
            # Don't raise an attribute error so we can use it in admin.
            try:
                return self.opts.translations_model._meta.get_field_by_name(
                                                        self.name)[0].default
            except FieldDoesNotExist as e:
                raise AttributeError(*e.args)
        return getattr(self.translation(instance), self.name)
    
    def __set__(self, instance, value):
        setattr(self.translation(instance), self.name, value)
    
    def __delete__(self, instance):
        delattr(self.translation(instance), self.name)


class LanguageCodeAttribute(TranslatedAttribute):
    """
    The language_code attribute is different from other attribtues as it cannot
    be deleted. Trying to do so will always cause an attribute error.
    
    """
    def __init__(self, opts):
        super(LanguageCodeAttribute, self).__init__(opts, 'language_code')
    
    def __set__(self, instance, value):
        raise AttributeError("The 'language_code' attribute cannot be " +\
                    "changed directly! Use the translate() method instead.")
    
    def __delete__(self, instance):
        raise AttributeError("The 'language_code' attribute cannot be deleted!")