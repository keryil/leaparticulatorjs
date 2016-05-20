/**
 * Created by Kerem on 19/05/16.
 */

var Theremin = (function () {
    var callbacks = [];
    var loopingCall = null;
    var frequency = 440;
    var synth = new Tone.SimpleSynth().toMaster();

    var dispatch = function(frame) {
        for (var i = 0; i < callbacks.length; i++) {
            callbacks[i](frame);
        }
    };

    var addCallback = function(callback) {
        if(callbacks.indexOf(callback) == -1) {
            callbacks.push(callback)
        }
    };

    var onFrame = function(frame) {
        if (frame.hands[0]) {
            var output3 = document.getElementById('output3');
            // calculate frequency
            x = frame.hands[0].palmPosition[0];
            freq = 110 * Math.pow(3, Math.abs(x + 200) / 200);

            // calculate amplitude
            y = frame.hands[0].palmPosition[1];
            amp = 1.1 - Math.log(Math.abs(y)) / Math.log(250.);
            amp = Math.min(1., Math.max(0., amp));
            amp_db = 20 * (Math.log(amp) / Math.log(10));

            output3.innerHTML = frame.hands[0].palmPosition[0] + ' ' + freq;
            synth.setNote(freq);
            synth.volume.value = amp_db;
            // console.log(synth.volume.value);
        }
        else {
            synth.volume.value = -99;
        }
    };

    LeapController = new Leap.Controller({
      frameEventName: 'deviceFrame'
    });
    LeapController.connect();

    LeapController.on("frame", function(frame){
        dispatch(frame);
    });
    addCallback(onFrame);

    return {
        dispatch: dispatch,
        addCallback: addCallback,
        callbacks: callbacks,
        synth: synth,
        frequency: frequency,
        loopingCall: loopingCall,
    };

})();

Theremin.synth.triggerAttack("C4", "8n");

