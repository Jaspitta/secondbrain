---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
home
automation
 ^iKdClJCK

building
automation ^1NhbpRTE

short range ^tse1eQ4a

same building ^QEw8siKr

software managed ^YDiOlvIG

light when dark ^DolMclcv

no user input ^iSWtUQs8

network ^8RZLBkQm

WiFi ^QOM3Bu4E

pass ^Q0ZCj4Up

range ^4anVgSzN

power ^hDYkATKL

sometimes ^a2rhynni

proliferation ^zLaC0RlH

Zigbee
6LowPAN
Bluethoot ^RPc59VOP

different uses ^k5iEGxP8

architecture ^lijr2MBt

protocol ^5FsaofXo

mesh network ^2OfyzI1i

OOS ^YMAaFx9t

node to node ^zzWjxIQx

hopping ^yGu2HapV

route evaluation
 ^cH8Jqf9B

hops ^IEgnqOeb

power ^poRyVCRd

latency ^exwY7Vqf

routing ^WkWIBjcH

floding ^jQGDeZXj

more devices
=
more range ^LzD9Jq1B

licence free spectrum ^ionjbjsF

=/ frequencies ^OYSDB5Lr

1 GHz ^2M8S8vEM

propagation ^qnIJ9OF1

=/ hub ^H0THbc8K

energy
and
power
 ^TzB2juHA

work ^WfGfYB2O

energy ^RkH7rg6S

joules (J) ^nAdC4EJp

10 j = 1 kg x 1m ^abfVu5F5

force ^kUrTi0RH

movement ^OcvVAwbZ

time ^U23o7Qmk

/ time = power ^dyXJUQQU

1W = 1j/1s ^od0r3ZcM

life ^YpjLqFoD

LED 5-15W ^yk263kO2

phone 3W ^nqeXInOx

battery devices ^P5EJ4wTt

1w ^ZTB2UbG8

Home automation is actually a term that is used for what
would be more accurate to call building automation. With it 
we mean all that is concerned with automating as many of the 
processes inside a building and therefore penetration is much more 
important than range int these type of applications. 
It is also important to specify that when we say automation we 
mean that all the processes should be managed by the software, 
for example the lights should turn on when it is dark and there 
are people in the office but without any extra inputs from someone 
except the initial setup. ^CCa4PPhc

As we saw before we need to ask ourselves which network
type is best suited for the application of building automation.
At firs one might think of wifi, but it comes with his own problems,
changing password would mean update all the devices, range is limitad
expecially in hard to reach places and devices that use wifi require
too much power. Wifi is still used for some applications but not all of them.
 ^evlerF7H

This problems brought the birth of many different protocols trying
to fix the short comings of wifi. The most importan once are Zigbee,
Bluethoot and 6LowPAN, every protocol has specific uses and more than one
might be used in the same network but since each uses a different
frequency each need his own hub to do protocol translation. In genera though
they all use the licence free spectrum and use lower than 1GHz frequencies
for higher propagation ^h1cIiVRx

One thing that is common on IOT networks i the use of a mesh type architecture (type of ad hoc architecture).
Especially in buildings where there are a lot of walls, mesh type architecture allows to extend the range
and get over the Out Of Sight problems using hopping. In this network every node act as a mini router
and therefore not only as a receiver but also as a sender when necessary. An algorithm recognize that
signal to get from point A to C might need help and therefore can use point B as an intermediate.
This process is called route evaluation and require the use of power and increased latency
but it is well worth the trade off compared to having to install many more hubs. One more thing to consider is
that with the use of idle modes every single node might go to sleep, so when the signal is re transmitted that node
needs to be woken up causing some extra delay. There is an alternative to this that is called flooding 
where every node re transmits all the signals to avoid doing route evaluation but it has also his drawbacks ^4VwVF9xk

