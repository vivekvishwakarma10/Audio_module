function Listening(){
    var recognition = new webkitSpeechRecognition;
        recognition.lang = "en-GB";
        recognition.onresult = function(event)
        {
            document.getElementById('SpeechToText').value=event.results[0][0].transcript;
        }
        recognition.start();

}