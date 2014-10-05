		
		
		
		
		
		function updateGradient(color, intensity) {
			endGradientPercent = 30*intensity/100+40;
			panelCenter = document.getElementById("panelCenter");
			panelCenter.style.background = "-webkit-radial-gradient("+color+" 0%, "+color+" 20%, rgb(186,181,186) "+endGradientPercent+"%)";
			panelCenter.style.background = "-o-radial-gradient("+color+" 0%, "+color+" 20%, rgb(186,181,186) "+endGradientPercent+"%)";
			panelCenter.style.background = "-moz-radial-gradient("+color+" 0%, "+color+" 20%, rgb(186,181,186) "+endGradientPercent+"%)";
			panelCenter.style.background = "radial-gradient("+color+" 0%, "+color+" 20%, rgb(186,181,186) "+endGradientPercent+"%)";
		}
		
		function updateNote(color) {
			panelNote = document.getElementById("panelNote");
			panelNote.style.background = color;
		}
		
		function updateImgGuessed(path) {
			img = document.getElementById("imgGuessed");
			img.style.display = "block";
			img.src = path;
		}
		
		function updateFeeling(feeling) {
			panelFeeling = document.getElementById("panelFeeling");
			opacity = feeling*50/100;
			panelFeeling.style.opacity = opacity/100;
			panelFeeling.style.filter = "alpha(opacity="+opacity+")";
		}
		
		function createImageFinal() {
			html2canvas($("#panelCenter"), {
				onrendered: function(canvas) {
					var imageUrl = canvas.toDataURL("image/png");
					var inputBase64 = document.getElementById("inputBase64"); 
					inputBase64.value = imageUrl;
				}
			});
		}