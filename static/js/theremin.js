/**
 * Created by Kerem on 19/05/16.
 */

var frequency = 440;
var synth = new Tone.SimpleSynth().toMaster();
synth.triggerAttack("C4", "8n");

LeapController = new Leap.Controller({
      frameEventName: 'deviceFrame'
    });
LeapController.connect();
var Theremin = function () {
    this.callbacks = [];
    this.loopingCall = null;
}

Theremin.prototype.dispatch = function(frame) {
        for (var i = 0; i < this.callbacks.length; i++) {
            this.callbacks[i](frame);
        }
    };
Theremin.prototype.addCallback = function(callback) {
        if(this.callbacks.indexOf(callback) == -1) {
            this.callbacks.push(callback)
        }
    };


var theremin = new Theremin();
LeapController.on("frame", function(frame){
        theremin.dispatch(frame);
    });

theremin.addCallback(function(frame) {
    if (frame.hands[0]) {
        var output3 = document.getElementById('output3');
        x = frame.hands[0].palmPosition[0];
        val = 110 * Math.pow(3, Math.abs(x + 200) / 200);
        output3.innerHTML = frame.hands[0].palmPosition[0] + ' ' + val;
        synth.setNote(val);
        synth.volume.value = 0;
        // console.log(synth.volume);
    }
    else {
        synth.volume.value = -99;
    }
});