Often we talked about power in the context of usage for battery life but we never defined
what power is scientifically and the difference from work or energy. Scientifically speaking
work and energy are almost the same, they represent a force applied causing a movement,
it is measured in Joules where 10j is the work from moving 1kg for 1m (on hearth). On note
is that work is totally abstracted from time, weather it takes 1s or 1 month to to the movement
the work is the same. If we factor in the time and therefore look at work over time
we have what we call power. Power is measured in Watts and 1W is 1j/1s, to make some examples
an LED require about 5-15W, a phone wants at most 3W and battery operated devices need to 
require less than 1W to be usable ^w7Th9Kq0

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.0.22",
	"elements": [
		{
			"type": "text",
			"version": 88,
			"versionNonce": 1329687698,
			"isDeleted": false,
			"id": "iKdClJCK",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1547.5227652658662,
			"y": -820.1381485137908,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 152.8519287109375,
			"height": 105,
			"seed": 47885,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "home\nautomation\n",
			"rawText": "home\nautomation\n",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "home\nautomation\n",
			"lineHeight": 1.25,
			"baseline": 95
		},
		{
			"type": "text",
			"version": 51,
			"versionNonce": 1363598734,
			"isDeleted": false,
			"id": "1NhbpRTE",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1292.7993556978622,
			"y": -966.7048382407356,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 109.17990112304688,
			"height": 50,
			"seed": 39994,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "building\nautomation",
			"rawText": "building\nautomation",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "building\nautomation",
			"lineHeight": 1.25,
			"baseline": 43
		},
		{
			"type": "text",
			"version": 62,
			"versionNonce": 1900677714,
			"isDeleted": false,
			"id": "tse1eQ4a",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1119.6633520618404,
			"y": -1018.6656199343189,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 113.95989990234375,
			"height": 25,
			"seed": 8827,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "short range",
			"rawText": "short range",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "short range",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 29,
			"versionNonce": 670038990,
			"isDeleted": false,
			"id": "QEw8siKr",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1122.0067929442473,
			"y": -923.0125077291553,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 124.07987976074219,
			"height": 25,
			"seed": 84361,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "same building",
			"rawText": "same building",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "same building",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 200863762,
			"isDeleted": false,
			"id": "rSXZJ9hunuAbYK70OvskI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1064.2996924324707,
			"y": -978.5796453002908,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.580862803380114,
			"height": 26.85647102535063,
			"seed": 319199661,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.8952157008450286
				],
				[
					0.8952157008450286,
					2.6856471025350857
				],
				[
					1.790431401690057,
					9.8473727092952
				],
				[
					1.790431401690057,
					17.009098316055315
				],
				[
					2.6856471025350857,
					25.9612553245056
				],
				[
					3.580862803380114,
					25.066039623660572
				],
				[
					2.6856471025350857,
					24.170823922815543
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.2659260332584381,
				0.3188140094280243,
				0.342928022146225,
				0.3669792115688324,
				0.1858353316783905,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 5984782,
			"isDeleted": false,
			"id": "-wwlkjKS3ETSSRnMvnZ2e",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1070.566202338386,
			"y": -942.7710172664899,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.056941307605257,
			"height": 13.428235512675315,
			"seed": 1279934221,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8952157008450286,
					0
				],
				[
					-0.8952157008450286,
					0.8952157008450286
				],
				[
					-0.8952157008450286,
					1.790431401690057
				],
				[
					3.580862803380114,
					8.952157008450172
				],
				[
					5.371294205070171,
					10.742588410140229
				],
				[
					6.2665099059152,
					5.371294205070171
				],
				[
					7.161725606760228,
					-1.790431401690057
				],
				[
					7.161725606760228,
					-2.6856471025350857
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.050641998648643494,
				0.15097197890281677,
				0.17254400253295898,
				0.22078005969524384,
				0.21380075812339783,
				0.22289776802062988,
				0.12202896177768707,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 1128603090,
			"isDeleted": false,
			"id": "jI26ldoomj7ipUCL7M5hD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1070.566202338386,
			"y": -983.950939505361,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.428235512675428,
			"height": 8.056941307605257,
			"seed": 1298088653,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8952157008450286,
					0
				],
				[
					0,
					0
				],
				[
					3.580862803380114,
					-4.476078504225143
				],
				[
					8.952157008450286,
					-8.056941307605257
				],
				[
					10.742588410140343,
					-8.056941307605257
				],
				[
					11.637804110985371,
					-4.476078504225143
				],
				[
					12.5330198118304,
					-1.790431401690057
				],
				[
					12.5330198118304,
					-1.790431401690057
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10895950347185135,
				0.1763095110654831,
				0.2726860046386719,
				0.3277069628238678,
				0.3499116599559784,
				0.3726963400840759,
				0.12289172410964966,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 32,
			"versionNonce": 1434574926,
			"isDeleted": false,
			"id": "RK73HPZwxGoRWP5cozjFU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1128.7552228933123,
			"y": -1017.0739204366268,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.90431401690057,
			"height": 117.27325681069806,
			"seed": 2033620621,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8952157008452559,
					0
				],
				[
					-2.685647102535313,
					0
				],
				[
					-3.580862803380114,
					0
				],
				[
					-6.2665099059152,
					0
				],
				[
					-11.637804110985371,
					3.5808628033800005
				],
				[
					-15.218666914365485,
					10.742588410140229
				],
				[
					-14.323451213520457,
					19.6947454185904
				],
				[
					-11.637804110985371,
					32.2277652304208
				],
				[
					-9.847372709295314,
					37.59905943549097
				],
				[
					-10.742588410140343,
					38.494275136336
				],
				[
					-12.5330198118304,
					38.494275136336
				],
				[
					-13.428235512675428,
					40.28470653802606
				],
				[
					-10.742588410140343,
					42.97035364056103
				],
				[
					-7.161725606760228,
					48.3416478456312
				],
				[
					-6.2665099059152,
					55.503373452391315
				],
				[
					-9.847372709295314,
					65.35074616168663
				],
				[
					-13.428235512675428,
					76.988550272672
				],
				[
					-16.113882615210514,
					88.62635438365726
				],
				[
					-17.90431401690057,
					102.05458989633257
				],
				[
					-16.113882615210514,
					111.90196260562789
				],
				[
					-9.847372709295314,
					116.37804110985303
				],
				[
					-1.790431401690057,
					117.27325681069806
				],
				[
					0,
					117.27325681069806
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06999682635068893,
				0.11049386858940125,
				0.16215460002422333,
				0.18756018579006195,
				0.21672390401363373,
				0.23455554246902466,
				0.2544306218624115,
				0.28650882840156555,
				0.2892937958240509,
				0.28162404894828796,
				0.27449050545692444,
				0.3030956983566284,
				0.3238864839076996,
				0.3550393879413605,
				0.38969969749450684,
				0.40398484468460083,
				0.38053417205810547,
				0.3684127628803253,
				0.3922489881515503,
				0.44095271825790405,
				0.42427152395248413,
				0.20770999789237976,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 19,
			"versionNonce": 608539538,
			"isDeleted": false,
			"id": "jJk8QmjRQ4go6Rv80BXw9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1423.6762043406875,
			"y": -808.3977925472245,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 67.52879196836761,
			"height": 100.7008301282674,
			"seed": 1478280685,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.1847156485680443,
					-1.184715648567817
				],
				[
					-1.1847156485680443,
					-7.108293891407129
				],
				[
					4.738862594271268,
					-26.06374426849277
				],
				[
					17.77073472851771,
					-50.94277288841772
				],
				[
					31.987322511331968,
					-72.267654562639
				],
				[
					46.203910294146226,
					-85.29952669688532
				],
				[
					58.05106677982462,
					-95.96196753399613
				],
				[
					63.974645022663935,
					-99.51611447969958
				],
				[
					65.15936067123175,
					-99.51611447969958
				],
				[
					66.34407631979957,
					-100.7008301282674
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06880291551351547,
				0.15248095989227295,
				0.22696645557880402,
				0.29639002680778503,
				0.3158055543899536,
				0.31637313961982727,
				0.3690202236175537,
				0.3876846432685852,
				0.10994286835193634,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 1530701454,
			"isDeleted": false,
			"id": "o2u_KeffXSpAVCiDdp8mh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1333.637815049531,
			"y": -932.7929356468491,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.58601907995012,
			"height": 17.770734728517823,
			"seed": 257419885,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.184715648567817,
					0
				],
				[
					4.738862594271495,
					-1.184715648567817
				],
				[
					13.031872134246441,
					-1.184715648567817
				],
				[
					15.401303431382303,
					1.1847156485679307
				],
				[
					11.847156485678624,
					8.29300953997506
				],
				[
					7.108293891407129,
					15.401303431382075
				],
				[
					8.293009539974946,
					16.586019079950006
				],
				[
					9.477725188542763,
					16.586019079950006
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11252246052026749,
				0.2920440137386322,
				0.32763198018074036,
				0.3065751791000366,
				0.34022045135498047,
				0.41315603256225586,
				0.18788263201713562,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 33,
			"versionNonce": 20009298,
			"isDeleted": false,
			"id": "L3o84_dm1zWiRXS152bgr",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1427.2303512863912,
			"y": -870.0030062727528,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 23.69431297135702,
			"height": 35.541469457035646,
			"seed": 279983661,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.184715648567817,
					0
				],
				[
					0,
					-8.293009539974946
				],
				[
					2.369431297135634,
					-14.216587782814258
				],
				[
					7.108293891407129,
					-15.401303431382075
				],
				[
					11.847156485678397,
					-14.216587782814258
				],
				[
					17.77073472851771,
					-16.586019079949892
				],
				[
					20.14016602565357,
					-24.879028619924952
				],
				[
					21.324881674221388,
					-33.1720381598999
				],
				[
					22.509597322789205,
					-35.541469457035646
				],
				[
					22.509597322789205,
					-35.541469457035646
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08434317260980606,
				0.23096029460430145,
				0.24905502796173096,
				0.26381468772888184,
				0.2868429124355316,
				0.30069565773010254,
				0.306121826171875,
				0.29826492071151733,
				0.27117952704429626,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 1648665806,
			"isDeleted": false,
			"id": "aSR7D_gF0iTZ9KMPy8A6_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -973.9580660070685,
			"y": -1012.6071001671899,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.615142681282805,
			"height": 11.332284952225336,
			"seed": 1628240557,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8717142270943441,
					2.615142681282805
				],
				[
					0,
					8.717142270942645
				],
				[
					0.8717142270942304,
					11.332284952225336
				],
				[
					1.7434284541884608,
					9.588856498036876
				],
				[
					1.7434284541884608,
					8.717142270942645
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.20764797925949097,
				0.25381800532341003,
				0.16239844262599945,
				0.011801513843238354,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 22,
			"versionNonce": 1298093842,
			"isDeleted": false,
			"id": "sbY-WUZzwWFfEpjPW2H8u",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -975.7014944612571,
			"y": -1013.4788143942842,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 37.483711765053386,
			"height": 6.1019995896597266,
			"seed": 641675085,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8717142270942304,
					0
				],
				[
					-0.8717142270942304,
					-0.8717142270941167
				],
				[
					1.7434284541885745,
					-1.7434284541884608
				],
				[
					8.717142270942645,
					-2.615142681282805
				],
				[
					17.43428454188529,
					-4.358571135471266
				],
				[
					24.407998358639475,
					-5.230285362565496
				],
				[
					31.381712175393545,
					-6.1019995896597266
				],
				[
					33.99685485667635,
					-5.230285362565496
				],
				[
					34.86856908377058,
					-4.358571135471266
				],
				[
					35.74028331086481,
					-3.4868569083769216
				],
				[
					36.611997537959155,
					-2.615142681282805
				],
				[
					35.74028331086481,
					-2.615142681282805
				],
				[
					35.74028331086481,
					-2.615142681282805
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09743741154670715,
				0.15305599570274353,
				0.24125199019908905,
				0.3425099849700928,
				0.4121859669685364,
				0.4451178014278412,
				0.4010576009750366,
				0.39768633246421814,
				0.38524317741394043,
				0.37311238050460815,
				0.3679693043231964,
				0.09536312520503998,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 1009965838,
			"isDeleted": false,
			"id": "f18bAEMb1VaeRwybP274J",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -939.9612111503923,
			"y": -1017.8373855297555,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7434284541885745,
			"height": 13.947427633508255,
			"seed": 1918917357,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8717142270943441,
					0
				],
				[
					0.8717142270943441,
					1.7434284541884608
				],
				[
					0.8717142270943441,
					4.358571135471266
				],
				[
					1.7434284541885745,
					12.20399917931968
				],
				[
					1.7434284541885745,
					13.947427633508255
				],
				[
					1.7434284541885745,
					13.947427633508255
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15963497757911682,
				0.245590478181839,
				0.3153799772262573,
				0.35018596053123474,
				0.09664697200059891,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 21,
			"versionNonce": 2034672850,
			"isDeleted": false,
			"id": "jwG5suUGQYKfozxIPP4Hi",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -975.7014944612571,
			"y": -998.6596725336817,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 39.22714021924196,
			"height": 5.230285362565496,
			"seed": 374660589,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8717142270942304,
					0
				],
				[
					1.7434284541885745,
					0
				],
				[
					4.358571135471379,
					-0.8717142270941167
				],
				[
					11.33228495222545,
					-1.7434284541884608
				],
				[
					20.921141450262326,
					-3.4868569083769216
				],
				[
					28.76656949411074,
					-3.4868569083769216
				],
				[
					34.86856908377058,
					-5.230285362565496
				],
				[
					36.611997537959155,
					-5.230285362565496
				],
				[
					37.483711765053386,
					-5.230285362565496
				],
				[
					38.355425992147616,
					-4.358571135471266
				],
				[
					39.22714021924196,
					-4.358571135471266
				],
				[
					39.22714021924196,
					-4.358571135471266
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05980987474322319,
				0.15785254538059235,
				0.20046399533748627,
				0.2612529993057251,
				0.26057618856430054,
				0.1997298002243042,
				0.19186578691005707,
				0.1945633888244629,
				0.19896654784679413,
				0.15423546731472015,
				0.008573517203330994,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 528501070,
			"isDeleted": false,
			"id": "KMwTh2ghsaNpTrjdb8M2t",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -969.5994948715972,
			"y": -1015.2222428484727,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.358571135471379,
			"height": 10.46057072513122,
			"seed": 1974864685,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.8717142270943441
				],
				[
					0.8717142270943441,
					2.615142681282805
				],
				[
					2.615142681282805,
					7.845428043848415
				],
				[
					3.486856908377149,
					9.588856498036876
				],
				[
					4.358571135471379,
					8.717142270942645
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07979898154735565,
				0.20167367160320282,
				0.20650310814380646,
				0.04871969670057297,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 1316895378,
			"isDeleted": false,
			"id": "CTU3j7dYjj70PI0fXMOfg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -963.4974952819373,
			"y": -1016.093957075567,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7434284541884608,
			"height": 5.23028536256561,
			"seed": 660066253,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8717142270941167,
					0
				],
				[
					0.8717142270941167,
					0.8717142270943441
				],
				[
					1.7434284541884608,
					4.358571135471379
				],
				[
					1.7434284541884608,
					5.23028536256561
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12593914568424225,
				0.14899884164333344,
				0.04447067156434059,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 193326990,
			"isDeleted": false,
			"id": "xAG_S0AIZG-sdwnJ8bqxe",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -958.2672099193718,
			"y": -1016.9656713026611,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7434284541885745,
			"height": 4.358571135471266,
			"seed": 508482061,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.7434284541884608
				],
				[
					0.8717142270942304,
					4.358571135471266
				],
				[
					1.7434284541885745,
					4.358571135471266
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.18529000878334045,
				0.056824035942554474,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 1270683730,
			"isDeleted": false,
			"id": "zY0xVhSHDZvgVqpx7IbsJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -953.0369245568062,
			"y": -1017.8373855297555,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.4868569083770353,
			"height": 12.20399917931968,
			"seed": 1856563693,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8717142270942304,
					0.8717142270943441
				],
				[
					0.8717142270942304,
					2.615142681282805
				],
				[
					2.615142681282805,
					8.717142270942645
				],
				[
					3.4868569083770353,
					12.20399917931968
				],
				[
					3.4868569083770353,
					12.20399917931968
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1891220360994339,
				0.215069979429245,
				0.2534313499927521,
				0.09183438122272491,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 746376654,
			"isDeleted": false,
			"id": "_5QkWwDlZAGciCXozNmN_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -945.1914965129579,
			"y": -1016.9656713026611,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 4.358571135471266,
			"seed": 247252621,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8717142270941167
				],
				[
					0,
					1.7434284541884608
				],
				[
					0,
					2.615142681282805
				],
				[
					0,
					4.358571135471266
				],
				[
					0,
					4.358571135471266
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.019999999552965164,
				0.12483599781990051,
				0.15642599761486053,
				0.07058105617761612,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 14302738,
			"isDeleted": false,
			"id": "Ur6pn8OufVcpNaXCTFdca",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -941.7046396045807,
			"y": -1016.093957075567,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8717142270942304,
			"height": 2.615142681282805,
			"seed": 1707415341,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8717142270943441
				],
				[
					0.8717142270942304,
					2.615142681282805
				],
				[
					0.8717142270942304,
					2.615142681282805
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10750900208950043,
				0.14526300132274628,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 1065214990,
			"isDeleted": false,
			"id": "tw2x96x7iF_f-j1K7w_k-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -984.4186367321997,
			"y": -1025.6828135736039,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.845428043848415,
			"height": 0,
			"seed": 1576008461,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.7434284541885745,
					0
				],
				[
					6.101999589659954,
					0
				],
				[
					7.845428043848415,
					0
				],
				[
					7.845428043848415,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2065879851579666,
				0.2881839871406555,
				0.2871688902378082,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 20,
			"versionNonce": 1791798226,
			"isDeleted": false,
			"id": "OomYQ6aCT-Y4VDBD_-vGO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -974.8297802341629,
			"y": -1031.7848131632636,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.46057072513122,
			"height": 7.845428043848301,
			"seed": 136154445,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8717142270942304,
					0
				],
				[
					-1.7434284541884608,
					0
				],
				[
					0.8717142270943441,
					0
				],
				[
					4.358571135471379,
					0.8717142270941167
				],
				[
					7.845428043848415,
					2.615142681282805
				],
				[
					8.717142270942759,
					4.358571135471266
				],
				[
					6.973713816754184,
					6.1019995896597266
				],
				[
					4.358571135471379,
					7.845428043848301
				],
				[
					3.486856908377149,
					7.845428043848301
				],
				[
					5.23028536256561,
					6.973713816754071
				],
				[
					5.23028536256561,
					6.973713816754071
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09775598347187042,
				0.2698820233345032,
				0.2987940013408661,
				0.24566927552223206,
				0.24956558644771576,
				0.2797761857509613,
				0.2979874312877655,
				0.2705044448375702,
				0.07586243003606796,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 1988244046,
			"isDeleted": false,
			"id": "U5fA-x2ANR5XmFQ78FilL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -937.3460684691095,
			"y": -1034.3999558445464,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.23028536256561,
			"height": 0.8717142270941167,
			"seed": 1870192685,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8717142270942304,
					0
				],
				[
					-3.4868569083770353,
					0
				],
				[
					-5.23028536256561,
					0.8717142270941167
				],
				[
					-5.23028536256561,
					0.8717142270941167
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2276739776134491,
				0.30355799198150635,
				0.06847863644361496,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 20,
			"versionNonce": 1336631698,
			"isDeleted": false,
			"id": "UOGT6kTf992gjmnHy5uMY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -945.1914965129579,
			"y": -1038.758526980018,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.845428043848301,
			"height": 9.588856498037103,
			"seed": 1581259373,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8717142270943441
				],
				[
					-0.8717142270941167,
					1.7434284541886882
				],
				[
					-0.8717142270941167,
					2.6151426812830323
				],
				[
					-2.615142681282805,
					5.23028536256561
				],
				[
					-4.358571135471266,
					8.717142270942759
				],
				[
					-5.230285362565496,
					9.588856498037103
				],
				[
					-2.615142681282805,
					9.588856498037103
				],
				[
					0.8717142270943441,
					8.717142270942759
				],
				[
					2.615142681282805,
					8.717142270942759
				],
				[
					2.615142681282805,
					7.845428043848415
				],
				[
					2.615142681282805,
					7.845428043848415
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05987387150526047,
				0.1535319834947586,
				0.18364159762859344,
				0.23290713131427765,
				0.24719133973121643,
				0.2317938208580017,
				0.26113930344581604,
				0.32515648007392883,
				0.3396889865398407,
				0.07028799504041672,
				0
			]
		},
		{
			"type": "text",
			"version": 34,
			"versionNonce": 1549973646,
			"isDeleted": false,
			"id": "YDiOlvIG",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1278.5493543696573,
			"y": -814.7866404441916,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 179.03985595703125,
			"height": 25,
			"seed": 66660,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "software managed",
			"rawText": "software managed",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "software managed",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 8,
			"versionNonce": 447569746,
			"isDeleted": false,
			"id": "DolMclcv",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1059.1154094806432,
			"y": -858.2981386988191,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 146.23988342285156,
			"height": 25,
			"seed": 95563,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "light when dark",
			"rawText": "light when dark",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "light when dark",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 30,
			"versionNonce": 953710286,
			"isDeleted": false,
			"id": "iSWtUQs8",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1055.1560230072214,
			"y": -771.1916362835377,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 128.4198760986328,
			"height": 25,
			"seed": 93213,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "no user input",
			"rawText": "no user input",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "no user input",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 64,
			"versionNonce": 942253330,
			"isDeleted": false,
			"id": "pFfzaLoFZ3C25nghYsS0J",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -882.1586795020114,
			"y": -851.9377229198492,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.189573773484426,
			"height": 24.609423340596663,
			"seed": 631915981,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5349874639259724,
					0
				],
				[
					-1.0699749278520585,
					-0.5349874639260861
				],
				[
					-2.139949855704117,
					-1.6049623917781446
				],
				[
					-3.209924783556062,
					-2.6749373196300894
				],
				[
					-4.814887175334206,
					-5.349874639260179
				],
				[
					-5.884862103186151,
					-9.094786886742327
				],
				[
					-5.884862103186151,
					-12.304711670298389
				],
				[
					-4.279899711408234,
					-14.979648989928478
				],
				[
					-2.139949855704117,
					-16.58461138170651
				],
				[
					0,
					-17.11959884563248
				],
				[
					1.604962391778031,
					-17.11959884563248
				],
				[
					3.209924783556062,
					-17.11959884563248
				],
				[
					3.744912247482034,
					-17.654586309558567
				],
				[
					3.209924783556062,
					-17.654586309558567
				],
				[
					3.209924783556062,
					-18.18957377348454
				],
				[
					2.6749373196300894,
					-18.724561237410626
				],
				[
					2.1399498557040033,
					-19.2595487013366
				],
				[
					0.5349874639259724,
					-20.329523629188657
				],
				[
					-1.6049623917781446,
					-20.329523629188657
				],
				[
					-3.744912247482148,
					-20.86451109311463
				],
				[
					-5.884862103186151,
					-20.329523629188657
				],
				[
					-6.95483703103821,
					-20.329523629188657
				],
				[
					-8.024811958890268,
					-19.79453616526257
				],
				[
					-9.094786886742213,
					-19.2595487013366
				],
				[
					-10.164761814594385,
					-18.18957377348454
				],
				[
					-11.23473674244633,
					-17.654586309558567
				],
				[
					-11.769724206372302,
					-16.58461138170651
				],
				[
					-12.839699134224475,
					-15.51463645385445
				],
				[
					-13.374686598150447,
					-14.444661526002392
				],
				[
					-13.90967406207642,
					-12.839699134224475
				],
				[
					-14.444661526002392,
					-11.23473674244633
				],
				[
					-14.444661526002392,
					-9.6297743506683
				],
				[
					-14.444661526002392,
					-8.024811958890268
				],
				[
					-13.90967406207642,
					-6.419849567112237
				],
				[
					-12.839699134224475,
					-4.814887175334206
				],
				[
					-11.769724206372302,
					-2.6749373196300894
				],
				[
					-10.699749278520358,
					-1.0699749278520585
				],
				[
					-9.6297743506683,
					0.5349874639259724
				],
				[
					-8.55979942281624,
					1.604962391778031
				],
				[
					-7.489824494964296,
					2.6749373196300894
				],
				[
					-6.95483703103821,
					3.209924783556062
				],
				[
					-5.884862103186151,
					3.744912247482034
				],
				[
					-4.814887175334206,
					3.744912247482034
				],
				[
					-3.744912247482148,
					3.744912247482034
				],
				[
					-2.6749373196300894,
					3.744912247482034
				],
				[
					-2.139949855704117,
					3.744912247482034
				],
				[
					-1.0699749278520585,
					3.209924783556062
				],
				[
					-0.5349874639259724,
					2.6749373196300894
				],
				[
					0,
					2.1399498557040033
				],
				[
					0.5349874639259724,
					1.604962391778031
				],
				[
					1.0699749278519448,
					1.0699749278519448
				],
				[
					1.604962391778031,
					1.0699749278519448
				],
				[
					1.604962391778031,
					0.5349874639259724
				],
				[
					2.1399498557040033,
					0.5349874639259724
				],
				[
					2.1399498557040033,
					0.5349874639259724
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0952528715133667,
				0.15008443593978882,
				0.1917436271905899,
				0.21382595598697662,
				0.24181963503360748,
				0.25123855471611023,
				0.24855227768421173,
				0.267238587141037,
				0.2694166302680969,
				0.26213422417640686,
				0.2770095765590668,
				0.30015161633491516,
				0.2720981538295746,
				0.2648981809616089,
				0.2678074240684509,
				0.2608448266983032,
				0.26199981570243835,
				0.27578064799308777,
				0.29936137795448303,
				0.3230864405632019,
				0.3370778262615204,
				0.34384799003601074,
				0.3474787771701813,
				0.3402544856071472,
				0.3401046097278595,
				0.34703153371810913,
				0.3468857407569885,
				0.341026246547699,
				0.34002232551574707,
				0.34479808807373047,
				0.3597548007965088,
				0.36234432458877563,
				0.3606041669845581,
				0.3606443405151367,
				0.366585373878479,
				0.3612682819366455,
				0.3554631173610687,
				0.356120228767395,
				0.3447987139225006,
				0.33276015520095825,
				0.33386921882629395,
				0.3390207588672638,
				0.33890822529792786,
				0.33876940608024597,
				0.3250541090965271,
				0.3221581280231476,
				0.32701531052589417,
				0.3264921009540558,
				0.3140491247177124,
				0.32433396577835083,
				0.34344255924224854,
				0.35046011209487915,
				0.3541192412376404,
				0.2236558496952057,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 1954311438,
			"isDeleted": false,
			"id": "S5EL6az9sbaLL_QCFUw-C",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -870.3889552956391,
			"y": -861.5674972705175,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.814887175334206,
			"height": 0,
			"seed": 471718189,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5349874639259724,
					0
				],
				[
					3.209924783556062,
					0
				],
				[
					4.814887175334206,
					0
				],
				[
					4.814887175334206,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2194959968328476,
				0.288112998008728,
				0.0988399013876915,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 19,
			"versionNonce": 1905734354,
			"isDeleted": false,
			"id": "gdpqnED5KPAAZDlC2i5Aa",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -860.7591809449708,
			"y": -864.7774220540737,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.489824494964296,
			"height": 5.349874639260179,
			"seed": 1662407533,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5349874639260861,
					0
				],
				[
					-1.0699749278520585,
					0
				],
				[
					1.604962391778031,
					0.5349874639260861
				],
				[
					4.814887175334093,
					1.6049623917781446
				],
				[
					6.419849567112237,
					2.6749373196300894
				],
				[
					6.419849567112237,
					3.2099247835561755
				],
				[
					4.27989971140812,
					4.279899711408234
				],
				[
					2.6749373196299757,
					5.349874639260179
				],
				[
					2.6749373196299757,
					4.814887175334206
				],
				[
					3.209924783556062,
					4.814887175334206
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0522419735789299,
				0.2229679822921753,
				0.315266489982605,
				0.28899946808815,
				0.27299511432647705,
				0.3077532649040222,
				0.3551495671272278,
				0.37632885575294495,
				0.17037661373615265,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 2093456206,
			"isDeleted": false,
			"id": "1BdXuJw_fOO_l70plZovv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -842.0346197075603,
			"y": -847.1228357445151,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.884862103186151,
			"height": 0.5349874639259724,
			"seed": 848902125,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5349874639259724,
					0
				],
				[
					1.604962391778031,
					0
				],
				[
					4.27989971140812,
					-0.5349874639259724
				],
				[
					5.884862103186151,
					-0.5349874639259724
				],
				[
					5.884862103186151,
					-0.5349874639259724
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16446799039840698,
				0.1986999809741974,
				0.24457401037216187,
				0.06462698429822922,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 1233979538,
			"isDeleted": false,
			"id": "taouiAr-jNeb2NW5FQJh2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -844.1745695632644,
			"y": -847.6578232084411,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.0699749278520585,
			"height": 5.884862103186265,
			"seed": 1085330573,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5349874639260861
				],
				[
					-0.5349874639259724,
					-0.5349874639260861
				],
				[
					-0.5349874639259724,
					-1.0699749278520585
				],
				[
					-0.5349874639259724,
					-2.139949855704117
				],
				[
					0,
					-4.814887175334206
				],
				[
					0,
					-5.884862103186265
				],
				[
					0.5349874639260861,
					-5.884862103186265
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.054825104773044586,
				0.06464767456054688,
				0.09400982409715652,
				0.13495740294456482,
				0.14595893025398254,
				0.03505752608180046,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 672334222,
			"isDeleted": false,
			"id": "MBPm0LnCMJOByoUI4ULNL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -837.7547199961522,
			"y": -848.1928106723672,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.5349874639260861,
			"height": 6.954837031038096,
			"seed": 800407021,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5349874639259724
				],
				[
					0,
					-2.1399498557040033
				],
				[
					0.5349874639260861,
					-4.27989971140812
				],
				[
					0.5349874639260861,
					-6.419849567112124
				],
				[
					0.5349874639260861,
					-6.954837031038096
				],
				[
					0.5349874639260861,
					-6.954837031038096
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06092257797718048,
				0.1236887201666832,
				0.14708368480205536,
				0.17017047107219696,
				0.0451786182820797,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 1472341586,
			"isDeleted": false,
			"id": "4QDOxuTaVXifuG2byS6Li",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -844.1745695632644,
			"y": -850.8677479919972,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.349874639260179,
			"height": 1.0699749278519448,
			"seed": 1448526061,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5349874639260861,
					0
				],
				[
					3.209924783556062,
					0
				],
				[
					5.349874639260179,
					-1.0699749278519448
				],
				[
					5.349874639260179,
					-1.0699749278519448
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14452224969863892,
				0.15503253042697906,
				0.011226623319089413,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 429367246,
			"isDeleted": false,
			"id": "4uM3jHtiIk4ZXeV2aSK8s",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -843.1045946354124,
			"y": -852.4727103837753,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.814887175334093,
			"height": 1.0699749278520585,
			"seed": 2095999789,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5349874639260861,
					0
				],
				[
					1.604962391778031,
					0
				],
				[
					4.27989971140812,
					-1.0699749278520585
				],
				[
					4.814887175334093,
					-1.0699749278520585
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1539052426815033,
				0.042103361338377,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 621644818,
			"isDeleted": false,
			"id": "_N6Tkgl_oKHXiF9USpPfl",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -838.2897074600783,
			"y": -857.2875975591094,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.11959884563248,
			"height": 20.329523629188543,
			"seed": 114386285,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5349874639259724
				],
				[
					0,
					-1.0699749278520585
				],
				[
					-0.5349874639259724,
					-1.604962391778031
				],
				[
					-0.5349874639259724,
					-2.139949855704117
				],
				[
					-0.5349874639259724,
					-2.6749373196300894
				],
				[
					0,
					-3.209924783556062
				],
				[
					0.5349874639260861,
					-3.744912247482148
				],
				[
					1.0699749278521722,
					-4.27989971140812
				],
				[
					2.139949855704117,
					-4.814887175334206
				],
				[
					2.6749373196300894,
					-5.349874639260179
				],
				[
					3.7449122474822616,
					-6.419849567112237
				],
				[
					4.279899711408234,
					-7.489824494964296
				],
				[
					4.279899711408234,
					-8.55979942281624
				],
				[
					4.814887175334206,
					-9.6297743506683
				],
				[
					4.814887175334206,
					-10.164761814594272
				],
				[
					4.279899711408234,
					-11.23473674244633
				],
				[
					4.279899711408234,
					-12.304711670298389
				],
				[
					3.7449122474822616,
					-12.839699134224361
				],
				[
					3.7449122474822616,
					-13.374686598150447
				],
				[
					2.6749373196300894,
					-13.90967406207642
				],
				[
					2.139949855704117,
					-14.979648989928478
				],
				[
					1.0699749278521722,
					-14.979648989928478
				],
				[
					-0.5349874639259724,
					-15.51463645385445
				],
				[
					-1.6049623917779172,
					-16.049623917780536
				],
				[
					-2.6749373196300894,
					-16.049623917780536
				],
				[
					-3.744912247482034,
					-16.58461138170651
				],
				[
					-4.279899711408007,
					-16.58461138170651
				],
				[
					-4.814887175334093,
					-16.58461138170651
				],
				[
					-5.884862103186151,
					-16.58461138170651
				],
				[
					-6.419849567112124,
					-16.58461138170651
				],
				[
					-7.489824494964068,
					-17.11959884563248
				],
				[
					-8.55979942281624,
					-17.11959884563248
				],
				[
					-9.094786886742213,
					-16.58461138170651
				],
				[
					-10.164761814594158,
					-16.58461138170651
				],
				[
					-10.699749278520244,
					-16.049623917780536
				],
				[
					-11.23473674244633,
					-14.979648989928478
				],
				[
					-11.769724206372302,
					-13.90967406207642
				],
				[
					-12.304711670298275,
					-13.374686598150447
				],
				[
					-12.304711670298275,
					-12.839699134224361
				],
				[
					-12.304711670298275,
					-11.769724206372302
				],
				[
					-12.304711670298275,
					-11.23473674244633
				],
				[
					-12.304711670298275,
					-10.164761814594272
				],
				[
					-12.304711670298275,
					-9.6297743506683
				],
				[
					-12.304711670298275,
					-8.55979942281624
				],
				[
					-11.769724206372302,
					-8.024811958890268
				],
				[
					-11.23473674244633,
					-7.489824494964296
				],
				[
					-10.164761814594158,
					-6.95483703103821
				],
				[
					-9.629774350668185,
					-6.419849567112237
				],
				[
					-9.094786886742213,
					-6.419849567112237
				],
				[
					-8.024811958890155,
					-6.419849567112237
				],
				[
					-7.489824494964068,
					-6.419849567112237
				],
				[
					-6.954837031038096,
					-5.884862103186151
				],
				[
					-6.419849567112124,
					-5.349874639260179
				],
				[
					-6.419849567112124,
					-4.814887175334206
				],
				[
					-6.419849567112124,
					-4.27989971140812
				],
				[
					-6.419849567112124,
					-3.744912247482148
				],
				[
					-6.419849567112124,
					-3.209924783556062
				],
				[
					-6.954837031038096,
					-2.139949855704117
				],
				[
					-6.954837031038096,
					-1.0699749278520585
				],
				[
					-6.954837031038096,
					0
				],
				[
					-6.954837031038096,
					1.604962391778031
				],
				[
					-6.419849567112124,
					3.209924783556062
				],
				[
					-6.419849567112124,
					2.6749373196300894
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11133556813001633,
				0.09399499744176865,
				0.0924440324306488,
				0.09916561841964722,
				0.09083849936723709,
				0.108766570687294,
				0.11251184344291687,
				0.137131929397583,
				0.14548471570014954,
				0.15455938875675201,
				0.16393262147903442,
				0.16423119604587555,
				0.16352587938308716,
				0.1638292819261551,
				0.16283917427062988,
				0.16605371236801147,
				0.16257686913013458,
				0.16631203889846802,
				0.17205584049224854,
				0.1739061325788498,
				0.17526090145111084,
				0.17536835372447968,
				0.1792895793914795,
				0.18402454257011414,
				0.1943046599626541,
				0.19080035388469696,
				0.18814092874526978,
				0.1880403757095337,
				0.18179070949554443,
				0.19032086431980133,
				0.20562386512756348,
				0.20072278380393982,
				0.20747369527816772,
				0.20795898139476776,
				0.20175985991954803,
				0.20760692656040192,
				0.20803536474704742,
				0.21023309230804443,
				0.21842513978481293,
				0.2197873592376709,
				0.22246289253234863,
				0.22750577330589294,
				0.2269081473350525,
				0.22377951443195343,
				0.22640566527843475,
				0.2269558161497116,
				0.23103384673595428,
				0.22307009994983673,
				0.21602056920528412,
				0.22466814517974854,
				0.2287290096282959,
				0.23583047091960907,
				0.24043777585029602,
				0.24428582191467285,
				0.24322043359279633,
				0.23305730521678925,
				0.22214022278785706,
				0.23608218133449554,
				0.24504919350147247,
				0.26734212040901184,
				0.27742689847946167,
				0.28152963519096375,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 627996174,
			"isDeleted": false,
			"id": "WYoUv53d3nq9igv1lz1nz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -852.7343689860807,
			"y": -871.1972716211858,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.1399498557040033,
			"height": 5.884862103186151,
			"seed": 2062895053,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5349874639259724,
					0
				],
				[
					-1.6049623917779172,
					-0.5349874639259724
				],
				[
					-1.6049623917779172,
					-1.0699749278520585
				],
				[
					-2.1399498557040033,
					-2.139949855704117
				],
				[
					-2.1399498557040033,
					-4.814887175334093
				],
				[
					-2.1399498557040033,
					-5.884862103186151
				],
				[
					-2.1399498557040033,
					-5.884862103186151
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14078399538993835,
				0.2097959965467453,
				0.23262201249599457,
				0.19593793153762817,
				0.08504922688007355,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 124139986,
			"isDeleted": false,
			"id": "juQUrY4RW_Tsdg1kVT9wT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -850.0594316664506,
			"y": -874.9421838686678,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.0699749278519448,
			"height": 8.024811958890268,
			"seed": 1448741165,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5349874639259724,
					0
				],
				[
					-0.5349874639259724,
					-0.5349874639260861
				],
				[
					-0.5349874639259724,
					-3.744912247482148
				],
				[
					0,
					-7.489824494964296
				],
				[
					0.5349874639259724,
					-8.024811958890268
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09203982353210449,
				0.16271130740642548,
				0.17444919049739838,
				0.025996338576078415,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 881886286,
			"isDeleted": false,
			"id": "QjdA_jCtpIvvnbyW7yKVV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -845.2445444911164,
			"y": -877.0821337243719,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.6749373196300894,
			"height": 5.349874639260179,
			"seed": 637898189,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.0699749278519448,
					-3.209924783556062
				],
				[
					2.6749373196300894,
					-5.349874639260179
				],
				[
					2.6749373196300894,
					-5.349874639260179
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19444924592971802,
				0.04120919853448868,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 2112040850,
			"isDeleted": false,
			"id": "JMX3lx4xU2cL46_5MVdfR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -839.3596823879302,
			"y": -875.4771713325939,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.884862103186151,
			"height": 5.349874639260179,
			"seed": 2045922733,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5349874639259724
				],
				[
					1.0699749278519448,
					-1.0699749278520585
				],
				[
					5.884862103186151,
					-5.349874639260179
				],
				[
					5.884862103186151,
					-5.349874639260179
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12298397719860077,
				0.1669580042362213,
				0.15482687950134277,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 685165198,
			"isDeleted": false,
			"id": "PVmmxZ8ZPHYjU7NY6N0Yo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -831.3348704290399,
			"y": -875.4771713325939,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.209924783556062,
			"height": 1.604962391778031,
			"seed": 1361668077,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5349874639259724,
					0
				],
				[
					3.209924783556062,
					-1.604962391778031
				],
				[
					3.209924783556062,
					-1.604962391778031
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.03400442376732826,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 213609810,
			"isDeleted": false,
			"id": "o8pCsdpRZDxoqyI6XPzd9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -827.5899581815579,
			"y": -870.1272966933337,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.814887175334206,
			"height": 1.0699749278520585,
			"seed": 80335821,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5349874639259724,
					0.5349874639259724
				],
				[
					1.0699749278520585,
					0.5349874639259724
				],
				[
					4.27989971140812,
					1.0699749278520585
				],
				[
					4.814887175334206,
					1.0699749278520585
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13492199778556824,
				0.14051717519760132,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 22,
			"versionNonce": 1090144462,
			"isDeleted": false,
			"id": "khpe2btrj4ghurtfbzDcm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -890.4512262013386,
			"y": -777.8551016192031,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.480467528860459,
			"height": 12.80644415241727,
			"seed": 1735251469,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.3480467528861482,
					0
				],
				[
					-2.0220701293292223,
					0.6740233764429604
				],
				[
					-4.044140258658217,
					2.0220701293291086
				],
				[
					-4.718163635101291,
					6.066210387987212
				],
				[
					-2.6960935057721827,
					9.436327270202241
				],
				[
					2.022070129328995,
					9.436327270202241
				],
				[
					6.066210387987098,
					7.4142571408732465
				],
				[
					8.762303893759167,
					3.370116882215143
				],
				[
					8.762303893759167,
					-0.6740233764429604
				],
				[
					6.740233764430059,
					-2.696093505772069
				],
				[
					2.022070129328995,
					-3.3701168822150294
				],
				[
					-4.718163635101291,
					-0.6740233764429604
				],
				[
					-4.718163635101291,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0394979864358902,
				0.057880278676748276,
				0.1482040137052536,
				0.1858665496110916,
				0.20971903204917908,
				0.21676284074783325,
				0.20987991988658905,
				0.19222183525562286,
				0.18753808736801147,
				0.2109336256980896,
				0.22272567451000214,
				0.06819314509630203,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 18,
			"versionNonce": 424014610,
			"isDeleted": false,
			"id": "leD2cU6cAdVJx1StFK25R",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -895.8434132128829,
			"y": -767.7447509725578,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.7181636351011775,
			"height": 12.806444152417498,
			"seed": 1876384173,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6740233764429604,
					-0.6740233764430741
				],
				[
					-2.0220701293291086,
					-0.6740233764430741
				],
				[
					-2.0220701293291086,
					0
				],
				[
					-2.696093505772069,
					1.3480467528860345
				],
				[
					-2.696093505772069,
					5.392187011544138
				],
				[
					-2.0220701293291086,
					9.436327270202355
				],
				[
					0,
					12.132420775974424
				],
				[
					1.3480467528860345,
					11.45839739953135
				],
				[
					2.0220701293291086,
					11.45839739953135
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07806780934333801,
				0.1271454393863678,
				0.18059509992599487,
				0.23996371030807495,
				0.2982661724090576,
				0.3111123740673065,
				0.061288055032491684,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 2090073870,
			"isDeleted": false,
			"id": "Fuy4cO_EDsZGo2fXfjZTf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -884.3850158133515,
			"y": -769.7668211018868,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.0220701293291086,
			"height": 12.806444152417384,
			"seed": 1030643661,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6740233764429604,
					0
				],
				[
					1.3480467528860345,
					-0.6740233764430741
				],
				[
					1.3480467528860345,
					0.6740233764429604
				],
				[
					2.0220701293291086,
					6.740233764430172
				],
				[
					1.3480467528860345,
					11.45839739953135
				],
				[
					0.6740233764429604,
					12.13242077597431
				],
				[
					0.6740233764429604,
					11.45839739953135
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16909243166446686,
				0.21936599910259247,
				0.27922800183296204,
				0.29770326614379883,
				0.041831083595752716,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 1173995730,
			"isDeleted": false,
			"id": "68uDy-LpAzieP5DMcE69z",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -899.2135300950979,
			"y": -750.2201431850392,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.546677916847557,
			"height": 2.696093505772069,
			"seed": 274211117,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6740233764429604,
					-0.6740233764430741
				],
				[
					3.3701168822150294,
					-0.6740233764430741
				],
				[
					14.154490905303419,
					-2.696093505772069
				],
				[
					18.872654540404483,
					-2.696093505772069
				],
				[
					19.546677916847557,
					-2.022070129328995
				],
				[
					17.52460778751845,
					-2.696093505772069
				],
				[
					17.52460778751845,
					-2.696093505772069
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19991201162338257,
				0.240556001663208,
				0.38490599393844604,
				0.41685202717781067,
				0.3877321183681488,
				0.15634982287883759,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 1895758,
			"isDeleted": false,
			"id": "1yH9ASCq2gS5GoFI_GYvU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -871.5785716609341,
			"y": -777.1810782427601,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.850584411075488,
			"height": 18.198631163961636,
			"seed": 1565480589,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.022070129328995,
					2.0220701293291086
				],
				[
					6.740233764430286,
					6.066210387987212
				],
				[
					12.132420775974424,
					11.45839739953135
				],
				[
					16.850584411075488,
					17.524607787518562
				],
				[
					16.176561034632527,
					18.198631163961636
				],
				[
					16.176561034632527,
					17.524607787518562
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1544959992170334,
				0.24657635390758514,
				0.3070819675922394,
				0.329257994890213,
				0.054043885320425034,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 1315821202,
			"isDeleted": false,
			"id": "q-6svfSJ0u5Q5J3aC4ryK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -854.0539638734156,
			"y": -774.4849847369879,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.524607787518562,
			"height": 18.872654540404596,
			"seed": 1272330637,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.3480467528860345,
					0
				],
				[
					-4.7181636351011775,
					2.696093505772069
				],
				[
					-12.132420775974424,
					10.784374023088276
				],
				[
					-17.524607787518562,
					18.872654540404596
				],
				[
					-14.828514281746493,
					15.502537658189453
				],
				[
					-14.828514281746493,
					14.82851428174638
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15898950397968292,
				0.2997940182685852,
				0.3578380048274994,
				0.3961767852306366,
				0.14331036806106567,
				0
			]
		},
		{
			"type": "text",
			"version": 91,
			"versionNonce": 2028868494,
			"isDeleted": false,
			"id": "8RZLBkQm",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1435.9000436193073,
			"y": -597.9238920422423,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 73.179931640625,
			"height": 25,
			"seed": 33642,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "network",
			"rawText": "network",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "network",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 39,
			"versionNonce": 1666790482,
			"isDeleted": false,
			"id": "rKl_BwwSNgqrY3u6kppYM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1157.392457033615,
			"y": -606.4546509546549,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.327703591234922,
			"height": 32.58258416219542,
			"seed": 1812311405,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6788038367124045,
					0
				],
				[
					-2.0364115101372136,
					-2.0364115101372136
				],
				[
					-2.715215346849618,
					-4.072823020274427
				],
				[
					-0.6788038367124045,
					-8.824449877261259
				],
				[
					6.109234530411641,
					-12.218469060823281
				],
				[
					11.539665224110877,
					-11.539665224110877
				],
				[
					14.9336844076729,
					-8.145646040548854
				],
				[
					15.612488244385304,
					-3.3940191835620226
				],
				[
					14.254880570960495,
					0.6788038367124045
				],
				[
					11.539665224110877,
					4.072823020274427
				],
				[
					8.824449877261259,
					7.46684220383645
				],
				[
					7.46684220383645,
					10.182057550686068
				],
				[
					6.109234530411641,
					14.254880570960495
				],
				[
					4.751626856986832,
					16.970095917810113
				],
				[
					4.072823020274427,
					19.006507427947327
				],
				[
					4.072823020274427,
					20.364115101372136
				],
				[
					4.072823020274427,
					20.364115101372136
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14429669082164764,
				0.20201000571250916,
				0.2742699980735779,
				0.3363639712333679,
				0.35122814774513245,
				0.3480646014213562,
				0.3238886892795563,
				0.3050846755504608,
				0.331954687833786,
				0.3756205439567566,
				0.3927951753139496,
				0.41993415355682373,
				0.43782007694244385,
				0.3994126319885254,
				0.08529955893754959,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 25,
			"versionNonce": 21000654,
			"isDeleted": false,
			"id": "XhPFAbYjKAABaihsU1VEL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1156.7136531969027,
			"y": -569.799243772185,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.0364115101372136,
			"height": 0,
			"seed": 1282567821,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6788038367124045,
					0
				],
				[
					2.0364115101372136,
					0
				],
				[
					2.0364115101372136,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.474731981754303,
				0.327910840511322,
				0
			]
		},
		{
			"type": "text",
			"version": 68,
			"versionNonce": 110287378,
			"isDeleted": false,
			"id": "QOM3Bu4E",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1064.2793131888377,
			"y": -662.6618442994886,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 35.15997314453125,
			"height": 25,
			"seed": 15364,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "WiFi",
			"rawText": "WiFi",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "WiFi",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 30,
			"versionNonce": 70060046,
			"isDeleted": false,
			"id": "Q0ZCj4Up",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -976.7190567509283,
			"y": -725.5411813452835,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 44.919952392578125,
			"height": 25,
			"seed": 1602339309,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "pass",
			"rawText": "pass",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "pass",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 41,
			"versionNonce": 1729218514,
			"isDeleted": false,
			"id": "4anVgSzN",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -976.7190567509283,
			"y": -695.4805846099661,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 52.239959716796875,
			"height": 25,
			"seed": 22737,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "range",
			"rawText": "range",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "range",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 29,
			"versionNonce": 564975182,
			"isDeleted": false,
			"id": "hDYkATKL",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -979.3776520869103,
			"y": -666.1434097734723,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 52.659942626953125,
			"height": 25,
			"seed": 60224,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "power",
			"rawText": "power",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "power",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 1022164370,
			"isDeleted": false,
			"id": "xe0mNC6SqquHMeDV72i6h",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1134.858565175206,
			"y": -616.6976799686277,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 26.23996664945321,
			"height": 15.903010090577709,
			"seed": 28933069,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					3.180602018115678,
					-3.180602018115451
				],
				[
					16.69816059510663,
					-12.722408072462144
				],
				[
					23.854515135866677,
					-15.903010090577709
				],
				[
					26.23996664945321,
					-15.903010090577709
				],
				[
					23.854515135866677,
					-15.10785958604879
				],
				[
					23.854515135866677,
					-14.31270908151987
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17263711988925934,
				0.1932690143585205,
				0.1973043531179428,
				0.18490035831928253,
				0.15284350514411926,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 312007822,
			"isDeleted": false,
			"id": "zP2-GiZnI2FudJNUX24_c",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1101.4622439849927,
			"y": -640.5521951044942,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.54180605434658,
			"height": 12.722408072462144,
			"seed": 869736141,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7951505045289196,
					0
				],
				[
					3.180602018115678,
					0
				],
				[
					5.5660535317022095,
					0.7951505045289196
				],
				[
					9.54180605434658,
					2.385451513586645
				],
				[
					7.156354540760049,
					6.361204036231129
				],
				[
					2.3854515135867587,
					11.132107063404419
				],
				[
					1.590301009057839,
					12.722408072462144
				],
				[
					4.77090302717329,
					10.336956558875613
				],
				[
					5.5660535317022095,
					10.336956558875613
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14121472835540771,
				0.19329999387264252,
				0.21929998695850372,
				0.22218424081802368,
				0.2273278534412384,
				0.31737038493156433,
				0.32906171679496765,
				0.14196349680423737,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 626752338,
			"isDeleted": false,
			"id": "8VhOXCsfLPaJoOiqkOmyj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -904.3767943393332,
			"y": -693.6771574424345,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.402179206503774,
			"height": 17.402179206503888,
			"seed": 1698142445,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8286752003097035,
					0
				],
				[
					3.314700801238814,
					2.4860256009291106
				],
				[
					13.258803204955257,
					12.430128004645667
				],
				[
					17.402179206503774,
					17.402179206503888
				],
				[
					16.57350400619407,
					17.402179206503888
				],
				[
					15.744828805884367,
					16.57350400619407
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16240686178207397,
				0.24112017452716827,
				0.3330340087413788,
				0.3326379954814911,
				0.05052194371819496,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 212474574,
			"isDeleted": false,
			"id": "dHKHzGF6KOn3urrsj3Bg4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -886.9746151328294,
			"y": -692.8484822421248,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.744828805884367,
			"height": 15.744828805884481,
			"seed": 1871584237,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8286752003097035,
					-0.8286752003097035
				],
				[
					-1.657350400619407,
					-0.8286752003097035
				],
				[
					-7.458076802787332,
					3.314700801238814
				],
				[
					-14.916153605574664,
					12.430128004645553
				],
				[
					-15.744828805884367,
					14.916153605574777
				],
				[
					-13.258803204955257,
					13.25880320495537
				],
				[
					-13.258803204955257,
					12.430128004645553
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15874673426151276,
				0.28932997584342957,
				0.3653540015220642,
				0.32787883281707764,
				0.10609176754951477,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 32,
			"versionNonce": 2125742354,
			"isDeleted": false,
			"id": "UnibHB-KwRN5PXXQmBUl-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -981.443587968136,
			"y": -718.5374134517257,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.916153605574664,
			"height": 89.49692163344832,
			"seed": 681130317,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8286752003097035,
					0
				],
				[
					-2.4860256009291106,
					-0.8286752003097035
				],
				[
					-4.143376001548518,
					0
				],
				[
					-5.800726402167925,
					1.6573504006195208
				],
				[
					-6.629401602477628,
					8.286752003097149
				],
				[
					-6.629401602477628,
					19.059529607123295
				],
				[
					-5.800726402167925,
					29.003632010839738
				],
				[
					-6.629401602477628,
					34.80435841300766
				],
				[
					-9.115427203406739,
					37.29038401393689
				],
				[
					-9.944102403716442,
					38.11905921424648
				],
				[
					-8.286752003097035,
					38.11905921424648
				],
				[
					-5.800726402167925,
					39.776409614865884
				],
				[
					-4.972051201858221,
					41.43376001548529
				],
				[
					-5.800726402167925,
					43.919785616414515
				],
				[
					-6.629401602477628,
					46.405811217343626
				],
				[
					-9.115427203406739,
					51.37786241920185
				],
				[
					-10.772777604026146,
					58.007264021679475
				],
				[
					-13.258803204955257,
					64.63666562415722
				],
				[
					-14.916153605574664,
					70.43739202632503
				],
				[
					-14.916153605574664,
					76.23811842849307
				],
				[
					-14.087478405265074,
					81.21016963035129
				],
				[
					-11.60145280433585,
					86.18222083220951
				],
				[
					-7.458076802787332,
					88.66824643313862
				],
				[
					-4.143376001548518,
					88.66824643313862
				],
				[
					-4.143376001548518,
					87.83957123282892
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1372774988412857,
				0.2110319882631302,
				0.2314019799232483,
				0.2833903729915619,
				0.26733919978141785,
				0.2706003189086914,
				0.2664182782173157,
				0.2782420814037323,
				0.2780096232891083,
				0.25257524847984314,
				0.2591642439365387,
				0.2990639805793762,
				0.3182121813297272,
				0.32034236192703247,
				0.3120010495185852,
				0.32062435150146484,
				0.35262638330459595,
				0.35919955372810364,
				0.36664044857025146,
				0.37122642993927,
				0.4102003574371338,
				0.39250707626342773,
				0.1926577091217041,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 9,
			"versionNonce": 645501198,
			"isDeleted": false,
			"id": "o3eqS0DPyrOBNszqQMRvC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1051.880979994461,
			"y": -672.9602774346918,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8286752003095899,
			"height": 0,
			"seed": 1738819949,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8286752003095899,
					0
				],
				[
					-0.8286752003095899,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.5427780151367188,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 1148079826,
			"isDeleted": false,
			"id": "bU6Mmeg073CQNh4lkTPhp",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1057.681706396629,
			"y": -675.446303035621,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.087478405265074,
			"height": 6.629401602477628,
			"seed": 553757421,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8286752003098172,
					0
				],
				[
					-0.8286752003098172,
					-0.8286752003095899
				],
				[
					0.8286752003095899,
					-2.486025600928997
				],
				[
					6.629401602477628,
					-5.800726402167811
				],
				[
					11.60145280433585,
					-6.629401602477628
				],
				[
					13.258803204955257,
					-5.800726402167811
				],
				[
					11.60145280433585,
					-4.972051201858221
				],
				[
					11.60145280433585,
					-4.972051201858221
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06476278603076935,
				0.1490972936153412,
				0.18450967967510223,
				0.28220000863075256,
				0.34126198291778564,
				0.37930557131767273,
				0.08893154561519623,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 998260558,
			"isDeleted": false,
			"id": "8Wy6TCUjSBfza24xlckjm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1063.482432798797,
			"y": -682.9043798384082,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.059529607123295,
			"height": 6.629401602477742,
			"seed": 1010521773,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8286752003098172,
					0
				],
				[
					7.458076802787446,
					-4.143376001548631
				],
				[
					14.916153605574664,
					-6.629401602477742
				],
				[
					19.059529607123295,
					-6.629401602477742
				],
				[
					19.059529607123295,
					-5.8007264021680385
				],
				[
					18.230854406813478,
					-4.143376001548631
				],
				[
					17.402179206503888,
					-4.143376001548631
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16290198266506195,
				0.2648559808731079,
				0.3296020030975342,
				0.3526214361190796,
				0.355250746011734,
				0.12357183545827866,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 1797301394,
			"isDeleted": false,
			"id": "ZtCmh3B5x97ohfwNrd5uW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1069.2831592009647,
			"y": -691.1911318415054,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 30.660982411459372,
			"height": 9.115427203406739,
			"seed": 1026710541,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8286752003098172,
					0
				],
				[
					-1.6573504006196345,
					0
				],
				[
					-0.8286752003098172,
					-0.8286752003097035
				],
				[
					7.458076802787218,
					-4.143376001548518
				],
				[
					19.059529607123295,
					-8.286752003097035
				],
				[
					25.688931209600923,
					-9.115427203406739
				],
				[
					27.346281610220103,
					-9.115427203406739
				],
				[
					28.17495681052992,
					-9.115427203406739
				],
				[
					29.003632010839738,
					-9.115427203406739
				],
				[
					29.003632010839738,
					-8.286752003097035
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07440798729658127,
				0.09366799890995026,
				0.1986359804868698,
				0.312144011259079,
				0.3971700072288513,
				0.4562620222568512,
				0.4665590822696686,
				0.43524885177612305,
				0.34377261996269226,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 18,
			"versionNonce": 1343694222,
			"isDeleted": false,
			"id": "Y3wBEZp1-S0sK6sGoHhQk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1139.9543306546968,
			"y": -634.1339881755969,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.791395072829118,
			"height": 12.791395072829118,
			"seed": 1675710605,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6732313196225732
				],
				[
					0,
					0
				],
				[
					0.6732313196225732,
					-1.3464626392451464
				],
				[
					3.3661565981130934,
					-4.039387917735439
				],
				[
					6.059081876603386,
					-4.7126192373580125
				],
				[
					8.752007155093679,
					-2.0196939588677196
				],
				[
					10.771701113961399,
					-2.0196939588677196
				],
				[
					12.118163753206545,
					-8.078775835471106
				],
				[
					12.118163753206545,
					-11.444932433583972
				],
				[
					12.791395072829118,
					-12.118163753206545
				],
				[
					12.791395072829118,
					-11.444932433583972
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1291191726922989,
				0.2778320014476776,
				0.3149139881134033,
				0.33999398350715637,
				0.33020737767219543,
				0.3294227123260498,
				0.3399568796157837,
				0.37630343437194824,
				0.3541467487812042,
				0.11373592913150787,
				0
			]
		},
		{
			"type": "text",
			"version": 43,
			"versionNonce": 1015169618,
			"isDeleted": false,
			"id": "a2rhynni",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1025.6014054497111,
			"y": -621.7766660348728,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 95.67988586425781,
			"height": 25,
			"seed": 42350,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "sometimes",
			"rawText": "sometimes",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "sometimes",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 1970750414,
			"isDeleted": false,
			"id": "2uFPVwraoT9voMDqSuOz5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1034.0513120303108,
			"y": -634.5169070072145,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.955756523220543,
			"height": 8.296463769350567,
			"seed": 1626240355,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8296463769349884,
					0
				],
				[
					-0.8296463769349884,
					0.8296463769351021
				],
				[
					0,
					2.4889391308051927
				],
				[
					4.14823188467517,
					6.637171015480362
				],
				[
					7.466817392415578,
					8.296463769350567
				],
				[
					9.126110146285555,
					8.296463769350567
				],
				[
					8.296463769350567,
					7.466817392415464
				],
				[
					8.296463769350567,
					6.637171015480362
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15469598770141602,
				0.1947707235813141,
				0.19261959195137024,
				0.26703041791915894,
				0.2857944071292877,
				0.29556557536125183,
				0.22729019820690155,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 862595090,
			"isDeleted": false,
			"id": "3NLb_yx80pjpeVJr4mf8F",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1028.2437873917654,
			"y": -624.561150483994,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.296463769350567,
			"height": 14.103988407895827,
			"seed": 1064805795,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.4889391308051927,
					1.6592927538702043
				],
				[
					5.807524638545374,
					4.148231884675397
				],
				[
					8.296463769350567,
					4.977878261610385
				],
				[
					8.296463769350567,
					4.148231884675397
				],
				[
					8.296463769350567,
					2.4889391308051927
				],
				[
					7.466817392415464,
					-1.6592927538699769
				],
				[
					7.466817392415464,
					-5.80752463854526
				],
				[
					7.466817392415464,
					-8.29646376935034
				],
				[
					7.466817392415464,
					-9.126110146285441
				],
				[
					7.466817392415464,
					-8.29646376935034
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.23474954068660736,
				0.27742505073547363,
				0.26852571964263916,
				0.25159451365470886,
				0.27505338191986084,
				0.2671191394329071,
				0.28595906496047974,
				0.3202604353427887,
				0.3332275152206421,
				0
			]
		},
		{
			"type": "text",
			"version": 22,
			"versionNonce": 767138318,
			"isDeleted": false,
			"id": "zLaC0RlH",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1124.831570894316,
			"y": -484.6713768593335,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 117.87986755371094,
			"height": 25,
			"seed": 93475,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "proliferation",
			"rawText": "proliferation",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "proliferation",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 21,
			"versionNonce": 1473205714,
			"isDeleted": false,
			"id": "RPc59VOP",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -949.4949263242471,
			"y": -571.4771405202515,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 96.73989868164062,
			"height": 75,
			"seed": 52974,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Zigbee\n6LowPAN\nBluethoot",
			"rawText": "Zigbee\n6LowPAN\nBluethoot",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "Zigbee\n6LowPAN\nBluethoot",
			"lineHeight": 1.25,
			"baseline": 68
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 1339500622,
			"isDeleted": false,
			"id": "LkNdxkCWPzV0aJhXX1OxZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -947.4381644921732,
			"y": -486.41519795102903,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.77409347772209,
			"height": 1.8493956518147456,
			"seed": 1223565187,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.9246978259074012,
					0
				],
				[
					1.8493956518148025,
					-0.9246978259073444
				],
				[
					2.77409347772209,
					-1.8493956518147456
				],
				[
					1.8493956518148025,
					-0.9246978259073444
				],
				[
					1.8493956518148025,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07463400065898895,
				0.12883025407791138,
				0.1766842007637024,
				0.05752658098936081,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 449366930,
			"isDeleted": false,
			"id": "99hRhhccgdx-y_7bSq8tE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -939.1158840590069,
			"y": -489.1892914287511,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.6234891295368925,
			"height": 4.623489129536836,
			"seed": 710426851,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.9246978259073444
				],
				[
					0.9246978259074012,
					1.8493956518147456
				],
				[
					1.8493956518148025,
					2.77409347772209
				],
				[
					2.77409347772209,
					2.77409347772209
				],
				[
					4.6234891295368925,
					1.8493956518147456
				],
				[
					4.6234891295368925,
					-0.9246978259073444
				],
				[
					3.6987913036294913,
					-1.8493956518147456
				],
				[
					4.6234891295368925,
					-0.9246978259073444
				],
				[
					4.6234891295368925,
					-0.9246978259073444
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08959997445344925,
				0.11375469714403152,
				0.11848916858434677,
				0.1342950165271759,
				0.1891421526670456,
				0.20289859175682068,
				0.034855011850595474,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 1806233230,
			"isDeleted": false,
			"id": "RsimQu8C0m7AOS7zvvOSu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -925.2454166703965,
			"y": -490.11398925465846,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.6234891295368925,
			"height": 0.9246978259073444,
			"seed": 1390998723,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9246978259074012,
					0
				],
				[
					-0.9246978259074012,
					0.9246978259073444
				],
				[
					0,
					0.9246978259073444
				],
				[
					1.8493956518146888,
					0.9246978259073444
				],
				[
					2.77409347772209,
					0
				],
				[
					2.77409347772209,
					0.9246978259073444
				],
				[
					3.6987913036294913,
					0.9246978259073444
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09797598421573639,
				0.15704001486301422,
				0.15188924968242645,
				0.10517901927232742,
				0.09585348516702652,
				0.02782580628991127,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 848136530,
			"isDeleted": false,
			"id": "Y7mCDWV0m_VZMOmNlSfc5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -911.374949281786,
			"y": -490.11398925465846,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.472884781351581,
			"height": 0.9246978259073444,
			"seed": 1945014627,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9246978259074012,
					0
				],
				[
					0.9246978259072876,
					0.9246978259073444
				],
				[
					4.623489129536779,
					0.9246978259073444
				],
				[
					5.54818695544418,
					0
				],
				[
					4.623489129536779,
					0
				],
				[
					5.54818695544418,
					0
				],
				[
					5.54818695544418,
					0.9246978259073444
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10223397612571716,
				0.13906630873680115,
				0.11675570905208588,
				0.18969348073005676,
				0.27264171838760376,
				0.08679089695215225,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 770174158,
			"isDeleted": false,
			"id": "Zl9WUmiSltVWsSTAfZ3V8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -893.8056905895462,
			"y": -491.03868708056586,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.54818695544418,
			"height": 1.8493956518147456,
			"seed": 1028454915,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9246978259074012,
					0.9246978259074012
				],
				[
					-0.9246978259074012,
					1.8493956518147456
				],
				[
					0,
					1.8493956518147456
				],
				[
					3.6987913036294913,
					0.9246978259074012
				],
				[
					4.623489129536779,
					0
				],
				[
					3.6987913036294913,
					0.9246978259074012
				],
				[
					2.77409347772209,
					0.9246978259074012
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1398070752620697,
				0.14119036495685577,
				0.08995162695646286,
				0.13214761018753052,
				0.16339947283267975,
				0
			]
		},
		{
			"type": "text",
			"version": 21,
			"versionNonce": 1987350290,
			"isDeleted": false,
			"id": "k5iEGxP8",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -964.0132143412925,
			"y": -410.2419158019337,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 140.33984375,
			"height": 25,
			"seed": 22875,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "different uses",
			"rawText": "different uses",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "different uses",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 1143808782,
			"isDeleted": false,
			"id": "M0JrBpgm6ojXQmEQKg4TK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1151.308249285686,
			"y": -550.8463481037998,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.101696137931413,
			"height": 36.8103843362079,
			"seed": 918931779,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9438560086205143,
					0
				],
				[
					-1.887712017241256,
					0
				],
				[
					-1.887712017241256,
					2.831568025862225
				],
				[
					0,
					12.270128112069415
				],
				[
					4.7192800431037085,
					25.484112232759344
				],
				[
					9.43856008620719,
					33.03496030172505
				],
				[
					12.270128112069415,
					36.8103843362079
				],
				[
					13.213984120690156,
					36.8103843362079
				],
				[
					13.213984120690156,
					36.8103843362079
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15730798244476318,
				0.21087408065795898,
				0.281525194644928,
				0.36248600482940674,
				0.4272639751434326,
				0.42793896794319153,
				0.1377377063035965,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 989125842,
			"isDeleted": false,
			"id": "UkqJMyC81WTqVIFKzltph",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1139.9819771822374,
			"y": -501.76583565552255,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.045552146552154,
			"height": 19.820976181035007,
			"seed": 824736035,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9438560086207417,
					0
				],
				[
					0,
					0.9438560086206849
				],
				[
					4.7192800431037085,
					6.606992060344965
				],
				[
					8.494704077586448,
					11.32627210344856
				],
				[
					9.43856008620719,
					9.438560086207133
				],
				[
					11.326272103448673,
					1.8877120172414266
				],
				[
					13.213984120690156,
					-6.606992060345021
				],
				[
					15.101696137931413,
					-7.550848068965706
				],
				[
					15.101696137931413,
					-8.494704077586448
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07788287103176117,
				0.1488959938287735,
				0.22398801147937775,
				0.2737221121788025,
				0.2819201350212097,
				0.2699682116508484,
				0.23167361319065094,
				0.053261350840330124,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 26,
			"versionNonce": 1089573198,
			"isDeleted": false,
			"id": "wGJz44Ea9dhKNvqN1cMPh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -958.7616235270602,
			"y": -565.0041882331104,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.21398412068993,
			"height": 72.67691266379501,
			"seed": 1591006467,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9438560086207417,
					0
				],
				[
					-2.831568025862225,
					0
				],
				[
					-6.606992060344965,
					0.9438560086207417
				],
				[
					-9.43856008620719,
					3.775424034482853
				],
				[
					-9.43856008620719,
					12.270128112069301
				],
				[
					-7.550848068965706,
					20.76483218965575
				],
				[
					-5.6631360517243365,
					29.259536267242083
				],
				[
					-5.6631360517243365,
					33.97881631034579
				],
				[
					-6.606992060344965,
					34.92267231896642
				],
				[
					-5.6631360517243365,
					33.97881631034579
				],
				[
					-4.719280043103595,
					33.03496030172505
				],
				[
					-3.775424034482967,
					35.86652832758716
				],
				[
					-6.606992060344965,
					42.473520387932126
				],
				[
					-8.494704077586448,
					50.968224465518574
				],
				[
					-8.494704077586448,
					58.51907253448428
				],
				[
					-5.6631360517243365,
					66.06992060344999
				],
				[
					-0.9438560086207417,
					71.73305665517427
				],
				[
					2.8315680258621114,
					72.67691266379501
				],
				[
					3.7754240344827394,
					71.73305665517427
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08186200261116028,
				0.10728000104427338,
				0.17875799536705017,
				0.21127423644065857,
				0.22227011620998383,
				0.23161225020885468,
				0.23588943481445312,
				0.23153500258922577,
				0.21591509878635406,
				0.1940767467021942,
				0.18561764061450958,
				0.2557262182235718,
				0.2875923812389374,
				0.29426661133766174,
				0.29712992906570435,
				0.3323447108268738,
				0.32312193512916565,
				0.14014306664466858,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 765817490,
			"isDeleted": false,
			"id": "1j-m-_W_MssMGblYlgqdH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1007.8421359753374,
			"y": -486.66413951759114,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 24.540256224138602,
			"height": 31.147248284483567,
			"seed": 182725923,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9438560086207417,
					0
				],
				[
					-0.9438560086207417,
					-0.9438560086206849
				],
				[
					0,
					-3.775424034482853
				],
				[
					7.550848068965706,
					-15.101696137931413
				],
				[
					16.045552146552154,
					-25.484112232759344
				],
				[
					22.65254420689712,
					-31.147248284483567
				],
				[
					23.59640021551786,
					-30.203392275862825
				],
				[
					23.59640021551786,
					-30.203392275862825
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.044534239917993546,
				0.09692084044218063,
				0.1347760558128357,
				0.20571663975715637,
				0.2579480707645416,
				0.2966870963573456,
				0.10105926543474197,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 2140026766,
			"isDeleted": false,
			"id": "flYe1kkzD9BOx-xourdVi",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -998.4035758891303,
			"y": -447.96604316414187,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.87712017241438,
			"height": 30.203392275862882,
			"seed": 748596579,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9438560086207417,
					0
				],
				[
					-1.8877120172414834,
					3.775424034482853
				],
				[
					-1.8877120172414834,
					6.606992060345021
				],
				[
					0,
					11.32627210344856
				],
				[
					6.606992060344965,
					20.764832189655692
				],
				[
					13.21398412068993,
					28.315680258621455
				],
				[
					16.989408155172896,
					30.203392275862882
				],
				[
					16.989408155172896,
					29.25953626724214
				],
				[
					16.045552146552154,
					28.315680258621455
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14776135981082916,
				0.22111496329307556,
				0.2675269842147827,
				0.37116798758506775,
				0.45270800590515137,
				0.4594030976295471,
				0.20591381192207336,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 826101842,
			"isDeleted": false,
			"id": "yMfax05DZ_YZk9jfUqT_1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -976.6948876908539,
			"y": -422.4819309313826,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.32627210344856,
			"height": 14.157840129310728,
			"seed": 446443843,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.8877120172414834,
					2.8315680258621683
				],
				[
					5.663136051724223,
					6.606992060345021
				],
				[
					8.494704077586448,
					9.438560086207133
				],
				[
					7.550848068965706,
					10.382416094827875
				],
				[
					1.8877120172414834,
					12.270128112069301
				],
				[
					-2.8315680258621114,
					14.157840129310728
				],
				[
					-1.8877120172414834,
					14.157840129310728
				],
				[
					-1.8877120172414834,
					13.213984120689986
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2166219800710678,
				0.2491600066423416,
				0.22357964515686035,
				0.23213934898376465,
				0.325420081615448,
				0.3982580304145813,
				0.15949545800685883,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 138155470,
			"isDeleted": false,
			"id": "s3tbasNC3cnwgFxqO5JOx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -984.2457357598196,
			"y": -526.3060918796612,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.382416094827931,
			"height": 14.15784012931067,
			"seed": 1655048579,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					4.719280043103595,
					0
				],
				[
					10.382416094827931,
					1.8877120172414834
				],
				[
					10.382416094827931,
					9.43856008620719
				],
				[
					7.550848068965706,
					14.15784012931067
				],
				[
					9.43856008620719,
					12.270128112069301
				],
				[
					9.43856008620719,
					12.270128112069301
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.24934600293636322,
				0.2544962763786316,
				0.31503912806510925,
				0.41232597827911377,
				0.10576415807008743,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 965965330,
			"isDeleted": false,
			"id": "HSuLJu1pQqcgMpWhO1jbK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -901.1864070011967,
			"y": -475.3378674141426,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.8877120172414834,
			"height": 25.484112232759287,
			"seed": 800200323,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9438560086207417,
					0
				],
				[
					-0.9438560086207417,
					1.8877120172414266
				],
				[
					-0.9438560086207417,
					5.66313605172428
				],
				[
					0,
					17.93326416379358
				],
				[
					0.9438560086207417,
					25.484112232759287
				],
				[
					0,
					25.484112232759287
				],
				[
					0,
					24.540256224138602
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.24407458305358887,
				0.32595929503440857,
				0.4262300133705139,
				0.4855020046234131,
				0.19441385567188263,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 1947479054,
			"isDeleted": false,
			"id": "fZsB4dRC_cFazxZVbYM1_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -905.9056870443003,
			"y": -440.41519509517616,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.989408155172896,
			"height": 24.540256224138545,
			"seed": 1842854691,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9438560086207417,
					0
				],
				[
					0,
					1.8877120172414266
				],
				[
					3.775424034482853,
					8.494704077586448
				],
				[
					6.606992060344965,
					11.32627210344856
				],
				[
					8.494704077586448,
					6.606992060345021
				],
				[
					10.382416094827818,
					-1.8877120172414266
				],
				[
					13.213984120690043,
					-7.550848068965706
				],
				[
					15.101696137931413,
					-10.382416094827818
				],
				[
					16.045552146552154,
					-13.213984120689986
				],
				[
					16.045552146552154,
					-13.213984120689986
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1545020192861557,
				0.26765599846839905,
				0.3530519902706146,
				0.3802103102207184,
				0.3555421233177185,
				0.3311654329299927,
				0.2618859112262726,
				0.13956427574157715,
				0.02866549603641033,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 20,
			"versionNonce": 664724434,
			"isDeleted": false,
			"id": "1RG2GItUPCDCqvjdUkUSF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1231.5999968044152,
			"y": -901.9176529750417,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.355358193698066,
			"height": 66.51178998770479,
			"seed": 372604579,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.0903572129132044,
					0
				],
				[
					-2.180714425826409,
					1.0903572129132044
				],
				[
					-2.180714425826409,
					2.180714425826409
				],
				[
					-2.180714425826409,
					4.361428851652818
				],
				[
					-1.0903572129132044,
					13.08428655495834
				],
				[
					1.0903572129132044,
					25.078215897003474
				],
				[
					4.361428851652818,
					35.981788026135405
				],
				[
					6.5421432774792265,
					45.79500294235413
				],
				[
					9.81321491621884,
					56.69857507148606
				],
				[
					11.993929342045249,
					63.24071834896529
				],
				[
					14.174643767871657,
					66.51178998770479
				],
				[
					13.084286554958453,
					63.24071834896529
				],
				[
					13.084286554958453,
					62.150361136052084
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15665240585803986,
				0.20949798822402954,
				0.24604398012161255,
				0.31998199224472046,
				0.37603670358657837,
				0.42752715945243835,
				0.4595161974430084,
				0.487602561712265,
				0.5169863104820251,
				0.5130560398101807,
				0.16845673322677612,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 1359968846,
			"isDeleted": false,
			"id": "Ot5IDaQMRVVrpJxRg8KnC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1226.1482107398492,
			"y": -831.0444341356841,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.355358193698066,
			"height": 19.626429832437452,
			"seed": 2017554691,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					3.2710716387396133,
					3.2710716387394996
				],
				[
					5.451786064566022,
					6.542143277479113
				],
				[
					9.81321491621884,
					11.993929342045135
				],
				[
					11.993929342045249,
					10.90357212913193
				],
				[
					11.993929342045249,
					4.361428851652704
				],
				[
					14.174643767871657,
					-5.451786064565908
				],
				[
					16.355358193698066,
					-7.632500490392317
				],
				[
					16.355358193698066,
					-7.632500490392317
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.21023999154567719,
				0.25024598836898804,
				0.3077319860458374,
				0.2934601902961731,
				0.30234354734420776,
				0.39720138907432556,
				0.3407910466194153,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 628529554,
			"isDeleted": false,
			"id": "ClvV9QxtJMAdob3cKWqlc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1370.0753628443908,
			"y": -762.351929722153,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 59.96964671022579,
			"height": 18.536072619524248,
			"seed": 120756547,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862184,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.0903572129132044,
					0
				],
				[
					-2.180714425826409,
					0
				],
				[
					3.2710716387396133,
					0
				],
				[
					16.355358193698066,
					-3.2710716387394996
				],
				[
					37.07214523904872,
					-10.903572129131817
				],
				[
					51.24678900692015,
					-16.35535819369784
				],
				[
					57.78893228439938,
					-18.536072619524248
				],
				[
					56.698575071486175,
					-18.536072619524248
				],
				[
					56.698575071486175,
					-18.536072619524248
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14226700365543365,
				0.3577140271663666,
				0.45786598324775696,
				0.5373439788818359,
				0.5432420372962952,
				0.49940043687820435,
				0.14876247942447662,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 101122190,
			"isDeleted": false,
			"id": "ak4wfbyROSFs1_5urToGR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1306.8346444954254,
			"y": -789.6108600449828,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.265000980784635,
			"height": 13.08428655495834,
			"seed": 423053603,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.0903572129132044,
					0
				],
				[
					1.0903572129132044,
					0
				],
				[
					7.632500490392204,
					0
				],
				[
					14.17464376787143,
					2.180714425826409
				],
				[
					14.17464376787143,
					5.451786064565908
				],
				[
					9.813214916218612,
					10.90357212913193
				],
				[
					6.542143277478999,
					13.08428655495834
				],
				[
					9.813214916218612,
					9.813214916218726
				],
				[
					9.813214916218612,
					8.722857703305522
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.3682340085506439,
				0.41842401027679443,
				0.4121840298175812,
				0.4731220006942749,
				0.5686509013175964,
				0.6313490271568298,
				0.2139584720134735,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 20,
			"versionNonce": 38901586,
			"isDeleted": false,
			"id": "Vn9LTw7ds5EnHfrdRsTWj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1141.1003481326202,
			"y": -785.2494311933301,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 54.517860645659766,
			"height": 34.891430813222314,
			"seed": 667264259,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.0903572129132044
				],
				[
					-1.0903572129132044,
					3.2710716387396133
				],
				[
					1.0903572129132044,
					9.81321491621884
				],
				[
					4.361428851652818,
					18.53607261952436
				],
				[
					9.81321491621884,
					26.16857310991668
				],
				[
					17.44571540661127,
					32.710716387395905
				],
				[
					26.16857310991668,
					33.80107360030911
				],
				[
					37.072145239048496,
					34.891430813222314
				],
				[
					45.79500294235413,
					33.80107360030911
				],
				[
					51.24678900692015,
					33.80107360030911
				],
				[
					53.42750343274656,
					33.80107360030911
				],
				[
					52.33714621983336,
					33.80107360030911
				],
				[
					52.33714621983336,
					33.80107360030911
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15504498779773712,
				0.3360440135002136,
				0.424811989068985,
				0.4845529794692993,
				0.50542151927948,
				0.5397263765335083,
				0.5661429166793823,
				0.5799447298049927,
				0.5634494423866272,
				0.572677493095398,
				0.5964518189430237,
				0.24701638519763947,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 18,
			"versionNonce": 917749454,
			"isDeleted": false,
			"id": "tdMdE3bm8cJGDljbe8VON",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1075.6789153578284,
			"y": -760.1712152963266,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.084286554958226,
			"height": 15.265000980784748,
			"seed": 84812643,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.0903572129132044,
					0
				],
				[
					-3.2710716387396133,
					0
				],
				[
					-3.2710716387396133,
					1.0903572129132044
				],
				[
					1.090357212912977,
					2.180714425826409
				],
				[
					5.451786064565795,
					4.361428851652818
				],
				[
					8.722857703305408,
					6.5421432774792265
				],
				[
					9.813214916218612,
					8.722857703305635
				],
				[
					4.36142885165259,
					11.993929342045249
				],
				[
					-1.0903572129132044,
					15.265000980784748
				],
				[
					-2.180714425826409,
					15.265000980784748
				],
				[
					-2.180714425826409,
					14.174643767871544
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05133099481463432,
				0.12496798485517502,
				0.22273001074790955,
				0.3091059923171997,
				0.34169647097587585,
				0.3039226830005646,
				0.30620262026786804,
				0.3770217001438141,
				0.4568787217140198,
				0.14955756068229675,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 243719442,
			"isDeleted": false,
			"id": "U8aAjBoGVT30cZterzSDJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1022.251411925082,
			"y": -768.894072999632,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.0903572129132044,
			"height": 15.265000980784862,
			"seed": 1315746435,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1.0903572129132044
				],
				[
					0,
					-3.2710716387396133
				],
				[
					1.0903572129132044,
					-8.722857703305635
				],
				[
					1.0903572129132044,
					-15.265000980784862
				],
				[
					1.0903572129132044,
					-15.265000980784862
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.25779998302459717,
				0.2917660176753998,
				0.3477819859981537,
				0.03718334808945656,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 665761038,
			"isDeleted": false,
			"id": "pIvORUNLK5KOnXhgIGq5P",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1022.251411925082,
			"y": -791.7915744708091,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 10.903572129132044,
			"seed": 2122986467,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1.0903572129132044
				],
				[
					0,
					-2.180714425826409
				],
				[
					0,
					-4.361428851652818
				],
				[
					0,
					-7.632500490392431
				],
				[
					0,
					-9.81321491621884
				],
				[
					0,
					-10.903572129132044
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.22127951681613922,
				0.27127599716186523,
				0.2952579855918884,
				0.2634977400302887,
				0.04370477423071861,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 2005756626,
			"isDeleted": false,
			"id": "SP3QYQ9hHPQNQKf4bNwsl",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1024.4321263509084,
			"y": -810.3276470903335,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.0903572129132044,
			"height": 6.542143277479113,
			"seed": 1056825571,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1.0903572129132044
				],
				[
					0,
					-2.180714425826409
				],
				[
					1.0903572129132044,
					-6.542143277479113
				],
				[
					1.0903572129132044,
					-6.542143277479113
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.23838672041893005,
				0.2516680061817169,
				0.09772384911775589,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 577823566,
			"isDeleted": false,
			"id": "sQVbFaFMkaSW6jvv7U0wz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1030.9742696283874,
			"y": -819.050504793639,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.084286554958112,
			"height": 13.08428655495834,
			"seed": 1024891555,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.0903572129132044,
					0
				],
				[
					-1.0903572129132044,
					-1.0903572129132044
				],
				[
					0,
					-2.180714425826409
				],
				[
					2.1807144258261815,
					-8.722857703305635
				],
				[
					4.36142885165259,
					-13.08428655495834
				],
				[
					6.542143277478999,
					-13.08428655495834
				],
				[
					8.722857703305408,
					-8.722857703305635
				],
				[
					10.903572129131817,
					-3.2710716387396133
				],
				[
					11.993929342044908,
					-2.180714425826409
				],
				[
					11.993929342044908,
					-3.2710716387396133
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09717172384262085,
				0.18101999163627625,
				0.2010720819234848,
				0.23571902513504028,
				0.26441580057144165,
				0.3042733669281006,
				0.3790286183357239,
				0.4256923794746399,
				0.12353415042161942,
				0
			]
		},
		{
			"type": "text",
			"version": 22,
			"versionNonce": 603734162,
			"isDeleted": false,
			"id": "lijr2MBt",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1478.2970556398097,
			"y": -428.97884439549875,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 120.71987915039062,
			"height": 25,
			"seed": 97609,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "architecture",
			"rawText": "architecture",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "architecture",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 56,
			"versionNonce": 1498630542,
			"isDeleted": false,
			"id": "5FsaofXo",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1253.7087243153753,
			"y": -608.4627539813075,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 78.29991149902344,
			"height": 25,
			"seed": 31373,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "protocol",
			"rawText": "protocol",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "protocol",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 19,
			"versionNonce": 260726354,
			"isDeleted": false,
			"id": "rraNnZPTWBiznCebMoGpb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1419.328718551108,
			"y": -736.0888425787643,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 21.890554817341126,
			"height": 86.61045601643639,
			"seed": 1588600451,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.9035265058560071,
					2.855289758783556
				],
				[
					3.8070530117115595,
					5.710579517567226
				],
				[
					7.614106023423119,
					16.179975299773787
				],
				[
					12.372922288062455,
					29.504660840764018
				],
				[
					16.179975299774014,
					42.82934638175425
				],
				[
					18.083501805629567,
					54.2505054168887
				],
				[
					19.987028311485574,
					68.52695421080671
				],
				[
					20.93879156441335,
					78.99634999301338
				],
				[
					21.890554817341126,
					85.6586927635085
				],
				[
					21.890554817341126,
					86.61045601643639
				],
				[
					19.987028311485574,
					86.61045601643639
				],
				[
					19.987028311485574,
					85.6586927635085
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1707456409931183,
				0.1981324404478073,
				0.23662905395030975,
				0.2664489150047302,
				0.29158470034599304,
				0.3076908588409424,
				0.3351227641105652,
				0.3526157736778259,
				0.33870527148246765,
				0.2946697473526001,
				0.0639943853020668,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 1267656654,
			"isDeleted": false,
			"id": "RbrEiC8QtvgfPimND-Ttk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1410.7628492747572,
			"y": -639.0089907801214,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.179975299774014,
			"height": 18.083501805629567,
			"seed": 471821635,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					3.8070530117115595,
					6.6623427704951155
				],
				[
					6.662342770495343,
					14.27644879391812
				],
				[
					8.565869276350895,
					18.083501805629567
				],
				[
					8.565869276350895,
					15.22821204684601
				],
				[
					10.469395782206675,
					9.517632529278671
				],
				[
					13.324685540990231,
					4.758816264639336
				],
				[
					16.179975299774014,
					1.9035265058557798
				],
				[
					16.179975299774014,
					1.9035265058557798
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2764774262905121,
				0.30079975724220276,
				0.29743266105651855,
				0.2896440029144287,
				0.314857542514801,
				0.3527412414550781,
				0.37173616886138916,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 655279122,
			"isDeleted": false,
			"id": "ouabfw7jZYqKagPKSAth7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1348.8982378344454,
			"y": -583.8067221103048,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 55.202268669816476,
			"height": 5.710579517567226,
			"seed": 2089698691,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					7.614106023423119,
					0
				],
				[
					19.987028311485346,
					-2.8552897587836696
				],
				[
					38.07053011711491,
					-4.758816264639336
				],
				[
					51.395215658105144,
					-5.710579517567226
				],
				[
					55.202268669816476,
					-4.758816264639336
				],
				[
					52.34697891103292,
					-2.8552897587836696
				],
				[
					47.588162646393585,
					-1.903526505855666
				],
				[
					47.588162646393585,
					-1.903526505855666
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.34022000432014465,
				0.4313419759273529,
				0.48116499185562134,
				0.41617918014526367,
				0.3592740595340729,
				0.34304773807525635,
				0.07928686589002609,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 691846670,
			"isDeleted": false,
			"id": "g3FbH5iHG_x5UdtJS_dSL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1287.9853896470615,
			"y": -595.2278811454393,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.179975299774014,
			"height": 13.324685540990231,
			"seed": 542625219,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9517632529280036,
					0
				],
				[
					0,
					0
				],
				[
					1.9035265058557798,
					0.9517632529278899
				],
				[
					10.469395782206675,
					3.807053011711446
				],
				[
					15.22821204684601,
					5.710579517567226
				],
				[
					14.276448793918235,
					6.6623427704951155
				],
				[
					7.614106023422892,
					9.517632529278785
				],
				[
					3.807053011711332,
					13.324685540990231
				],
				[
					3.807053011711332,
					12.372922288062341
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09544998407363892,
				0.1956709921360016,
				0.2442999929189682,
				0.2863280177116394,
				0.2711041569709778,
				0.30585792660713196,
				0.38765186071395874,
				0.40589872002601624,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 22,
			"versionNonce": 612397522,
			"isDeleted": false,
			"id": "nq0xPl67tJ9Vjz58RtBVU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1400.2934534925505,
			"y": -570.4820365693146,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.372922288062227,
			"height": 110.40453733963318,
			"seed": 1234587043,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.9517632529278899
				],
				[
					-1.9035265058557798,
					4.758816264639336
				],
				[
					-3.807053011711332,
					15.228212046845897
				],
				[
					-6.6623427704951155,
					28.552897587836128
				],
				[
					-9.517632529278671,
					43.78110963468214
				],
				[
					-11.421159035134451,
					55.20226866981659
				],
				[
					-12.372922288062227,
					69.47871746373465
				],
				[
					-12.372922288062227,
					80.89987649886916
				],
				[
					-12.372922288062227,
					91.36927228107572
				],
				[
					-12.372922288062227,
					98.98337830449873
				],
				[
					-11.421159035134451,
					105.64572107499384
				],
				[
					-11.421159035134451,
					109.45277408670529
				],
				[
					-11.421159035134451,
					110.40453733963318
				],
				[
					-11.421159035134451,
					106.59748432792168
				],
				[
					-11.421159035134451,
					105.64572107499384
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16528888046741486,
				0.22872799634933472,
				0.28915339708328247,
				0.3361901044845581,
				0.3439953327178955,
				0.36931347846984863,
				0.3911830186843872,
				0.42148807644844055,
				0.4453160762786865,
				0.4616093635559082,
				0.4663489758968353,
				0.38626378774642944,
				0.1267624795436859,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 18,
			"versionNonce": 928369742,
			"isDeleted": false,
			"id": "GYmh5pKGvyj3Ts4EEE08x",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1421.2322450569636,
			"y": -458.1739727238256,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.035265058557343,
			"height": 18.083501805629567,
			"seed": 618019651,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.951763252927833
				],
				[
					3.8070530117115595,
					8.565869276350838
				],
				[
					6.6623427704951155,
					16.179975299773787
				],
				[
					9.517632529278671,
					18.083501805629567
				],
				[
					11.421159035134451,
					10.469395782206561
				],
				[
					14.276448793918007,
					4.758816264639336
				],
				[
					17.13173855270179,
					1.903526505855723
				],
				[
					18.083501805629567,
					0.951763252927833
				],
				[
					19.035265058557343,
					0.951763252927833
				],
				[
					19.035265058557343,
					0
				],
				[
					19.035265058557343,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19704397022724152,
				0.2640639841556549,
				0.32661402225494385,
				0.27858349680900574,
				0.24544189870357513,
				0.24487246572971344,
				0.23755337297916412,
				0.22954028844833374,
				0.20923224091529846,
				0.05232366919517517,
				0
			]
		},
		{
			"type": "text",
			"version": 29,
			"versionNonce": 1794533266,
			"isDeleted": false,
			"id": "2OfyzI1i",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1567.7569400737318,
			"y": -321.48300093660805,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 127.51988220214844,
			"height": 25,
			"seed": 77095,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "mesh network",
			"rawText": "mesh network",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "mesh network",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 13,
			"versionNonce": 867373710,
			"isDeleted": false,
			"id": "YMAaFx9t",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1355.9692946344205,
			"y": -358.5091526403895,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 41.19996643066406,
			"height": 25,
			"seed": 58327,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "OOS",
			"rawText": "OOS",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "OOS",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 1655154002,
			"isDeleted": false,
			"id": "hrUtwh3zttSEYG7QR8vcB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1444.7854280902602,
			"y": -404.71177395873093,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.521860485399202,
			"height": 53.21790706294638,
			"seed": 1887841325,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7826162803376064,
					4.695697682024672
				],
				[
					2.3478488410123646,
					13.304476765736581
				],
				[
					2.3478488410123646,
					22.695872129785982
				],
				[
					0,
					31.304651213497834
				],
				[
					-3.9130814016871227,
					41.47866285788467
				],
				[
					-8.608779083711852,
					49.304825661259144
				],
				[
					-10.174011644386837,
					53.21790706294638
				],
				[
					-10.174011644386837,
					52.435290782608945
				],
				[
					-9.391395364049458,
					50.870058221934016
				],
				[
					-8.608779083711852,
					50.870058221934016
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.3242020010948181,
				0.3743320405483246,
				0.3962799310684204,
				0.4298970699310303,
				0.45588019490242004,
				0.49276024103164673,
				0.46850669384002686,
				0.3124910295009613,
				0.10957946628332138,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 957190350,
			"isDeleted": false,
			"id": "PfiJk9RQxLAIYJtGr17Ox",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1460.4377536970092,
			"y": -351.49386689578455,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.739244205061823,
			"height": 18.782790728098746,
			"seed": 1885466797,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.5652325606748718
				],
				[
					0,
					3.9130814016872364
				],
				[
					-0.7826162803373791,
					11.73924420506171
				],
				[
					-2.3478488410123646,
					17.217558167423817
				],
				[
					-2.3478488410123646,
					18.000174447761253
				],
				[
					0,
					18.782790728098746
				],
				[
					3.1304651213497436,
					18.000174447761253
				],
				[
					6.260930242699487,
					16.43494188708638
				],
				[
					8.608779083711852,
					15.652325606748946
				],
				[
					9.391395364049458,
					15.652325606748946
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.24848000705242157,
				0.27522000670433044,
				0.29870209097862244,
				0.3028225302696228,
				0.3123851716518402,
				0.3131505250930786,
				0.39483338594436646,
				0.4356893002986908,
				0.15647274255752563,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 1424698130,
			"isDeleted": false,
			"id": "FrJjzPbDCYChW2EXsfltx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1375.1325791402273,
			"y": -393.75514603400666,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.695697682024729,
			"height": 7.04354652303698,
			"seed": 1120597293,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7826162803374359
				],
				[
					2.3478488410123646,
					3.9130814016872364
				],
				[
					3.9130814016871227,
					7.04354652303698
				],
				[
					4.695697682024729,
					7.04354652303698
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.20020999014377594,
				0.24611200392246246,
				0.0504220575094223,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 587089678,
			"isDeleted": false,
			"id": "iK7hImSmmYGu-Tky8SN6U",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1368.0890326171905,
			"y": -379.66805298793264,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.478313962362108,
			"height": 4.695697682024672,
			"seed": 71200621,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7826162803376064,
					0.7826162803374359
				],
				[
					3.1304651213497436,
					2.3478488410123077
				],
				[
					4.695697682024729,
					3.9130814016872364
				],
				[
					5.478313962362108,
					4.695697682024672
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2729939818382263,
				0.30113399028778076,
				0.08736364543437958,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 10,
			"versionNonce": 1211627730,
			"isDeleted": false,
			"id": "Kncm-38tR4IRUrBy5KkMp",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1361.0454860941534,
			"y": -370.27665762388324,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.695697682024729,
			"height": 2.3478488410123077,
			"seed": 1709259181,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.3478488410123646,
					1.5652325606748718
				],
				[
					4.695697682024729,
					2.3478488410123077
				],
				[
					4.695697682024729,
					2.3478488410123077
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.32031601667404175,
				0.21270664036273956,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 1912485198,
			"isDeleted": false,
			"id": "EQs_DEMVIsqQrTg3tw6xy",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1359.4802535334784,
			"y": -363.23311110084626,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.956627924724216,
			"height": 10.956627924724273,
			"seed": 732335501,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7826162803374359
				],
				[
					-0.7826162803376064,
					-0.7826162803374359
				],
				[
					0,
					-0.7826162803374359
				],
				[
					3.1304651213497436,
					0
				],
				[
					6.260930242699487,
					2.3478488410123646
				],
				[
					8.608779083711852,
					2.3478488410123646
				],
				[
					8.608779083711852,
					-1.5652325606748718
				],
				[
					9.391395364049231,
					-7.04354652303698
				],
				[
					10.17401164438661,
					-8.608779083711909
				],
				[
					10.17401164438661,
					-7.826162803374473
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1047859787940979,
				0.15457598865032196,
				0.2334979921579361,
				0.2882930338382721,
				0.3090435862541199,
				0.3022627532482147,
				0.27201974391937256,
				0.28839734196662903,
				0.29333022236824036,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 1545932434,
			"isDeleted": false,
			"id": "KbtLM2CHG3ngxdmHADpyz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1305.4797301901947,
			"y": -356.97218085814666,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.869709326411567,
			"height": 18.000174447761253,
			"seed": 138887693,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7826162803373791,
					0
				],
				[
					3.1304651213497436,
					4.695697682024672
				],
				[
					6.260930242699715,
					8.608779083711909
				],
				[
					9.391395364049231,
					13.304476765736581
				],
				[
					13.304476765736581,
					18.000174447761253
				],
				[
					14.08709304607396,
					18.000174447761253
				],
				[
					14.869709326411567,
					17.217558167423817
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1483408510684967,
				0.22494454681873322,
				0.2682879865169525,
				0.3260299861431122,
				0.02479165606200695,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 795237262,
			"isDeleted": false,
			"id": "A2IqMscLjG2ZPWTmcHpPX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1289.0447883031084,
			"y": -356.1895645778092,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.652325606748946,
			"height": 14.087093046074017,
			"seed": 1181514605,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7826162803373791,
					0
				],
				[
					-3.9130814016871227,
					1.5652325606748718
				],
				[
					-7.043546523037094,
					3.9130814016872364
				],
				[
					-10.956627924724216,
					7.826162803374473
				],
				[
					-15.652325606748946,
					13.304476765736581
				],
				[
					-15.652325606748946,
					14.087093046074017
				],
				[
					-15.652325606748946,
					14.087093046074017
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1615239828824997,
				0.23325000703334808,
				0.30326199531555176,
				0.35550951957702637,
				0.08541284501552582,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 627666002,
			"isDeleted": false,
			"id": "NJHQGql8FGbTGpbFrWO1a",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1433.0461838851984,
			"y": -306.8847389165501,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 37.56558145619738,
			"height": 20.348023288773618,
			"seed": 211493891,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.5652325606747581,
					0
				],
				[
					7.043546523036866,
					-0.7826162803374359
				],
				[
					18.78279072809869,
					-7.043546523037037
				],
				[
					30.522034933160285,
					-14.087093046074074
				],
				[
					36.00034889552239,
					-18.000174447761253
				],
				[
					37.56558145619738,
					-20.348023288773618
				],
				[
					37.56558145619738,
					-20.348023288773618
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13877157866954803,
				0.1713757961988449,
				0.17615649104118347,
				0.15598657727241516,
				0.12108367681503296,
				0.136492520570755,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 1366276558,
			"isDeleted": false,
			"id": "EZjqMkv5oqQN1le6Y18Pv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1390.7849047469763,
			"y": -335.8415412890356,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.434941887086325,
			"height": 9.391395364049401,
			"seed": 904763555,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7826162803373791,
					0
				],
				[
					7.826162803374473,
					-0.7826162803374359
				],
				[
					14.86970932641134,
					-1.5652325606749287
				],
				[
					16.434941887086325,
					-0.7826162803374359
				],
				[
					13.304476765736581,
					2.3478488410123077
				],
				[
					9.391395364049231,
					6.260930242699544
				],
				[
					7.826162803374473,
					7.826162803374473
				],
				[
					10.956627924724216,
					7.043546523037037
				],
				[
					10.956627924724216,
					6.260930242699544
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19863399863243103,
				0.24049600958824158,
				0.2114461362361908,
				0.17463763058185577,
				0.21668758988380432,
				0.2853769361972809,
				0.3398285508155823,
				0.07107836753129959,
				0
			]
		},
		{
			"type": "text",
			"version": 33,
			"versionNonce": 165417490,
			"isDeleted": false,
			"id": "zzWjxIQx",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1645.9888660689696,
			"y": -229.20553562630846,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 127.85989379882812,
			"height": 25,
			"seed": 24168,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "node to node",
			"rawText": "node to node",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "node to node",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 523456526,
			"isDeleted": false,
			"id": "7tFEFd-l5dMIViJTJk4vN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1438.9609314476152,
			"y": -253.55365159648898,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.424399597036654,
			"height": 12.10739657481244,
			"seed": 1937881037,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7121997985183839
				],
				[
					0,
					2.848799194073507
				],
				[
					0,
					7.121997985183782
				],
				[
					0,
					10.682996977775673
				],
				[
					0.7121997985182134,
					12.10739657481244
				],
				[
					1.424399597036654,
					9.97079717925729
				],
				[
					1.424399597036654,
					9.258597380738905
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.19816263020038605,
				0.24756890535354614,
				0.2933654189109802,
				0.2837824523448944,
				0.022763976827263832,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 477364178,
			"isDeleted": false,
			"id": "0czZ2xfjJE4rzKU5hgIN6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1440.385331044652,
			"y": -254.97805119352572,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.668395567404332,
			"height": 0.7121997985183839,
			"seed": 711489837,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					3.5609989925919763,
					0
				],
				[
					8.546397582220607,
					0
				],
				[
					12.819596373330796,
					0
				],
				[
					15.668395567404332,
					-0.7121997985183839
				],
				[
					14.956195768886118,
					-0.7121997985183839
				],
				[
					14.956195768886118,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2541239857673645,
				0.30893802642822266,
				0.3020246922969818,
				0.29897212982177734,
				0.04486538842320442,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 346693198,
			"isDeleted": false,
			"id": "ffb6QK7C5_Azv_uVWsRrT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1424.0047356787293,
			"y": -255.6902509920441,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7121997985184407,
			"height": 12.107396574812412,
			"seed": 162184237,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7121997985183839
				],
				[
					0,
					1.4243995970367394
				],
				[
					0,
					2.848799194073507
				],
				[
					0.7121997985184407,
					6.409798186665398
				],
				[
					0.7121997985184407,
					9.97079717925729
				],
				[
					0.7121997985184407,
					11.395196776294028
				],
				[
					0,
					12.107396574812412
				],
				[
					0,
					12.107396574812412
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.17291399836540222,
				0.23364999890327454,
				0.2872239947319031,
				0.31070926785469055,
				0.27482855319976807,
				0.03412289544939995,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 2034775442,
			"isDeleted": false,
			"id": "OibSDtApT0Qg4UdTyqrTt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1441.0975308431703,
			"y": -242.8706546187133,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.668395567404332,
			"height": 1.4243995970367678,
			"seed": 2105268205,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7121997985182134,
					0
				],
				[
					2.848799194073308,
					0
				],
				[
					4.98539858962863,
					0
				],
				[
					9.97079717925726,
					0
				],
				[
					13.53179617184901,
					0
				],
				[
					14.956195768885891,
					0.7121997985183839
				],
				[
					15.668395567404332,
					0.7121997985183839
				],
				[
					15.668395567404332,
					0
				],
				[
					15.668395567404332,
					-0.7121997985183839
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12045498937368393,
				0.23304449021816254,
				0.2916640043258667,
				0.3648580014705658,
				0.4072737395763397,
				0.3832034766674042,
				0.270874559879303,
				0.11570397764444351,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 1185752206,
			"isDeleted": false,
			"id": "gS2BxDi8HwKUdzwEgxt1C",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1441.0975308431703,
			"y": -262.8122489772279,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.560998992591749,
			"height": 7.12199798518381,
			"seed": 1512457741,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7121997985182134,
					0.7121997985184407
				],
				[
					1.424399597036654,
					3.5609989925919194
				],
				[
					2.136599395555095,
					7.12199798518381
				],
				[
					2.848799194073308,
					7.12199798518381
				],
				[
					3.560998992591749,
					7.12199798518381
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.23146799206733704,
				0.29725196957588196,
				0.302947998046875,
				0.09808681905269623,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 563065682,
			"isDeleted": false,
			"id": "RZIxxLEc1Lctm1cr2FViK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1424.7169354772477,
			"y": -262.8122489772279,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7121997985184407,
			"height": 8.546397582220521,
			"seed": 507578029,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.712199798518327
				],
				[
					0,
					2.1365993955551517
				],
				[
					0,
					5.697598388147071
				],
				[
					0.7121997985184407,
					7.834197783702194
				],
				[
					0.7121997985184407,
					7.834197783702194
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11100424081087112,
				0.26182401180267334,
				0.3204200267791748,
				0.0851687639951706,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 10,
			"versionNonce": 1190486734,
			"isDeleted": false,
			"id": "Pd-5THTEWnO_h6dkUxxUM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1445.3707296342807,
			"y": -269.2220471638933,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7121997985184407,
			"height": 1.4243995970367678,
			"seed": 347650893,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7121997985184407,
					0
				],
				[
					-0.7121997985184407,
					0.7121997985184407
				],
				[
					-0.7121997985184407,
					1.4243995970367678
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.009999999776482582,
				0.056395966559648514,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 1470200082,
			"isDeleted": false,
			"id": "a7OZIJl0gfLMlDEYP-622",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1445.3707296342807,
			"y": -268.50984736537487,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7121997985184407,
			"height": 1.4243995970367678,
			"seed": 1601768237,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7121997985184407,
					0
				],
				[
					0,
					0
				],
				[
					0,
					-0.7121997985184407
				],
				[
					0,
					-1.4243995970367678
				],
				[
					-0.7121997985184407,
					-1.4243995970367678
				],
				[
					-0.7121997985184407,
					-0.7121997985184407
				],
				[
					-0.7121997985184407,
					-0.7121997985184407
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1598540097475052,
				0.1292247325181961,
				0.15005376935005188,
				0.1302787810564041,
				0.16946271061897278,
				0.10636138916015625,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 136042766,
			"isDeleted": false,
			"id": "3IG7qi7spgNxtGLpG9KZZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1424.0047356787293,
			"y": -272.0708463579668,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4243995970368815,
			"height": 0.7121997985183839,
			"seed": 519635085,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7121997985184407,
					0
				],
				[
					0,
					0
				],
				[
					0.7121997985184407,
					0
				],
				[
					0.7121997985184407,
					-0.7121997985183839
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11128402501344681,
				0.14778973162174225,
				0.12937912344932556,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 2062845650,
			"isDeleted": false,
			"id": "Z_QcJRYKXCxre5rYGusHQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1448.2195288283542,
			"y": -199.42646690909226,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 9.258597380738934,
			"seed": 1459909325,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7121997985183839
				],
				[
					0,
					4.98539858962863
				],
				[
					0,
					8.54639758222055
				],
				[
					0,
					9.258597380738934
				],
				[
					0,
					9.258597380738934
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19828598201274872,
				0.25414592027664185,
				0.27650678157806396,
				0.06389157474040985,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 1100580686,
			"isDeleted": false,
			"id": "VZNwA5bFxw0V0ep7Memq4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1451.0683280224275,
			"y": -208.6850642898312,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.136599395555095,
			"height": 2.136599395555095,
			"seed": 1341459309,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7121997985184407,
					0.7121997985183839
				],
				[
					-0.7121997985184407,
					1.4243995970367678
				],
				[
					0,
					0.7121997985183839
				],
				[
					0,
					0
				],
				[
					0,
					-0.712199798518327
				],
				[
					0.7121997985182134,
					0
				],
				[
					1.424399597036654,
					0
				],
				[
					1.424399597036654,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13401421904563904,
				0.12809552252292633,
				0.1056075170636177,
				0.16742105782032013,
				0.20870418846607208,
				0.19010739028453827,
				0.14428041875362396,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 1679809682,
			"isDeleted": false,
			"id": "Q4K-gePI38mRtY2NttLh8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1393.380144342439,
			"y": -240.0218554246398,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.8487991940735355,
			"height": 4.98539858962863,
			"seed": 59250477,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7121997985183839
				],
				[
					-0.7121997985184407,
					-0.7121997985183839
				],
				[
					-1.424399597036654,
					1.4243995970367678
				],
				[
					0,
					2.848799194073507
				],
				[
					1.4243995970368815,
					2.848799194073507
				],
				[
					1.4243995970368815,
					0
				],
				[
					0,
					-2.1365993955551232
				],
				[
					-1.424399597036654,
					-0.7121997985183839
				],
				[
					-1.424399597036654,
					-0.7121997985183839
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.009999999776482582,
				0.22329001128673553,
				0.25559303164482117,
				0.21619094908237457,
				0.20471441745758057,
				0.21467360854148865,
				0.24346402287483215,
				0.0688541904091835,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 18,
			"versionNonce": 1405578638,
			"isDeleted": false,
			"id": "KmJZu0O_yT6wZ_kFmBn1-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1394.8045439394757,
			"y": -241.44625502167654,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.136599395555095,
			"height": 3.560998992591891,
			"seed": 633376077,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7121997985183555
				],
				[
					0,
					1.4243995970367394
				],
				[
					0,
					0.7121997985183555
				],
				[
					0,
					0
				],
				[
					0,
					-0.7121997985183839
				],
				[
					0,
					0.7121997985183555
				],
				[
					0.7121997985182134,
					2.1365993955551232
				],
				[
					1.424399597036654,
					2.1365993955551232
				],
				[
					2.136599395555095,
					0.7121997985183555
				],
				[
					1.424399597036654,
					-0.7121997985183839
				],
				[
					0.7121997985182134,
					-1.4243995970367678
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11405423283576965,
				0.19703784584999084,
				0.181486114859581,
				0.20928244292736053,
				0.2586292326450348,
				0.2746303975582123,
				0.25602060556411743,
				0.2442222535610199,
				0.21248050034046173,
				0.21497277915477753,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 1088059986,
			"isDeleted": false,
			"id": "ryfsKYRU9uhmLCCI_It_i",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1393.380144342439,
			"y": -229.33885844686412,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7121997985184407,
			"height": 9.258597380738905,
			"seed": 1950081069,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7121997985183839
				],
				[
					0,
					2.1365993955551232
				],
				[
					0,
					3.560998992591891
				],
				[
					0,
					5.697598388147014
				],
				[
					0.7121997985184407,
					7.121997985183782
				],
				[
					0.7121997985184407,
					8.546397582220521
				],
				[
					0.7121997985184407,
					9.258597380738905
				],
				[
					0.7121997985184407,
					8.546397582220521
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12522998452186584,
				0.1670791655778885,
				0.1622677594423294,
				0.1842310130596161,
				0.1994209587574005,
				0.20806719362735748,
				0.2004646360874176,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 736005070,
			"isDeleted": false,
			"id": "W2dpuBzE3mUNa9PNaNnNt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1401.2143421261412,
			"y": -190.16786952835332,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.424399597036654,
			"height": 3.5609989925918626,
			"seed": 1404042221,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.424399597036711
				],
				[
					0.7121997985184407,
					2.136599395555095
				],
				[
					0.7121997985184407,
					0.7121997985183839
				],
				[
					0.7121997985184407,
					-0.7121997985183839
				],
				[
					-0.7121997985182134,
					-1.4243995970367678
				],
				[
					-0.7121997985182134,
					-0.7121997985183839
				],
				[
					0,
					-0.7121997985183839
				],
				[
					0,
					-0.7121997985183839
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19715499877929688,
				0.15098300576210022,
				0.15156374871730804,
				0.23525048792362213,
				0.2322770655155182,
				0.17048348486423492,
				0.13213177025318146,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1878745106,
			"isDeleted": false,
			"id": "KvljM0yMhPxDXpi5BHGH0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1400.5021423276228,
			"y": -183.04587154316954,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.424399597036654,
			"height": 11.395196776294028,
			"seed": 375941037,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7121997985184407,
					0
				],
				[
					0.7121997985184407,
					1.424399597036711
				],
				[
					0.7121997985184407,
					3.5609989925918626
				],
				[
					0.7121997985184407,
					6.409798186665398
				],
				[
					0.7121997985184407,
					7.834197783702109
				],
				[
					0.7121997985184407,
					9.258597380738877
				],
				[
					0.7121997985184407,
					9.97079717925726
				],
				[
					0.7121997985184407,
					10.682996977775645
				],
				[
					1.424399597036654,
					10.682996977775645
				],
				[
					1.424399597036654,
					11.395196776294028
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08256597816944122,
				0.17328870296478271,
				0.19741466641426086,
				0.22285033762454987,
				0.23550371825695038,
				0.24680666625499725,
				0.23984810709953308,
				0.19708389043807983,
				0.041526734828948975,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 670556686,
			"isDeleted": false,
			"id": "vJYPGnFc3af50W8TT1oQQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1402.6387417231779,
			"y": -190.8800693268717,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7121997985184407,
			"height": 2.1365993955551517,
			"seed": 1454828589,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7121997985183839
				],
				[
					0,
					1.4243995970367678
				],
				[
					0.7121997985184407,
					0.7121997985183839
				],
				[
					0.7121997985184407,
					-0.7121997985183839
				],
				[
					0,
					-0.7121997985183839
				],
				[
					0,
					0
				],
				[
					0.7121997985184407,
					0
				],
				[
					0.7121997985184407,
					-0.7121997985183839
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10475198179483414,
				0.12563656270503998,
				0.12625069916248322,
				0.16477496922016144,
				0.19778573513031006,
				0.15601354837417603,
				0.07984600961208344,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 23,
			"versionNonce": 1568247250,
			"isDeleted": false,
			"id": "lQNiYdRd7d7qE8BX9Gn_j",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1431.8389334624314,
			"y": -194.44106831946362,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 24.926992948143152,
			"height": 13.53179617184918,
			"seed": 1376520173,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7121997985184407,
					0
				],
				[
					1.424399597036654,
					0
				],
				[
					2.136599395555095,
					0
				],
				[
					6.409798186665512,
					-2.136599395555095
				],
				[
					12.107396574812356,
					-6.409798186665398
				],
				[
					17.804994962959427,
					-9.97079717925726
				],
				[
					20.653794157032962,
					-11.395196776294028
				],
				[
					21.365993955551403,
					-12.107396574812412
				],
				[
					22.078193754069844,
					-12.107396574812412
				],
				[
					22.078193754069844,
					-12.819596373330796
				],
				[
					22.790393552588057,
					-12.819596373330796
				],
				[
					23.502593351106498,
					-12.819596373330796
				],
				[
					23.502593351106498,
					-13.53179617184918
				],
				[
					24.21479314962494,
					-13.53179617184918
				],
				[
					24.926992948143152,
					-13.53179617184918
				],
				[
					24.926992948143152,
					-13.53179617184918
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08393999934196472,
				0.11476599425077438,
				0.16306200623512268,
				0.23848599195480347,
				0.28462401032447815,
				0.2820432484149933,
				0.281337708234787,
				0.2923066318035126,
				0.31495100259780884,
				0.31593000888824463,
				0.330780565738678,
				0.34455400705337524,
				0.3662072718143463,
				0.3819316029548645,
				0.15408237278461456,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 2064412750,
			"isDeleted": false,
			"id": "xuq6dHXWtvclOjHmiWJQN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1447.5073290298358,
			"y": -241.44625502167654,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.546397582220607,
			"height": 7.8341977837021375,
			"seed": 707081901,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7121997985183555
				],
				[
					2.136599395555095,
					3.560998992591891
				],
				[
					5.697598388147071,
					6.409798186665398
				],
				[
					7.834197783702166,
					7.8341977837021375
				],
				[
					8.546397582220607,
					7.8341977837021375
				],
				[
					8.546397582220607,
					7.8341977837021375
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.3045560419559479,
				0.4171159863471985,
				0.46436402201652527,
				0.31473812460899353,
				0.05760189890861511,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 1584137106,
			"isDeleted": false,
			"id": "Wk5RhptZpCSXCe1hnsPpd",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1453.9171272165013,
			"y": -232.899857439456,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.546397582220607,
			"height": 4.985398589628659,
			"seed": 447871405,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7121997985184407,
					0.7121997985183839
				],
				[
					0.7121997985184407,
					1.4243995970367678
				],
				[
					4.273198791110417,
					4.273198791110275
				],
				[
					7.1219979851839526,
					4.985398589628659
				],
				[
					8.546397582220607,
					4.985398589628659
				],
				[
					7.834197783702166,
					4.985398589628659
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.20442400872707367,
				0.23868799209594727,
				0.3725360035896301,
				0.41469401121139526,
				0.4078993499279022,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 284505742,
			"isDeleted": false,
			"id": "X_6rX7jmSnINZmeSgWzWP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1458.1903260076115,
			"y": -221.50466066316196,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.97079717925726,
			"height": 2.1365993955551232,
			"seed": 1879817389,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4243995970368815,
					0.7121997985183555
				],
				[
					6.409798186665512,
					2.1365993955551232
				],
				[
					9.97079717925726,
					2.1365993955551232
				],
				[
					9.97079717925726,
					2.1365993955551232
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.214462012052536,
				0.32934999465942383,
				0.3606419861316681,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 218743122,
			"isDeleted": false,
			"id": "s5aqoS6OkwTb0aGAoH5VN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1409.7607397083616,
			"y": -249.99265260389708,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.424399597036654,
			"height": 10.682996977775645,
			"seed": 1998821101,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7121997985182134,
					-0.7121997985183839
				],
				[
					1.424399597036654,
					-1.4243995970367394
				],
				[
					1.424399597036654,
					0.7121997985183839
				],
				[
					0.7121997985182134,
					5.697598388147014
				],
				[
					0,
					9.258597380738905
				],
				[
					0.7121997985182134,
					8.54639758222055
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.26241400837898254,
				0.3395119905471802,
				0.37161898612976074,
				0.28229016065597534,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 1919628494,
			"isDeleted": false,
			"id": "bXLddsDoFoLEfw99ocm8E",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1401.2143421261412,
			"y": -249.99265260389708,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.5609989925919763,
			"height": 9.97079717925729,
			"seed": 1998330349,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7121997985183839
				],
				[
					0,
					2.848799194073507
				],
				[
					-0.7121997985182134,
					4.273198791110275
				],
				[
					-2.136599395555095,
					8.54639758222055
				],
				[
					-3.5609989925919763,
					9.97079717925729
				],
				[
					-3.5609989925919763,
					9.97079717925729
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.23352600634098053,
				0.2709659934043884,
				0.3443849980831146,
				0.09576556086540222,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 615106322,
			"isDeleted": false,
			"id": "_XUB8_0NrXlh4ckuF27uk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1429.7023340668763,
			"y": -234.32425703649275,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.97079717925726,
			"height": 1.4243995970367678,
			"seed": 1679924461,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					4.273198791110417,
					0
				],
				[
					8.546397582220607,
					-0.7121997985183839
				],
				[
					9.97079717925726,
					-1.4243995970367678
				],
				[
					9.97079717925726,
					-1.4243995970367678
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.289216011762619,
				0.3070129454135895,
				0.024100646376609802,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 688352014,
			"isDeleted": false,
			"id": "ytwuu1jkTJ6_KmRMzqcxf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1427.5657346713213,
			"y": -224.35345985723546,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.546397582220607,
			"height": 2.8487991940735355,
			"seed": 65292077,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.136599395555322,
					0
				],
				[
					6.409798186665512,
					-2.1365993955551517
				],
				[
					8.546397582220607,
					-2.8487991940735355
				],
				[
					7.834197783702166,
					-2.8487991940735355
				],
				[
					7.834197783702166,
					-2.1365993955551517
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.29023200273513794,
				0.32451701164245605,
				0.24552035331726074,
				0.007627990562468767,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 1573065938,
			"isDeleted": false,
			"id": "GSdD_3WafekoJIlvmisT-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1424.7169354772477,
			"y": -213.67046287945982,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.1219979851839526,
			"height": 2.848799194073507,
			"seed": 1596033997,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.8487991940735355,
					-0.7121997985183555
				],
				[
					6.409798186665512,
					-2.848799194073507
				],
				[
					7.1219979851839526,
					-2.1365993955551232
				],
				[
					7.1219979851839526,
					-2.1365993955551232
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.3299799859523773,
				0.3544885218143463,
				0.04833999648690224,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 591583566,
			"isDeleted": false,
			"id": "wPDaxKei_m7x0Qe-KAqzL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1423.2925358802108,
			"y": -206.54846489427604,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.834197783702166,
			"height": 5.697598388147014,
			"seed": 983272973,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					3.560998992591749,
					1.4243995970367678
				],
				[
					6.4097981866652844,
					3.5609989925919194
				],
				[
					7.834197783702166,
					4.98539858962863
				],
				[
					7.121997985183725,
					5.697598388147014
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.3460939824581146,
				0.36350998282432556,
				0.07445871084928513,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 1240246930,
			"isDeleted": false,
			"id": "jb3ohcuE-P7CjxWj3lafn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1414.7461382979905,
			"y": -209.39726408834952,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.97079717925726,
			"height": 14.243995970367507,
			"seed": 1908334669,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7121997985182134,
					0
				],
				[
					-1.424399597036654,
					0.712199798518327
				],
				[
					-2.848799194073308,
					2.136599395555095
				],
				[
					-7.121997985183725,
					8.546397582220493
				],
				[
					-9.97079717925726,
					14.243995970367507
				],
				[
					-7.834197783702166,
					12.107396574812412
				],
				[
					-7.121997985183725,
					11.395196776294028
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09880499541759491,
				0.22478549182415009,
				0.27670401334762573,
				0.3715820014476776,
				0.41214796900749207,
				0.055059660226106644,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 410419086,
			"isDeleted": false,
			"id": "oHB3nzDDShnfKP1z7IqAI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1395.5167437379941,
			"y": -211.53386348390467,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.121997985183725,
			"height": 4.2731987911102465,
			"seed": 1206653357,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.8487991940735355,
					1.4243995970367678
				],
				[
					5.697598388147071,
					3.5609989925918626
				],
				[
					7.121997985183725,
					4.2731987911102465
				],
				[
					7.121997985183725,
					4.2731987911102465
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.3603139817714691,
				0.39236101508140564,
				0.07460320740938187,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 803047506,
			"isDeleted": false,
			"id": "L6Bzrd9VrQVV5ByMDdpS7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1394.8045439394757,
			"y": -201.5630663046474,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.121997985183725,
			"height": 4.273198791110303,
			"seed": 1912613869,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7121997985184407,
					0
				],
				[
					0.7121997985182134,
					1.4243995970367678
				],
				[
					3.560998992591749,
					2.8487991940735355
				],
				[
					5.697598388146844,
					3.5609989925919194
				],
				[
					6.4097981866652844,
					4.273198791110303
				],
				[
					6.4097981866652844,
					4.273198791110303
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04338598623871803,
				0.3459930121898651,
				0.423520028591156,
				0.38454052805900574,
				0.029709625989198685,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 1826315726,
			"isDeleted": false,
			"id": "4TinLeKH3PY7lctisctoE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1391.9557447454022,
			"y": -182.33367174465116,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.53179617184901,
			"height": 17.804994962959427,
			"seed": 206810861,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.712199798518327
				],
				[
					0.7121997985182134,
					4.2731987911102465
				],
				[
					1.424399597036654,
					5.697598388147014
				],
				[
					2.136599395555095,
					7.834197783702109
				],
				[
					3.560998992591749,
					4.98539858962863
				],
				[
					7.121997985183725,
					-1.4243995970367678
				],
				[
					11.395196776293915,
					-6.409798186665455
				],
				[
					12.819596373330569,
					-7.834197783702166
				],
				[
					13.53179617184901,
					-9.258597380738934
				],
				[
					13.53179617184901,
					-9.970797179257318
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.19957998394966125,
				0.22744698822498322,
				0.23562097549438477,
				0.2828514277935028,
				0.34596943855285645,
				0.3645396828651428,
				0.3400963246822357,
				0.08309521526098251,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 19,
			"versionNonce": 1735175698,
			"isDeleted": false,
			"id": "qEMe_Uah3-m_ZsdaQNFyD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1466.7063054580224,
			"y": -248.41569134018505,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.9485792204893642,
			"height": 25.98105627319316,
			"seed": 815354733,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6495264068296365,
					0
				],
				[
					-0.6495264068296365,
					0.6495264068298354
				],
				[
					-1.2990528136595003,
					1.9485792204894778
				],
				[
					-1.9485792204893642,
					5.1962112546386265
				],
				[
					-1.9485792204893642,
					9.09336969561761
				],
				[
					-1.9485792204893642,
					13.640054543426402
				],
				[
					-1.2990528136595003,
					17.537212984405386
				],
				[
					-0.6495264068296365,
					21.43437142538437
				],
				[
					-0.6495264068296365,
					24.68200345953349
				],
				[
					-0.6495264068296365,
					25.98105627319316
				],
				[
					-0.6495264068296365,
					25.331529866363326
				],
				[
					-0.6495264068296365,
					25.331529866363326
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06582452356815338,
				0.057769011706113815,
				0.10401559621095657,
				0.13095302879810333,
				0.12838055193424225,
				0.09893503040075302,
				0.07107479870319366,
				0.05372525006532669,
				0.07355395704507828,
				0.06924218684434891,
				0.006212371867150068,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 361395214,
			"isDeleted": false,
			"id": "NDZZHxOtWjX2Qzc8aYQ-l",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1471.2529903058312,
			"y": -214.64031818503395,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.443843288787775,
			"height": 8.443843288787775,
			"seed": 1790369965,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6495264068298638,
					0.6495264068298354
				],
				[
					1.2990528136597277,
					1.9485792204895063
				],
				[
					1.9485792204895915,
					3.2476320341491487
				],
				[
					2.5981056273194554,
					3.897158440978984
				],
				[
					4.5466848478088195,
					5.1962112546386265
				],
				[
					5.845737661468547,
					3.2476320341491487
				],
				[
					7.144790475128275,
					-0.649526406829807
				],
				[
					7.794316881957911,
					-3.2476320341491487
				],
				[
					8.443843288787775,
					-3.2476320341491487
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12105859071016312,
				0.14560174942016602,
				0.14290520548820496,
				0.1627735048532486,
				0.2004840075969696,
				0.22946929931640625,
				0.1166798397898674,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 898702290,
			"isDeleted": false,
			"id": "uGP4vNM2DOcZyZLrkziuX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1408.2489288433376,
			"y": -262.05574588361145,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.640054543426231,
			"height": 9.09336969561761,
			"seed": 1978681037,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.9485792204893642,
					0
				],
				[
					3.8971584409787283,
					0.649526406829807
				],
				[
					9.742896102447276,
					3.2476320341491487
				],
				[
					12.990528136596367,
					6.495264068298297
				],
				[
					13.640054543426231,
					8.443843288787775
				],
				[
					13.640054543426231,
					9.09336969561761
				],
				[
					13.640054543426231,
					9.09336969561761
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14955797791481018,
				0.17355798184871674,
				0.21133577823638916,
				0.22891445457935333,
				0.21818172931671143,
				0.07919598370790482,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 2088550990,
			"isDeleted": false,
			"id": "bduFTYFEuvyou1UCsPp8U",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1393.3098214862516,
			"y": -250.36427056067453,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.1447904751280475,
			"height": 7.79431688195794,
			"seed": 458106925,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6495264068298638,
					0.649526406829807
				],
				[
					1.2990528136597277,
					1.2990528136596424
				],
				[
					3.247632034149092,
					3.8971584409789557
				],
				[
					5.196211254638683,
					5.1962112546386265
				],
				[
					5.196211254638683,
					3.8971584409789557
				],
				[
					5.196211254638683,
					0.649526406829807
				],
				[
					5.84573766146832,
					-1.9485792204895063
				],
				[
					6.495264068298184,
					-2.5981056273193133
				],
				[
					7.1447904751280475,
					-1.9485792204895063
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14239388704299927,
				0.1535475105047226,
				0.19508865475654602,
				0.1968066394329071,
				0.1668556183576584,
				0.14104904234409332,
				0.19494634866714478,
				0.08005169779062271,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 677499282,
			"isDeleted": false,
			"id": "RQwAyQ7GdonaMmSNinCje",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1378.3707141291657,
			"y": -223.08416147382172,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.9485792204895915,
			"height": 14.289580950256237,
			"seed": 1972584013,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6495264068298354
				],
				[
					1.2990528136597277,
					1.2990528136596708
				],
				[
					1.9485792204895915,
					7.144790475128133
				],
				[
					1.9485792204895915,
					12.990528136596595
				],
				[
					1.9485792204895915,
					13.640054543426402
				],
				[
					1.9485792204895915,
					13.640054543426402
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05763998255133629,
				0.19991907477378845,
				0.24059826135635376,
				0.2711138129234314,
				0.12893377244472504,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 1686849678,
			"isDeleted": false,
			"id": "I7b5uPXB4ZAih1j5SRQsZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1380.968819756485,
			"y": -204.24789567575667,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.093369695617639,
			"height": 7.144790475128133,
			"seed": 937845069,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6495264068298354
				],
				[
					0,
					0
				],
				[
					1.2990528136597277,
					1.9485792204894778
				],
				[
					3.247632034149092,
					3.2476320341491487
				],
				[
					5.845737661468547,
					1.2990528136596424
				],
				[
					8.443843288787775,
					-2.5981056273193133
				],
				[
					9.093369695617639,
					-3.897158440978984
				],
				[
					9.093369695617639,
					-3.2476320341491487
				],
				[
					9.093369695617639,
					-2.5981056273193133
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.03560247644782066,
				0.15268078446388245,
				0.1955653727054596,
				0.1988096684217453,
				0.19686651229858398,
				0.20065808296203613,
				0.13540174067020416,
				0.03512759506702423,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 1930809170,
			"isDeleted": false,
			"id": "lQnuimuVnC8qgQo3eJ6bS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1509.8133499115102,
			"y": -219.94893009605335,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.953765843623842,
			"height": 0.9346103652264901,
			"seed": 1822780269,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.9346103652264901,
					0
				],
				[
					4.6730518261324505,
					0
				],
				[
					10.280714017491391,
					0.9346103652264901
				],
				[
					14.953765843623842,
					0.9346103652264901
				],
				[
					13.084545113170861,
					0.9346103652264901
				],
				[
					13.084545113170861,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.27168798446655273,
				0.35805201530456543,
				0.41054999828338623,
				0.42280474305152893,
				0.10947415232658386,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 18,
			"versionNonce": 1299121870,
			"isDeleted": false,
			"id": "nJnNIMLpAaHgzOe0WFg7S",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1492.0557529722068,
			"y": -224.6219819221858,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.084545113170861,
			"height": 11.215324382717881,
			"seed": 639725165,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9346103652264901,
					0
				],
				[
					0.9346103652264901,
					0.9346103652264901
				],
				[
					6.542272556585431,
					2.8038310956794703
				],
				[
					11.215324382717881,
					4.6730518261324505
				],
				[
					12.149934747944371,
					5.607662191358941
				],
				[
					9.346103652264901,
					7.476882921811921
				],
				[
					4.6730518261324505,
					9.346103652264901
				],
				[
					0,
					11.215324382717881
				],
				[
					-0.9346103652264901,
					11.215324382717881
				],
				[
					0.9346103652264901,
					11.215324382717881
				],
				[
					1.8692207304529802,
					11.215324382717881
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12290798872709274,
				0.36337602138519287,
				0.3994438648223877,
				0.3838217854499817,
				0.3329066038131714,
				0.33206021785736084,
				0.3685963749885559,
				0.4458731710910797,
				0.448722779750824,
				0.15962612628936768,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 32,
			"versionNonce": 1241781522,
			"isDeleted": false,
			"id": "RyGjXJOpPdWymNgHAt0XO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1550.0015956162495,
			"y": -252.6602928789805,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 87.8533743312903,
			"height": 35.51519387860668,
			"seed": 1131736397,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9346103652264901,
					0
				],
				[
					-1.8692207304529802,
					0
				],
				[
					-1.8692207304529802,
					-0.9346103652264901
				],
				[
					0.9346103652264901,
					-4.6730518261324505
				],
				[
					6.542272556585431,
					-10.280714017491391
				],
				[
					13.084545113171089,
					-14.019155478397352
				],
				[
					18.69220730453003,
					-13.084545113170861
				],
				[
					23.36525913066248,
					-12.149934747944371
				],
				[
					28.03831095679493,
					-13.084545113170861
				],
				[
					32.71136278292738,
					-21.496038400209272
				],
				[
					35.51519387860685,
					-28.97292132202125
				],
				[
					36.44980424383334,
					-33.6459731481537
				],
				[
					37.38441460905983,
					-32.71136278292721
				],
				[
					38.31902497428632,
					-30.84214205247423
				],
				[
					40.1882457047393,
					-27.10370059156827
				],
				[
					42.05746643519228,
					-23.365259130662253
				],
				[
					44.86129753087175,
					-22.430648765435762
				],
				[
					49.5343493570042,
					-25.234479861115233
				],
				[
					57.011232278816124,
					-31.77675241770072
				],
				[
					62.618894470175064,
					-34.58058351338019
				],
				[
					68.226556661534,
					-35.51519387860668
				],
				[
					74.76882921811944,
					-35.51519387860668
				],
				[
					82.24571213993136,
					-34.58058351338019
				],
				[
					85.98415360083732,
					-31.77675241770072
				],
				[
					85.98415360083732,
					-32.71136278292721
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10343600809574127,
				0.1559108942747116,
				0.2064381092786789,
				0.2532469928264618,
				0.2785431742668152,
				0.2879381775856018,
				0.30279555916786194,
				0.3214035928249359,
				0.30915704369544983,
				0.2713193893432617,
				0.2736840844154358,
				0.34130388498306274,
				0.3568841218948364,
				0.3670975863933563,
				0.36412596702575684,
				0.35060006380081177,
				0.35351887345314026,
				0.3451242446899414,
				0.3431839346885681,
				0.38313767313957214,
				0.4345652461051941,
				0.48441246151924133,
				0.532362163066864,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 1472265486,
			"isDeleted": false,
			"id": "jg0afmoWH6lsbVAnboZTh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1336.9104323446095,
			"y": -331.1675635580057,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 21.496038400209272,
			"height": 55.14201154836297,
			"seed": 147881325,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.9346103652264901,
					6.542272556585431
				],
				[
					0.9346103652264901,
					14.019155478397352
				],
				[
					-0.9346103652264901,
					23.365259130662253
				],
				[
					-5.607662191358941,
					30.842142052474173
				],
				[
					-12.149934747944371,
					40.188245704739074
				],
				[
					-16.822986574076822,
					49.534349357003975
				],
				[
					-20.561428034982782,
					55.14201154836297
				],
				[
					-20.561428034982782,
					53.27279081790999
				],
				[
					-20.561428034982782,
					52.3381804526835
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2814980149269104,
				0.29089391231536865,
				0.3143801987171173,
				0.34411779046058655,
				0.3689661920070648,
				0.4000858664512634,
				0.3994225263595581,
				0.10949447751045227,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 1050911442,
			"isDeleted": false,
			"id": "bKRVXQG0bEerhIqryuL_P",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1371.4910158579896,
			"y": -275.09094164441626,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.149934747944371,
			"height": 13.084545113170861,
			"seed": 1969052557,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.9346103652264901
				],
				[
					0,
					1.8692207304529802
				],
				[
					-0.9346103652264901,
					9.346103652264901
				],
				[
					-0.9346103652264901,
					13.084545113170861
				],
				[
					1.8692207304529802,
					12.149934747944371
				],
				[
					7.476882921811921,
					8.411493287038411
				],
				[
					10.280714017491391,
					5.607662191358941
				],
				[
					11.215324382717881,
					5.607662191358941
				],
				[
					11.215324382717881,
					4.6730518261324505
				],
				[
					11.215324382717881,
					3.7384414609059604
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2100600004196167,
				0.23406000435352325,
				0.2735423743724823,
				0.2947838604450226,
				0.32767319679260254,
				0.39876043796539307,
				0.44776007533073425,
				0.4235643446445465,
				0.17926564812660217,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 687483726,
			"isDeleted": false,
			"id": "dAIVgHPUA9-OIIdm6EvEo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1357.1079440074059,
			"y": -204.06984902036447,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 20.217933647939617,
			"height": 4.621241976671939,
			"seed": 1509494797,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.577655247084067,
					0
				],
				[
					-0.577655247084067,
					0.5776552470839817
				],
				[
					2.3106209883358133,
					0.5776552470839817
				],
				[
					9.242483953343708,
					-1.7329657412519737
				],
				[
					16.75200216543567,
					-2.8882762354199656
				],
				[
					19.64027840085555,
					-2.310620988335984
				],
				[
					18.484967906687643,
					-4.0435867295879575
				],
				[
					18.484967906687643,
					-4.0435867295879575
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1412193924188614,
				0.2393449991941452,
				0.3391839861869812,
				0.411482036113739,
				0.4186684787273407,
				0.17847847938537598,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 462125202,
			"isDeleted": false,
			"id": "4tFauxY8dbVU1I0Lb9Ehe",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1330.5358026415424,
			"y": -213.88998822079233,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.664828706259868,
			"height": 8.087173459175858,
			"seed": 1408029645,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5776552470839817
				],
				[
					1.155310494168134,
					-0.5776552470839817
				],
				[
					2.8882762354201077,
					-0.5776552470839817
				],
				[
					7.509518212091962,
					0
				],
				[
					8.664828706259868,
					2.3106209883359554
				],
				[
					5.198897223755921,
					4.621241976671939
				],
				[
					1.155310494168134,
					7.509518212091876
				],
				[
					2.8882762354201077,
					6.354207717923913
				],
				[
					3.4659314825039473,
					6.354207717923913
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13636599481105804,
				0.17796798050403595,
				0.21586401760578156,
				0.2400711327791214,
				0.18416187167167664,
				0.18708856403827667,
				0.25561025738716125,
				0.07952267676591873,
				0
			]
		},
		{
			"type": "text",
			"version": 21,
			"versionNonce": 1332973966,
			"isDeleted": false,
			"id": "yGu2HapV",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1310.8955242406864,
			"y": -227.75371415080812,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 64.419921875,
			"height": 25,
			"seed": 12447,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "hopping",
			"rawText": "hopping",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "hopping",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 115,
			"versionNonce": 1081251410,
			"isDeleted": false,
			"id": "cH8Jqf9B",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1393.1299305672103,
			"y": -47.62625728230819,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 164.07984924316406,
			"height": 50,
			"seed": 4948,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "route evaluation\n",
			"rawText": "route evaluation\n",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "route evaluation\n",
			"lineHeight": 1.25,
			"baseline": 43
		},
		{
			"type": "text",
			"version": 90,
			"versionNonce": 644231118,
			"isDeleted": false,
			"id": "IEgnqOeb",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1212.1433841734454,
			"y": -83.1150949770836,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 41.67994689941406,
			"height": 25,
			"seed": 48730,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "hops",
			"rawText": "hops",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "hops",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 90,
			"versionNonce": 2117073938,
			"isDeleted": false,
			"id": "poRyVCRd",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1212.3469418088034,
			"y": -58.96038436630266,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 52.659942626953125,
			"height": 25,
			"seed": 18133,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "power",
			"rawText": "power",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "power",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 110,
			"versionNonce": 971703822,
			"isDeleted": false,
			"id": "exwY7Vqf",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1213.036291849148,
			"y": -29.178982438660455,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 69.59994506835938,
			"height": 25,
			"seed": 7967,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "latency",
			"rawText": "latency",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "latency",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 113,
			"versionNonce": 1924835794,
			"isDeleted": false,
			"id": "vzOlIvEN9HyjakzQ46kF9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1120.822845064257,
			"y": -16.88205941467953,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.713668814393941,
			"height": 10.407502301136503,
			"seed": 1224648845,
			"groupIds": [
				"qQq_PpVjmSen37uUu_zAa"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6938334867424487
				],
				[
					0.6938334867425056,
					4.856834407197027
				],
				[
					1.3876669734847837,
					7.632168354166765
				],
				[
					1.3876669734847837,
					10.407502301136503
				],
				[
					2.0815004602272893,
					5.550667893939476
				],
				[
					3.469167433712073,
					0
				],
				[
					4.856834407197084,
					0
				],
				[
					5.550667893939362,
					4.163000920454579
				],
				[
					6.244501380681868,
					7.632168354166765
				],
				[
					6.244501380681868,
					5.550667893939476
				],
				[
					7.632168354166652,
					1.3876669734848406
				],
				[
					9.019835327651663,
					0.6938334867424487
				],
				[
					9.713668814393941,
					4.163000920454579
				],
				[
					9.019835327651663,
					8.326001840909214
				],
				[
					9.019835327651663,
					7.632168354166765
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06824292242527008,
				0.12084060907363892,
				0.1357163041830063,
				0.10541930794715881,
				0.0459829717874527,
				0.044173065572977066,
				0.1171114519238472,
				0.13336288928985596,
				0.12609051167964935,
				0.07377465814352036,
				0.05577529966831207,
				0.09781897068023682,
				0.1458684355020523,
				0.051797423511743546,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 107,
			"versionNonce": 721097806,
			"isDeleted": false,
			"id": "-GBp1FkZVo-a-X24OhswP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1106.252341842666,
			"y": -14.106725467709794,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.469167433712073,
			"height": 7.632168354166765,
			"seed": 1117918445,
			"groupIds": [
				"qQq_PpVjmSen37uUu_zAa"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6938334867422782,
					0
				],
				[
					-1.3876669734847837,
					0
				],
				[
					-2.775333946969795,
					0.6938334867424487
				],
				[
					-2.0815004602272893,
					2.0815004602272893
				],
				[
					0,
					4.163000920454579
				],
				[
					0,
					5.550667893939476
				],
				[
					-2.775333946969795,
					7.632168354166765
				],
				[
					-3.469167433712073,
					7.632168354166765
				],
				[
					-3.469167433712073,
					6.938334867424317
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08218798786401749,
				0.11175103485584259,
				0.12360134720802307,
				0.08778484910726547,
				0.0736875906586647,
				0.11638891696929932,
				0.19170473515987396,
				0.14249160885810852,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 104,
			"versionNonce": 1697226642,
			"isDeleted": false,
			"id": "pgGH2EAKJ49T-FEwAL0Xn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1144.8522354422187,
			"y": -54.68223978740386,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4508923188252538,
			"height": 13.058030869427654,
			"seed": 1632412429,
			"groupIds": [
				"oERuUm8SNq2GghP4kLmTY"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7254461594126553
				],
				[
					0.7254461594127406,
					5.0781231158885305
				],
				[
					0.7254461594127406,
					10.881692391189716
				],
				[
					1.4508923188252538,
					13.058030869427654
				],
				[
					1.4508923188252538,
					12.33258471001497
				],
				[
					1.4508923188252538,
					9.430800072364406
				],
				[
					1.4508923188252538,
					8.705353912951779
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.130680114030838,
				0.1681014746427536,
				0.1956506073474884,
				0.1692095696926117,
				0.09724634140729904,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 105,
			"versionNonce": 326064782,
			"isDeleted": false,
			"id": "5NhqU874Apk_RLJyq2pBs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1147.0285739204564,
			"y": -56.13313210622914,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.607138550602258,
			"height": 0.7254461594126553,
			"seed": 873249901,
			"groupIds": [
				"oERuUm8SNq2GghP4kLmTY"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7254461594125132,
					-0.7254461594126553
				],
				[
					2.176338478237767,
					-0.7254461594126553
				],
				[
					5.803569275301015,
					-0.7254461594126553
				],
				[
					8.705353912951523,
					-0.7254461594126553
				],
				[
					10.881692391189517,
					-0.7254461594126553
				],
				[
					11.607138550602258,
					-0.7254461594126553
				],
				[
					10.881692391189517,
					-0.7254461594126553
				],
				[
					10.881692391189517,
					-0.7254461594126553
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.055244140326976776,
				0.12022094428539276,
				0.14576424658298492,
				0.16227737069129944,
				0.1693376749753952,
				0.15967333316802979,
				0.011148345656692982,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 108,
			"versionNonce": 565435730,
			"isDeleted": false,
			"id": "6hgWoeOso9Cq01jW7vKG_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1137.5977738480922,
			"y": -57.58402442505442,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.1763384782379944,
			"height": 16.685261666490845,
			"seed": 1558612013,
			"groupIds": [
				"oERuUm8SNq2GghP4kLmTY"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7254461594127406,
					0.7254461594126269
				],
				[
					0.7254461594127406,
					3.62723079706322
				],
				[
					1.4508923188252538,
					6.529015434713813
				],
				[
					1.4508923188252538,
					10.156246231777033
				],
				[
					1.4508923188252538,
					11.607138550602343
				],
				[
					1.4508923188252538,
					13.78347702884028
				],
				[
					1.4508923188252538,
					14.508923188252908
				],
				[
					2.1763384782379944,
					15.234369347665535
				],
				[
					2.1763384782379944,
					15.959815507078218
				],
				[
					2.1763384782379944,
					16.685261666490845
				],
				[
					1.4508923188252538,
					16.685261666490845
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11692821979522705,
				0.11928234994411469,
				0.12540921568870544,
				0.13272644579410553,
				0.1343749463558197,
				0.14140506088733673,
				0.14009612798690796,
				0.14141793549060822,
				0.14161327481269836,
				0.14090999960899353,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 108,
			"versionNonce": 1778440398,
			"isDeleted": false,
			"id": "sfE_5EG2CyoAXYlNE1XJd",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1145.5776816016312,
			"y": -40.89876275856358,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.607138550602258,
			"height": 0.7254461594126269,
			"seed": 681848589,
			"groupIds": [
				"oERuUm8SNq2GghP4kLmTY"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7254461594125132,
					0
				],
				[
					1.4508923188252538,
					0
				],
				[
					3.6272307970632482,
					0
				],
				[
					5.803569275301243,
					0
				],
				[
					7.254461594126269,
					0
				],
				[
					8.70535391295175,
					0
				],
				[
					9.430800072364264,
					0
				],
				[
					10.156246231777004,
					0
				],
				[
					10.881692391189745,
					-0.7254461594126269
				],
				[
					11.607138550602258,
					-0.7254461594126269
				],
				[
					11.607138550602258,
					-0.7254461594126269
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07989422976970673,
				0.13377273082733154,
				0.13540679216384888,
				0.1540224850177765,
				0.16147467494010925,
				0.1626282036304474,
				0.1757424920797348,
				0.19216199219226837,
				0.19413867592811584,
				0.046207673847675323,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 101,
			"versionNonce": 1437623058,
			"isDeleted": false,
			"id": "bW9QjUOilQkE11UlpUxRl",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1144.8522354422187,
			"y": -47.42777819327739,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7254461594127406,
			"height": 7.979907753539123,
			"seed": 1366075885,
			"groupIds": [
				"oERuUm8SNq2GghP4kLmTY"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7254461594127406,
					1.4508923188253107
				],
				[
					0.7254461594127406,
					5.078123115888502
				],
				[
					0.7254461594127406,
					7.979907753539123
				],
				[
					0.7254461594127406,
					7.979907753539123
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13672830164432526,
				0.12864382565021515,
				0.026817718520760536,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 111,
			"versionNonce": 1716031246,
			"isDeleted": false,
			"id": "85LdHoUk6aeBviUoJLF8Q",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1144.126789282806,
			"y": -57.58402442505442,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.6272307970632482,
			"height": 7.254461594126468,
			"seed": 1656853549,
			"groupIds": [
				"oERuUm8SNq2GghP4kLmTY"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1.4508923188253107
				],
				[
					0,
					-4.352676956475875
				],
				[
					0,
					-5.803569275301186
				],
				[
					0,
					-7.254461594126468
				],
				[
					0,
					-6.529015434713813
				],
				[
					0.7254461594125132,
					-6.529015434713813
				],
				[
					2.1763384782379944,
					-6.529015434713813
				],
				[
					2.9017846376505076,
					-6.529015434713813
				],
				[
					3.6272307970632482,
					-6.529015434713813
				],
				[
					3.6272307970632482,
					-5.803569275301186
				],
				[
					3.6272307970632482,
					-3.6272307970632482
				],
				[
					3.6272307970632482,
					-1.4508923188253107
				],
				[
					3.6272307970632482,
					0
				],
				[
					3.6272307970632482,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09064535796642303,
				0.08935476839542389,
				0.09286587685346603,
				0.10695330798625946,
				0.12328323721885681,
				0.1269577592611313,
				0.12028899788856506,
				0.11376742273569107,
				0.11302371323108673,
				0.12736301124095917,
				0.14274288713932037,
				0.1632666289806366,
				0.1682012677192688,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 102,
			"versionNonce": 1805005010,
			"isDeleted": false,
			"id": "8imt1ji-rG2_Fo2tSV1-Q",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1141.950450804568,
			"y": -55.407685946816486,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7254461594125132,
			"height": 7.254461594126468,
			"seed": 1971132973,
			"groupIds": [
				"oERuUm8SNq2GghP4kLmTY"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7254461594126269
				],
				[
					0.7254461594125132,
					3.62723079706322
				],
				[
					0.7254461594125132,
					6.529015434713813
				],
				[
					0.7254461594125132,
					7.254461594126468
				],
				[
					0.7254461594125132,
					7.254461594126468
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14187945425510406,
				0.1572294682264328,
				0.12312469631433487,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 103,
			"versionNonce": 1690271054,
			"isDeleted": false,
			"id": "zcaKjzrGEb1ysN_yMK3Uj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1144.126789282806,
			"y": -52.50590130916592,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.529015434713756,
			"height": 0.7254461594126553,
			"seed": 1869987533,
			"groupIds": [
				"oERuUm8SNq2GghP4kLmTY"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7254461594126553
				],
				[
					0.7254461594125132,
					0.7254461594126553
				],
				[
					2.1763384782379944,
					0.7254461594126553
				],
				[
					5.078123115888502,
					0.7254461594126553
				],
				[
					6.529015434713756,
					0.7254461594126553
				],
				[
					6.529015434713756,
					0.7254461594126553
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07175979763269424,
				0.1545906662940979,
				0.20878702402114868,
				0.2336772084236145,
				0.19492147862911224,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 112,
			"versionNonce": 1727809170,
			"isDeleted": false,
			"id": "lGpB5Zgj7skuoQnDT7fMt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1143.4013431233934,
			"y": -44.525993555626826,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.2544615941264965,
			"height": 0,
			"seed": 1054892493,
			"groupIds": [
				"oERuUm8SNq2GghP4kLmTY"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7254461594127406,
					0
				],
				[
					1.4508923188254812,
					0
				],
				[
					4.352676956475989,
					0
				],
				[
					6.529015434713983,
					0
				],
				[
					7.2544615941264965,
					0
				],
				[
					7.2544615941264965,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.20563656091690063,
				0.19798150658607483,
				0.19127319753170013,
				0.08624542504549026,
				0
			]
		},
		{
			"type": "text",
			"version": 23,
			"versionNonce": 1254007694,
			"isDeleted": false,
			"id": "WkWIBjcH",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1339.1033438946044,
			"y": -136.69243128872722,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 66.07992553710938,
			"height": 25,
			"seed": 51338,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "routing",
			"rawText": "routing",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "routing",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 41,
			"versionNonce": 1083810898,
			"isDeleted": false,
			"id": "jQGDeZXj",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1488.8101956429734,
			"y": -135.27340899727346,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 61.179931640625,
			"height": 25,
			"seed": 72484,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "floding",
			"rawText": "floding",
			"textAlign": "left",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "floding",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 1786708430,
			"isDeleted": false,
			"id": "duf_I6ml_3Ngw-7gnPRjy",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1374.5789011809477,
			"y": -172.16798857507058,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.737778643171623,
			"height": 19.156800934625437,
			"seed": 2011330595,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7095111457268786
				],
				[
					0,
					1.4190222914537287
				],
				[
					0,
					2.1285334371806073
				],
				[
					0.7095111457267649,
					2.838044582907486
				],
				[
					3.547555728634279,
					6.385600311541822
				],
				[
					7.804622602995323,
					12.061689477356765
				],
				[
					12.061689477356822,
					17.02826749744483
				],
				[
					16.318756351717866,
					19.156800934625437
				],
				[
					17.737778643171623,
					19.156800934625437
				],
				[
					16.318756351717866,
					17.02826749744483
				],
				[
					16.318756351717866,
					16.31875635171795
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05090148746967316,
				0.051214173436164856,
				0.0753350555896759,
				0.08211272954940796,
				0.13655120134353638,
				0.18722528219223022,
				0.23288561403751373,
				0.2634892463684082,
				0.2674960196018219,
				0.09937795996665955,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 1111837202,
			"isDeleted": false,
			"id": "3s7TJCqGvIuazUW_zO-8Y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1358.2601448292298,
			"y": -149.4636319118108,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.609245205991101,
			"height": 14.190222914537344,
			"seed": 1937461059,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7095111457269923,
					0.7095111457268786
				],
				[
					2.128533437180522,
					2.128533437180579
				],
				[
					4.257066874361271,
					4.257066874361215
				],
				[
					9.223644894449308,
					8.51413374872243
				],
				[
					11.352178331630057,
					9.22364489444925
				],
				[
					11.352178331630057,
					6.385600311541793
				],
				[
					11.352178331630057,
					2.128533437180579
				],
				[
					13.480711768810579,
					-2.838044582907486
				],
				[
					14.899734060264109,
					-4.966578020088093
				],
				[
					15.609245205991101,
					-4.966578020088093
				],
				[
					15.609245205991101,
					-4.257066874361215
				],
				[
					15.609245205991101,
					-4.257066874361215
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11661490052938461,
				0.1595659852027893,
				0.1947680115699768,
				0.2270609438419342,
				0.21009725332260132,
				0.20774658024311066,
				0.2353789061307907,
				0.27363768219947815,
				0.3023700416088104,
				0.32477182149887085,
				0.29372382164001465,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 1729730574,
			"isDeleted": false,
			"id": "vVsr85jjDPr-MZdiVY1fB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1437.015882004912,
			"y": -177.84407774088552,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.966578020088264,
			"height": 22.704356663259773,
			"seed": 742542851,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4190222914537571,
					2.838044582907486
				],
				[
					2.1285334371807494,
					10.642667185903008
				],
				[
					1.4190222914537571,
					18.44728978889856
				],
				[
					-0.7095111457267649,
					21.994845517532895
				],
				[
					-2.128533437180522,
					22.704356663259773
				],
				[
					-2.8380445829075143,
					21.994845517532895
				],
				[
					-2.8380445829075143,
					21.994845517532895
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2232348918914795,
				0.25010573863983154,
				0.28951361775398254,
				0.31285154819488525,
				0.2498602271080017,
				0.055391814559698105,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 1660303314,
			"isDeleted": false,
			"id": "merqjW3hGB-mnPXuW3jnZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1445.5300157536344,
			"y": -155.84923222335263,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.223644894449308,
			"height": 12.061689477356737,
			"seed": 185959075,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7095111457268786
				],
				[
					0,
					2.1285334371806073
				],
				[
					-1.4190222914537571,
					7.0951114572687
				],
				[
					-2.1285334371807494,
					11.352178331629858
				],
				[
					-1.4190222914537571,
					12.061689477356737
				],
				[
					0,
					11.352178331629858
				],
				[
					2.8380445829075143,
					10.642667185903036
				],
				[
					6.385600311541793,
					9.22364489444928
				],
				[
					7.095111457268558,
					8.5141337487224
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.18487197160720825,
				0.21044598519802094,
				0.22345858812332153,
				0.22739063203334808,
				0.25080642104148865,
				0.29942312836647034,
				0.37722235918045044,
				0.23256686329841614,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 411526734,
			"isDeleted": false,
			"id": "b9a47o6qhPxLmxQvUyEvd",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1313.560942648437,
			"y": -103.34540743956444,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7095111457267649,
			"height": 19.156800934625437,
			"seed": 489344643,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7095111457268786
				],
				[
					0,
					4.966578020088093
				],
				[
					0.7095111457267649,
					14.899734060264223
				],
				[
					0.7095111457267649,
					19.156800934625437
				],
				[
					0.7095111457267649,
					17.02826749744486
				],
				[
					0.7095111457267649,
					17.02826749744486
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.20750799775123596,
				0.26742398738861084,
				0.34219425916671753,
				0.37489938735961914,
				0.10077523440122604,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 583232914,
			"isDeleted": false,
			"id": "Wl-Ee7qD1XnkNMNlLPsPR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1319.946542959979,
			"y": -78.51251733912409,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.352178331630057,
			"height": 12.061689477356708,
			"seed": 895605635,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7095111457268217
				],
				[
					0,
					1.4190222914537571
				],
				[
					0.7095111457269923,
					3.547555728634336
				],
				[
					2.8380445829075143,
					9.223644894449308
				],
				[
					4.966578020088036,
					11.352178331629887
				],
				[
					6.385600311542021,
					11.352178331629887
				],
				[
					8.514133748722543,
					7.8046226029955506
				],
				[
					9.9331560401763,
					4.257066874361215
				],
				[
					10.642667185903065,
					2.8380445829075143
				],
				[
					11.352178331630057,
					2.8380445829075143
				],
				[
					10.642667185903065,
					2.8380445829075143
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08155199885368347,
				0.18458399176597595,
				0.20849399268627167,
				0.2594374120235443,
				0.2872150242328644,
				0.2897973954677582,
				0.3510901629924774,
				0.4085211455821991,
				0.39392754435539246,
				0.12337100505828857,
				0
			]
		},
		{
			"type": "text",
			"version": 164,
			"versionNonce": 1872850062,
			"isDeleted": false,
			"id": "LzD9Jq1B",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1609.927616894435,
			"y": -160.9305193669415,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 60.22279357910156,
			"height": 36.95094760869668,
			"seed": 90426,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 9.853586028985783,
			"fontFamily": 1,
			"text": "more devices\n=\nmore range",
			"rawText": "more devices\n=\nmore range",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "more devices\n=\nmore range",
			"lineHeight": 1.25,
			"baseline": 33
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 1726212946,
			"isDeleted": false,
			"id": "DCxscBuOzU4rL9r0bJ2zD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1580.1735139661753,
			"y": -197.0797096467308,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.590645497423111,
			"height": 21.473714215209156,
			"seed": 917420813,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7953227487114418
				],
				[
					0,
					-1.5906454974228836
				],
				[
					0,
					-2.3859682461343255
				],
				[
					0.7953227487114418,
					0
				],
				[
					1.590645497423111,
					7.953227487114532
				],
				[
					0.7953227487114418,
					17.497100471651947
				],
				[
					0.7953227487114418,
					19.08774596907483
				],
				[
					0.7953227487114418,
					13.520486728094681
				],
				[
					1.590645497423111,
					12.72516397938324
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09129199385643005,
				0.1086839884519577,
				0.1785379946231842,
				0.22191540896892548,
				0.2759138345718384,
				0.339649498462677,
				0.31975799798965454,
				0.06777017563581467,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 1512090318,
			"isDeleted": false,
			"id": "pscYhF5LgOXouBEJZrtS0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1587.3314187045783,
			"y": -175.60599543152165,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.31580947680618,
			"height": 11.1345184819603,
			"seed": 1695636781,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7953227487114418,
					-0.7953227487114418
				],
				[
					3.1812909948457673,
					3.976613743557266
				],
				[
					5.567259240980093,
					7.953227487114532
				],
				[
					7.157904738402976,
					9.543872984537416
				],
				[
					9.54387298453753,
					5.56725924098015
				],
				[
					11.929841230671855,
					0.7953227487114418
				],
				[
					13.520486728094738,
					-1.5906454974228836
				],
				[
					14.31580947680618,
					-1.5906454974228836
				],
				[
					13.520486728094738,
					-1.5906454974228836
				],
				[
					13.520486728094738,
					-0.7953227487114418
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.22892001271247864,
				0.26466506719589233,
				0.2602634131908417,
				0.27746129035949707,
				0.31033164262771606,
				0.3147357404232025,
				0.2763828635215759,
				0.13818594813346863,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 1437511954,
			"isDeleted": false,
			"id": "HuHnHePinhFrL9KhOGLl8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1299.4285570996606,
			"y": -232.46395687223253,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.776898311332161,
			"height": 12.438288179324559,
			"seed": 1029585539,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-2.665347466998128
				],
				[
					0,
					-5.330694933996256
				],
				[
					-0.8884491556661942,
					-9.772940712326431
				],
				[
					-0.8884491556661942,
					-11.549839023658535
				],
				[
					-1.776898311332161,
					-12.438288179324559
				],
				[
					-1.776898311332161,
					-12.438288179324559
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1472644954919815,
				0.1377284824848175,
				0.17360663414001465,
				0.19802063703536987,
				0.015831084921956062,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 647897358,
			"isDeleted": false,
			"id": "fJ_ZQ6cskCnz1NHA49WQR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1306.536150344989,
			"y": -255.56363491954954,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.665347466998128,
			"height": 13.32673733499064,
			"seed": 443107203,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.8884491556660805
				],
				[
					-0.8884491556659668,
					-1.7768983113321042
				],
				[
					-0.8884491556659668,
					-3.5537966226642084
				],
				[
					-1.7768983113319337,
					-6.219144089662279
				],
				[
					-1.7768983113319337,
					-8.884491556660407
				],
				[
					-1.7768983113319337,
					-11.549839023658535
				],
				[
					-2.665347466998128,
					-12.438288179324559
				],
				[
					-2.665347466998128,
					-13.32673733499064
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04771548509597778,
				0.1368499994277954,
				0.18597516417503357,
				0.22340448200702667,
				0.23241488635540009,
				0.16966943442821503,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 849002194,
			"isDeleted": false,
			"id": "i47c1ruhyZxuaU9ur1dnO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1314.5321927459831,
			"y": -277.7748638112006,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7768983113323884,
			"height": 11.549839023658478,
			"seed": 1958236099,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.8884491556660237
				],
				[
					0,
					-3.5537966226641515
				],
				[
					-0.8884491556661942,
					-7.107593245328303
				],
				[
					-0.8884491556661942,
					-9.772940712326431
				],
				[
					-1.7768983113323884,
					-11.549839023658478
				],
				[
					-1.7768983113323884,
					-11.549839023658478
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16761401295661926,
				0.1877700239419937,
				0.1868019700050354,
				0.17645111680030823,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 1754451790,
			"isDeleted": false,
			"id": "nRCo1G9oFbn9nH6S3IHnZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1320.7513368356456,
			"y": -299.9860927028516,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8884491556661942,
			"height": 11.549839023658478,
			"seed": 845814979,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.8884491556660237
				],
				[
					0,
					-2.665347466998128
				],
				[
					0,
					-6.2191440896622225
				],
				[
					0,
					-8.88449155666035
				],
				[
					-0.8884491556661942,
					-10.661389867992455
				],
				[
					-0.8884491556661942,
					-11.549839023658478
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07612597942352295,
				0.19166919589042664,
				0.1957310438156128,
				0.17475128173828125,
				0.012261565774679184,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 977212562,
			"isDeleted": false,
			"id": "fINBjq1EC040O7SeBomi7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1327.858930080974,
			"y": -318.64352497183836,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.661389867992511,
			"height": 14.215186490656606,
			"seed": 2009000387,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8884491556659668
				],
				[
					0,
					-1.776898311332161
				],
				[
					1.776898311332161,
					-7.10759324532836
				],
				[
					3.553796622664322,
					-12.438288179324559
				],
				[
					4.442245778330289,
					-13.32673733499064
				],
				[
					6.2191440896622225,
					-9.772940712326488
				],
				[
					8.884491556660578,
					-3.5537966226642084
				],
				[
					10.661389867992511,
					0
				],
				[
					10.661389867992511,
					-0.8884491556660805
				],
				[
					9.772940712326545,
					-1.776898311332161
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07969601452350616,
				0.19067353010177612,
				0.21552996337413788,
				0.22629614174365997,
				0.2542344629764557,
				0.3039701581001282,
				0.35646647214889526,
				0.3631182610988617,
				0.148484468460083,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 1549251982,
			"isDeleted": false,
			"id": "NZUzdpzZVNlXiUBTTN0Ws",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1293.2094130099983,
			"y": -198.702888956923,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.553796622664322,
			"height": 33.761067915309525,
			"seed": 377470275,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8884491556660237
				],
				[
					0,
					1.7768983113321042
				],
				[
					0,
					2.665347466998128
				],
				[
					0.8884491556661942,
					4.442245778330175
				],
				[
					1.776898311332161,
					10.661389867992455
				],
				[
					1.776898311332161,
					19.545881424652862
				],
				[
					0.8884491556661942,
					28.43037298131327
				],
				[
					-0.8884491556661942,
					33.761067915309525
				],
				[
					-1.776898311332161,
					33.761067915309525
				],
				[
					-1.776898311332161,
					32.8726187596435
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08048398047685623,
				0.1337609589099884,
				0.20772573351860046,
				0.23934997618198395,
				0.2866460680961609,
				0.33458220958709717,
				0.38437020778656006,
				0.40021437406539917,
				0.1068619042634964,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 2119348818,
			"isDeleted": false,
			"id": "OhJ-zBRfWFXAI8d1X_k9z",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1302.9823537223247,
			"y": -161.38802441894933,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.661389867992511,
			"height": 16.880533957654734,
			"seed": 932139203,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.7768983113321042
				],
				[
					0,
					4.442245778330175
				],
				[
					0.8884491556659668,
					13.326737334990582
				],
				[
					1.7768983113319337,
					16.880533957654734
				],
				[
					2.6653474669979005,
					16.880533957654734
				],
				[
					4.4422457783300615,
					13.326737334990582
				],
				[
					7.107593245328189,
					9.772940712326431
				],
				[
					9.772940712326317,
					7.996042400994384
				],
				[
					10.661389867992511,
					7.996042400994384
				],
				[
					9.772940712326317,
					7.996042400994384
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.21565601229667664,
				0.23656399548053741,
				0.2861599922180176,
				0.2984795868396759,
				0.27345985174179077,
				0.3087555170059204,
				0.3789089322090149,
				0.41332730650901794,
				0.39477744698524475,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 18,
			"versionNonce": 1260770254,
			"isDeleted": false,
			"id": "bttPVG4CdIauUcXsWnWxP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1475.3414899215365,
			"y": -190.70684655592862,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 40.868661160637885,
			"height": 30.207271292645316,
			"seed": 1926079555,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8884491556659668,
					0
				],
				[
					-1.776898311332161,
					0
				],
				[
					-2.665347466998128,
					1.7768983113320473
				],
				[
					-4.4422457783300615,
					5.330694933996199
				],
				[
					-7.996042400994384,
					9.772940712326431
				],
				[
					-11.549839023658478,
					14.215186490656606
				],
				[
					-15.992084801988767,
					17.768983113320758
				],
				[
					-23.98812720298315,
					22.21122889165099
				],
				[
					-33.76106791530947,
					26.653474669981165
				],
				[
					-39.091762849305724,
					30.207271292645316
				],
				[
					-40.868661160637885,
					30.207271292645316
				],
				[
					-36.426415382307596,
					28.43037298131327
				],
				[
					-35.53796622664163,
					27.54192382564719
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10423996299505234,
				0.16254736483097076,
				0.1804845631122589,
				0.21715518832206726,
				0.26693814992904663,
				0.28094297647476196,
				0.2895662784576416,
				0.28605806827545166,
				0.2818664610385895,
				0.2956824004650116,
				0.2944927513599396,
				0.01784338429570198,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 1101830162,
			"isDeleted": false,
			"id": "Rc0qDh8sjMZt45weX7kQP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1519.7639477048385,
			"y": -167.6071685086116,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.438288179324672,
			"height": 14.215186490656663,
			"seed": 144607907,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8884491556659668,
					0.8884491556660237
				],
				[
					-1.776898311332161,
					1.7768983113321042
				],
				[
					-3.5537966226640947,
					7.107593245328303
				],
				[
					-7.107593245328417,
					12.438288179324559
				],
				[
					-7.107593245328417,
					14.215186490656663
				],
				[
					-6.2191440896622225,
					14.215186490656663
				],
				[
					-2.665347466998128,
					13.326737334990582
				],
				[
					0.8884491556659668,
					12.438288179324559
				],
				[
					3.5537966226640947,
					11.549839023658535
				],
				[
					5.330694933996256,
					11.549839023658535
				],
				[
					5.330694933996256,
					10.661389867992455
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08454129099845886,
				0.15770748257637024,
				0.1962900459766388,
				0.19837628304958344,
				0.20451506972312927,
				0.22869083285331726,
				0.2952040433883667,
				0.35910746455192566,
				0.33195582032203674,
				0.14342810213565826,
				0
			]
		},
		{
			"type": "text",
			"version": 190,
			"versionNonce": 1863723534,
			"isDeleted": false,
			"id": "ionjbjsF",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -757.267619274374,
			"y": -539.3699621782704,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 141.01016235351562,
			"height": 17.05547362630013,
			"seed": 20589,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 13.644378901040104,
			"fontFamily": 1,
			"text": "licence free spectrum",
			"rawText": "licence free spectrum",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "licence free spectrum",
			"lineHeight": 1.25,
			"baseline": 12
		},
		{
			"type": "text",
			"version": 122,
			"versionNonce": 1413727698,
			"isDeleted": false,
			"id": "OYSDB5Lr",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -733.4095765849373,
			"y": -566.4785352712092,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 112.30393981933594,
			"height": 20,
			"seed": 69900,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "=/ frequencies",
			"rawText": "=/ frequencies",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "=/ frequencies",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "text",
			"version": 56,
			"versionNonce": 1461827662,
			"isDeleted": false,
			"id": "2M8S8vEM",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -679.0467566868796,
			"y": -478.2600605960305,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 42.927978515625,
			"height": 20,
			"seed": 65671,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "1 GHz",
			"rawText": "1 GHz",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "1 GHz",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "text",
			"version": 116,
			"versionNonce": 1865366418,
			"isDeleted": false,
			"id": "qnIJ9OF1",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -608.6520643227166,
			"y": -478.38837908040756,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 89.75993347167969,
			"height": 20,
			"seed": 9760,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "propagation",
			"rawText": "propagation",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "propagation",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 1260486286,
			"isDeleted": false,
			"id": "bXPehOvqGMcSJCNRJoUoF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -688.4205398963342,
			"y": -479.5906116830103,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.5697744350217135,
			"height": 11.965263135454848,
			"seed": 2062891469,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5697744350216567
				],
				[
					0,
					1.70932330506497
				],
				[
					0,
					3.41864661012994
				],
				[
					0,
					5.127969915194967
				],
				[
					0,
					8.546616525324907
				],
				[
					0.5697744350217135,
					11.965263135454848
				],
				[
					0.5697744350217135,
					11.965263135454848
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09121536463499069,
				0.11517348885536194,
				0.12421289086341858,
				0.15542978048324585,
				0.1602104753255844,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 279312722,
			"isDeleted": false,
			"id": "Mv6bQhWLGjnnDKgrWrh03",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -691.8391865064641,
			"y": -463.6369275024038,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.697744350216567,
			"height": 7.976842090303251,
			"seed": 1127856941,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5697744350216567
				],
				[
					0.5697744350215999,
					2.279097740086627
				],
				[
					1.709323305065027,
					5.12796991519491
				],
				[
					2.8488721751082267,
					5.697744350216567
				],
				[
					3.41864661012994,
					3.988421045151597
				],
				[
					4.558195480173254,
					0.5697744350216567
				],
				[
					5.697744350216567,
					-1.709323305065027
				],
				[
					5.697744350216567,
					-2.2790977400866836
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0882459431886673,
				0.12753784656524658,
				0.13724148273468018,
				0.1161394938826561,
				0.11410772800445557,
				0.13147298991680145,
				0.07903683185577393,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 10,
			"versionNonce": 802061518,
			"isDeleted": false,
			"id": "yMCAG6fs88eMnfdiVZHiS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -612.6405400384534,
			"y": -471.0439951576854,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.139548870043427,
			"height": 10.255939830389877,
			"seed": 1109923565,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5697744350217135,
					0.5697744350216567
				],
				[
					0,
					3.41864661012994
				],
				[
					0,
					9.116390960346564
				],
				[
					0.5697744350217135,
					10.255939830389877
				],
				[
					0,
					9.68616539536822
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08000555634498596,
				0.13803604245185852,
				0.1810203492641449,
				0.03389095887541771,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 1476329234,
			"isDeleted": false,
			"id": "OkxnpgKiVYX_atENJ_K2g",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -617.1987355186267,
			"y": -475.60219063785866,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.697744350216567,
			"height": 5.697744350216624,
			"seed": 1853920141,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5697744350217135,
					-1.1395488700433702
				],
				[
					1.7093233050649133,
					-3.9884210451516537
				],
				[
					3.41864661012994,
					-5.697744350216624
				],
				[
					3.98842104515154,
					-5.697744350216624
				],
				[
					5.127969915194967,
					-2.8488721751083403
				],
				[
					5.697744350216567,
					0
				],
				[
					5.697744350216567,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07916723936796188,
				0.11152609437704086,
				0.1298064887523651,
				0.1706724911928177,
				0.21991091966629028,
				0.1379108875989914,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 9,
			"versionNonce": 1791079182,
			"isDeleted": false,
			"id": "ZSZ1mvrkMiBJUZYqmTvph",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -629.1639986540815,
			"y": -471.0439951576854,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.1279699151948535,
			"height": 1.1395488700433134,
			"seed": 1445338349,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.1395488700433134,
					0
				],
				[
					3.41864661012994,
					0
				],
				[
					5.1279699151948535,
					0.5697744350216567
				],
				[
					5.1279699151948535,
					1.1395488700433134
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16186001896858215,
				0.12394766509532928,
				0.007707641460001469,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 9,
			"versionNonce": 1639009490,
			"isDeleted": false,
			"id": "L0D7tdTVUToZ-1tTzcous",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -629.1639986540815,
			"y": -465.34625080746883,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.697744350216567,
			"height": 1.1395488700433134,
			"seed": 1216923437,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.1395488700433134,
					0
				],
				[
					3.41864661012994,
					0
				],
				[
					5.1279699151948535,
					-0.5697744350216567
				],
				[
					5.697744350216567,
					-1.1395488700433134
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1683119833469391,
				0.21935400366783142,
				0.12822458148002625,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 35,
			"versionNonce": 1182015822,
			"isDeleted": false,
			"id": "7sSdliqsCtrN1JdWe8BJO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -636.3923837677248,
			"y": -508.8283953439046,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 53.81135795020464,
			"height": 37.07004658791868,
			"seed": 167166317,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5979039772245187,
					0
				],
				[
					0.5979039772245187,
					0.5979039772245187
				],
				[
					1.1958079544490374,
					1.1958079544490374
				],
				[
					2.98951988612248,
					0.5979039772245187
				],
				[
					5.97903977224496,
					-1.1958079544489806
				],
				[
					8.96855965836744,
					-4.185327840571404
				],
				[
					11.360175567265514,
					-6.5769437494694785
				],
				[
					13.751791476163362,
					-6.5769437494694785
				],
				[
					16.143407385061437,
					-5.381135795020441
				],
				[
					17.339215339510474,
					-4.185327840571404
				],
				[
					18.535023293959398,
					-3.5874238633469986
				],
				[
					19.132927271183917,
					-3.5874238633469986
				],
				[
					20.328735225632954,
					-5.97903977224496
				],
				[
					20.328735225632954,
					-8.370655681142921
				],
				[
					20.92663920285736,
					-10.164367612816363
				],
				[
					20.92663920285736,
					-11.3601755672654
				],
				[
					21.524543180081878,
					-11.3601755672654
				],
				[
					23.318255111755434,
					-10.762271590040882
				],
				[
					26.90567897510232,
					-10.762271590040882
				],
				[
					31.68891079289824,
					-11.95807954448992
				],
				[
					37.6679505651432,
					-15.545503407836918
				],
				[
					43.049086360163756,
					-18.535023293959398
				],
				[
					47.23441420073516,
					-20.926639202857245
				],
				[
					50.22393408685764,
					-22.7203511345308
				],
				[
					52.017646018531195,
					-23.916159088979725
				],
				[
					52.6155499957556,
					-27.503582952326724
				],
				[
					53.81135795020464,
					-32.28681477012276
				],
				[
					53.81135795020464,
					-35.27633465624524
				],
				[
					53.81135795020464,
					-35.874238633469645
				],
				[
					53.81135795020464,
					-35.27633465624524
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.03245745971798897,
				0.07348742336034775,
				0.10697107017040253,
				0.13019628822803497,
				0.15671783685684204,
				0.17257416248321533,
				0.18601571023464203,
				0.20592886209487915,
				0.2091173678636551,
				0.20590060949325562,
				0.20144487917423248,
				0.19089840352535248,
				0.17684197425842285,
				0.17307738959789276,
				0.1812225878238678,
				0.18142007291316986,
				0.18183761835098267,
				0.20799346268177032,
				0.20577938854694366,
				0.21832147240638733,
				0.23240716755390167,
				0.23575253784656525,
				0.23623424768447876,
				0.24002911150455475,
				0.23452740907669067,
				0.2268616259098053,
				0.19738656282424927,
				0.04021161049604416,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 592700050,
			"isDeleted": false,
			"id": "ClIzRechEJ4sCqI5MsY7y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -620.2489763826634,
			"y": -508.2304913666801,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.597903977224405,
			"height": 10.16436761281642,
			"seed": 1281150317,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.597903977224405,
					0.5979039772245187
				],
				[
					0.597903977224405,
					1.7937119316734425
				],
				[
					0.597903977224405,
					5.381135795020441
				],
				[
					0,
					9.566463635591901
				],
				[
					0,
					10.16436761281642
				],
				[
					0,
					10.16436761281642
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13812600076198578,
				0.16473855078220367,
				0.19884365797042847,
				0.21613213419914246,
				0.06295345723628998,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 1446954894,
			"isDeleted": false,
			"id": "Y6YAz3YoIc_lsW7w20LyV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -626.2280161549083,
			"y": -494.47869989051674,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.772751703918402,
			"height": 8.370655681142978,
			"seed": 785829997,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.1958079544490374
				],
				[
					0.597903977224405,
					4.783231817795979
				],
				[
					1.1958079544490374,
					8.370655681142978
				],
				[
					3.587423863346885,
					7.174847726693997
				],
				[
					5.97903977224496,
					4.185327840571517
				],
				[
					7.174847726693997,
					2.98951988612248
				],
				[
					7.772751703918402,
					2.391615908898018
				],
				[
					7.174847726693997,
					2.98951988612248
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.136000856757164,
				0.1624743938446045,
				0.17146097123622894,
				0.17862387001514435,
				0.22423791885375977,
				0.23051877319812775,
				0.07369760423898697,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 32,
			"versionNonce": 1201520722,
			"isDeleted": false,
			"id": "8wbR5Jxsr_uiFh_H0MNzT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -755.9731792126238,
			"y": -560.8460413624357,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 23.318255111755207,
			"height": 113.60175567265418,
			"seed": 501718061,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.1958079544490374,
					-0.5979039772245187
				],
				[
					-2.391615908898075,
					-1.1958079544490374
				],
				[
					-3.5874238633469986,
					-1.1958079544490374
				],
				[
					-6.5769437494694785,
					-1.1958079544490374
				],
				[
					-8.96855965836744,
					1.1958079544490374
				],
				[
					-10.164367612816477,
					6.5769437494694785
				],
				[
					-10.762271590040996,
					13.153887498938957
				],
				[
					-11.360175567265514,
					19.73083124840832
				],
				[
					-11.360175567265514,
					25.70987102065328
				],
				[
					-8.96855965836744,
					31.68891079289824
				],
				[
					-6.5769437494694785,
					36.47214261069416
				],
				[
					-6.5769437494694785,
					40.05956647404116
				],
				[
					-8.96855965836744,
					43.04908636016364
				],
				[
					-11.360175567265514,
					46.03860624628612
				],
				[
					-11.95807954448992,
					49.62603010963312
				],
				[
					-10.762271590040996,
					52.6155499957556
				],
				[
					-7.772751703918516,
					56.80087783632706
				],
				[
					-6.5769437494694785,
					61.58410965412304
				],
				[
					-5.381135795020555,
					69.35686135804144
				],
				[
					-5.97903977224496,
					78.32542101640888
				],
				[
					-7.174847726693997,
					87.29398067477632
				],
				[
					-7.772751703918516,
					94.46882840147026
				],
				[
					-5.97903977224496,
					100.44786817371522
				],
				[
					-2.391615908898075,
					105.2310999915112
				],
				[
					2.391615908897961,
					109.41642783208266
				],
				[
					10.762271590040882,
					111.80804374098062
				],
				[
					11.360175567265287,
					112.40594771820514
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10179653763771057,
				0.16332833468914032,
				0.2065918892621994,
				0.2137746512889862,
				0.18891344964504242,
				0.186155766248703,
				0.20202869176864624,
				0.21567748486995697,
				0.22226913273334503,
				0.21327002346515656,
				0.2381499707698822,
				0.25555238127708435,
				0.2501451373100281,
				0.2592218518257141,
				0.2737236022949219,
				0.28675034642219543,
				0.3256843090057373,
				0.39466699957847595,
				0.4049365222454071,
				0.43076494336128235,
				0.45764073729515076,
				0.4535290598869324,
				0.44450005888938904,
				0.46953973174095154,
				0.23411862552165985,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 1515890126,
			"isDeleted": false,
			"id": "zSwNlxmhkD_Yd_N6tGoh5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -824.1342326162163,
			"y": -522.580186820068,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 32.28681477012276,
			"height": 5.381135795020441,
			"seed": 884377869,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.1958079544490374,
					-0.5979039772245187
				],
				[
					7.1748477266938835,
					-2.98951988612248
				],
				[
					13.153887498938843,
					-2.98951988612248
				],
				[
					19.132927271183803,
					-1.1958079544490374
				],
				[
					24.514063066204358,
					0.5979039772245187
				],
				[
					28.69939090677576,
					1.1958079544489237
				],
				[
					31.68891079289824,
					1.7937119316734425
				],
				[
					32.28681477012276,
					2.391615908897961
				],
				[
					31.68891079289824,
					2.391615908897961
				],
				[
					31.091006815673722,
					2.391615908897961
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13739977777004242,
				0.1649433970451355,
				0.17006289958953857,
				0.21822552382946014,
				0.2381223440170288,
				0.2535313665866852,
				0.2616959810256958,
				0.26202186942100525,
				0.15053246915340424,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 174450194,
			"isDeleted": false,
			"id": "pfRf1h_AkUr__ZdyzylZD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -779.8893383016036,
			"y": -524.9718027289659,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.370655681142921,
			"height": 14.34969545338788,
			"seed": 1932131725,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.597903977224405
				],
				[
					1.1958079544489237,
					1.7937119316734425
				],
				[
					4.185327840571404,
					4.185327840571404
				],
				[
					6.576943749469365,
					5.97903977224496
				],
				[
					7.1748477266938835,
					7.772751703918402
				],
				[
					5.97903977224496,
					8.370655681142921
				],
				[
					3.587423863346885,
					10.164367612816363
				],
				[
					0.597903977224405,
					12.555983521714325
				],
				[
					-1.1958079544490374,
					14.34969545338788
				],
				[
					0.597903977224405,
					13.153887498938843
				],
				[
					1.1958079544489237,
					13.153887498938843
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.2006239891052246,
				0.20999087393283844,
				0.20761898159980774,
				0.2159338742494583,
				0.23797330260276794,
				0.2620731294155121,
				0.3370201885700226,
				0.4010024070739746,
				0.09645089507102966,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 601930766,
			"isDeleted": false,
			"id": "dKXkAgVW6pDV-Dbu4wN_B",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -658.2361934975686,
			"y": -577.628519029052,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.859360336855957,
			"height": 19.981464102940436,
			"seed": 735984291,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6244207532168957
				],
				[
					-0.6244207532168957,
					0.6244207532168957
				],
				[
					-0.6244207532168957,
					-1.2488415064337914
				],
				[
					1.8732622596505735,
					-6.2442075321688435
				],
				[
					8.11746979181953,
					-14.361677323988374
				],
				[
					13.112835817554583,
					-18.73262259650653
				],
				[
					14.98609807720527,
					-19.35704334972354
				],
				[
					16.23493958363906,
					-19.35704334972354
				],
				[
					16.23493958363906,
					-18.73262259650653
				],
				[
					16.23493958363906,
					-18.73262259650653
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.043879974633455276,
				0.08569943159818649,
				0.21720987558364868,
				0.24532291293144226,
				0.23720043897628784,
				0.2454318255186081,
				0.2900718152523041,
				0.32367271184921265,
				0.11038848757743835,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 346248146,
			"isDeleted": false,
			"id": "LLjnPd-E3NcsBRV8KW8K4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -638.8791501478452,
			"y": -603.8541906641613,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.11746979181953,
			"height": 11.239573557903896,
			"seed": 350797347,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.2488415064337914,
					-0.624420753216782
				],
				[
					6.244207532168957,
					-0.624420753216782
				],
				[
					8.11746979181953,
					0.6244207532170094
				],
				[
					6.868628285385739,
					3.7465245193013743
				],
				[
					3.7465245193013743,
					8.741890545036426
				],
				[
					2.497683012867583,
					10.615152804687114
				],
				[
					4.37094527251827,
					9.990732051470218
				],
				[
					4.995366025735166,
					9.366311298253322
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2749980092048645,
				0.2986123263835907,
				0.25546932220458984,
				0.30395662784576416,
				0.37890109419822693,
				0.38215184211730957,
				0.08227121084928513,
				0
			]
		},
		{
			"type": "text",
			"version": 22,
			"versionNonce": 2026506830,
			"isDeleted": false,
			"id": "H0THbc8K",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -624.2809660816082,
			"y": -631.5490516979398,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 50.991973876953125,
			"height": 20,
			"seed": 37886,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "=/ hub",
			"rawText": "=/ hub",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "=/ hub",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "text",
			"version": 58,
			"versionNonce": 1483540882,
			"isDeleted": false,
			"id": "TzB2juHA",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2664.111478631617,
			"y": -852.4983669210859,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 82.907958984375,
			"height": 140,
			"seed": 47562,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "energy\nand\npower\n",
			"rawText": "energy\nand\npower\n",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "energy\nand\npower\n",
			"lineHeight": 1.25,
			"baseline": 130
		},
		{
			"type": "text",
			"version": 31,
			"versionNonce": 2012188814,
			"isDeleted": false,
			"id": "WfGfYB2O",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2489.7017605800766,
			"y": -898.1161343614361,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 41.59996032714844,
			"height": 25,
			"seed": 57430,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "work",
			"rawText": "work",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "work",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 53,
			"versionNonce": 1828325202,
			"isDeleted": false,
			"id": "RkH7rg6S",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2405.084937898432,
			"y": -900.099444733506,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 59.219940185546875,
			"height": 25,
			"seed": 73600,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "energy",
			"rawText": "energy",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "energy",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 2097827534,
			"isDeleted": false,
			"id": "q_X8vrVAJBYD2Lca4Znqj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2431.724656894736,
			"y": -889.1035947170791,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.891517418453532,
			"height": 2.9749655581046,
			"seed": 1290665750,
			"groupIds": [
				"1kETuWt6M1XTtaj2IIzW4"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.9916551860346772,
					0
				],
				[
					4.958275930174295,
					0
				],
				[
					9.916551860349045,
					0.9916551860347909
				],
				[
					12.891517418453532,
					1.9833103720696954
				],
				[
					12.891517418453532,
					2.9749655581046
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17724597454071045,
				0.2153748720884323,
				0.17908737063407898,
				0.005222473293542862,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 1788955922,
			"isDeleted": false,
			"id": "whZ8Hj8swjMpeRQsA0n0i",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2434.6996224528407,
			"y": -880.1786980427652,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.883172604488209,
			"height": 1.983310372069809,
			"seed": 55440342,
			"groupIds": [
				"1kETuWt6M1XTtaj2IIzW4"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.9916551860346772,
					0.9916551860349045
				],
				[
					5.949931116209427,
					0.9916551860349045
				],
				[
					10.908207046383723,
					0.9916551860349045
				],
				[
					13.883172604488209,
					0
				],
				[
					13.883172604488209,
					-0.9916551860349045
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05829797312617302,
				0.19168899953365326,
				0.20585326850414276,
				0.029471740126609802,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 63,
			"versionNonce": 78857486,
			"isDeleted": false,
			"id": "JAkENxXjBZGxXXKQWjJYz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2434.6996224528407,
			"y": -900.0118017634629,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 21.816414092767445,
			"height": 7.933241488279009,
			"seed": 1339342998,
			"groupIds": [
				"1kETuWt6M1XTtaj2IIzW4"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.9916551860346772,
					-0.9916551860349045
				],
				[
					6.9415863022441044,
					-3.9666207441395045
				],
				[
					10.908207046383723,
					-2.9749655581046
				],
				[
					11.8998622324184,
					1.9833103720696954
				],
				[
					14.87482779052334,
					3.9666207441395045
				],
				[
					18.841448534662504,
					0.9916551860347909
				],
				[
					20.824758906732768,
					-1.983310372069809
				],
				[
					21.816414092767445,
					-1.983310372069809
				],
				[
					21.816414092767445,
					-1.983310372069809
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2099280059337616,
				0.2482355684041977,
				0.1894206553697586,
				0.178344264626503,
				0.20073944330215454,
				0.2418152391910553,
				0.21673406660556793,
				0.062051452696323395,
				0
			]
		},
		{
			"type": "text",
			"version": 78,
			"versionNonce": 1188682450,
			"isDeleted": false,
			"id": "nAdC4EJp",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2283.7054757921833,
			"y": -948.3413468884617,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 93.79991149902344,
			"height": 25,
			"seed": 90745,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "joules (J)",
			"rawText": "joules (J)",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "joules (J)",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 64,
			"versionNonce": 274953038,
			"isDeleted": false,
			"id": "abfVu5F5",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2293.9352227185727,
			"y": -893.5802028458095,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 152.57994079589844,
			"height": 25,
			"seed": 75279,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "10 j = 1 kg x 1m",
			"rawText": "10 j = 1 kg x 1m",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "10 j = 1 kg x 1m",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 13,
			"versionNonce": 809152658,
			"isDeleted": false,
			"id": "kUrTi0RH",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2296.1236284801776,
			"y": -843.8876385443101,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 50.37994384765625,
			"height": 25,
			"seed": 43320,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "force",
			"rawText": "force",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "force",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 42,
			"versionNonce": 175364494,
			"isDeleted": false,
			"id": "OcvVAwbZ",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2177.3965588847796,
			"y": -844.4344218683027,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 89.37991333007812,
			"height": 25,
			"seed": 28339,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "movement",
			"rawText": "movement",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "movement",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 1786433106,
			"isDeleted": false,
			"id": "5QEyTd2nGVIb0kqx29gXj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2218.463276915378,
			"y": -834.7253941911367,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 21.59135141947172,
			"height": 0.8636540567788416,
			"seed": 1948838422,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8636540567786142,
					0
				],
				[
					0.8636540567790689,
					-0.8636540567788416
				],
				[
					1.727308113557683,
					-0.8636540567788416
				],
				[
					4.318270283894435,
					-0.8636540567788416
				],
				[
					9.50019462456794,
					-0.8636540567788416
				],
				[
					17.273081135577286,
					0
				],
				[
					20.727697362693107,
					0
				],
				[
					19.000389249135424,
					0
				],
				[
					19.000389249135424,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09049282968044281,
				0.23386801779270172,
				0.27154800295829773,
				0.31845465302467346,
				0.3413911759853363,
				0.36003607511520386,
				0.3366221487522125,
				0.15277224779129028,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 706574286,
			"isDeleted": false,
			"id": "uOHBOn13RGJbD3Qi4G7_V",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2193.4173092687906,
			"y": -841.6346266453677,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.227502738125168,
			"height": 12.091156794904236,
			"seed": 751182806,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8636540567790689,
					0
				],
				[
					-0.8636540567790689,
					0.8636540567789552
				],
				[
					1.727308113557683,
					1.7273081135577968
				],
				[
					6.909232454230732,
					4.318270283894435
				],
				[
					10.363848681346099,
					6.90923245423096
				],
				[
					10.363848681346099,
					7.772886511009915
				],
				[
					7.772886511009801,
					8.636540567788757
				],
				[
					3.454616227115366,
					10.363848681346553
				],
				[
					0.8636540567786142,
					12.091156794904236
				],
				[
					2.5909621703362973,
					12.091156794904236
				],
				[
					3.454616227115366,
					11.227502738125395
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09732400625944138,
				0.1386529803276062,
				0.22310000658035278,
				0.2393823266029358,
				0.21936504542827606,
				0.21682235598564148,
				0.23901116847991943,
				0.30909085273742676,
				0.3738701343536377,
				0.1765662282705307,
				0
			]
		},
		{
			"type": "text",
			"version": 32,
			"versionNonce": 712061970,
			"isDeleted": false,
			"id": "U23o7Qmk",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2245.6132906941475,
			"y": -1018.3257507099067,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 39.27995300292969,
			"height": 25,
			"seed": 86592,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "time",
			"rawText": "time",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "time",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 20,
			"versionNonce": 1467567630,
			"isDeleted": false,
			"id": "Uh2yZiWZ66eXJ_98IQzoV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2187.3388823156088,
			"y": -1011.8499943851806,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.57664340366773,
			"height": 18.313634151818405,
			"seed": 526174870,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6315046259246628,
					-0.6315046259247765
				],
				[
					-1.2630092518493257,
					-1.8945138777743296
				],
				[
					-2.526018503699106,
					-1.8945138777743296
				],
				[
					-3.7890277555484317,
					-1.8945138777743296
				],
				[
					-6.315046259247538,
					1.8945138777743296
				],
				[
					-6.315046259247538,
					7.578055511097318
				],
				[
					-1.8945138777744432,
					12.63009251849553
				],
				[
					3.7890277555484317,
					14.52460639626986
				],
				[
					8.209560137021981,
					13.261597144420307
				],
				[
					11.998587892570868,
					9.472569388871648
				],
				[
					13.261597144420193,
					5.052037007398212
				],
				[
					11.998587892570868,
					1.263009251849553
				],
				[
					8.841064762946644,
					-1.8945138777743296
				],
				[
					4.420532381473549,
					-3.7890277555485454
				],
				[
					-0.6315046259246628,
					-2.526018503699106
				],
				[
					-0.6315046259246628,
					-2.526018503699106
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09688610583543777,
				0.14818087220191956,
				0.17073923349380493,
				0.21424490213394165,
				0.23447439074516296,
				0.2450745850801468,
				0.23238970339298248,
				0.19844119250774384,
				0.16832706332206726,
				0.17803329229354858,
				0.20502471923828125,
				0.20447488129138947,
				0.20296594500541687,
				0.07871419936418533,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 8,
			"versionNonce": 1913971154,
			"isDeleted": false,
			"id": "eUa_cquNx0DwtCf1oZn8P",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2184.181359185985,
			"y": -1015.6390221407291,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6315046259246628,
			"height": 5.0520370073980985,
			"seed": 1453830422,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.8945138777742159
				],
				[
					0,
					3.7890277555485454
				],
				[
					0,
					5.0520370073980985
				],
				[
					0.6315046259246628,
					5.0520370073980985
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.21341198682785034,
				0.18465499579906464,
				0.042019072920084,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 9,
			"versionNonce": 260070478,
			"isDeleted": false,
			"id": "Q_291FbR1GK4a6oYIyI_K",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2175.9717990489626,
			"y": -1006.1664527518576,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.420532381473549,
			"height": 1.263009251849553,
			"seed": 1477535894,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6315046259251176,
					0.6315046259247765
				],
				[
					-1.2630092518497804,
					0.6315046259247765
				],
				[
					-3.1575231296242237,
					0.6315046259247765
				],
				[
					-4.420532381473549,
					-0.6315046259247765
				],
				[
					-4.420532381473549,
					-0.6315046259247765
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12794598937034607,
				0.2240539789199829,
				0.2500339150428772,
				0.08296874910593033,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 7,
			"versionNonce": 1820120978,
			"isDeleted": false,
			"id": "0D-0QTmBVgujwyiiESvrY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2194.2854332007814,
			"y": -1006.7979573777824,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.68354163332333,
			"height": 1.263009251849553,
			"seed": 1974406486,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6315046259251176,
					-0.6315046259247765
				],
				[
					5.052037007398212,
					0
				],
				[
					5.68354163332333,
					0.6315046259247765
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19687600433826447,
				0.02489916980266571,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 7,
			"versionNonce": 1208722062,
			"isDeleted": false,
			"id": "YOYymlDBTiiadUvNy0IRj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2183.5498545600603,
			"y": -1005.5349481259328,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6315046259251176,
			"height": 3.1575231296238826,
			"seed": 1571682198,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6315046259247765
				],
				[
					0.6315046259251176,
					3.1575231296238826
				],
				[
					0.6315046259251176,
					3.1575231296238826
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1963079869747162,
				0.05305502191185951,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 7,
			"versionNonce": 1239422290,
			"isDeleted": false,
			"id": "d5F7dYgi0nxSC9D9CgliF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2179.129322178587,
			"y": -1011.8499943851806,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.526018503699106,
			"height": 3.789027755548659,
			"seed": 1037203926,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.2630092518493257,
					0.6315046259247765
				],
				[
					-1.8945138777739885,
					3.1575231296238826
				],
				[
					-2.526018503699106,
					3.789027755548659
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1294739991426468,
				0.08389068394899368,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 7,
			"versionNonce": 1406410958,
			"isDeleted": false,
			"id": "NBhGleTzD1qthIFA0oR3q",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2180.392331430436,
			"y": -1004.903443500008,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 1.263009251849553,
			"seed": 1402835990,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6315046259247765
				],
				[
					0,
					1.263009251849553
				],
				[
					0,
					1.263009251849553
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.04019095003604889,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 6,
			"versionNonce": 462789394,
			"isDeleted": false,
			"id": "lhs01eJBLqXi8Mbccvbsu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2181.023836056361,
			"y": -1004.2719388740833,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2630092518493257,
			"height": 1.263009251849553,
			"seed": 1274037846,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6315046259246628,
					1.263009251849553
				],
				[
					1.2630092518493257,
					1.263009251849553
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.045899536460638046,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 7,
			"versionNonce": 1181931278,
			"isDeleted": false,
			"id": "LP4yqhsNw2OKZ2i9o6vbi",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2186.707377689684,
			"y": -1003.0089296222337,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.8945138777739885,
			"height": 1.8945138777743296,
			"seed": 556231510,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6315046259246628,
					0
				],
				[
					-1.8945138777739885,
					1.8945138777743296
				],
				[
					-1.8945138777739885,
					1.8945138777743296
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16427399218082428,
				0.038073088973760605,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 6,
			"versionNonce": 806643922,
			"isDeleted": false,
			"id": "jY40AkDEmbBIB_tmTDqma",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2192.390919323007,
			"y": -1011.2184897592558,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.157523129623769,
			"height": 1.8945138777743296,
			"seed": 1009489302,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.526018503699106,
					1.263009251849553
				],
				[
					3.157523129623769,
					1.8945138777743296
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07748083770275116,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 9,
			"versionNonce": 1482736974,
			"isDeleted": false,
			"id": "wbfeFu0JZgNEmBekZFIfy",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2157.658164897144,
			"y": -1016.9020313925787,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.36708326664575,
			"height": 14.524606396269746,
			"seed": 580983446,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6315046259246628,
					1.263009251849553
				],
				[
					1.8945138777739885,
					3.157523129623769
				],
				[
					6.946550885172201,
					10.735578640721087
				],
				[
					10.735578640721087,
					14.524606396269746
				],
				[
					11.36708326664575,
					14.524606396269746
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15115024149417877,
				0.16295529901981354,
				0.029746612533926964,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 10,
			"versionNonce": 1861451410,
			"isDeleted": false,
			"id": "F5lHy05flFwgVjzWFJhEg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2143.1335585008746,
			"y": -1017.5335360185036,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.261597144420193,
			"height": 16.41912027404419,
			"seed": 574291798,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6315046259246628,
					0.6315046259248902
				],
				[
					-1.8945138777744432,
					0.6315046259248902
				],
				[
					-3.7890277555484317,
					2.526018503699106
				],
				[
					-9.472569388871307,
					9.472569388871648
				],
				[
					-13.261597144420193,
					16.41912027404419
				],
				[
					-13.261597144420193,
					16.41912027404419
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11747399717569351,
				0.17294800281524658,
				0.23118197917938232,
				0.27360400557518005,
				0.24333016574382782,
				0
			]
		},
		{
			"type": "text",
			"version": 20,
			"versionNonce": 1257696142,
			"isDeleted": false,
			"id": "dyXJUQQU",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2445.76823958329,
			"y": -743.0122509152976,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 144.27989196777344,
			"height": 25,
			"seed": 43729,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "/ time = power",
			"rawText": "/ time = power",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "/ time = power",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 38,
			"versionNonce": 887741522,
			"isDeleted": false,
			"id": "od0r3ZcM",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2220.8574670381645,
			"y": -788.0658381925111,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 90.93997192382812,
			"height": 25,
			"seed": 27481,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "1W = 1j/1s",
			"rawText": "1W = 1j/1s",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "1W = 1j/1s",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 1282296270,
			"isDeleted": false,
			"id": "faT5SdBWZymh8MgpTfXGT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2563.23133193274,
			"y": -821.9697436447337,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 50.02215558524631,
			"height": 46.13154348417174,
			"seed": 599517834,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5558017287248731,
					0.5558017287249868
				],
				[
					-1.1116034574497462,
					1.1116034574499736
				],
				[
					-1.1116034574497462,
					0.5558017287249868
				],
				[
					2.223206914899947,
					-4.446413829799667
				],
				[
					12.227638031949027,
					-16.11825013302382
				],
				[
					26.678482978798,
					-28.345888164972962
				],
				[
					37.79451755329728,
					-36.68291409584731
				],
				[
					44.464138297997124,
					-40.5735261969221
				],
				[
					48.35475039907169,
					-43.908336569271796
				],
				[
					48.910552127796564,
					-45.01994002672177
				],
				[
					48.35475039907169,
					-45.01994002672177
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.17151199281215668,
				0.24188800156116486,
				0.2874213755130768,
				0.30516907572746277,
				0.37073376774787903,
				0.4059571325778961,
				0.40198129415512085,
				0.3776271939277649,
				0.37209200859069824,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 802062866,
			"isDeleted": false,
			"id": "Ij3SFriKNKuMAN3K57KY6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2512.0975728900435,
			"y": -871.9918992299802,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.450844946848974,
			"height": 12.227638031949027,
			"seed": 2102766154,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5558017287248731,
					0
				],
				[
					3.3348103723496934,
					-0.5558017287248731
				],
				[
					9.448629388324207,
					-2.7790086436248203
				],
				[
					12.7834397606739,
					-3.3348103723496934
				],
				[
					13.895043218124101,
					-1.1116034574498599
				],
				[
					12.227638031949027,
					4.446413829799667
				],
				[
					11.671836303224154,
					8.892827659599334
				],
				[
					11.116034574499281,
					8.33702593087446
				],
				[
					11.116034574499281,
					7.781224202149474
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06107717752456665,
				0.23226401209831238,
				0.2791000008583069,
				0.21846966445446014,
				0.1903456449508667,
				0.2428397238254547,
				0.2936371862888336,
				0.1493159532546997,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 1541398542,
			"isDeleted": false,
			"id": "DwHlOkYFev6dmqW2b9s6I",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2559.8965215603903,
			"y": -780.2846139903617,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 73.92162992041995,
			"height": 44.4641382979969,
			"seed": 751430794,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5558017287248731,
					0
				],
				[
					-0.5558017287248731,
					-0.5558017287249868
				],
				[
					0.5558017287253278,
					-0.5558017287249868
				],
				[
					3.334810372350148,
					1.6674051861748467
				],
				[
					8.892827659599334,
					10.004431117049307
				],
				[
					18.89725877664887,
					20.0088622340985
				],
				[
					32.2365002660481,
					28.90168989369795
				],
				[
					49.46635385652189,
					36.127112367122436
				],
				[
					65.02880226082061,
					41.12932792564709
				],
				[
					73.36582819169507,
					43.90833656927191
				],
				[
					68.91941436189518,
					43.90833656927191
				],
				[
					66.69620744699523,
					42.24093138309695
				],
				[
					66.69620744699523,
					41.68512965437196
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.059199828654527664,
				0.07305960357189178,
				0.13798226416110992,
				0.17797045409679413,
				0.24572482705116272,
				0.27375996112823486,
				0.24458657205104828,
				0.24768780171871185,
				0.33471691608428955,
				0.41805341839790344,
				0.41078513860702515,
				0.15589316189289093,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 18,
			"versionNonce": 983068626,
			"isDeleted": false,
			"id": "DDYMJfj7kn3A2pUpzeBxs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2484.8632881825206,
			"y": -730.2624584051152,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.895043218124101,
			"height": 13.895043218123988,
			"seed": 718627274,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5558017287248731,
					0
				],
				[
					-0.5558017287248731,
					0.5558017287248731
				],
				[
					-1.1116034574497462,
					1.1116034574499736
				],
				[
					2.223206914899947,
					1.1116034574499736
				],
				[
					7.2254224734247146,
					2.7790086436248203
				],
				[
					11.116034574499281,
					4.446413829799667
				],
				[
					12.227638031949482,
					3.890612101074794
				],
				[
					12.783439760674355,
					1.6674051861748467
				],
				[
					12.227638031949482,
					-1.1116034574499736
				],
				[
					11.116034574499281,
					-5.002215558524654
				],
				[
					10.004431117049535,
					-8.33702593087446
				],
				[
					10.004431117049535,
					-9.44862938832432
				],
				[
					11.116034574499281,
					-9.44862938832432
				],
				[
					11.116034574499281,
					-9.44862938832432
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999197393655777,
				0.12330398708581924,
				0.2883780002593994,
				0.35341399908065796,
				0.37143081426620483,
				0.3817637860774994,
				0.363221675157547,
				0.2969192862510681,
				0.2783007025718689,
				0.3268674314022064,
				0.44391754269599915,
				0.4855259954929352,
				0.14846262335777283,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 759475790,
			"isDeleted": false,
			"id": "329pIj_KZCTPhJv8wYAPn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2444.8455637143234,
			"y": -861.4316663842059,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.5580172872496405,
			"height": 75.03323337786969,
			"seed": 1072926154,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5558017287249868
				],
				[
					-0.5558017287248731,
					-0.5558017287249868
				],
				[
					-0.5558017287248731,
					0
				],
				[
					-1.1116034574497462,
					7.225422473424487
				],
				[
					-1.1116034574497462,
					22.78787087772332
				],
				[
					2.223206914899947,
					37.79451755329728
				],
				[
					4.446413829799894,
					51.1337590426964
				],
				[
					4.446413829799894,
					61.69399188847058
				],
				[
					3.3348103723496934,
					66.69620744699523
				],
				[
					2.7790086436248203,
					71.69842300551989
				],
				[
					2.7790086436248203,
					74.4774316491447
				],
				[
					3.3348103723496934,
					73.92162992041972
				],
				[
					3.3348103723496934,
					73.92162992041972
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06395462155342102,
				0.12464511394500732,
				0.17745919525623322,
				0.22239315509796143,
				0.2885781228542328,
				0.3310340344905853,
				0.33482518792152405,
				0.389608770608902,
				0.40605202317237854,
				0.3330934941768646,
				0.3203897476196289,
				0.10824951529502869,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 962504082,
			"isDeleted": false,
			"id": "iCoysXaunvPAGw6bwilkT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2445.4013654430482,
			"y": -773.0591915169372,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.116034574498826,
			"height": 13.895043218123988,
			"seed": 697281290,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5558017287248731,
					0.5558017287249868
				],
				[
					-1.1116034574497462,
					1.1116034574498599
				],
				[
					-1.1116034574497462,
					2.7790086436248203
				],
				[
					3.3348103723496934,
					8.337025930874347
				],
				[
					6.113819015974514,
					13.339241489399
				],
				[
					6.669620744699387,
					13.339241489399
				],
				[
					6.669620744699387,
					9.44862938832432
				],
				[
					7.781224202149588,
					3.89061210107468
				],
				[
					9.448629388324207,
					-0.5558017287249868
				],
				[
					10.00443111704908,
					-0.5558017287249868
				],
				[
					9.448629388324207,
					-0.5558017287249868
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0968490019440651,
				0.140193909406662,
				0.20672400295734406,
				0.21613556146621704,
				0.2420760542154312,
				0.26804494857788086,
				0.3353599011898041,
				0.37609049677848816,
				0.3905276358127594,
				0.1796441674232483,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 225817742,
			"isDeleted": false,
			"id": "8sO3L-BrnFEdu0C82jq0v",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2280.328252011735,
			"y": -727.4834497614904,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 38.350319282022156,
			"height": 28.345888164972962,
			"seed": 896047818,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5558017287249868
				],
				[
					6.113819015974514,
					-7.225422473424487
				],
				[
					20.564663962823488,
					-18.341457047923768
				],
				[
					31.124896808597896,
					-25.01107779262327
				],
				[
					37.23871582457241,
					-27.790086436247975
				],
				[
					38.350319282022156,
					-28.345888164972962
				],
				[
					35.571310638397335,
					-27.234284707523102
				],
				[
					35.01550890967246,
					-27.234284707523102
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1017022430896759,
				0.187578484416008,
				0.2900319993495941,
				0.29188284277915955,
				0.23592592775821686,
				0.24503478407859802,
				0.10012606531381607,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 16,
			"versionNonce": 1968710482,
			"isDeleted": false,
			"id": "37lOQwcZAA6x0BgxIkfxb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2236.975717171188,
			"y": -760.831553484988,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.339241489399228,
			"height": 12.227638031949141,
			"seed": 118982218,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.1116034574497462,
					0
				],
				[
					-1.667405186175074,
					0
				],
				[
					-1.667405186175074,
					-0.5558017287249868
				],
				[
					2.7790086436248203,
					-1.6674051861748467
				],
				[
					10.00443111704908,
					-2.2232069148998335
				],
				[
					11.671836303224154,
					0
				],
				[
					11.116034574499281,
					0.5558017287248731
				],
				[
					8.892827659599334,
					2.2232069148998335
				],
				[
					4.4464138297994396,
					6.113819015974514
				],
				[
					3.3348103723496934,
					9.44862938832432
				],
				[
					4.4464138297994396,
					10.004431117049307
				],
				[
					5.002215558524767,
					9.44862938832432
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.026762329041957855,
				0.11884622275829315,
				0.23114199936389923,
				0.3375539779663086,
				0.32435137033462524,
				0.2548049986362457,
				0.2909867763519287,
				0.3578788936138153,
				0.36784815788269043,
				0.1874462515115738,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 1177285326,
			"isDeleted": false,
			"id": "HXNFtIzGT80-J0iDJ7q8S",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2336.560197437146,
			"y": -884.9155669054028,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 25.70365548822201,
			"height": 24.385519309338974,
			"seed": 1200217290,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6590680894415755
				],
				[
					0.6590680894414618,
					-1.97720426832484
				],
				[
					3.2953404472077636,
					-5.272544715532717
				],
				[
					13.840429878273426,
					-15.158566057156577
				],
				[
					23.72645121989717,
					-22.408315041014134
				],
				[
					25.70365548822201,
					-24.385519309338974
				],
				[
					22.408315041013793,
					-22.408315041014134
				],
				[
					23.06738313045571,
					-22.408315041014134
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05914938449859619,
				0.11702881008386612,
				0.17571797966957092,
				0.2711400091648102,
				0.30649298429489136,
				0.31903076171875,
				0.11001233011484146,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 2027677970,
			"isDeleted": false,
			"id": "Nm5xWfDBmMteaX-SZaQ_j",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2306.243065322833,
			"y": -917.2099032880408,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.545089431065207,
			"height": 9.88602134162386,
			"seed": 1492011082,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6590680894414618,
					-0.6590680894416892
				],
				[
					6.590680894415982,
					-2.6362723577664156
				],
				[
					10.545089431065207,
					-3.295340447207991
				],
				[
					9.886021341623746,
					-0.6590680894416892
				],
				[
					6.590680894415982,
					3.954408536649453
				],
				[
					4.613476626091142,
					6.590680894415868
				],
				[
					5.272544715532604,
					5.272544715532717
				],
				[
					5.9316128049740655,
					4.613476626091142
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2295759916305542,
				0.27977100014686584,
				0.2474633753299713,
				0.27008259296417236,
				0.36709609627723694,
				0.34355300664901733,
				0.23940353095531464,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 33581326,
			"isDeleted": false,
			"id": "62nd1zHiDnkVsNOS8dxSJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2333.2648569899384,
			"y": -875.6886136532205,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 22.408315041013793,
			"height": 28.998995935430116,
			"seed": 619336650,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6590680894414618,
					0
				],
				[
					-1.3181361788829236,
					0
				],
				[
					0.6590680894414618,
					4.613476626091142
				],
				[
					6.590680894415982,
					13.840429878273426
				],
				[
					14.499497967714888,
					23.7264512198974
				],
				[
					19.772042683247946,
					28.33992784598854
				],
				[
					21.09017886213087,
					28.998995935430116
				],
				[
					18.453906504364568,
					26.3627235776637
				],
				[
					17.794838414923106,
					25.703655488222125
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11918628215789795,
				0.23952999711036682,
				0.3046640157699585,
				0.34723928570747375,
				0.33555686473846436,
				0.3509036898612976,
				0.21091848611831665,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 1801516754,
			"isDeleted": false,
			"id": "fAySSe7eVKfJobjpskm-j",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2306.9021334122745,
			"y": -853.9393667016479,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.545089431065662,
			"height": 13.18136178883185,
			"seed": 1154188810,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6590680894414618,
					1.318136178883151
				],
				[
					3.9544085366492254,
					5.272544715532717
				],
				[
					6.590680894415527,
					8.567885162740708
				],
				[
					7.249748983857444,
					10.545089431065435
				],
				[
					5.272544715532604,
					11.204157520507124
				],
				[
					1.3181361788829236,
					12.522293699390275
				],
				[
					-2.6362723577667566,
					13.18136178883185
				],
				[
					-3.2953404472082184,
					13.18136178883185
				],
				[
					-1.97720426832484,
					13.18136178883185
				],
				[
					-1.3181361788833783,
					13.18136178883185
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.30159398913383484,
				0.33193403482437134,
				0.3112148344516754,
				0.2899114191532135,
				0.29562774300575256,
				0.3812790513038635,
				0.4695819914340973,
				0.44351911544799805,
				0.13965271413326263,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 812390222,
			"isDeleted": false,
			"id": "mBEhGvHld5iE8uB3NvrGS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2323.3788356483146,
			"y": -879.6430221898701,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.522293699390502,
			"height": 1.97720426832484,
			"seed": 1794246410,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6590680894414618,
					0
				],
				[
					-0.6590680894414618,
					-0.6590680894415755
				],
				[
					3.2953404472082184,
					-0.6590680894415755
				],
				[
					7.90881707329936,
					0
				],
				[
					11.86322560994904,
					1.3181361788832646
				],
				[
					11.204157520507124,
					1.3181361788832646
				],
				[
					10.545089431065662,
					0.6590680894415755
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11515799164772034,
				0.22329050302505493,
				0.3104499876499176,
				0.3309898376464844,
				0.1235705241560936,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 1836993682,
			"isDeleted": false,
			"id": "n_Ecu3hWtyPWwgqK9VC-e",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2306.243065322833,
			"y": -882.938362637078,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.249748983857444,
			"height": 10.545089431065549,
			"seed": 2097589194,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6590680894414618,
					-0.6590680894416892
				],
				[
					1.3181361788829236,
					0.6590680894414618
				],
				[
					4.613476626091142,
					1.9772042683247264
				],
				[
					6.590680894415982,
					3.2953404472078773
				],
				[
					6.590680894415982,
					5.272544715532604
				],
				[
					3.2953404472077636,
					7.908817073299019
				],
				[
					1.3181361788829236,
					9.88602134162386
				],
				[
					0.6590680894414618,
					9.88602134162386
				],
				[
					1.3181361788829236,
					8.567885162740595
				],
				[
					1.97720426832484,
					7.908817073299019
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11658599972724915,
				0.32691699266433716,
				0.33969396352767944,
				0.26237359642982483,
				0.2647930085659027,
				0.31767040491104126,
				0.3767843544483185,
				0.32843565940856934,
				0.06585866957902908,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 1774714254,
			"isDeleted": false,
			"id": "Zsrql-3A6wGACUwnHrEhi",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2348.4234230470947,
			"y": -903.3694734097674,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.567885162740822,
			"height": 11.8632256099487,
			"seed": 2107280586,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6590680894419165,
					0
				],
				[
					-1.3181361788833783,
					0
				],
				[
					-1.3181361788833783,
					-0.6590680894416892
				],
				[
					2.636272357766302,
					-5.931612804974407
				],
				[
					6.590680894415527,
					-11.204157520507124
				],
				[
					7.249748983857444,
					-11.8632256099487
				],
				[
					6.590680894415527,
					-11.204157520507124
				],
				[
					6.590680894415527,
					-10.545089431065549
				],
				[
					6.590680894415527,
					-11.204157520507124
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.044563017785549164,
				0.13827039301395416,
				0.20321087539196014,
				0.23698227107524872,
				0.2627294361591339,
				0.2433789074420929,
				0.035626862198114395,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 11,
			"versionNonce": 1961552466,
			"isDeleted": false,
			"id": "S5YdHo7v4PZNuZMnkFcWL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2335.9011293477047,
			"y": -924.4596522718983,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.567885162740367,
			"height": 7.908817073299133,
			"seed": 825319178,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6590680894414618,
					0
				],
				[
					0,
					0
				],
				[
					2.636272357766302,
					-3.295340447207991
				],
				[
					5.93161280497452,
					-7.2497489838575575
				],
				[
					6.590680894415982,
					-7.908817073299133
				],
				[
					7.249748983857444,
					-7.2497489838575575
				],
				[
					7.908817073298906,
					-7.2497489838575575
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.17948584258556366,
				0.25547000765800476,
				0.29999488592147827,
				0.2847979962825775,
				0.0607137456536293,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 12,
			"versionNonce": 1397562318,
			"isDeleted": false,
			"id": "iHWarJvspbPf-cbUVq0S7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2320.742563290548,
			"y": -939.618218329055,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.90881707329936,
			"height": 9.226953252182284,
			"seed": 1438843850,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6590680894419165,
					0
				],
				[
					-0.6590680894419165,
					-0.6590680894415755
				],
				[
					1.3181361788829236,
					-2.636272357766302
				],
				[
					5.9316128049740655,
					-7.249748983857444
				],
				[
					7.249748983857444,
					-9.226953252182284
				],
				[
					6.590680894415527,
					-8.567885162740708
				],
				[
					6.590680894415527,
					-7.908817073299133
				],
				[
					6.590680894415527,
					-7.908817073299133
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05786199867725372,
				0.14052025973796844,
				0.20613998174667358,
				0.2531700134277344,
				0.2232275754213333,
				0.1756044626235962,
				0.057508423924446106,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 10,
			"versionNonce": 679333906,
			"isDeleted": false,
			"id": "ttiZuXgDhw1yxvsd1xeNc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2308.220269591158,
			"y": -952.7995801178869,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.545089431065662,
			"height": 9.88602134162386,
			"seed": 993177418,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.3181361788833783,
					-0.6590680894415755
				],
				[
					7.249748983857444,
					-5.272544715532717
				],
				[
					10.545089431065662,
					-9.88602134162386
				],
				[
					9.886021341623746,
					-9.88602134162386
				],
				[
					9.226953252182284,
					-9.88602134162386
				],
				[
					9.226953252182284,
					-9.88602134162386
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15275774896144867,
				0.2319840043783188,
				0.2544821798801422,
				0.2158089578151703,
				0.07237447798252106,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 10,
			"versionNonce": 51671566,
			"isDeleted": false,
			"id": "JGOpfN3F7RpgC3Z3hGjnA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2289.7663630867933,
			"y": -969.2762823539267,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.226953252182284,
			"height": 6.590680894415868,
			"seed": 1333216586,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6590680894415755
				],
				[
					1.3181361788833783,
					-1.9772042683247264
				],
				[
					5.93161280497452,
					-4.613476626091142
				],
				[
					9.226953252182284,
					-6.590680894415868
				],
				[
					8.567885162740822,
					-6.590680894415868
				],
				[
					8.567885162740822,
					-6.590680894415868
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0999319776892662,
				0.1867164671421051,
				0.2764039933681488,
				0.3148309886455536,
				0.0463523268699646,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 10,
			"versionNonce": 1009647058,
			"isDeleted": false,
			"id": "2bBx2hMkLWsSRwmboAIgw",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2271.97152467187,
			"y": -983.1167122322001,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.567885162740822,
			"height": 5.931612804974293,
			"seed": 88464202,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6590680894415755
				],
				[
					0.6590680894414618,
					-1.318136178883151
				],
				[
					5.272544715532604,
					-3.9544085366495665
				],
				[
					8.567885162740822,
					-5.931612804974293
				],
				[
					7.908817073298906,
					-4.613476626091142
				],
				[
					7.908817073298906,
					-4.613476626091142
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.024736754596233368,
				0.09573473781347275,
				0.19254998862743378,
				0.25448450446128845,
				0.03538961708545685,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 1679229006,
			"isDeleted": false,
			"id": "NAzjeoVmJAz83a0OxHPU-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2258.790162883038,
			"y": -996.9571421104736,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.886021341623746,
			"height": 8.567885162740708,
			"seed": 849244490,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6590680894415755
				],
				[
					0.6590680894414618,
					0.6590680894415755
				],
				[
					6.590680894415982,
					0
				],
				[
					9.886021341623746,
					0
				],
				[
					9.886021341623746,
					1.97720426832484
				],
				[
					7.249748983857444,
					5.272544715532717
				],
				[
					4.613476626091142,
					7.908817073299133
				],
				[
					3.9544085366492254,
					8.567885162740708
				],
				[
					3.2953404472077636,
					7.2497489838575575
				],
				[
					3.2953404472077636,
					7.2497489838575575
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1520184874534607,
				0.19922998547554016,
				0.21457314491271973,
				0.21297726035118103,
				0.23902356624603271,
				0.29157477617263794,
				0.3346105217933655,
				0.28504717350006104,
				0.1250794380903244,
				0
			]
		},
		{
			"type": "text",
			"version": 11,
			"versionNonce": 1293054866,
			"isDeleted": false,
			"id": "YpjLqFoD",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2259.6467509992654,
			"y": -672.0564720817059,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 30.299957275390625,
			"height": 25,
			"seed": 65191,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "life",
			"rawText": "life",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "life",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 3,
			"versionNonce": 439207566,
			"isDeleted": false,
			"id": "yk263kO2",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2188.784427034465,
			"y": -704.8951100166136,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 104.33993530273438,
			"height": 25,
			"seed": 78233,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "LED 5-15W",
			"rawText": "LED 5-15W",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "LED 5-15W",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 34,
			"versionNonce": 1029845330,
			"isDeleted": false,
			"id": "nqeXInOx",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2184.7018096975985,
			"y": -670.5941091467049,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 89.63993835449219,
			"height": 25,
			"seed": 37784,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "phone 3W",
			"rawText": "phone 3W",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "phone 3W",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 15,
			"versionNonce": 1712440526,
			"isDeleted": false,
			"id": "P5EJ4wTt",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2179.5319163880927,
			"y": -607.1611854092023,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 154.0198516845703,
			"height": 25,
			"seed": 75401,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "battery devices",
			"rawText": "battery devices",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "battery devices",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 36,
			"versionNonce": 276051730,
			"isDeleted": false,
			"id": "ZTB2UbG8",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1986.215983079442,
			"y": -608.5435478724083,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.599990844726562,
			"height": 25,
			"seed": 92681,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 1
			},
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "1w",
			"rawText": "1w",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": null,
			"originalText": "1w",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "freedraw",
			"version": 19,
			"versionNonce": 157022990,
			"isDeleted": false,
			"id": "QDuJiTazBVBgaf6iHzqJ3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2002.7903609803016,
			"y": -602.6500757286385,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.017282832966885,
			"height": 11.416418691318654,
			"seed": 334442326,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6008641416483442
				],
				[
					-1.2017282832966885,
					0
				],
				[
					-4.20604899153841,
					2.403456566593377
				],
				[
					-6.6095055581317865,
					4.206048991538523
				],
				[
					-8.41209798307682,
					5.407777274835212
				],
				[
					-7.811233841428475,
					5.407777274835212
				],
				[
					-7.210369699780131,
					6.008641416483556
				],
				[
					-6.6095055581317865,
					6.6095055581319
				],
				[
					-6.008641416483442,
					6.6095055581319
				],
				[
					-4.20604899153841,
					7.2103696997802444
				],
				[
					-1.2017282832966885,
					7.811233841428589
				],
				[
					1.2017282832966885,
					9.012962124725277
				],
				[
					3.004320708241721,
					9.613826266373621
				],
				[
					3.6051848498900654,
					10.81555454967031
				],
				[
					3.6051848498900654,
					10.81555454967031
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15639999508857727,
				0.21199624240398407,
				0.19913701713085175,
				0.23850855231285095,
				0.25624987483024597,
				0.23989632725715637,
				0.24759377539157867,
				0.2656727433204651,
				0.2885676324367523,
				0.3361193537712097,
				0.37986940145492554,
				0.39094436168670654,
				0.3641164004802704,
				0.3158387839794159,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 15,
			"versionNonce": 1186956498,
			"isDeleted": false,
			"id": "tWFxxfmKAfq9VnQ3MJqM9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2305.6294146275904,
			"y": -711.5407998580788,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 20.520270192922908,
			"height": 35.05546157957633,
			"seed": 1286858902,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.8550112580385303
				],
				[
					0,
					0
				],
				[
					0,
					5.130067548230727
				],
				[
					0.8550112580387577,
					12.825168870576704
				],
				[
					3.4200450321536664,
					19.665258934884264
				],
				[
					8.550112580384393,
					25.650337741153407
				],
				[
					13.68018012861512,
					29.925394031345604
				],
				[
					17.955236418807544,
					32.49042780546097
				],
				[
					20.520270192922908,
					34.2004503215378
				],
				[
					19.66525893488415,
					33.345439063499384
				],
				[
					19.66525893488415,
					33.345439063499384
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08481737971305847,
				0.18348461389541626,
				0.23276391625404358,
				0.28533342480659485,
				0.32104435563087463,
				0.3554031550884247,
				0.38425490260124207,
				0.42705050110816956,
				0.4619126617908478,
				0.10504709184169769,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 713386318,
			"isDeleted": false,
			"id": "HHJFKI4YpUX69W6qe71Xe",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2281.689099402514,
			"y": -682.4704170847716,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.405123838423151,
			"height": 11.970157612538173,
			"seed": 134812886,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.7100225160770606,
					0.8550112580384166
				],
				[
					4.275056290192424,
					4.275056290192197
				],
				[
					6.8400900643077875,
					7.695101322345977
				],
				[
					8.550112580384393,
					9.405123838422924
				],
				[
					9.405123838423151,
					10.26013509646134
				],
				[
					5.98507880626903,
					10.26013509646134
				],
				[
					2.5650337741153635,
					11.115146354499757
				],
				[
					0.8550112580383029,
					11.970157612538173
				],
				[
					1.7100225160770606,
					11.115146354499757
				],
				[
					1.7100225160770606,
					10.26013509646134
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2008100003004074,
				0.26050201058387756,
				0.2821104824542999,
				0.2898273169994354,
				0.28957638144493103,
				0.3548896610736847,
				0.4016856849193573,
				0.40088188648223877,
				0.16122177243232727,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 970660498,
			"isDeleted": false,
			"id": "t_26J6q8uelserwOYeL9V",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2223.5483338558997,
			"y": -666.2252031820411,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.66525893488415,
			"height": 19.665258934884264,
			"seed": 768426966,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8550112580383029,
					-0.8550112580384166
				],
				[
					0.8550112580387577,
					-2.5650337741153635
				],
				[
					5.130067548230727,
					-6.84009006430756
				],
				[
					11.970157612538515,
					-13.680180128615234
				],
				[
					17.955236418807544,
					-19.665258934884264
				],
				[
					18.810247676845847,
					-19.665258934884264
				],
				[
					18.810247676845847,
					-18.810247676845847
				],
				[
					17.10022516076924,
					-17.1002251607689
				],
				[
					17.10022516076924,
					-17.1002251607689
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1341399848461151,
				0.2403779923915863,
				0.29976198077201843,
				0.3393682539463043,
				0.334840327501297,
				0.3307635486125946,
				0.34342774748802185,
				0.0689561739563942,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 13,
			"versionNonce": 954666894,
			"isDeleted": false,
			"id": "KcV870_xPQEodiTmCa3t2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2202.1730524049385,
			"y": -691.8755409231945,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.405123838422696,
			"height": 13.68018012861512,
			"seed": 1636701590,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8550112580383029,
					0
				],
				[
					2.5650337741153635,
					-0.8550112580384166
				],
				[
					5.985078806269485,
					-0.8550112580384166
				],
				[
					8.550112580384393,
					0
				],
				[
					8.550112580384393,
					3.42004503215378
				],
				[
					6.8400900643077875,
					8.550112580384507
				],
				[
					4.275056290192424,
					12.825168870576704
				],
				[
					4.275056290192424,
					11.970157612538173
				],
				[
					4.275056290192424,
					11.115146354499757
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09866098314523697,
				0.3218039870262146,
				0.32809361815452576,
				0.2740893065929413,
				0.29569560289382935,
				0.3872813284397125,
				0.4499839246273041,
				0.22919970750808716,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 8,
			"versionNonce": 2021521490,
			"isDeleted": false,
			"id": "zZvNA0es4Vq088TsYNJm-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2219.2732775657073,
			"y": -653.4000343114644,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.535191386653423,
			"height": 0,
			"seed": 576041814,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8550112580383029,
					0
				],
				[
					6.8400900643077875,
					0
				],
				[
					12.825168870576817,
					0
				],
				[
					14.535191386653423,
					0
				],
				[
					14.535191386653423,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.280349999666214,
				0.33264198899269104,
				0.3329342305660248,
				0.30554571747779846,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 1354362318,
			"isDeleted": false,
			"id": "l0SEo1iXmsjA3d_6h6xKd",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2199.608018630823,
			"y": -659.3851131177336,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.260135096461454,
			"height": 12.82516887057659,
			"seed": 142012438,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8550112580383029,
					-0.8550112580384166
				],
				[
					1.7100225160770606,
					-0.8550112580384166
				],
				[
					4.275056290192424,
					0
				],
				[
					7.6951013223460905,
					1.7100225160769469
				],
				[
					9.405123838423151,
					2.56503377411525
				],
				[
					8.550112580384393,
					3.42004503215378
				],
				[
					6.8400900643077875,
					4.275056290192197
				],
				[
					4.275056290192424,
					5.130067548230613
				],
				[
					0.8550112580387577,
					5.985078806269144
				],
				[
					0,
					8.550112580384507
				],
				[
					0,
					10.26013509646134
				],
				[
					0,
					11.970157612538173
				],
				[
					-0.8550112580383029,
					11.970157612538173
				],
				[
					-0.8550112580383029,
					11.970157612538173
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.20344598591327667,
				0.30903199315071106,
				0.3812990188598633,
				0.4009886085987091,
				0.38954392075538635,
				0.37645551562309265,
				0.44622600078582764,
				0.47159314155578613,
				0.48981964588165283,
				0.47951197624206543,
				0.41500189900398254,
				0.29026347398757935,
				0.06547961384057999,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 14,
			"versionNonce": 578756114,
			"isDeleted": false,
			"id": "O7sXD9so9QbT5vF3o0cEj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2224.403345113938,
			"y": -646.5599442471569,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.66525893488415,
			"height": 35.91047283761475,
			"seed": 394855446,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8550112580384166
				],
				[
					0,
					1.7100225160768332
				],
				[
					0,
					7.695101322345977
				],
				[
					1.7100225160770606,
					17.955236418807317
				],
				[
					6.8400900643077875,
					26.505348999191824
				],
				[
					13.68018012861512,
					29.925394031345604
				],
				[
					17.10022516076924,
					32.49042780546097
				],
				[
					19.66525893488415,
					35.05546157957633
				],
				[
					19.66525893488415,
					35.91047283761475
				],
				[
					17.955236418807544,
					35.05546157957633
				],
				[
					17.955236418807544,
					35.05546157957633
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05562524497509003,
				0.16156664490699768,
				0.23149321973323822,
				0.2998867928981781,
				0.35499754548072815,
				0.3790256083011627,
				0.36640289425849915,
				0.3827005922794342,
				0.37528854608535767,
				0.10322097688913345,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 17,
			"versionNonce": 521602062,
			"isDeleted": false,
			"id": "jnT5EBrZfZ61sDwRPsho9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2197.042984856708,
			"y": -614.9245276997344,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.550112580384393,
			"height": 14.53519138665365,
			"seed": 1970896982,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709018862185,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8550112580385303
				],
				[
					-0.8550112580383029,
					1.7100225160769469
				],
				[
					-0.8550112580383029,
					2.5650337741153635
				],
				[
					2.5650337741153635,
					5.985078806269257
				],
				[
					5.130067548230727,
					10.260135096461454
				],
				[
					6.8400900643077875,
					12.825168870576817
				],
				[
					6.8400900643077875,
					13.680180128615234
				],
				[
					5.130067548230727,
					14.53519138665365
				],
				[
					3.4200450321536664,
					14.53519138665365
				],
				[
					0.8550112580387577,
					13.680180128615234
				],
				[
					0,
					13.680180128615234
				],
				[
					-0.8550112580383029,
					12.825168870576817
				],
				[
					-1.7100225160766058,
					12.825168870576817
				],
				[
					-1.7100225160766058,
					11.970157612538287
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.111580990254879,
				0.1661820113658905,
				0.25693202018737793,
				0.24862463772296906,
				0.245756596326828,
				0.2568167448043823,
				0.302886039018631,
				0.3749156594276428,
				0.3982541263103485,
				0.3732124865055084,
				0.25301051139831543,
				0.08849798887968063,
				0
			]
		},
		{
			"type": "text",
			"version": 239,
			"versionNonce": 1705761200,
			"isDeleted": false,
			"id": "CCa4PPhc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -646.4364700808269,
			"y": -1096.6960607108545,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 680.37939453125,
			"height": 250,
			"seed": 364028114,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709026583857,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Home automation is actually a term that is used for what\nwould be more accurate to call building automation. With it \nwe mean all that is concerned with automating as many of the \nprocesses inside a building and therefore penetration is much more \nimportant than range int these type of applications. \nIt is also important to specify that when we say automation we \nmean that all the processes should be managed by the software, \nfor example the lights should turn on when it is dark and there \nare people in the office but without any extra inputs from someone \nexcept the initial setup.",
			"rawText": "Home automation is actually a term that is used for what\nwould be more accurate to call building automation. With it \nwe mean all that is concerned with automating as many of the \nprocesses inside a building and therefore penetration is much more \nimportant than range int these type of applications. \nIt is also important to specify that when we say automation we \nmean that all the processes should be managed by the software, \nfor example the lights should turn on when it is dark and there \nare people in the office but without any extra inputs from someone \nexcept the initial setup.",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Home automation is actually a term that is used for what\nwould be more accurate to call building automation. With it \nwe mean all that is concerned with automating as many of the \nprocesses inside a building and therefore penetration is much more \nimportant than range int these type of applications. \nIt is also important to specify that when we say automation we \nmean that all the processes should be managed by the software, \nfor example the lights should turn on when it is dark and there \nare people in the office but without any extra inputs from someone \nexcept the initial setup.",
			"lineHeight": 1.25,
			"baseline": 243
		},
		{
			"id": "evlerF7H",
			"type": "text",
			"x": -527.1306534589867,
			"y": -782.4226897257454,
			"width": 753.2193603515625,
			"height": 175,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 907363152,
			"version": 543,
			"versionNonce": 1227011504,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1709025481180,
			"link": null,
			"locked": false,
			"text": "As we saw before we need to ask ourselves which network\ntype is best suited for the application of building automation.\nAt firs one might think of wifi, but it comes with his own problems,\nchanging password would mean update all the devices, range is limitad\nexpecially in hard to reach places and devices that use wifi require\ntoo much power. Wifi is still used for some applications but not all of them.\n",
			"rawText": "As we saw before we need to ask ourselves which network\ntype is best suited for the application of building automation.\nAt firs one might think of wifi, but it comes with his own problems,\nchanging password would mean update all the devices, range is limitad\nexpecially in hard to reach places and devices that use wifi require\ntoo much power. Wifi is still used for some applications but not all of them.\n",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 168,
			"containerId": null,
			"originalText": "As we saw before we need to ask ourselves which network\ntype is best suited for the application of building automation.\nAt firs one might think of wifi, but it comes with his own problems,\nchanging password would mean update all the devices, range is limitad\nexpecially in hard to reach places and devices that use wifi require\ntoo much power. Wifi is still used for some applications but not all of them.\n",
			"lineHeight": 1.25
		},
		{
			"id": "h1cIiVRx",
			"type": "text",
			"x": -448.8765892994162,
			"y": -490.7484505855274,
			"width": 770.859375,
			"height": 175,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1188239696,
			"version": 575,
			"versionNonce": 505898416,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1709025480443,
			"link": null,
			"locked": false,
			"text": "This problems brought the birth of many different protocols trying\nto fix the short comings of wifi. The most importan once are Zigbee,\nBluethoot and 6LowPAN, every protocol has specific uses and more than one\nmight be used in the same network but since each uses a different\nfrequency each need his own hub to do protocol translation. In genera though\nthey all use the licence free spectrum and use lower than 1GHz frequencies\nfor higher propagation",
			"rawText": "This problems brought the birth of many different protocols trying\nto fix the short comings of wifi. The most importan once are Zigbee,\nBluethoot and 6LowPAN, every protocol has specific uses and more than one\nmight be used in the same network but since each uses a different\nfrequency each need his own hub to do protocol translation. In genera though\nthey all use the licence free spectrum and use lower than 1GHz frequencies\nfor higher propagation",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 168,
			"containerId": null,
			"originalText": "This problems brought the birth of many different protocols trying\nto fix the short comings of wifi. The most importan once are Zigbee,\nBluethoot and 6LowPAN, every protocol has specific uses and more than one\nmight be used in the same network but since each uses a different\nfrequency each need his own hub to do protocol translation. In genera though\nthey all use the licence free spectrum and use lower than 1GHz frequencies\nfor higher propagation",
			"lineHeight": 1.25
		},
		{
			"id": "4VwVF9xk",
			"type": "text",
			"x": -1766.7461698049215,
			"y": 105.04953790211289,
			"width": 1155.4390869140625,
			"height": 250,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2011714480,
			"version": 1281,
			"versionNonce": 530874192,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1709026561335,
			"link": null,
			"locked": false,
			"text": "One thing that is common on IOT networks i the use of a mesh type architecture (type of ad hoc architecture).\nEspecially in buildings where there are a lot of walls, mesh type architecture allows to extend the range\nand get over the Out Of Sight problems using hopping. In this network every node act as a mini router\nand therefore not only as a receiver but also as a sender when necessary. An algorithm recognize that\nsignal to get from point A to C might need help and therefore can use point B as an intermediate.\nThis process is called route evaluation and require the use of power and increased latency\nbut it is well worth the trade off compared to having to install many more hubs. One more thing to consider is\nthat with the use of idle modes every single node might go to sleep, so when the signal is re transmitted that node\nneeds to be woken up causing some extra delay. There is an alternative to this that is called flooding \nwhere every node re transmits all the signals to avoid doing route evaluation but it has also his drawbacks",
			"rawText": "One thing that is common on IOT networks i the use of a mesh type architecture (type of ad hoc architecture).\nEspecially in buildings where there are a lot of walls, mesh type architecture allows to extend the range\nand get over the Out Of Sight problems using hopping. In this network every node act as a mini router\nand therefore not only as a receiver but also as a sender when necessary. An algorithm recognize that\nsignal to get from point A to C might need help and therefore can use point B as an intermediate.\nThis process is called route evaluation and require the use of power and increased latency\nbut it is well worth the trade off compared to having to install many more hubs. One more thing to consider is\nthat with the use of idle modes every single node might go to sleep, so when the signal is re transmitted that node\nneeds to be woken up causing some extra delay. There is an alternative to this that is called flooding \nwhere every node re transmits all the signals to avoid doing route evaluation but it has also his drawbacks",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 243,
			"containerId": null,
			"originalText": "One thing that is common on IOT networks i the use of a mesh type architecture (type of ad hoc architecture).\nEspecially in buildings where there are a lot of walls, mesh type architecture allows to extend the range\nand get over the Out Of Sight problems using hopping. In this network every node act as a mini router\nand therefore not only as a receiver but also as a sender when necessary. An algorithm recognize that\nsignal to get from point A to C might need help and therefore can use point B as an intermediate.\nThis process is called route evaluation and require the use of power and increased latency\nbut it is well worth the trade off compared to having to install many more hubs. One more thing to consider is\nthat with the use of idle modes every single node might go to sleep, so when the signal is re transmitted that node\nneeds to be woken up causing some extra delay. There is an alternative to this that is called flooding \nwhere every node re transmits all the signals to avoid doing route evaluation but it has also his drawbacks",
			"lineHeight": 1.25
		},
		{
			"id": "w7Th9Kq0",
			"type": "text",
			"x": -2743.143470341389,
			"y": -476.52043892015047,
			"width": 973.4991455078125,
			"height": 225,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1514638768,
			"version": 924,
			"versionNonce": 242992048,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1709026254244,
			"link": null,
			"locked": false,
			"text": "Often we talked about power in the context of usage for battery life but we never defined\nwhat power is scientifically and the difference from work or energy. Scientifically speaking\nwork and energy are almost the same, they represent a force applied causing a movement,\nit is measured in Joules where 10j is the work from moving 1kg for 1m (on hearth). On note\nis that work is totally abstracted from time, weather it takes 1s or 1 month to to the movement\nthe work is the same. If we factor in the time and therefore look at work over time\nwe have what we call power. Power is measured in Watts and 1W is 1j/1s, to make some examples\nan LED require about 5-15W, a phone wants at most 3W and battery operated devices need to \nrequire less than 1W to be usable",
			"rawText": "Often we talked about power in the context of usage for battery life but we never defined\nwhat power is scientifically and the difference from work or energy. Scientifically speaking\nwork and energy are almost the same, they represent a force applied causing a movement,\nit is measured in Joules where 10j is the work from moving 1kg for 1m (on hearth). On note\nis that work is totally abstracted from time, weather it takes 1s or 1 month to to the movement\nthe work is the same. If we factor in the time and therefore look at work over time\nwe have what we call power. Power is measured in Watts and 1W is 1j/1s, to make some examples\nan LED require about 5-15W, a phone wants at most 3W and battery operated devices need to \nrequire less than 1W to be usable",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 218,
			"containerId": null,
			"originalText": "Often we talked about power in the context of usage for battery life but we never defined\nwhat power is scientifically and the difference from work or energy. Scientifically speaking\nwork and energy are almost the same, they represent a force applied causing a movement,\nit is measured in Joules where 10j is the work from moving 1kg for 1m (on hearth). On note\nis that work is totally abstracted from time, weather it takes 1s or 1 month to to the movement\nthe work is the same. If we factor in the time and therefore look at work over time\nwe have what we call power. Power is measured in Watts and 1W is 1j/1s, to make some examples\nan LED require about 5-15W, a phone wants at most 3W and battery operated devices need to \nrequire less than 1W to be usable",
			"lineHeight": 1.25
		}
	],
	"appState": {
		"theme": "dark",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#1e1e1e",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 0.5,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 20,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 1686.141558577831,
		"scrollY": 1524.7458015918555,
		"zoom": {
			"value": 0.4122711161720367
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"gridColor": {
			"Bold": "#C9C9C9FF",
			"Regular": "#EDEDEDFF"
		},
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		}
	},
	"files": {}
}
```
%%