var text = ["This is Pulse.", "Welcome.", "Hi."];
var counter = 1;
var elem = document.getElementById("changeText");
var inst = setInterval(change, 5000);

function change() {
	elem.innerHTML = text[counter];
	counter++;
	if (counter >= text.length) {
		counter = 0;
	}
}