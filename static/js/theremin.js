/**
 * Created by Kerem on 19/05/16.
 */

var Theremin = (function () {
    var callbacks = [];
    var loopingCall = null;
    var frequency = 440;
    var amp = Math.log(.5);
    var synth = new Tone.SimpleSynth().toMaster();
    var muted = false;
    var playing = false;

    var toggleMute = function() {
        muted = !muted;
    };

    var isMuted = function() {
        return muted;
    }

    var getFrequency = function() {
        return frequency;
    }

    var getAmplitude = function() {
        return amp;
    }

    var isPlaying = function() {
        return playing;
    }

    var to_dB = function(amp) {
        return 20 * (Math.log(amp) / Math.log(10));
    }

    var dispatch = function(frame) {
        for (var i = 0; i < callbacks.length; i++) {
            callbacks[i](frame);
        }
    };

    var addCallback = function(callback) {
        if(callbacks.indexOf(callback) == -1) {
            callbacks.push(callback);
        }
        else {
            console.log("Duplicate callback " + callback);
        }
    };

    var onFrame = function(frame) {
        if (muted) {
            playing = false;
            synth.triggerRelease();
            return;
        }
        if (frame.hands[0]) {
            // calculate frequency
            x = frame.hands[0].palmPosition[0];
            frequency = 110 * Math.pow(3, Math.abs(x + 200) / 200);

            // calculate amplitude
            y = frame.hands[0].palmPosition[1];
            amp = 1.1 - Math.log(Math.abs(y)) / Math.log(250.);
            amp = Math.min(1., Math.max(0., amp));

            synth.setNote(frequency);
            synth.volume.value = to_dB(amp);
            if (!playing) {
                synth.triggerAttack(frequency);
                playing = true;
            }
        }
        else {
            synth.triggerRelease();
            playing = false;
        }
    };

    var LeapController = new Leap.Controller({
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
        getFrequency: getFrequency,
        loopingCall: loopingCall,
        toggleMute:toggleMute,
        getAmplitude:getAmplitude,
        isPlaying:isPlaying,
        isMuted:isMuted
    };

}());


