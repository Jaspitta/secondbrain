---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
the amount of data to send
for single packets in the world of IOT
is fairly low, as low as a few bytes even.
Although the single message can be very small,
often there is the need to add extra data on top
like date, location, id and error correction/prevention.
Additionally, when transmitted using something
like tcp/ip over the internet it is also necessary
to add headers and tails to the message bringing
the message size to even 1kb.
This is still very small, but IOT also has the peculiarity
to have very high volumes and potentially flooding
a regular network.
This, among other problems that we will see later (connections,
power, security, networking...) is one of the first challenges presented
by IOT. This devices send small messages and close the connection
immediately which is the opposite use of regular users.
Initially this brought back the use of 2G and than
a re-adaptation of 4G/3G with the birth of also new protocols ^mLcCnr2L

As a communication medium, radio waves have the 
obvious advantage of being wireless but comes with their
set of problems that affect also but not exclusively applications
of IOT.
The first of these problems comes from interference, IOT include many
devices of itself, plus many more exists in the world in general that
create magnetic fields that produce what is called noise, this noise
contrast with the signal we want to send and produce errors. In general
this type of problems are faced using error corrections in one of its forms,
this might be sending the message multiple times or using parity checks.
Another issue of this communication medium is blocking, this can occur in the form
of killing or wakening the signal and depends on the surface the wave has
to go through, in particular metals and concrete blocks a lot more than
wood for example.
Yet another problem is reflection, some surfaces and objects like buildings can
bounce the signal around, causing the signal to be delivered twice and even
with a different length after the bounce which would produce interference with
the original signal ^GgA8Mp7U

As anticipated one of the solutions to this problems is error correction.
There are many ways to go about it but it is important to remember that error corrections 
has its limits and if there are to many errors in the signal nothing can be done to fix it.
Also error correction is not free, it often require sending much more data than usual which means
that higher data rates might be required and often it needs extra processing at the sender and receiver
which costs time and power that drain the battery.
Another approach is to sacrifice the speed or range of the signal we send, in general slower
signals allow for less errors and more penetration or range but at the cost of speeds which
thankfully are not as important in most IOT applications. Also for this reason the max range
is interpreted as the highest error rate acceptable at a the lowest bps since range in our case changes 
in function of these 2
 ^wAvtBnlE

In the context of radio communication we saw how to convert
real data to digital we need to go through a process called modulation.
This process increases the bandwidth needed for a signal and so the range
required by the channel. As we know the number of available frequencies is limited
and techniques for reuse are possible only where there are agreed standards in place
treat everyone follows. The frequencies of mobile phones follow specific regulated standards
and are very secure and reliable, to achieve this however these channels need to be regulated
and therefore they are licensed by law, getting the name of licensed spectrum.
There is however a portion of the spectrum that is for free use and that is the 
unlicensed spectrum used by WiFi, Bluetooth, zigbee and more. This spectrum
include much smaller channels and the max power allowed is much less (o.1w) but it still is
essential for the communications we saw above ^Y7Bgb5Tp

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.0.22",
	"elements": [
		{
			"type": "freedraw",
			"version": 82,
			"versionNonce": 872996605,
			"isDeleted": false,
			"id": "zw9TkFYKStbaNH1tNQ1dz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -67.80107103970698,
			"y": -51.49639972017724,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.89318302602112,
			"height": 35.63903471892371,
			"seed": 1394988886,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6040514359139593
				],
				[
					-0.6040514359139593,
					-1.2081028718279185
				],
				[
					-0.6040514359139593,
					-0.6040514359139593
				],
				[
					0,
					3.0202571795697963
				],
				[
					0,
					8.456720102795458
				],
				[
					0,
					15.70533733376297
				],
				[
					0,
					23.55800600064447
				],
				[
					0,
					28.39041748795617
				],
				[
					0.6040514359139593,
					30.20257179569805
				],
				[
					0.6040514359139593,
					28.99446892387013
				],
				[
					0,
					26.578263180214293
				],
				[
					-0.6040514359139593,
					22.34990312881655
				],
				[
					-1.2081028718279185,
					16.913440205590916
				],
				[
					-1.8121543077418778,
					12.685080154193173
				],
				[
					-1.8121543077418778,
					7.852668666881499
				],
				[
					-1.8121543077418778,
					3.0202571795697963
				],
				[
					-0.6040514359139593,
					-1.8121543077419062
				],
				[
					1.2081028718279185,
					-4.832411487311703
				],
				[
					3.6243086154838124,
					-5.436462923225662
				],
				[
					5.43646292322569,
					-5.436462923225662
				],
				[
					8.456720102795487,
					-1.8121543077419062
				],
				[
					10.268874410537364,
					3.0202571795697963
				],
				[
					10.872925846451324,
					8.456720102795458
				],
				[
					10.872925846451324,
					12.685080154193173
				],
				[
					9.664822974623405,
					15.70533733376297
				],
				[
					8.456720102795487,
					16.309388769676957
				],
				[
					6.644565795053609,
					15.70533733376297
				],
				[
					5.43646292322569,
					13.893183026021092
				],
				[
					4.832411487311731,
					12.685080154193173
				],
				[
					4.832411487311731,
					12.081028718279214
				],
				[
					4.832411487311731,
					13.289131590107132
				],
				[
					6.0405143591396495,
					15.70533733376297
				],
				[
					7.248617230967568,
					18.121543077418835
				],
				[
					8.456720102795487,
					20.537748821074672
				],
				[
					9.664822974623405,
					22.34990312881655
				],
				[
					10.872925846451324,
					23.55800600064447
				],
				[
					11.476977282365283,
					24.162057436558428
				],
				[
					12.081028718279242,
					24.162057436558428
				],
				[
					12.081028718279242,
					23.55800600064447
				],
				[
					11.476977282365283,
					23.55800600064447
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.22370998561382294,
				0.26951202750205994,
				0.2893190085887909,
				0.30834800004959106,
				0.3172236979007721,
				0.310907781124115,
				0.29410073161125183,
				0.1598789095878601,
				0.1340378373861313,
				0.1331154853105545,
				0.14294864237308502,
				0.15292055904865265,
				0.14535167813301086,
				0.15503619611263275,
				0.17316623032093048,
				0.1855725646018982,
				0.22369906306266785,
				0.24523846805095673,
				0.30128276348114014,
				0.327658474445343,
				0.35922008752822876,
				0.36426183581352234,
				0.3533198833465576,
				0.304781973361969,
				0.22191296517848969,
				0.155733123421669,
				0.1274379938840866,
				0.12656399607658386,
				0.1907181441783905,
				0.23948261141777039,
				0.2948601245880127,
				0.35961055755615234,
				0.4095799922943115,
				0.4315360188484192,
				0.41166406869888306,
				0.3325863182544708,
				0.150435209274292,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 347495251,
			"isDeleted": false,
			"id": "1UBeLji1BN8X-Vo-ktvy3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -49.07547652637419,
			"y": -33.3748566427584,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.060771538709446,
			"height": 9.060771538709417,
			"seed": 61991894,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6040514359139593,
					0
				],
				[
					-1.2081028718279185,
					0.6040514359139593
				],
				[
					-1.8121543077418778,
					1.8121543077418778
				],
				[
					-2.416205743655837,
					3.6243086154837556
				],
				[
					-1.8121543077418778,
					6.040514359139593
				],
				[
					0,
					7.852668666881499
				],
				[
					1.8121543077419346,
					8.456720102795458
				],
				[
					4.228360051397772,
					7.852668666881499
				],
				[
					6.0405143591396495,
					6.64456579505358
				],
				[
					6.644565795053609,
					4.832411487311674
				],
				[
					6.644565795053609,
					3.0202571795697963
				],
				[
					6.644565795053609,
					1.2081028718279185
				],
				[
					5.43646292322569,
					0
				],
				[
					2.416205743655894,
					-0.6040514359139593
				],
				[
					-0.6040514359139593,
					-0.6040514359139593
				],
				[
					-1.8121543077418778,
					0
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06021999940276146,
				0.06865032762289047,
				0.13814136385917664,
				0.1920280158519745,
				0.239656001329422,
				0.2555435001850128,
				0.23683352768421173,
				0.21131576597690582,
				0.1975136399269104,
				0.23705816268920898,
				0.27360787987709045,
				0.2737260162830353,
				0.2665359079837799,
				0.1746710240840912,
				0.09919171035289764,
				0.023751525208353996,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 2095970141,
			"isDeleted": false,
			"id": "nT1j5gbD6cv7P5rpPLVHQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -44.24306503906246,
			"y": -29.750548027274647,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.040514359139593,
			"height": 4.832411487311703,
			"seed": 1912792278,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6040514359139593,
					3.624308615483784
				],
				[
					1.8121543077418778,
					4.832411487311703
				],
				[
					5.436462923225633,
					4.228360051397743
				],
				[
					6.040514359139593,
					3.624308615483784
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.23028451204299927,
				0.29980599880218506,
				0.20479290187358856,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 177567987,
			"isDeleted": false,
			"id": "A6aZkIJSgBbqXV9K9tCgd",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -25.517470525729664,
			"y": -52.1004511560912,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.121543077418835,
			"height": 26.578263180214293,
			"seed": 534957142,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.2081028718279185
				],
				[
					0,
					4.228360051397715
				],
				[
					0,
					9.060771538709417
				],
				[
					0,
					14.49723446193505
				],
				[
					0.6040514359139593,
					17.517491641504876
				],
				[
					0.6040514359139593,
					19.329645949246753
				],
				[
					0.6040514359139593,
					20.537748821074672
				],
				[
					1.2081028718279185,
					20.537748821074672
				],
				[
					0.6040514359139593,
					19.933697385160713
				],
				[
					-1.2081028718279185,
					16.913440205590916
				],
				[
					-3.0202571795697963,
					15.10128589784901
				],
				[
					-5.43646292322569,
					14.49723446193505
				],
				[
					-7.248617230967568,
					15.70533733376297
				],
				[
					-7.248617230967568,
					18.121543077418835
				],
				[
					-7.248617230967568,
					20.537748821074672
				],
				[
					-6.644565795053609,
					22.34990312881655
				],
				[
					-6.0405143591396495,
					23.55800600064447
				],
				[
					-4.832411487311674,
					24.162057436558428
				],
				[
					-3.0202571795697963,
					24.162057436558428
				],
				[
					-0.6040514359139593,
					23.55800600064447
				],
				[
					1.8121543077418778,
					22.34990312881655
				],
				[
					3.6243086154837556,
					20.537748821074672
				],
				[
					4.832411487311674,
					19.933697385160713
				],
				[
					5.436462923225633,
					20.537748821074672
				],
				[
					5.436462923225633,
					21.74585169290259
				],
				[
					6.040514359139593,
					23.55800600064447
				],
				[
					6.644565795053552,
					25.370160308386374
				],
				[
					7.8526686668814705,
					26.578263180214293
				],
				[
					9.060771538709389,
					26.578263180214293
				],
				[
					10.268874410537308,
					25.370160308386374
				],
				[
					10.872925846451267,
					24.766108872472387
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1443060040473938,
				0.21309201419353485,
				0.2202799916267395,
				0.23079824447631836,
				0.24105264246463776,
				0.26177436113357544,
				0.27988678216934204,
				0.26531580090522766,
				0.21895037591457367,
				0.13928042352199554,
				0.06681197881698608,
				0.08634625375270844,
				0.16032828390598297,
				0.2320670485496521,
				0.2552313208580017,
				0.25620293617248535,
				0.2510247230529785,
				0.25433722138404846,
				0.2590961158275604,
				0.24896787106990814,
				0.20750325918197632,
				0.151872918009758,
				0.12627466022968292,
				0.13913892209529877,
				0.14162179827690125,
				0.19166900217533112,
				0.2821011245250702,
				0.28146135807037354,
				0.24500885605812073,
				0.13254046440124512,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 777061309,
			"isDeleted": false,
			"id": "DTE5UoBYEfX8Gh-mOWIwD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -14.644544679278397,
			"y": -41.2275253096399,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.416205743655837,
			"height": 1.8121543077418778,
			"seed": 63502742,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.2081028718279185,
					0.6040514359139593
				],
				[
					-2.416205743655837,
					1.2081028718279185
				],
				[
					-2.416205743655837,
					1.8121543077418778
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.23193374276161194,
				0.23176251351833344,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1577050771,
			"isDeleted": false,
			"id": "WbqwhZeYIddw5lziDbDRD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -9.208081756052707,
			"y": -35.18701095050028,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.060771538709389,
			"height": 7.24861723096754,
			"seed": 398704214,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6040514359139593,
					1.8121543077418778
				],
				[
					-0.6040514359139593,
					3.6243086154837556
				],
				[
					0,
					4.832411487311674
				],
				[
					1.2081028718279185,
					5.436462923225633
				],
				[
					3.0202571795697963,
					6.040514359139593
				],
				[
					4.832411487311674,
					5.436462923225633
				],
				[
					6.040514359139593,
					4.832411487311674
				],
				[
					6.644565795053552,
					3.0202571795697963
				],
				[
					7.248617230967511,
					0
				],
				[
					6.040514359139593,
					-1.208102871827947
				],
				[
					3.0202571795697963,
					-1.208102871827947
				],
				[
					0,
					0.6040514359139593
				],
				[
					-1.8121543077418778,
					3.0202571795697963
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14581100642681122,
				0.17011398077011108,
				0.1611100435256958,
				0.15652740001678467,
				0.2427074909210205,
				0.3312332034111023,
				0.3767080008983612,
				0.28497669100761414,
				0.22781701385974884,
				0.1270180642604828,
				0.12125000357627869,
				0.06905270367860794,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1817412637,
			"isDeleted": false,
			"id": "uCeRtJOV6GRlAsScOzAnk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -59.948402372825456,
			"y": -3.1722848470603537,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2081028718279185,
			"height": 0.6040514359139593,
			"seed": 576755606,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6040514359139593,
					0
				],
				[
					0,
					-0.6040514359139593
				],
				[
					0.6040514359139593,
					-0.6040514359139593
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0,
				0,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 87,
			"versionNonce": 1470896179,
			"isDeleted": false,
			"id": "CR15sdCBwK1L-q_qJQSkx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -52.699785141857944,
			"y": -7.400644898458069,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 22.95395456473051,
			"height": 15.10128589784901,
			"seed": 1488526422,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6040514359139593
				],
				[
					-0.6040514359139593,
					-1.2081028718279185
				],
				[
					-1.2081028718279185,
					-1.2081028718279185
				],
				[
					-3.0202571795697963,
					0
				],
				[
					-4.832411487311674,
					1.8121543077418778
				],
				[
					-6.644565795053552,
					3.6243086154837556
				],
				[
					-7.8526686668814705,
					6.040514359139593
				],
				[
					-8.45672010279543,
					8.456720102795458
				],
				[
					-8.45672010279543,
					10.872925846451295
				],
				[
					-7.8526686668814705,
					12.685080154193173
				],
				[
					-6.040514359139593,
					13.289131590107132
				],
				[
					-4.228360051397715,
					13.289131590107132
				],
				[
					-1.8121543077418778,
					13.289131590107132
				],
				[
					0.6040514359139593,
					12.685080154193173
				],
				[
					2.416205743655837,
					11.476977282365254
				],
				[
					3.0202571795697963,
					9.664822974623377
				],
				[
					3.0202571795697963,
					8.456720102795458
				],
				[
					3.0202571795697963,
					7.852668666881499
				],
				[
					1.8121543077418778,
					7.852668666881499
				],
				[
					0.6040514359139593,
					8.456720102795458
				],
				[
					0,
					9.664822974623377
				],
				[
					-0.6040514359139593,
					11.476977282365254
				],
				[
					-0.6040514359139593,
					13.289131590107132
				],
				[
					1.2081028718279185,
					13.893183026021092
				],
				[
					3.6243086154837556,
					13.893183026021092
				],
				[
					6.644565795053609,
					12.081028718279214
				],
				[
					8.456720102795487,
					10.268874410537336
				],
				[
					9.060771538709446,
					8.456720102795458
				],
				[
					9.060771538709446,
					7.24861723096754
				],
				[
					7.852668666881527,
					7.24861723096754
				],
				[
					7.248617230967568,
					7.852668666881499
				],
				[
					6.644565795053609,
					9.664822974623377
				],
				[
					7.248617230967568,
					11.476977282365254
				],
				[
					9.060771538709446,
					12.685080154193173
				],
				[
					10.872925846451324,
					13.289131590107132
				],
				[
					13.28913159010716,
					13.289131590107132
				],
				[
					14.49723446193508,
					12.081028718279214
				],
				[
					14.49723446193508,
					10.872925846451295
				],
				[
					14.49723446193508,
					9.664822974623377
				],
				[
					13.89318302602112,
					8.456720102795458
				],
				[
					12.685080154193201,
					7.24861723096754
				],
				[
					10.268874410537364,
					6.040514359139593
				],
				[
					7.852668666881527,
					6.040514359139593
				],
				[
					6.0405143591396495,
					8.456720102795458
				],
				[
					6.0405143591396495,
					9.060771538709417
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1286499947309494,
				0.1760140061378479,
				0.19672000408172607,
				0.21131201088428497,
				0.22507821023464203,
				0.23757803440093994,
				0.24430721998214722,
				0.2473663091659546,
				0.24923907220363617,
				0.23151744902133942,
				0.22749072313308716,
				0.21893185377120972,
				0.20042666792869568,
				0.1796339750289917,
				0.16206133365631104,
				0.15353338420391083,
				0.1522337645292282,
				0.1569041758775711,
				0.15570013225078583,
				0.14648431539535522,
				0.15468481183052063,
				0.19285492599010468,
				0.19182181358337402,
				0.1968810111284256,
				0.1974012702703476,
				0.2060970813035965,
				0.21085479855537415,
				0.21171130239963531,
				0.2205766886472702,
				0.2232869267463684,
				0.2221975475549698,
				0.2223486602306366,
				0.2384866327047348,
				0.24932077527046204,
				0.2603786289691925,
				0.24136605858802795,
				0.22610077261924744,
				0.2360840141773224,
				0.24070248007774353,
				0.257666677236557,
				0.18239101767539978,
				0.10553304851055145,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 66,
			"versionNonce": 1525086333,
			"isDeleted": false,
			"id": "IkXwyra68fA2QNRIB0-CL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -35.18229350035307,
			"y": -3.776336282974313,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.268874410537364,
			"height": 10.268874410537336,
			"seed": 78621462,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6040514359139593
				],
				[
					0,
					3.0202571795697963
				],
				[
					0,
					5.436462923225662
				],
				[
					0.6040514359139593,
					7.852668666881499
				],
				[
					1.2081028718279185,
					8.456720102795458
				],
				[
					1.8121543077418778,
					8.456720102795458
				],
				[
					2.416205743655837,
					7.24861723096754
				],
				[
					3.0202571795697963,
					4.228360051397743
				],
				[
					3.6243086154837556,
					2.416205743655837
				],
				[
					4.228360051397715,
					1.2081028718279185
				],
				[
					4.832411487311731,
					1.2081028718279185
				],
				[
					5.43646292322569,
					3.624308615483784
				],
				[
					6.0405143591396495,
					5.436462923225662
				],
				[
					6.644565795053609,
					6.64456579505358
				],
				[
					7.248617230967568,
					7.24861723096754
				],
				[
					7.852668666881527,
					6.040514359139621
				],
				[
					9.060771538709446,
					3.0202571795697963
				],
				[
					9.664822974623405,
					0.6040514359139593
				],
				[
					10.268874410537364,
					1.2081028718279185
				],
				[
					10.268874410537364,
					3.624308615483784
				],
				[
					9.664822974623405,
					7.24861723096754
				],
				[
					9.664822974623405,
					9.664822974623377
				],
				[
					9.060771538709446,
					10.268874410537336
				],
				[
					9.060771538709446,
					9.664822974623377
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13168399035930634,
				0.17263199388980865,
				0.18613998591899872,
				0.20681799948215485,
				0.16476553678512573,
				0.12896008789539337,
				0.10953683406114578,
				0.10299551486968994,
				0.10015790164470673,
				0.11996395885944366,
				0.15154559910297394,
				0.17713843286037445,
				0.1816290318965912,
				0.18599368631839752,
				0.17479217052459717,
				0.12904392182826996,
				0.09712466597557068,
				0.12348693609237671,
				0.16459105908870697,
				0.2490343600511551,
				0.29700201749801636,
				0.2969039976596832,
				0.18177640438079834,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1702926803,
			"isDeleted": false,
			"id": "kGR-MIy2bxAZRYHxcLtgb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -19.47695616659007,
			"y": -3.1722848470603537,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.8526686668814705,
			"height": 10.268874410537336,
			"seed": 1194326934,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6040514359139593,
					1.2081028718279185
				],
				[
					-1.8121543077418778,
					3.624308615483784
				],
				[
					-1.8121543077418778,
					6.040514359139621
				],
				[
					-0.6040514359139593,
					8.456720102795458
				],
				[
					1.2081028718279185,
					10.268874410537336
				],
				[
					3.0202571795697963,
					10.268874410537336
				],
				[
					4.832411487311674,
					9.060771538709417
				],
				[
					5.436462923225633,
					6.64456579505358
				],
				[
					6.040514359139593,
					4.228360051397743
				],
				[
					6.040514359139593,
					2.416205743655837
				],
				[
					5.436462923225633,
					1.8121543077418778
				],
				[
					5.436462923225633,
					1.8121543077418778
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0895639955997467,
				0.12290399521589279,
				0.14522500336170197,
				0.1706753522157669,
				0.1856442242860794,
				0.20114953815937042,
				0.21147772669792175,
				0.20061077177524567,
				0.1588365137577057,
				0.07344015687704086,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 600629469,
			"isDeleted": false,
			"id": "ed199qPGH0phikLcurkbq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -11.020236063794584,
			"y": -2.5682334111463945,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.664822974623348,
			"height": 9.664822974623377,
			"seed": 986373398,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6040514359139593
				],
				[
					0,
					2.4162057436558655
				],
				[
					0,
					3.624308615483784
				],
				[
					0.6040514359139593,
					4.832411487311703
				],
				[
					1.2081028718279185,
					5.436462923225662
				],
				[
					2.416205743655837,
					5.436462923225662
				],
				[
					3.6243086154837556,
					4.228360051397743
				],
				[
					4.832411487311674,
					1.2081028718279185
				],
				[
					5.436462923225633,
					0
				],
				[
					6.040514359139593,
					-1.2081028718279185
				],
				[
					7.248617230967511,
					-1.2081028718279185
				],
				[
					7.8526686668814705,
					0.6040514359139593
				],
				[
					8.45672010279543,
					3.0202571795698248
				],
				[
					8.45672010279543,
					6.040514359139621
				],
				[
					8.45672010279543,
					7.852668666881499
				],
				[
					8.45672010279543,
					8.456720102795458
				],
				[
					9.060771538709389,
					6.64456579505358
				],
				[
					9.664822974623348,
					5.436462923225662
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10831399261951447,
				0.16529199481010437,
				0.2041260004043579,
				0.2161339968442917,
				0.21385300159454346,
				0.17743036150932312,
				0.12543755769729614,
				0.09947970509529114,
				0.08736968785524368,
				0.11312765628099442,
				0.16492310166358948,
				0.2195315808057785,
				0.25388213992118835,
				0.2856140732765198,
				0.2899041771888733,
				0.2486719936132431,
				0.06900842487812042,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1955850099,
			"isDeleted": false,
			"id": "Bc1gzHUnbuAs6F7q0IhZ5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2.2688955263125195,
			"y": -2.5682334111463945,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2081028718279185,
			"height": 10.268874410537336,
			"seed": 1980675606,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.8121543077418778
				],
				[
					-0.6040514359139593,
					4.228360051397743
				],
				[
					-0.6040514359139593,
					6.040514359139621
				],
				[
					-0.6040514359139593,
					8.456720102795458
				],
				[
					0,
					9.664822974623377
				],
				[
					0.6040514359139593,
					10.268874410537336
				],
				[
					0.6040514359139593,
					10.268874410537336
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1926480084657669,
				0.25678399205207825,
				0.22937899827957153,
				0.16537658870220184,
				0.06835949420928955,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1016511805,
			"isDeleted": false,
			"id": "5_80znaK8kTHaOkfLfmbH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 4.081049834054397,
			"y": -9.212799206199946,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2081028718279185,
			"height": 0.6040514359139877,
			"seed": 1218596182,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6040514359139593,
					0
				],
				[
					-1.2081028718279185,
					-0.6040514359139877
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1464489996433258,
				0.059333983808755875,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 187466003,
			"isDeleted": false,
			"id": "wWP5LaQaD3YhYwsFgV20Y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 12.537769936849884,
			"y": -3.1722848470603537,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.121543077418835,
			"height": 13.89318302602112,
			"seed": 922342614,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.2081028718279185,
					0
				],
				[
					-2.416205743655837,
					0
				],
				[
					-4.228360051397715,
					0.6040514359139593
				],
				[
					-6.644565795053552,
					3.0202571795698248
				],
				[
					-7.248617230967511,
					5.436462923225662
				],
				[
					-7.248617230967511,
					9.060771538709417
				],
				[
					-4.832411487311674,
					12.081028718279242
				],
				[
					-1.8121543077418778,
					13.89318302602112
				],
				[
					1.2081028718279185,
					13.89318302602112
				],
				[
					3.0202571795697963,
					12.685080154193201
				],
				[
					3.6243086154837556,
					10.872925846451295
				],
				[
					3.6243086154837556,
					9.060771538709417
				],
				[
					3.6243086154837556,
					8.456720102795458
				],
				[
					3.0202571795697963,
					8.456720102795458
				],
				[
					2.416205743655837,
					9.060771538709417
				],
				[
					2.416205743655837,
					10.872925846451295
				],
				[
					2.416205743655837,
					11.476977282365283
				],
				[
					4.228360051397715,
					12.685080154193201
				],
				[
					6.644565795053552,
					12.685080154193201
				],
				[
					9.060771538709389,
					12.081028718279242
				],
				[
					10.268874410537364,
					10.268874410537336
				],
				[
					10.872925846451324,
					8.456720102795458
				],
				[
					10.872925846451324,
					7.24861723096754
				],
				[
					10.268874410537364,
					6.040514359139621
				],
				[
					9.060771538709389,
					6.040514359139621
				],
				[
					6.644565795053552,
					6.040514359139621
				],
				[
					4.832411487311674,
					6.64456579505358
				],
				[
					3.6243086154837556,
					7.852668666881499
				],
				[
					3.6243086154837556,
					7.852668666881499
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14685024321079254,
				0.20546798408031464,
				0.24244800209999084,
				0.267987996339798,
				0.2960119843482971,
				0.28153154253959656,
				0.25397971272468567,
				0.2151518017053604,
				0.1714295893907547,
				0.1403137743473053,
				0.12570618093013763,
				0.12863709032535553,
				0.14906252920627594,
				0.17326690256595612,
				0.19498862326145172,
				0.20350787043571472,
				0.19863076508045197,
				0.19865737855434418,
				0.21088558435440063,
				0.23024392127990723,
				0.25065284967422485,
				0.26624393463134766,
				0.2777688801288605,
				0.28840476274490356,
				0.2595931589603424,
				0.1802709400653839,
				0.053039856255054474,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1822821789,
			"isDeleted": false,
			"id": "VVZwHu7hL4-rJExcBVXnb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 21.598541475559273,
			"y": 4.076332383907186,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.852668666881527,
			"height": 4.228360051397743,
			"seed": 1503092630,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6040514359140161,
					0.6040514359139593
				],
				[
					1.8121543077419346,
					3.6243086154837556
				],
				[
					4.228360051397772,
					4.228360051397743
				],
				[
					7.248617230967568,
					3.6243086154837556
				],
				[
					7.852668666881527,
					3.0202571795697963
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.19475717842578888,
				0.22915200889110565,
				0.13933080434799194,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 583067315,
			"isDeleted": false,
			"id": "Y8001dX7B-oplccm4sbKk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 35.49172450158039,
			"y": -18.273570744909392,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2081028718279185,
			"height": 25.974211744300334,
			"seed": 1591796822,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6040514359139593,
					0.6040514359139877
				],
				[
					-0.6040514359139593,
					1.208102871827947
				],
				[
					-0.6040514359139593,
					4.228360051397743
				],
				[
					-0.6040514359139593,
					10.872925846451324
				],
				[
					-0.6040514359139593,
					16.913440205590916
				],
				[
					-0.6040514359139593,
					21.14180025698866
				],
				[
					-0.6040514359139593,
					24.162057436558456
				],
				[
					-0.6040514359139593,
					25.370160308386374
				],
				[
					-0.6040514359139593,
					25.974211744300334
				],
				[
					-1.2081028718279185,
					25.974211744300334
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14180798828601837,
				0.18682599067687988,
				0.21160970628261566,
				0.20148272812366486,
				0.1930166333913803,
				0.16909493505954742,
				0.11570773273706436,
				0.06681112945079803,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 321671677,
			"isDeleted": false,
			"id": "mVU3aqulk22icIgwDhYcw",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 28.84715870652684,
			"y": -0.15202766749052898,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.664822974623348,
			"height": 0.6040514359139593,
			"seed": 802804566,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6040514359139593
				],
				[
					1.2081028718279185,
					0.6040514359139593
				],
				[
					3.6243086154837556,
					0.6040514359139593
				],
				[
					6.644565795053552,
					0.6040514359139593
				],
				[
					9.060771538709389,
					0.6040514359139593
				],
				[
					9.664822974623348,
					0.6040514359139593
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16501900553703308,
				0.23728398978710175,
				0.26328399777412415,
				0.23738400638103485,
				0.12906768918037415,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1106745427,
			"isDeleted": false,
			"id": "OkWqRy_yCwpuRE7e08jLh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 43.34439316846192,
			"y": 1.0560752043373896,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.8121543077418778,
			"height": 7.24861723096754,
			"seed": 1525718358,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					3.6243086154837556
				],
				[
					0,
					4.832411487311674
				],
				[
					0.6040514359139593,
					6.644565795053552
				],
				[
					1.2081028718279185,
					7.24861723096754
				],
				[
					1.8121543077418778,
					7.24861723096754
				],
				[
					1.8121543077418778,
					7.24861723096754
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13362200558185577,
				0.1334960013628006,
				0.18941278755664825,
				0.13254684209823608,
				0.07435262948274612,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 757795421,
			"isDeleted": false,
			"id": "1wDB3OHT0GRtPxjfuqtG3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 46.36465034803172,
			"y": -6.19254202663015,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.8121543077418778,
			"height": 1.8121543077418778,
			"seed": 1260218198,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6040514359139593,
					0.6040514359139593
				],
				[
					-1.2081028718279185,
					0.6040514359139593
				],
				[
					-1.8121543077418778,
					1.2081028718279185
				],
				[
					-1.2081028718279185,
					1.8121543077418778
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.20660997927188873,
				0.21044763922691345,
				0.160127654671669,
				0.10422210395336151,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1453790707,
			"isDeleted": false,
			"id": "yXdyMBg0baN2mk4ErJ8HH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 51.80111327125735,
			"y": 2.264178076165308,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.644565795053609,
			"height": 12.685080154193201,
			"seed": 174076246,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6040514359139593,
					1.2081028718279185
				],
				[
					-1.2081028718279185,
					4.228360051397715
				],
				[
					-1.2081028718279185,
					6.040514359139621
				],
				[
					0,
					7.24861723096754
				],
				[
					1.2081028718279185,
					7.24861723096754
				],
				[
					3.0202571795697963,
					6.64456579505358
				],
				[
					4.228360051397715,
					4.228360051397715
				],
				[
					5.43646292322569,
					0.6040514359139593
				],
				[
					5.43646292322569,
					-3.0202571795698248
				],
				[
					4.832411487311674,
					-4.832411487311703
				],
				[
					3.0202571795697963,
					-5.436462923225662
				],
				[
					1.2081028718279185,
					-3.624308615483784
				],
				[
					-0.6040514359139593,
					-1.2081028718279185
				],
				[
					-0.6040514359139593,
					0.6040514359139593
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13805700838565826,
				0.18193601071834564,
				0.2333119809627533,
				0.25467798113822937,
				0.2701359987258911,
				0.2641851305961609,
				0.24513046443462372,
				0.22598648071289062,
				0.22834017872810364,
				0.22717538475990295,
				0.19911237061023712,
				0.15045040845870972,
				0.04309762641787529,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 460568253,
			"isDeleted": false,
			"id": "OiTpkNacXSjmS8mUCvCS8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 58.44567906631096,
			"y": -1.9641819752324352,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.268874410537308,
			"height": 10.872925846451324,
			"seed": 1743448022,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.2081028718279185
				],
				[
					0,
					3.0202571795698248
				],
				[
					0,
					5.436462923225662
				],
				[
					0.6040514359139593,
					7.852668666881499
				],
				[
					1.2081028718279185,
					8.456720102795458
				],
				[
					3.0202571795697963,
					7.852668666881499
				],
				[
					4.832411487311674,
					4.832411487311703
				],
				[
					6.040514359139593,
					2.4162057436558655
				],
				[
					7.248617230967511,
					1.2081028718279185
				],
				[
					7.8526686668814705,
					2.4162057436558655
				],
				[
					7.8526686668814705,
					5.436462923225662
				],
				[
					8.45672010279543,
					8.456720102795458
				],
				[
					9.060771538709389,
					10.872925846451324
				],
				[
					10.268874410537308,
					10.872925846451324
				],
				[
					10.268874410537308,
					10.872925846451324
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1761399805545807,
				0.2210339903831482,
				0.2608630061149597,
				0.2797980010509491,
				0.18493573367595673,
				0.08768032491207123,
				0.034026000648736954,
				0.033465974032878876,
				0.12451907247304916,
				0.27585065364837646,
				0.35828813910484314,
				0.3350279927253723,
				0.2686845660209656,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 1339416467,
			"isDeleted": false,
			"id": "n15yNiZYho8r59ZJD3cfw",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 142.20914590176753,
			"y": -105.73919172559307,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.304167107443675,
			"height": 19.782292438026445,
			"seed": 582023079,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.40372025383727816
				],
				[
					-0.40372025383726395,
					-0.40372025383727816
				],
				[
					-0.40372025383726395,
					2.4223215230236406
				],
				[
					0,
					11.707887361280953
				],
				[
					0,
					16.956250661165527
				],
				[
					0.4037202538373208,
					16.956250661165527
				],
				[
					0.4037202538373208,
					12.111607615118231
				],
				[
					-0.40372025383726395,
					5.2483632998845735
				],
				[
					-1.6148810153490558,
					0.40372025383727816
				],
				[
					-2.4223215230236406,
					-2.4223215230236406
				],
				[
					-2.4223215230236406,
					-2.8260417768609187
				],
				[
					0.4037202538373208,
					-2.8260417768609187
				],
				[
					5.248363299884602,
					-1.2111607615118203
				],
				[
					8.881845584420034,
					2.4223215230236406
				],
				[
					8.881845584420034,
					4.844643046047295
				],
				[
					6.863244315233658,
					5.2483632998845735
				],
				[
					4.440922792210017,
					4.037202538372739
				],
				[
					4.037202538372753,
					3.633482284535475
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07048797607421875,
				0.05913400277495384,
				0.15942537784576416,
				0.19761651754379272,
				0.18523654341697693,
				0.1440420299768448,
				0.07791262865066528,
				0.04719458147883415,
				0.060350678861141205,
				0.07882525771856308,
				0.12708929181098938,
				0.16461233794689178,
				0.19721844792366028,
				0.2319907248020172,
				0.2687578797340393,
				0.2822180688381195,
				0.09788284450769424,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 682088221,
			"isDeleted": false,
			"id": "ns7Glqzeven77EjREKkT9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 151.49471174002488,
			"y": -96.45362588733576,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.248363299884602,
			"height": 6.459524061396394,
			"seed": 79674919,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4037202538373208,
					-0.40372025383727816
				],
				[
					0,
					0.40372025383727816
				],
				[
					0.8074405076745279,
					3.633482284535461
				],
				[
					0.8074405076745279,
					6.055803807559116
				],
				[
					0.8074405076745279,
					4.844643046047281
				],
				[
					2.4223215230236406,
					1.2111607615118203
				],
				[
					4.844643046047281,
					0
				],
				[
					4.844643046047281,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.055467985570430756,
				0.13513720035552979,
				0.16101324558258057,
				0.16454477608203888,
				0.11911690980195999,
				0.11371740698814392,
				0.015207336284220219,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 2008708403,
			"isDeleted": false,
			"id": "PXb0Niz3EVyAEwf3tW2-F",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 159.16539656293307,
			"y": -95.64618537966122,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.844643046047338,
			"height": 6.863244315233658,
			"seed": 1893828967,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.40372025383726395,
					0.40372025383727816
				],
				[
					-1.2111607615118487,
					1.6148810153490984
				],
				[
					-1.2111607615118487,
					2.4223215230236548
				],
				[
					0.40372025383726395,
					4.440922792210017
				],
				[
					2.8260417768609045,
					4.844643046047295
				],
				[
					3.6334822845354893,
					2.4223215230236548
				],
				[
					2.8260417768609045,
					-1.2111607615118203
				],
				[
					0.8074405076745279,
					-2.0186012691863624
				],
				[
					0.8074405076745279,
					1.6148810153490984
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08311233669519424,
				0.12137539684772491,
				0.14734134078025818,
				0.16130343079566956,
				0.1636420041322708,
				0.15593771636486053,
				0.13527347147464752,
				0.017175354063510895,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 1329130365,
			"isDeleted": false,
			"id": "5TRicgUvvHL9vQ25h6zak",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 167.64352189351584,
			"y": -106.54663223326762,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.459524061396394,
			"height": 14.93764939197915,
			"seed": 630002183,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.40372025383727816
				],
				[
					-0.40372025383726395,
					-0.8074405076745563
				],
				[
					-0.8074405076745848,
					0.40372025383726395
				],
				[
					-0.8074405076745848,
					6.45952406139638
				],
				[
					-0.40372025383726395,
					10.496726599769133
				],
				[
					0.8074405076745279,
					9.285565838257298
				],
				[
					3.2297620306981685,
					8.881845584420034
				],
				[
					4.440922792210017,
					10.496726599769133
				],
				[
					4.037202538372753,
					12.919048122792773
				],
				[
					2.0186012691863766,
					14.130208884304594
				],
				[
					-1.2111607615118487,
					14.130208884304594
				],
				[
					-2.0186012691863766,
					12.919048122792773
				],
				[
					-1.6148810153491127,
					12.515327868955495
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07197698950767517,
				0.059528473764657974,
				0.14067736268043518,
				0.16637729108333588,
				0.15137088298797607,
				0.09740021079778671,
				0.12440377473831177,
				0.15143011510372162,
				0.204896941781044,
				0.2211119681596756,
				0.1858353614807129,
				0.01021136436611414,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 230381267,
			"isDeleted": false,
			"id": "3vcITGRaOkRZVhJO_9B1S",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 178.54396874712225,
			"y": -109.77639426396581,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8074405076745848,
			"height": 18.97485193035189,
			"seed": 896686311,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.40372025383726395,
					0.40372025383727816
				],
				[
					-0.8074405076745848,
					1.6148810153490984
				],
				[
					-0.8074405076745848,
					9.689286092094576
				],
				[
					-0.8074405076745848,
					16.956250661165512
				],
				[
					-0.8074405076745848,
					18.97485193035189
				],
				[
					-0.40372025383726395,
					18.97485193035189
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06334549188613892,
				0.16582223773002625,
				0.24246349930763245,
				0.04389047250151634,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1063810013,
			"isDeleted": false,
			"id": "2HFcS9aDpCX2wvXHWYOAh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 183.38861179316953,
			"y": -93.62758411047484,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.074405076745506,
			"height": 7.670684822908214,
			"seed": 1668137447,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8074405076745279,
					0
				],
				[
					1.2111607615117919,
					0
				],
				[
					2.4223215230236406,
					-0.40372025383727816
				],
				[
					2.8260417768609045,
					-2.8260417768609187
				],
				[
					0.8074405076745279,
					-3.633482284535475
				],
				[
					-1.2111607615118487,
					-1.2111607615118203
				],
				[
					-0.8074405076745279,
					2.4223215230236406
				],
				[
					2.4223215230236406,
					4.037202538372739
				],
				[
					6.459524061396394,
					2.4223215230236406
				],
				[
					6.863244315233658,
					2.0186012691863624
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08198834210634232,
				0.1640854775905609,
				0.13175366818904877,
				0.10583813488483429,
				0.1440180391073227,
				0.2628563940525055,
				0.2921585738658905,
				0.09870263934135437,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 544146547,
			"isDeleted": false,
			"id": "JjLLGh9_uH0VcMjJS80le",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 192.67417763142683,
			"y": -97.26106639501032,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.074405076745506,
			"height": 7.266964569070936,
			"seed": 769392487,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.40372025383726395
				],
				[
					0.40372025383726395,
					0
				],
				[
					0.8074405076745279,
					2.8260417768609187
				],
				[
					1.6148810153491127,
					5.2483632998845735
				],
				[
					2.4223215230236406,
					4.844643046047295
				],
				[
					3.2297620306981685,
					2.0186012691863766
				],
				[
					4.440922792210017,
					0
				],
				[
					4.844643046047281,
					1.6148810153490984
				],
				[
					4.844643046047281,
					4.440922792210017
				],
				[
					5.248363299884545,
					4.844643046047295
				],
				[
					6.459524061396394,
					2.0186012691863766
				],
				[
					7.670684822908186,
					0.8074405076745563
				],
				[
					8.074405076745506,
					4.037202538372753
				],
				[
					7.670684822908186,
					6.863244315233672
				],
				[
					7.670684822908186,
					6.459524061396394
				],
				[
					8.074405076745506,
					6.055803807559116
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0914440006017685,
				0.12898801267147064,
				0.1724272519350052,
				0.16305285692214966,
				0.12015121430158615,
				0.09603454917669296,
				0.09125213325023651,
				0.1205078735947609,
				0.13978704810142517,
				0.13228793442249298,
				0.08036389201879501,
				0.12151681631803513,
				0.20086704194545746,
				0.18141372501850128,
				0.039962951093912125,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 625471549,
			"isDeleted": false,
			"id": "-IZ6j8-XcjJ2pzUGLD9Ef",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 209.63042829259237,
			"y": -97.66478664884758,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.863244315233658,
			"height": 7.266964569070936,
			"seed": 151446439,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4037202538373208,
					0
				],
				[
					-1.6148810153491127,
					0
				],
				[
					-3.2297620306982253,
					1.2111607615118203
				],
				[
					-3.6334822845354893,
					2.4223215230236406
				],
				[
					-0.8074405076745848,
					3.633482284535461
				],
				[
					1.6148810153490558,
					4.844643046047281
				],
				[
					0.40372025383726395,
					5.6520835537218375
				],
				[
					-3.2297620306982253,
					7.266964569070936
				],
				[
					-5.248363299884602,
					7.266964569070936
				],
				[
					-5.248363299884602,
					6.863244315233658
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09545218199491501,
				0.16482232511043549,
				0.18255376815795898,
				0.1743013560771942,
				0.1594781130552292,
				0.2140231877565384,
				0.21412090957164764,
				0.022395508363842964,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 664534547,
			"isDeleted": false,
			"id": "MQbmj9Vp7TfgbizWtv4lg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 71.55810148024455,
			"y": -22.16909918127729,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 40.37202538372742,
			"height": 42.79434690675107,
			"seed": 71860519,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.40372025383726395
				],
				[
					0,
					0.8074405076745279
				],
				[
					-0.40372025383726395,
					1.2111607615118203
				],
				[
					0.4037202538372924,
					0.8074405076745279
				],
				[
					2.0186012691863766,
					-2.0186012691863766
				],
				[
					7.26696456907095,
					-10.900446853606411
				],
				[
					17.76369116884007,
					-23.8194949763992
				],
				[
					29.8752987839583,
					-35.12366208384287
				],
				[
					38.35342411454107,
					-41.17946589140199
				],
				[
					39.968305129890155,
					-41.58318614523925
				],
				[
					38.757144368378334,
					-39.56458487605289
				],
				[
					38.757144368378334,
					-39.16086462221561
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.04435800015926361,
				0.11580301076173782,
				0.17912274599075317,
				0.19941937923431396,
				0.21848390996456146,
				0.2795168161392212,
				0.30565908551216125,
				0.2797664403915405,
				0.2342001050710678,
				0.06369909644126892,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 783868061,
			"isDeleted": false,
			"id": "mM5VjZkcJczE5E-YE4gQc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 115.56360914850745,
			"y": -69.80808913407566,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.881845584420034,
			"height": 9.68928609209459,
			"seed": 1225892071,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.4223215230236406,
					0
				],
				[
					7.266964569070922,
					-1.2111607615118345
				],
				[
					8.881845584420034,
					-0.8074405076745563
				],
				[
					6.055803807559101,
					2.4223215230236406
				],
				[
					2.8260417768609045,
					6.45952406139638
				],
				[
					2.4223215230236406,
					8.478125330582756
				],
				[
					4.844643046047281,
					7.6706848229082
				],
				[
					5.2483632998845735,
					7.266964569070936
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16536150872707367,
				0.1752808839082718,
				0.14632375538349152,
				0.2070821225643158,
				0.2914843261241913,
				0.3033868968486786,
				0.10341955721378326,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 1580778419,
			"isDeleted": false,
			"id": "2SZ3vLFSE2astTwD1XYxs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 338.0859819867863,
			"y": -269.21636208825623,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.3271704268319695,
			"height": 4.253215548815973,
			"seed": 87751719,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.6358521341599896
				],
				[
					0,
					4.253215548815973
				],
				[
					0.3271704268319695,
					4.253215548815973
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16010522842407227,
				0.0441560372710228,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1366082813,
			"isDeleted": false,
			"id": "86PcEscoh9oRp-30PpA2V",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 338.7403228404503,
			"y": -274.4510889175682,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.32717042683202635,
			"height": 0.32717042683202635,
			"seed": 1450542023,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.32717042683202635
				],
				[
					-0.32717042683202635,
					-0.32717042683202635
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07854598760604858,
				0.13424044847488403,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1550570835,
			"isDeleted": false,
			"id": "HkhDHSbRHoOICquIFlITq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 341.68485668193824,
			"y": -269.54353251508826,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.9075564024799405,
			"height": 6.216238109807961,
			"seed": 2123874951,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.3271704268319695,
					0
				],
				[
					0.32717042683202635,
					1.9630225609919876
				],
				[
					0.9815112804960222,
					2.9445338414879814
				],
				[
					1.635852134160018,
					1.3086817073279917
				],
				[
					2.94453384148801,
					-1.9630225609919876
				],
				[
					4.2532155488160015,
					-1.6358521341599612
				],
				[
					4.580385975647971,
					1.9630225609919876
				],
				[
					4.580385975647971,
					4.253215548815973
				],
				[
					4.580385975647971,
					3.926045121983975
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07397570461034775,
				0.12428918480873108,
				0.07347732782363892,
				0.026557067409157753,
				0.04004302993416786,
				0.12260431051254272,
				0.16844713687896729,
				0.05337673798203468,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1357192541,
			"isDeleted": false,
			"id": "ZAACDmzpan09ILIck1BLN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 351.4999694868982,
			"y": -280.99449745420816,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6543408536639959,
			"height": 15.049839634271876,
			"seed": 1233732839,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.32717042683202635,
					0.32717042683199793
				],
				[
					-0.32717042683202635,
					0.9815112804959938
				],
				[
					-0.32717042683202635,
					3.2717042683199793
				],
				[
					0.3271704268319695,
					9.815112804959938
				],
				[
					0.3271704268319695,
					14.39549878060788
				],
				[
					0.3271704268319695,
					15.049839634271876
				],
				[
					0,
					15.049839634271876
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1318339854478836,
				0.17919400334358215,
				0.22680401802062988,
				0.20887281000614166,
				0.07088610529899597,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 1904980723,
			"isDeleted": false,
			"id": "BE_0iOXkbLPsa2ikC26bD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 348.8826060722422,
			"y": -272.81523678340824,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.561897256143936,
			"height": 1.3086817073279917,
			"seed": 1836603655,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.9630225609919876,
					0.32717042683202635
				],
				[
					5.234726829311967,
					0.9815112804960222
				],
				[
					5.561897256143936,
					1.3086817073279917
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.20041190087795258,
				0.019530456513166428,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 74672573,
			"isDeleted": false,
			"id": "2E8ye-p9iB9c2fwcCnzLa",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 358.04337802353814,
			"y": -269.87070294192023,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.216238109807932,
			"height": 6.543408536639959,
			"seed": 1750914215,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.32717042683202635
				],
				[
					0.3271704268319695,
					-0.32717042683202635
				],
				[
					0.3271704268319695,
					-0.6543408536639959
				],
				[
					0.3271704268319695,
					-1.635852134160018
				],
				[
					-0.9815112804960222,
					-1.635852134160018
				],
				[
					-2.6173634146559834,
					1.6358521341599612
				],
				[
					-1.635852134160018,
					4.9075564024799405
				],
				[
					2.944533841487953,
					2.944533841487953
				],
				[
					3.598874695151949,
					2.617363414655955
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08709716796875,
				0.14499405026435852,
				0.16458676755428314,
				0.12165039032697678,
				0.11372543126344681,
				0.18576465547084808,
				0.03490838780999184,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1042209939,
			"isDeleted": false,
			"id": "oHEIfpiIKVtmLuINantvU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 363.6052752796821,
			"y": -271.8337255029122,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.5988746951520056,
			"height": 6.8705789634719565,
			"seed": 1017244423,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.32717042683202635,
					0
				],
				[
					-0.32717042683202635,
					0.3271704268319695
				],
				[
					-0.32717042683202635,
					0.9815112804959654
				],
				[
					0.3271704268319695,
					3.9260451219839467
				],
				[
					0.6543408536639959,
					5.889067682975934
				],
				[
					0.9815112804959654,
					5.2347268293119384
				],
				[
					1.3086817073279917,
					1.9630225609919876
				],
				[
					2.944533841487953,
					-0.9815112804960222
				],
				[
					3.2717042683199793,
					-0.9815112804960222
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.04843798652291298,
				0.07496219128370285,
				0.1375998556613922,
				0.143202543258667,
				0.09600457549095154,
				0.10326971113681793,
				0.06981518864631653,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 84,
			"versionNonce": 1564027421,
			"isDeleted": false,
			"id": "5gio11HuFYhJJaOXB3mI_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 369.82151338949,
			"y": -268.88919166142426,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.543408536639959,
			"height": 26.500804573391775,
			"seed": 1850588519,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.32717042683202635,
					0
				],
				[
					0.9815112804960222,
					-0.32717042683199793
				],
				[
					4.580385975647971,
					-3.2717042683199793
				],
				[
					6.543408536639959,
					-7.197749390303954
				],
				[
					5.889067682975963,
					-10.796624085455903
				],
				[
					3.926045121983975,
					-12.432476219615893
				],
				[
					2.290192987824014,
					-11.123794512287901
				],
				[
					2.290192987824014,
					-8.506431097631918
				],
				[
					2.94453384148801,
					-2.944533841487953
				],
				[
					3.926045121983975,
					3.926045121983975
				],
				[
					3.926045121983975,
					9.815112804959938
				],
				[
					2.94453384148801,
					13.413987500111887
				],
				[
					1.635852134160018,
					14.068328353775883
				],
				[
					0,
					11.778135365951925
				],
				[
					0.9815112804960222,
					5.234726829311967
				],
				[
					1.3086817073279917,
					4.907556402479969
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11407998949289322,
				0.1513899862766266,
				0.24578997492790222,
				0.22783459722995758,
				0.1345873475074768,
				0.082189179956913,
				0.09308892488479614,
				0.1067245751619339,
				0.10808462649583817,
				0.09829980134963989,
				0.11713097989559174,
				0.14300274848937988,
				0.1910373866558075,
				0.19202081859111786,
				0.015194916166365147,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 232510003,
			"isDeleted": false,
			"id": "X1LuzJujkXx95t6ePCLJe",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 377.34643320662593,
			"y": -270.19787336875225,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.197749390303954,
			"height": 7.524919817135924,
			"seed": 795156903,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.32717042683202635,
					0
				],
				[
					1.635852134160018,
					-0.3271704268319695
				],
				[
					3.926045121983975,
					-2.290192987823957
				],
				[
					3.5988746951520056,
					-3.598874695151949
				],
				[
					1.635852134160018,
					-2.6173634146559834
				],
				[
					0,
					0
				],
				[
					0.32717042683202635,
					2.9445338414879814
				],
				[
					2.6173634146559834,
					3.926045121983975
				],
				[
					6.870578963471985,
					1.9630225609919876
				],
				[
					7.197749390303954,
					1.6358521341599896
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12299197167158127,
				0.17844000458717346,
				0.15270648896694183,
				0.1016850620508194,
				0.09598767012357712,
				0.14272543787956238,
				0.20162619650363922,
				0.20315200090408325,
				0.05700073391199112,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 740810365,
			"isDeleted": false,
			"id": "u7vx978W6xyHVV4dpyweD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 385.5256938774259,
			"y": -272.81523678340824,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.889067682975963,
			"height": 7.524919817135952,
			"seed": 821673767,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.32717042683202635
				],
				[
					-0.32717042683202635,
					1.9630225609919876
				],
				[
					0,
					5.234726829311967
				],
				[
					0.3271704268319695,
					6.216238109807961
				],
				[
					0.9815112804959654,
					4.580385975647971
				],
				[
					2.944533841487953,
					0.32717042683202635
				],
				[
					5.23472682931191,
					-1.3086817073279917
				],
				[
					5.561897256143936,
					-1.3086817073279917
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.052914489060640335,
				0.08908858895301819,
				0.11066592484712601,
				0.10828561335802078,
				0.10193295031785965,
				0.12751851975917816,
				0.04946737736463547,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1906906067,
			"isDeleted": false,
			"id": "dLtUWT520M1Ed2CxS95zt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 392.7234432677298,
			"y": -271.1793846492482,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.543408536639959,
			"height": 7.197749390303926,
			"seed": 448678503,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.32717042683202635,
					0.3271704268319695
				],
				[
					0.6543408536639959,
					0.3271704268319695
				],
				[
					1.9630225609919876,
					-0.6543408536639959
				],
				[
					2.6173634146559834,
					-2.6173634146559834
				],
				[
					0.9815112804960222,
					-2.6173634146559834
				],
				[
					-0.9815112804959654,
					0.6543408536639959
				],
				[
					-0.3271704268319695,
					3.9260451219839467
				],
				[
					2.290192987824014,
					4.580385975647943
				],
				[
					4.907556402479997,
					2.290192987823957
				],
				[
					5.561897256143993,
					1.9630225609919592
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07026998698711395,
				0.09399240463972092,
				0.20658321678638458,
				0.16218362748622894,
				0.09471054375171661,
				0.11696136742830276,
				0.24056395888328552,
				0.2585631310939789,
				0.06635034084320068,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 671155933,
			"isDeleted": false,
			"id": "IhbYMTjQhXn12GaMKcMKU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 399.59402223120173,
			"y": -273.1424072102402,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.234726829311967,
			"height": 6.8705789634719565,
			"seed": 1395902439,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.3271704268319695
				],
				[
					0,
					0.9815112804959654
				],
				[
					0.32717042683202635,
					3.598874695151949
				],
				[
					1.635852134160018,
					4.253215548815945
				],
				[
					3.5988746951520056,
					0.9815112804959654
				],
				[
					5.234726829311967,
					-0.9815112804960222
				],
				[
					5.234726829311967,
					1.9630225609919876
				],
				[
					4.2532155488160015,
					5.889067682975934
				],
				[
					4.580385975647971,
					5.889067682975934
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07078799605369568,
				0.09390991181135178,
				0.18347445130348206,
				0.1674312800168991,
				0.10035082697868347,
				0.10563049465417862,
				0.18995584547519684,
				0.10123419016599655,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 429728115,
			"isDeleted": false,
			"id": "_lZVzv561MliWYHqCdXJb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 410.71781674348966,
			"y": -273.46957763707223,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.216238109807932,
			"height": 8.179260670799948,
			"seed": 798975559,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.3271704268319695
				],
				[
					-0.3271704268319695,
					-0.6543408536639959
				],
				[
					-0.6543408536639959,
					-0.6543408536639959
				],
				[
					-2.290192987823957,
					1.3086817073279917
				],
				[
					-2.944533841487953,
					5.234726829311967
				],
				[
					-1.3086817073279917,
					7.524919817135952
				],
				[
					2.944533841487953,
					5.234726829311967
				],
				[
					3.2717042683199793,
					4.580385975647971
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.05844021588563919,
				0.10196112096309662,
				0.15755774080753326,
				0.26040399074554443,
				0.27699899673461914,
				0.08327124267816544,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 861283133,
			"isDeleted": false,
			"id": "hRLFJ4NIm3td3_cQm-08n",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 417.5883957069616,
			"y": -270.85221422241625,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.524919817135924,
			"height": 5.561897256143936,
			"seed": 462653831,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.32717042683202635,
					-0.3271704268319695
				],
				[
					0.6543408536639959,
					-0.6543408536639959
				],
				[
					0.6543408536639959,
					-0.9815112804959654
				],
				[
					0,
					-1.6358521341599612
				],
				[
					-1.6358521341599612,
					-0.9815112804959654
				],
				[
					-3.2717042683199793,
					0.32717042683202635
				],
				[
					-2.6173634146559834,
					2.2901929878239855
				],
				[
					0.32717042683202635,
					3.926045121983975
				],
				[
					3.926045121983975,
					3.2717042683199793
				],
				[
					4.253215548815945,
					2.9445338414879814
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06336398422718048,
				0.10586883872747421,
				0.15860086679458618,
				0.1972372978925705,
				0.11213739216327667,
				0.13389718532562256,
				0.21263360977172852,
				0.2613633871078491,
				0.0995071679353714,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 1862171411,
			"isDeleted": false,
			"id": "k6xvpMh2f3yVf2F96y0xf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 447.2354294663128,
			"y": -306.13240638996604,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.8990275767909,
			"height": 13.284728197330168,
			"seed": 23549703,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.359046708035919
				],
				[
					0.3590467080359758,
					5.3857006205392395
				],
				[
					1.4361868321437896,
					8.617120992862795
				],
				[
					1.4361868321437896,
					8.258074284826876
				],
				[
					-0.359046708035919,
					6.8218874526830575
				],
				[
					-3.231420372323555,
					6.8218874526830575
				],
				[
					-5.7447473285751585,
					9.694261116970665
				],
				[
					-5.0266539125033205,
					12.566634781258273
				],
				[
					-2.1542802482156844,
					13.284728197330168
				],
				[
					1.7952335401797654,
					11.84854136518635
				],
				[
					2.1542802482157413,
					11.48949465715043
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12626199424266815,
				0.19416598975658417,
				0.21471311151981354,
				0.14621508121490479,
				0.0940072312951088,
				0.108572818338871,
				0.17085863649845123,
				0.23707297444343567,
				0.2504458427429199,
				0.04680426046252251,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1653126045,
			"isDeleted": false,
			"id": "jDN0VTmUPTgG_b1F24HRQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 453.33922350292397,
			"y": -297.15623868906727,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.539980868754981,
			"height": 7.8990275767909,
			"seed": 1367522215,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.359046708035919,
					-0.3590467080359758
				],
				[
					1.0771401241078706,
					-1.0771401241078706
				],
				[
					1.4361868321437896,
					-3.231420372323555
				],
				[
					-0.7180934160718948,
					-3.231420372323555
				],
				[
					-2.872373664287636,
					0.7180934160718948
				],
				[
					-1.7952335401797654,
					4.667607204467345
				],
				[
					3.94951378839545,
					3.231420372323555
				],
				[
					4.667607204467345,
					2.5133269562516602
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07217797636985779,
				0.1982720047235489,
				0.19063180685043335,
				0.15745562314987183,
				0.19449755549430847,
				0.27778148651123047,
				0.11063937097787857,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1849925811,
			"isDeleted": false,
			"id": "VaU3hq_MsSXjqaokVpNFg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 460.87920437167895,
			"y": -298.95147222924703,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.0266539125033205,
			"height": 6.103794036611163,
			"seed": 713926375,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.3590467080359474
				],
				[
					-0.3590467080359758,
					-0.3590467080359474
				],
				[
					-0.3590467080359758,
					0
				],
				[
					-0.3590467080359758,
					2.5133269562516602
				],
				[
					1.0771401241078706,
					3.94951378839545
				],
				[
					3.231420372323555,
					2.5133269562516602
				],
				[
					4.667607204467345,
					-0.7180934160718948
				],
				[
					4.667607204467345,
					-2.154280248215713
				],
				[
					4.308560496431426,
					-1.7952335401797654
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10947997868061066,
				0.19248999655246735,
				0.22364196181297302,
				0.22179275751113892,
				0.21722793579101562,
				0.182816743850708,
				0.018413269892334938,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1103771645,
			"isDeleted": false,
			"id": "Ztpcn9oaNr8PkaiukKM3s",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 465.5468115761463,
			"y": -301.1057524774627,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.0771401241078706,
			"height": 6.8218874526830575,
			"seed": 549627207,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7180934160719232
				],
				[
					0,
					3.5904670803595025
				],
				[
					0.7180934160718948,
					6.8218874526830575
				],
				[
					1.0771401241078706,
					6.8218874526830575
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1177930012345314,
				0.2043599784374237,
				0.040798310190439224,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1091768915,
			"isDeleted": false,
			"id": "ogd2QIzd7OhmAgEOfIIJ5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 468.77823194846985,
			"y": -303.97812614175035,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.359046708035919,
			"height": 1.0771401241078422,
			"seed": 872268807,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.3590467080359474
				],
				[
					-0.359046708035919,
					-0.3590467080359474
				],
				[
					-0.359046708035919,
					-0.7180934160718948
				],
				[
					-0.359046708035919,
					-1.0771401241078422
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.17239300906658173,
				0.22267287969589233,
				0.10012970119714737,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1528574045,
			"isDeleted": false,
			"id": "U_1aA6HJ_1anc1RoYldg0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 472.3686990288294,
			"y": -300.0286123533549,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.103794036611134,
			"height": 6.103794036611134,
			"seed": 2105806087,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.359046708035919,
					0
				],
				[
					0.359046708035919,
					-0.359046708035919
				],
				[
					-1.0771401241078706,
					0
				],
				[
					-2.5133269562516602,
					2.1542802482157413
				],
				[
					-2.1542802482157413,
					4.308560496431426
				],
				[
					0.7180934160718948,
					5.744747328575215
				],
				[
					3.231420372323555,
					3.9495137883954783
				],
				[
					3.590467080359474,
					3.590467080359531
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1272839903831482,
				0.21997198462486267,
				0.2911355495452881,
				0.3019874393939972,
				0.28689107298851013,
				0.23590411245822906,
				0.07903894037008286,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 407064563,
			"isDeleted": false,
			"id": "TlDgh_noVa5cnV8O3RDZs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 478.4724930654405,
			"y": -299.6695656453189,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.539980868754981,
			"height": 6.821887452683086,
			"seed": 1570422855,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7180934160718948,
					0.3590467080359474
				],
				[
					2.1542802482157413,
					0.7180934160718948
				],
				[
					3.590467080359531,
					-0.3590467080359758
				],
				[
					3.590467080359531,
					-2.154280248215713
				],
				[
					1.7952335401797654,
					-2.872373664287636
				],
				[
					0.3590467080359758,
					-1.436186832143818
				],
				[
					0.3590467080359758,
					1.4361868321437896
				],
				[
					1.7952335401797654,
					3.94951378839545
				],
				[
					6.821887452683086,
					1.7952335401797654
				],
				[
					7.539980868754981,
					1.4361868321437896
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15516500174999237,
				0.2627420127391815,
				0.2833572328090668,
				0.16230520606040955,
				0.0827159732580185,
				0.11608221381902695,
				0.24021057784557343,
				0.3257319927215576,
				0.05396951362490654,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 2085625021,
			"isDeleted": false,
			"id": "s13p3Ak1berdHsnM7TuK4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 490.3210344306269,
			"y": -303.6190794337144,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.539980868754981,
			"height": 8.258074284826847,
			"seed": 1902800327,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7180934160718948,
					0
				],
				[
					-1.4361868321437896,
					0.359046708035919
				],
				[
					-3.231420372323555,
					0.7180934160718948
				],
				[
					-3.590467080359531,
					1.795233540179737
				],
				[
					-1.4361868321437896,
					3.590467080359474
				],
				[
					1.0771401241078706,
					6.103794036611134
				],
				[
					0,
					7.8990275767909
				],
				[
					-2.872373664287636,
					8.258074284826847
				],
				[
					-6.46284074464711,
					6.103794036611134
				],
				[
					-6.46284074464711,
					5.744747328575215
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09049798548221588,
				0.1627500057220459,
				0.21943399310112,
				0.2187993824481964,
				0.2352483570575714,
				0.27656251192092896,
				0.2615777552127838,
				0.12789177894592285,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1171970451,
			"isDeleted": false,
			"id": "RKmEvx0fd7GHuWbib8KPe",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 511.09532463455184,
			"y": -307.0684509943587,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.9483512467493256,
			"height": 11.040657064912494,
			"seed": 827448135,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.3247252077915448
				],
				[
					-0.3247252077915732,
					-0.3247252077915448
				],
				[
					-0.6494504155831464,
					2.922526870123903
				],
				[
					-1.9483512467493256,
					9.741756233746344
				],
				[
					-1.6236260389577524,
					10.71593185712095
				],
				[
					-1.6236260389577524,
					10.06648144153786
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10746661573648453,
				0.23340636491775513,
				0.19893509149551392,
				0.058607056736946106,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1023900957,
			"isDeleted": false,
			"id": "XTrTtM7cQoVbifxt3HdkZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 510.77059942676027,
			"y": -308.3673518255249,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.767580610371738,
			"height": 0.9741756233746344,
			"seed": 534570055,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.3247252077915732,
					0
				],
				[
					-0.6494504155830896,
					0
				],
				[
					0.3247252077915732,
					0
				],
				[
					3.8967024934985375,
					0.6494504155830896
				],
				[
					7.143954571413985,
					0.9741756233746344
				],
				[
					8.118130194788648,
					0.9741756233746344
				],
				[
					8.118130194788648,
					0.6494504155830896
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0766487717628479,
				0.1987716108560562,
				0.26774999499320984,
				0.2297368198633194,
				0.06275497376918793,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 386936627,
			"isDeleted": false,
			"id": "w-XV5O_8t91lujBg7ZVzB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 518.5640044137574,
			"y": -307.7179014099418,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.273076454540785,
			"height": 11.040657064912523,
			"seed": 1517268071,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.3247252077915732,
					0
				],
				[
					-0.3247252077915732,
					2.5978016623323583
				],
				[
					-1.2989008311661792,
					7.46867977920553
				],
				[
					-1.9483512467492687,
					11.040657064912523
				],
				[
					-2.273076454540785,
					10.71593185712095
				],
				[
					-2.273076454540785,
					10.391206649329433
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.2391120046377182,
				0.25547659397125244,
				0.24477750062942505,
				0.04194183275103569,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1152635261,
			"isDeleted": false,
			"id": "vMqI_rMgoFf9H4q0h0IF4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 507.84807255663634,
			"y": -294.72889309828,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.819229363622469,
			"height": 0.6494504155830896,
			"seed": 2134873447,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.2989008311661792,
					0
				],
				[
					4.8708781168732,
					0.32472520779151637
				],
				[
					6.819229363622469,
					-0.3247252077915732
				],
				[
					6.819229363622469,
					-0.3247252077915732
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2770940065383911,
				0.30511876940727234,
				0.08293023705482483,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1850331347,
			"isDeleted": false,
			"id": "ZfTiUpkttHrCBsgM2FVB6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 512.394225465718,
			"y": -299.92449642294474,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.273076454540842,
			"height": 6.494504155830867,
			"seed": 1632640039,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.3247252077915732,
					0
				],
				[
					-0.6494504155831464,
					0.6494504155830896
				],
				[
					-0.3247252077915732,
					2.5978016623323583
				],
				[
					0.6494504155830327,
					4.221427701290054
				],
				[
					1.2989008311661792,
					3.247252077915448
				],
				[
					1.6236260389576955,
					0
				],
				[
					1.2989008311661792,
					-2.2730764545408135
				],
				[
					-0.6494504155831464,
					0
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.23813000321388245,
				0.20597580075263977,
				0.194597989320755,
				0.21602411568164825,
				0.20014618337154388,
				0.18092308938503265,
				0.14727111160755157,
				0.05270922929048538,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 1352047069,
			"isDeleted": false,
			"id": "aFREBZpv4D70KREVBazHS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 513.3684010890927,
			"y": -299.59977121515317,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.3247252077915732,
			"height": 0,
			"seed": 1091631527,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.3247252077915732,
					0
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 488521331,
			"isDeleted": false,
			"id": "80LLgbCX3RnKgGrZF52hZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 506.22444651767864,
			"y": -313.88768035798114,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.5978016623323583,
			"height": 7.46867977920553,
			"seed": 1767706951,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.3247252077915732
				],
				[
					-0.6494504155830896,
					-0.3247252077915732
				],
				[
					-1.2989008311661792,
					0.6494504155830896
				],
				[
					-2.273076454540842,
					3.896702493498509
				],
				[
					-2.5978016623323583,
					7.143954571413957
				],
				[
					-2.273076454540842,
					7.143954571413957
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.055832549929618835,
				0.1608399897813797,
				0.2385520040988922,
				0.13137808442115784,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 2042713661,
			"isDeleted": false,
			"id": "Aqk6x8bghXI-NaQJoT2Bs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 503.6266448553463,
			"y": -315.8360316047304,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.5978016623323583,
			"height": 8.118130194788591,
			"seed": 1355946567,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6494504155830327,
					0.32472520779151637
				],
				[
					-1.2989008311661792,
					0.974175623374606
				],
				[
					-2.5978016623323583,
					3.5719772857069643
				],
				[
					-2.5978016623323583,
					8.118130194788591
				],
				[
					-2.273076454540785,
					8.118130194788591
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07322698831558228,
				0.09300399571657181,
				0.17759399116039276,
				0.05252804607152939,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 2119432211,
			"isDeleted": false,
			"id": "ftJUvJSYIVqMcWKkScOs7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 498.43104153068157,
			"y": -318.43383326706277,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.273076454540785,
			"height": 13.963183935036398,
			"seed": 449495079,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.32472520779151637,
					0.3247252077915448
				],
				[
					-0.6494504155830327,
					0.9741756233746344
				],
				[
					-1.6236260389576955,
					4.221427701290054
				],
				[
					-2.273076454540785,
					9.41703102595477
				],
				[
					-1.2989008311661792,
					13.638458727244853
				],
				[
					-0.974175623374606,
					13.963183935036398
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07334057986736298,
				0.20575100183486938,
				0.28630200028419495,
				0.0999707356095314,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 991266461,
			"isDeleted": false,
			"id": "_ZQSTcIRr7lq8vPdfXdyo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 520.8370808682981,
			"y": -316.4854820203135,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2989008311661792,
			"height": 8.767580610371681,
			"seed": 1752885543,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.32472520779151637
				],
				[
					0.6494504155831464,
					3.5719772857069643
				],
				[
					1.2989008311661792,
					8.767580610371681
				],
				[
					1.2989008311661792,
					8.767580610371681
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0696500837802887,
				0.17499053478240967,
				0.07548364251852036,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1340177843,
			"isDeleted": false,
			"id": "Fth7aSR4MjnTi18hrU238",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 526.0326841929628,
			"y": -317.7843828514797,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.32472520779151637,
			"height": 7.7934049869970465,
			"seed": 1483317223,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.32472520779151637,
					0.974175623374606
				],
				[
					-0.32472520779151637,
					4.221427701290054
				],
				[
					0,
					7.7934049869970465
				],
				[
					0,
					7.7934049869970465
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09585083276033401,
				0.19514797627925873,
				0.08931927382946014,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 927247101,
			"isDeleted": false,
			"id": "zHBUIa4VfiANo8s8mtxB0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 531.2282875176276,
			"y": -321.0316349293951,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 11.690107480495584,
			"seed": 1326466727,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					3.5719772857069927
				],
				[
					0,
					9.41703102595477
				],
				[
					0,
					11.690107480495584
				],
				[
					0,
					11.690107480495584
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12225799262523651,
				0.2821659743785858,
				0.22315698862075806,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1290620755,
			"isDeleted": false,
			"id": "IWtdivMwMBLKhJkk3PbjU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 443.227756206119,
			"y": -273.9464797996212,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.8708781168732,
			"height": 7.143954571413985,
			"seed": 1035656551,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.3247252077915732,
					1.9483512467492687
				],
				[
					0.9741756233746628,
					5.195603324664717
				],
				[
					1.2989008311661792,
					5.845053740247806
				],
				[
					2.273076454540842,
					3.247252077915448
				],
				[
					3.8967024934985375,
					0
				],
				[
					4.8708781168732,
					-1.2989008311661792
				],
				[
					4.8708781168732,
					-0.974175623374606
				],
				[
					4.546152909081684,
					-0.6494504155830896
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15402807295322418,
				0.16519784927368164,
				0.1343458592891693,
				0.12238656729459763,
				0.1679013967514038,
				0.13754989206790924,
				0.017652709037065506,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 1053836125,
			"isDeleted": false,
			"id": "tDQddeOzcdBzkD5pGvK2-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 450.37171077753305,
			"y": -273.2970293840381,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.546152909081684,
			"height": 6.494504155830896,
			"seed": 1239062695,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.32472520779151637
				],
				[
					-0.3247252077915732,
					0.3247252077915732
				],
				[
					-0.6494504155831464,
					2.9225268701239315
				],
				[
					0.32472520779151637,
					4.8708781168732
				],
				[
					2.273076454540785,
					4.546152909081627
				],
				[
					3.8967024934985375,
					2.273076454540842
				],
				[
					3.5719772857069643,
					-0.974175623374606
				],
				[
					1.6236260389576955,
					-1.6236260389576955
				],
				[
					0,
					-0.32472520779151637
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06656298786401749,
				0.12169943004846573,
				0.17780472338199615,
				0.19789138436317444,
				0.23023608326911926,
				0.24257156252861023,
				0.18733541667461395,
				0.11089077591896057,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 130936051,
			"isDeleted": false,
			"id": "jYxrdaQOt49mSzhTZDw0z",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 442.9030309983275,
			"y": -274.5959302152043,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.546152909081627,
			"height": 7.143954571413985,
			"seed": 55138631,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.9741756233746628
				],
				[
					1.2989008311661792,
					4.546152909081627
				],
				[
					1.6236260389576955,
					5.195603324664717
				],
				[
					1.9483512467492687,
					3.247252077915448
				],
				[
					2.9225268701238747,
					0.3247252077915732
				],
				[
					3.8967024934985375,
					-0.974175623374606
				],
				[
					4.546152909081627,
					-0.32472520779151637
				],
				[
					4.546152909081627,
					2.5978016623323583
				],
				[
					3.8967024934985375,
					6.169778948039379
				],
				[
					3.8967024934985375,
					6.169778948039379
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14824895560741425,
				0.16734814643859863,
				0.13486236333847046,
				0.10885699093341827,
				0.09845758229494095,
				0.14503441751003265,
				0.1855941116809845,
				0.2164248377084732,
				0.0949869379401207,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 369741757,
			"isDeleted": false,
			"id": "AmIZisXG4RMGOTgpx5kQW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 452.9695124398654,
			"y": -270.3745025139142,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.8967024934985375,
			"height": 4.8708781168732,
			"seed": 337348295,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.3247252077915732
				],
				[
					0.32472520779151637,
					-0.6494504155830896
				],
				[
					0.32472520779151637,
					-1.6236260389577524
				],
				[
					0.6494504155830327,
					-3.571977285707021
				],
				[
					-0.6494504155831464,
					-4.8708781168732
				],
				[
					-2.5978016623323583,
					-3.8967024934985375
				],
				[
					-3.2472520779155047,
					-1.6236260389577524
				],
				[
					-2.9225268701239315,
					-1.2989008311661792
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08263800293207169,
				0.09963998198509216,
				0.13910998404026031,
				0.1986520141363144,
				0.1596345752477646,
				0.1107514351606369,
				0.006166137754917145,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 67753619,
			"isDeleted": false,
			"id": "um0olhWmQiO5k_qakkBe6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 455.56731410219777,
			"y": -271.99812855287195,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.2472520779155047,
			"height": 3.8967024934985375,
			"seed": 1752762887,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.3247252077915732,
					0
				],
				[
					-0.6494504155831464,
					0.6494504155830896
				],
				[
					-0.6494504155831464,
					1.2989008311661792
				],
				[
					0.32472520779151637,
					3.247252077915448
				],
				[
					1.948351246749212,
					3.8967024934985375
				],
				[
					2.5978016623323583,
					3.571977285707021
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10140398889780045,
				0.16844424605369568,
				0.24101199209690094,
				0.14826449751853943,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 2064830493,
			"isDeleted": false,
			"id": "0RpDhhR_RF1XOmD0E04Iv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 463.0359938814032,
			"y": -280.7657091632436,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.974175623374606,
			"height": 12.014832688287157,
			"seed": 769217287,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.3247252077915448
				],
				[
					0,
					1.9483512467492687
				],
				[
					0.3247252077915732,
					7.793404986997075
				],
				[
					-0.32472520779151637,
					11.690107480495612
				],
				[
					-0.6494504155830327,
					11.36538227270404
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0795067772269249,
				0.16836385428905487,
				0.18054437637329102,
				0.006838287226855755,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 274172979,
			"isDeleted": false,
			"id": "AdREa2VW9shmPq2D-FjRp",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 458.48984097232164,
			"y": -274.27120500741273,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.442855402580108,
			"height": 1.2989008311661792,
			"seed": 864899303,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.32472520779151637,
					0
				],
				[
					0.6494504155830896,
					-0.3247252077915732
				],
				[
					1.9483512467492687,
					-0.3247252077915732
				],
				[
					5.520328532456233,
					0
				],
				[
					8.118130194788591,
					0.974175623374606
				],
				[
					8.442855402580108,
					0.974175623374606
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07864398509263992,
				0.0760309174656868,
				0.22650198638439178,
				0.015054138377308846,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1809630333,
			"isDeleted": false,
			"id": "lOu2PPmhusWH7O1_ZNsBK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 467.9068719982764,
			"y": -273.2970293840381,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.221427701290111,
			"height": 5.845053740247806,
			"seed": 1561377255,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.32472520779151637
				],
				[
					-0.6494504155830896,
					0.3247252077915732
				],
				[
					-0.9741756233746628,
					2.9225268701239315
				],
				[
					0.6494504155830896,
					5.195603324664717
				],
				[
					2.5978016623323583,
					4.546152909081627
				],
				[
					3.247252077915448,
					1.6236260389577524
				],
				[
					2.9225268701238747,
					-0.32472520779151637
				],
				[
					2.9225268701238747,
					-0.6494504155830896
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06534124910831451,
				0.13823889195919037,
				0.17105944454669952,
				0.2166496217250824,
				0.24148029088974,
				0.1981668770313263,
				0.03594863787293434,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1620938195,
			"isDeleted": false,
			"id": "bw134HKxfELqe6aYyN_Dl",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 474.0766509463158,
			"y": -273.62175459182964,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.54615290908157,
			"height": 6.819229363622412,
			"seed": 1742656807,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.32472520779151637
				],
				[
					0.32472520779151637,
					2.5978016623323583
				],
				[
					0.6494504155830327,
					4.870878116873143
				],
				[
					0.974175623374606,
					3.8967024934985375
				],
				[
					2.9225268701238747,
					0.32472520779151637
				],
				[
					4.54615290908157,
					-1.9483512467492687
				],
				[
					4.54615290908157,
					-1.6236260389577524
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.03945452719926834,
				0.12764917314052582,
				0.13381606340408325,
				0.12857358157634735,
				0.14780588448047638,
				0.04838522523641586,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 740895965,
			"isDeleted": false,
			"id": "HDTl0C9fjyxkahms-9JM5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 481.2206055177297,
			"y": -271.6734033450804,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.118130194788591,
			"height": 7.468679779205559,
			"seed": 1190502727,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.3247252077915732,
					0
				],
				[
					0.6494504155831464,
					0
				],
				[
					1.6236260389576955,
					-0.3247252077915732
				],
				[
					2.9225268701238747,
					-1.2989008311661792
				],
				[
					1.9483512467492687,
					-2.9225268701239315
				],
				[
					-0.974175623374606,
					-2.273076454540842
				],
				[
					-2.273076454540785,
					1.2989008311661792
				],
				[
					0.6494504155831464,
					4.221427701290054
				],
				[
					5.520328532456233,
					4.546152909081627
				],
				[
					5.845053740247806,
					4.546152909081627
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08248598873615265,
				0.1260180026292801,
				0.20444899797439575,
				0.12932714819908142,
				0.03361907973885536,
				0.12141034007072449,
				0.2837520241737366,
				0.16225311160087585,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 143,
			"versionNonce": 1743936371,
			"isDeleted": false,
			"id": "e3hfBC_lHLJIBBsG4wsC5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 505.57499610209555,
			"y": -286.935488111283,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 23.380214960991225,
			"height": 23.05548975319965,
			"seed": 412864199,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.3247252077915732,
					0
				],
				[
					-0.6494504155830896,
					0
				],
				[
					-0.974175623374606,
					0
				],
				[
					-2.273076454540785,
					1.2989008311661792
				],
				[
					-3.247252077915448,
					2.922526870123903
				],
				[
					-3.5719772857069643,
					4.221427701290082
				],
				[
					-2.9225268701238747,
					4.546152909081627
				],
				[
					-1.2989008311661792,
					4.546152909081627
				],
				[
					0.3247252077915732,
					3.8967024934985375
				],
				[
					1.2989008311661792,
					3.8967024934985375
				],
				[
					1.6236260389577524,
					4.546152909081627
				],
				[
					2.5978016623323583,
					5.845053740247806
				],
				[
					3.247252077915448,
					6.169778948039351
				],
				[
					3.5719772857069643,
					6.494504155830896
				],
				[
					3.247252077915448,
					6.819229363622441
				],
				[
					3.247252077915448,
					7.143954571413985
				],
				[
					2.5978016623323583,
					8.11813019478862
				],
				[
					1.2989008311661792,
					9.417031025954799
				],
				[
					0.3247252077915732,
					10.066481441537888
				],
				[
					-0.3247252077915732,
					11.040657064912494
				],
				[
					-0.3247252077915732,
					11.365382272704068
				],
				[
					-0.3247252077915732,
					11.690107480495584
				],
				[
					-0.974175623374606,
					11.365382272704068
				],
				[
					-2.5978016623323015,
					11.365382272704068
				],
				[
					-3.5719772857069643,
					11.040657064912494
				],
				[
					-4.870878116873143,
					11.040657064912494
				],
				[
					-5.19560332466466,
					10.715931857120978
				],
				[
					-5.19560332466466,
					10.066481441537888
				],
				[
					-5.845053740247806,
					9.417031025954799
				],
				[
					-6.494504155830839,
					9.092305818163254
				],
				[
					-6.819229363622412,
					9.417031025954799
				],
				[
					-7.143954571413985,
					10.715931857120978
				],
				[
					-6.819229363622412,
					13.638458727244853
				],
				[
					-6.494504155830839,
					15.262084766202605
				],
				[
					-6.169778948039323,
					14.937359558411032
				],
				[
					-6.169778948039323,
					14.287909142827942
				],
				[
					-6.169778948039323,
					13.963183935036426
				],
				[
					-6.169778948039323,
					13.638458727244853
				],
				[
					-5.520328532456233,
					14.287909142827942
				],
				[
					-3.5719772857069643,
					14.287909142827942
				],
				[
					-0.974175623374606,
					13.313733519453336
				],
				[
					-0.3247252077915732,
					12.989008311661763
				],
				[
					-0.6494504155830896,
					12.989008311661763
				],
				[
					-0.3247252077915732,
					12.989008311661763
				],
				[
					0.6494504155830896,
					12.664283103870247
				],
				[
					1.9483512467492687,
					11.690107480495584
				],
				[
					2.273076454540785,
					11.365382272704068
				],
				[
					1.9483512467492687,
					13.313733519453336
				],
				[
					1.9483512467492687,
					15.911535181785695
				],
				[
					1.9483512467492687,
					17.859886428534963
				],
				[
					2.273076454540785,
					17.53516122074339
				],
				[
					2.9225268701239315,
					16.560985597368784
				],
				[
					5.195603324664717,
					14.287909142827942
				],
				[
					7.143954571413985,
					12.014832688287157
				],
				[
					7.793404986997075,
					11.040657064912494
				],
				[
					7.793404986997075,
					11.690107480495584
				],
				[
					7.793404986997075,
					12.014832688287157
				],
				[
					8.442855402580165,
					12.339557896078674
				],
				[
					10.391206649329433,
					12.664283103870247
				],
				[
					11.690107480495612,
					12.989008311661763
				],
				[
					11.040657064912523,
					14.937359558411032
				],
				[
					9.417031025954827,
					17.210436012951874
				],
				[
					11.36538227270404,
					16.23626038957721
				],
				[
					14.93735955841106,
					14.612634350619516
				],
				[
					16.23626038957724,
					14.612634350619516
				],
				[
					15.262084766202577,
					16.560985597368784
				],
				[
					14.28790914282797,
					19.158787259701143
				],
				[
					13.638458727244881,
					20.45768809086732
				],
				[
					12.989008311661792,
					21.107138506450383
				],
				[
					10.391206649329433,
					21.431863714241928
				],
				[
					7.793404986997075,
					22.081314129825017
				],
				[
					7.468679779205502,
					22.730764545408107
				],
				[
					8.118130194788648,
					23.05548975319965
				],
				[
					10.06648144153786,
					22.081314129825017
				],
				[
					10.06648144153786,
					21.756588922033472
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07118597626686096,
				0.13788723945617676,
				0.20620599389076233,
				0.24754886329174042,
				0.2523996829986572,
				0.25920751690864563,
				0.26422080397605896,
				0.26994016766548157,
				0.2729686200618744,
				0.3035721778869629,
				0.31444597244262695,
				0.31738898158073425,
				0.3356274366378784,
				0.33777961134910583,
				0.3252902030944824,
				0.3251538872718811,
				0.3161942660808563,
				0.32388588786125183,
				0.33629629015922546,
				0.334128737449646,
				0.3360489308834076,
				0.33488377928733826,
				0.32258108258247375,
				0.32983827590942383,
				0.34615558385849,
				0.3620036840438843,
				0.37738150358200073,
				0.39196130633354187,
				0.39664629101753235,
				0.39911022782325745,
				0.42100054025650024,
				0.45735257863998413,
				0.45975935459136963,
				0.4438014328479767,
				0.43010982871055603,
				0.4287424087524414,
				0.43887946009635925,
				0.4665541350841522,
				0.5004532337188721,
				0.47824278473854065,
				0.44685015082359314,
				0.4393557906150818,
				0.4135211110115051,
				0.4053134024143219,
				0.38338708877563477,
				0.3831596374511719,
				0.44489067792892456,
				0.4828295409679413,
				0.4794626533985138,
				0.4337288737297058,
				0.4379517734050751,
				0.4457145929336548,
				0.4355776607990265,
				0.43415337800979614,
				0.47498032450675964,
				0.47614720463752747,
				0.5069276094436646,
				0.5398789048194885,
				0.5116531848907471,
				0.49803537130355835,
				0.4672905504703522,
				0.40198561549186707,
				0.48557525873184204,
				0.4716678857803345,
				0.4586433172225952,
				0.51788729429245,
				0.48434436321258545,
				0.45278576016426086,
				0.42866647243499756,
				0.4478076994419098,
				0.4831857979297638,
				0.4585001766681671,
				0.1338968575000763,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 87,
			"versionNonce": 193562941,
			"isDeleted": false,
			"id": "R2TCpt_hMvazVM6elsWj6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 508.822248180011,
			"y": -263.5552731502918,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.690107480495612,
			"height": 3.247252077915448,
			"seed": 303293287,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.32472520779151637,
					0
				],
				[
					-0.6494504155830896,
					0
				],
				[
					-0.32472520779151637,
					-0.9741756233746344
				],
				[
					-0.32472520779151637,
					-2.2730764545408135
				],
				[
					-1.2989008311661792,
					-2.2730764545408135
				],
				[
					-2.9225268701238747,
					-0.3247252077915448
				],
				[
					-3.247252077915448,
					0.3247252077915448
				],
				[
					-3.247252077915448,
					-0.3247252077915448
				],
				[
					-3.247252077915448,
					-1.9483512467492687
				],
				[
					-3.8967024934985375,
					-1.9483512467492687
				],
				[
					-4.8708781168732,
					-0.6494504155830896
				],
				[
					-5.520328532456233,
					-0.6494504155830896
				],
				[
					-6.819229363622412,
					-2.2730764545408135
				],
				[
					-8.442855402580108,
					-2.5978016623323583
				],
				[
					-10.391206649329433,
					-0.9741756233746344
				],
				[
					-11.690107480495612,
					-0.6494504155830896
				],
				[
					-11.36538227270404,
					-0.9741756233746344
				],
				[
					-9.092305818163254,
					0.3247252077915448
				],
				[
					-8.442855402580108,
					0.6494504155830896
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11189083755016327,
				0.203975647687912,
				0.18756403028964996,
				0.1636408120393753,
				0.20029012858867645,
				0.21374182403087616,
				0.19562754034996033,
				0.16964007914066315,
				0.19466815888881683,
				0.2313614785671234,
				0.21848250925540924,
				0.16616705060005188,
				0.18690575659275055,
				0.21740588545799255,
				0.2086033970117569,
				0.168136864900589,
				0.09232034534215927,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 84,
			"versionNonce": 1922856211,
			"isDeleted": false,
			"id": "F4l-bsNEALVZt_kvwKDht",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 516.9403783747996,
			"y": -263.23054794250027,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.158787259701114,
			"height": 5.520328532456233,
			"seed": 1617655047,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.9741756233746344
				],
				[
					0,
					1.623626038957724
				],
				[
					0.3247252077915732,
					1.623626038957724
				],
				[
					2.273076454540842,
					-1.2989008311661792
				],
				[
					3.8967024934985375,
					-3.5719772857069927
				],
				[
					3.8967024934985375,
					-1.623626038957724
				],
				[
					4.546152909081684,
					0
				],
				[
					6.169778948039379,
					-2.2730764545408135
				],
				[
					7.793404986997075,
					-3.2472520779154195
				],
				[
					8.767580610371738,
					-1.9483512467492687
				],
				[
					10.71593185712095,
					-2.5978016623323583
				],
				[
					12.664283103870275,
					-3.2472520779154195
				],
				[
					14.93735955841106,
					-1.9483512467492687
				],
				[
					17.210436012951845,
					-2.5978016623323583
				],
				[
					18.834062051909598,
					-3.5719772857069927
				],
				[
					19.158787259701114,
					-3.896702493498509
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10513141006231308,
				0.2029220014810562,
				0.2140139490365982,
				0.16909117996692657,
				0.17871566116809845,
				0.2522355616092682,
				0.19933991134166718,
				0.18269012868404388,
				0.22356781363487244,
				0.2354132980108261,
				0.22712472081184387,
				0.266690194606781,
				0.22326290607452393,
				0.11774536222219467,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 96,
			"versionNonce": 1801410973,
			"isDeleted": false,
			"id": "VyIno7vBywc0yS3ZGOWl5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 549.359541698894,
			"y": -320.89559741983896,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.224495037031545,
			"height": 55.74832535059028,
			"seed": 1267609927,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7482996691354344
				],
				[
					-0.3741498345676746,
					-1.1224495037031659
				],
				[
					1.1224495037031943,
					0
				],
				[
					5.238097683948126,
					2.993198676541766
				],
				[
					7.857146525922133,
					6.360547187651235
				],
				[
					7.857146525922133,
					9.727895698760705
				],
				[
					5.986397353083532,
					12.7210943753025
				],
				[
					3.7414983456772575,
					14.965993382708803
				],
				[
					1.4965993382709257,
					16.836742555547403
				],
				[
					1.4965993382709257,
					18.3333418938183
				],
				[
					2.619048841974063,
					19.82994123208917
				],
				[
					3.7414983456772575,
					20.578240901224603
				],
				[
					3.7414983456772575,
					21.326540570360038
				],
				[
					2.619048841974063,
					22.074840239495472
				],
				[
					1.4965993382709257,
					22.823139908630907
				],
				[
					1.1224495037031943,
					23.945589412334073
				],
				[
					1.1224495037031943,
					25.816338585172673
				],
				[
					2.619048841974063,
					27.687087758011273
				],
				[
					4.115648180244932,
					30.306136599985308
				],
				[
					5.612247518515858,
					34.42178478023024
				],
				[
					6.360547187651264,
					38.53743296047517
				],
				[
					6.734697022218995,
					42.27893130615237
				],
				[
					6.734697022218995,
					46.76872932096501
				],
				[
					4.863947849380395,
					50.51022766664221
				],
				[
					1.8707491728386003,
					53.87757617775168
				],
				[
					-1.496599338270812,
					54.62587584688711
				],
				[
					-3.3673485111094124,
					53.12927650861624
				],
				[
					-2.9931986765417378,
					52.38097683948081
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1509971022605896,
				0.2283278852701187,
				0.27503302693367004,
				0.26526737213134766,
				0.2618531584739685,
				0.29464590549468994,
				0.3133338391780853,
				0.30983874201774597,
				0.3099427819252014,
				0.3082767128944397,
				0.31314244866371155,
				0.345560759305954,
				0.34166237711906433,
				0.30624741315841675,
				0.2859693467617035,
				0.28775787353515625,
				0.30357295274734497,
				0.3195979595184326,
				0.36466994881629944,
				0.37871551513671875,
				0.35476937890052795,
				0.3701934218406677,
				0.4736426770687103,
				0.5450069308280945,
				0.4713653028011322,
				0.12327902019023895,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 82,
			"versionNonce": 1202867,
			"isDeleted": false,
			"id": "d2_JFTc01mw6_bzBrG2Pb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 565.4479845853059,
			"y": -316.0316495704586,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.231296360489864,
			"height": 9.353745864193002,
			"seed": 1939090183,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.37414983456773143,
					0
				],
				[
					-0.7482996691354629,
					0
				],
				[
					-0.37414983456773143,
					0.37414983456773143
				],
				[
					1.4965993382708689,
					2.2448990074063317
				],
				[
					4.863947849380338,
					4.115648180244932
				],
				[
					6.734697022218938,
					4.489798014812635
				],
				[
					7.482996691354401,
					4.489798014812635
				],
				[
					6.734697022218938,
					4.863947849380338
				],
				[
					4.863947849380338,
					5.612247518515801
				],
				[
					2.2448990074063317,
					7.482996691354401
				],
				[
					0.7482996691354629,
					9.353745864193002
				],
				[
					1.1224495037031375,
					9.353745864193002
				],
				[
					2.619048841974063,
					8.605446195057539
				],
				[
					2.619048841974063,
					8.605446195057539
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06368698179721832,
				0.06677325069904327,
				0.20130999386310577,
				0.23661679029464722,
				0.22889624536037445,
				0.22604131698608398,
				0.21646569669246674,
				0.20447112619876862,
				0.2319396734237671,
				0.2923114597797394,
				0.3317987024784088,
				0.2762969732284546,
				0.10571926832199097,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 81534461,
			"isDeleted": false,
			"id": "5X9Pym1ioG_X-57l7uBQq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 579.5926835690818,
			"y": -314.8735465841524,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.4230493345893365,
			"height": 5.528811668236756,
			"seed": 668581127,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.27644058341184063
				],
				[
					-0.5528811668236813,
					-0.27644058341184063
				],
				[
					-1.3822029170592032,
					-0.27644058341184063
				],
				[
					-1.6586435004710438,
					1.1057623336473625
				],
				[
					0,
					3.317287000942059
				],
				[
					0.8293217502354651,
					4.423049334589393
				],
				[
					0.8293217502354651,
					4.975930501413075
				],
				[
					-1.3822029170592032,
					5.252371084824915
				],
				[
					-3.5937275843538714,
					5.252371084824915
				],
				[
					-3.5937275843538714,
					4.975930501413075
				],
				[
					-3.5937275843538714,
					4.423049334589393
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08993853628635406,
				0.17019857466220856,
				0.17926037311553955,
				0.16106225550174713,
				0.17445644736289978,
				0.1701376885175705,
				0.22710907459259033,
				0.24353475868701935,
				0.2578178346157074,
				0.12175589054822922,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1559923795,
			"isDeleted": false,
			"id": "evpOLDm7DpFtB6E5m2iJN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 583.4628517368476,
			"y": -315.7028683343879,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.699489918001291,
			"height": 6.358133418472278,
			"seed": 741302695,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.27644058341184063,
					0
				],
				[
					-0.5528811668236813,
					0
				],
				[
					-0.8293217502355219,
					0.27644058341184063
				],
				[
					-0.8293217502355219,
					1.3822029170592032
				],
				[
					0,
					4.699489918001234
				],
				[
					1.6586435004710438,
					6.081692835060437
				],
				[
					3.870168167765769,
					4.423049334589393
				],
				[
					3.870168167765769,
					0
				],
				[
					3.5937275843539283,
					-0.27644058341184063
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13528800010681152,
				0.1618500053882599,
				0.1702214628458023,
				0.17833426594734192,
				0.1828591674566269,
				0.17774905264377594,
				0.0907578393816948,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 1862358621,
			"isDeleted": false,
			"id": "puW6XK5203Ymggr068z7W",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 591.7560692392027,
			"y": -315.97930891779976,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.975930501413018,
			"height": 7.46389575211964,
			"seed": 818321415,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.27644058341184063,
					0
				],
				[
					-0.5528811668236813,
					-0.27644058341184063
				],
				[
					-1.3822029170591463,
					0
				],
				[
					-2.7644058341183495,
					1.6586435004710438
				],
				[
					-2.2115246672946682,
					3.040846417530247
				],
				[
					0,
					4.423049334589422
				],
				[
					0.5528811668236813,
					5.528811668236756
				],
				[
					-0.5528811668236813,
					6.911014585295959
				],
				[
					-3.5937275843538714,
					7.1874551687078
				],
				[
					-4.4230493345893365,
					4.975930501413075
				],
				[
					-4.146608751177496,
					4.423049334589422
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.04311081022024155,
				0.056639738380908966,
				0.18141934275627136,
				0.21651598811149597,
				0.20211230218410492,
				0.23449011147022247,
				0.29004883766174316,
				0.24824368953704834,
				0.021877991035580635,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 2100005363,
			"isDeleted": false,
			"id": "F53_6onQwnd8Ng81Axp6A",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 597.0084403240277,
			"y": -316.2557495012116,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.4638957521195834,
			"height": 5.8052522516485965,
			"seed": 784882855,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.27644058341184063,
					0.27644058341184063
				],
				[
					-1.1057623336473625,
					0.8293217502355219
				],
				[
					-2.211524667294725,
					2.4879652507065657
				],
				[
					-2.4879652507065657,
					4.423049334589422
				],
				[
					-0.5528811668236813,
					5.8052522516485965
				],
				[
					4.4230493345893365,
					4.423049334589422
				],
				[
					4.975930501413018,
					3.8701681677657405
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07320999354124069,
				0.19892600178718567,
				0.2699640095233917,
				0.293146550655365,
				0.061541564762592316,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1688240829,
			"isDeleted": false,
			"id": "TA9_qBB3yqUFWrBaQ74gP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 604.1958954927354,
			"y": -316.2557495012116,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.528811668236813,
			"height": 6.358133418472249,
			"seed": 378714311,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.27644058341184063,
					0
				],
				[
					0.5528811668236813,
					-0.27644058341184063
				],
				[
					1.1057623336473625,
					-0.8293217502354935
				],
				[
					0,
					-1.1057623336473341
				],
				[
					-2.211524667294725,
					0.27644058341184063
				],
				[
					-2.4879652507065657,
					2.7644058341184063
				],
				[
					0.5528811668236813,
					5.252371084824915
				],
				[
					3.040846417530247,
					4.699489918001262
				],
				[
					3.040846417530247,
					4.146608751177581
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.05616949498653412,
				0.14204202592372894,
				0.1940111666917801,
				0.21918945014476776,
				0.29930704832077026,
				0.2891933023929596,
				0.13042379915714264,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 363582355,
			"isDeleted": false,
			"id": "cIZ4ITPGlTS8goQ1ghkp5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 611.936231828267,
			"y": -322.6138829196839,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.5528811668236813,
			"height": 11.057623336473512,
			"seed": 1922212647,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.27644058341184063,
					0.27644058341184063
				],
				[
					-0.27644058341184063,
					4.699489918001234
				],
				[
					-0.5528811668236813,
					10.50474216964983
				],
				[
					-0.5528811668236813,
					11.057623336473512
				],
				[
					-0.27644058341184063,
					10.50474216964983
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14116692543029785,
				0.2411699891090393,
				0.25033310055732727,
				0.053979676216840744,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1247486749,
			"isDeleted": false,
			"id": "DLUawTmBJvgcrZP5ad-yb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 614.9770782457971,
			"y": -327.3133728376851,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1057623336473625,
			"height": 15.204232087651093,
			"seed": 151520519,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8293217502355219
				],
				[
					0,
					7.1874551687078
				],
				[
					-0.27644058341184063,
					13.545588587180077
				],
				[
					-0.8293217502355219,
					15.204232087651093
				],
				[
					-1.1057623336473625,
					14.927791504239252
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.21545001864433289,
				0.2959419786930084,
				0.2941450774669647,
				0.03135156258940697,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1991371059,
			"isDeleted": false,
			"id": "Z9SyVi-CEc4_hay5nS46t",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 611.1069100780314,
			"y": -317.3615118348589,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.358133418472221,
			"height": 2.2115246672946967,
			"seed": 697844455,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.27644058341184063,
					0.27644058341184063
				],
				[
					0.8293217502355219,
					0.5528811668236813
				],
				[
					1.3822029170590895,
					0.5528811668236813
				],
				[
					6.08169283506038,
					-1.3822029170591748
				],
				[
					6.358133418472221,
					-1.6586435004710154
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15453198552131653,
				0.28006574511528015,
				0.3966841995716095,
				0.14298895001411438,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1956820861,
			"isDeleted": false,
			"id": "7aGLAXMu_QSIt-TtiM5NG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 619.4001275803865,
			"y": -317.08507125144706,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.5528811668236813,
			"height": 4.146608751177581,
			"seed": 609410247,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.27644058341184063
				],
				[
					-0.27644058341184063,
					1.1057623336473341
				],
				[
					-0.27644058341184063,
					3.0408464175302186
				],
				[
					0.27644058341184063,
					4.146608751177581
				],
				[
					0.27644058341184063,
					4.146608751177581
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.23257800936698914,
				0.3030700087547302,
				0.0712374597787857,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 631524051,
			"isDeleted": false,
			"id": "JoBs-kNx1JoQ5vFGRwh53",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 621.0587710808575,
			"y": -321.23168000262467,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.27644058341184063,
			"height": 0.5528811668236813,
			"seed": 1572295335,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.27644058341184063
				],
				[
					-0.27644058341184063,
					-0.5528811668236813
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11558639258146286,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 82,
			"versionNonce": 767082461,
			"isDeleted": false,
			"id": "8eAyn6h38JkYwBoKU1b7i",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 624.9289392486232,
			"y": -327.86625400450873,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.252371084824972,
			"height": 14.651350920827412,
			"seed": 1588128103,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.27644058341184063,
					0.27644058341184063
				],
				[
					-0.5528811668236813,
					0.8293217502354935
				],
				[
					-0.8293217502355219,
					4.423049334589393
				],
				[
					-1.1057623336473625,
					9.675420419414337
				],
				[
					-1.1057623336473625,
					11.610504503297165
				],
				[
					-0.8293217502355219,
					11.057623336473512
				],
				[
					0.5528811668236813,
					9.398979836002496
				],
				[
					2.4879652507065657,
					9.675420419414337
				],
				[
					2.7644058341184063,
					12.163385670120846
				],
				[
					2.211524667294725,
					13.545588587180049
				],
				[
					0.8293217502355219,
					14.374910337415571
				],
				[
					-1.1057623336473625,
					14.651350920827412
				],
				[
					-2.4879652507065657,
					13.82202917059189
				],
				[
					-2.4879652507065657,
					13.545588587180049
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07846999913454056,
				0.10494140535593033,
				0.18901227414608002,
				0.21086080372333527,
				0.17792953550815582,
				0.12595847249031067,
				0.05872732400894165,
				0.04901702702045441,
				0.14823056757450104,
				0.30302998423576355,
				0.319457471370697,
				0.2895478904247284,
				0.0422322079539299,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 924416115,
			"isDeleted": false,
			"id": "AER3ArPG7f38-b_R0TiSd",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 632.3928350007429,
			"y": -330.3542192552153,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.4879652507065657,
			"height": 14.374910337415542,
			"seed": 578141031,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.27644058341184063,
					0.5528811668236813
				],
				[
					0.27644058341184063,
					2.2115246672946967
				],
				[
					-0.5528811668236813,
					4.975930501413075
				],
				[
					-1.9350840838828844,
					10.50474216964983
				],
				[
					-2.211524667294725,
					13.822029170591861
				],
				[
					-1.6586435004710438,
					14.374910337415542
				],
				[
					-1.6586435004710438,
					14.374910337415542
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10979998856782913,
				0.14177170395851135,
				0.2653080224990845,
				0.2885715067386627,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 2075049021,
			"isDeleted": false,
			"id": "luhDMYCLu95OmxwtZdqXv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 632.9457161675666,
			"y": -317.9143930016826,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.699489918001177,
			"height": 6.911014585295959,
			"seed": 899907463,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.27644058341184063,
					0
				],
				[
					0.8293217502355219,
					0
				],
				[
					1.9350840838827708,
					-0.2764405834118122
				],
				[
					2.2115246672946114,
					-2.4879652507065373
				],
				[
					1.1057623336473625,
					-2.4879652507065373
				],
				[
					0.5528811668236813,
					1.3822029170591748
				],
				[
					4.4230493345893365,
					4.423049334589422
				],
				[
					4.699489918001177,
					4.146608751177581
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1706554889678955,
				0.3045880198478699,
				0.2529297173023224,
				0.1761961430311203,
				0.2863155007362366,
				0.18733297288417816,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1758982675,
			"isDeleted": false,
			"id": "S7-PyXEmnhgdyAsEIbyHm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 587.5919604379296,
			"y": -303.09741329443364,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4195830200636124,
			"height": 11.120066990498259,
			"seed": 92607175,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.2365971700105831
				],
				[
					-0.23659717001061153,
					-0.47319434002119465
				],
				[
					0,
					1.1829858500530008
				],
				[
					0.9463886800423893,
					6.624720760296839
				],
				[
					0.9463886800423893,
					10.646872650477064
				],
				[
					-0.23659717001061153,
					10.646872650477064
				],
				[
					-0.47319434002122307,
					10.410275480466453
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0706929937005043,
				0.07213421911001205,
				0.1390025019645691,
				0.18544375896453857,
				0.16881857812404633,
				0.006745880004018545,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 644230301,
			"isDeleted": false,
			"id": "WEyrU00IKK2hzT-Yp-L-Z",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 582.623419867707,
			"y": -296.94588687415796,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.776247180572454,
			"height": 1.1829858500530293,
			"seed": 887589607,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.23659717001061153,
					0
				],
				[
					-0.47319434002122307,
					0
				],
				[
					2.6025688701165564,
					-0.2365971700105831
				],
				[
					8.99069246040284,
					-0.7097915100318062
				],
				[
					12.303052840551231,
					-0.9463886800424177
				],
				[
					12.303052840551231,
					-1.1829858500530293
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07411300390958786,
				0.21689200401306152,
				0.2832529842853546,
				0.03636584430932999,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 81,
			"versionNonce": 2077636531,
			"isDeleted": false,
			"id": "XnbrYk-EHvxnwvoWToEmf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 596.1094585583112,
			"y": -304.043801974476,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.151526420275616,
			"height": 12.539650010561871,
			"seed": 353432551,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.23659717001061153
				],
				[
					-0.23659717001061153,
					-0.23659717001061153
				],
				[
					0.7097915100317778,
					3.075763210137808
				],
				[
					1.4195830200636124,
					8.754095290392229
				],
				[
					0.9463886800424461,
					11.829858500530065
				],
				[
					0.7097915100317778,
					12.30305284055126
				],
				[
					0.9463886800424461,
					9.93708114044523
				],
				[
					2.129374530095447,
					7.097915100318033
				],
				[
					4.495346230201449,
					6.388123590286227
				],
				[
					5.914929250265004,
					8.044303780360451
				],
				[
					5.914929250265004,
					10.646872650477064
				],
				[
					5.914929250265004,
					12.066455670540648
				],
				[
					5.914929250265004,
					11.829858500530065
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08616000413894653,
				0.1243639811873436,
				0.21811801195144653,
				0.2744860351085663,
				0.25997552275657654,
				0.19602759182453156,
				0.14267553389072418,
				0.13706029951572418,
				0.1996922641992569,
				0.24970589578151703,
				0.27363651990890503,
				0.07120318710803986,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 2106626301,
			"isDeleted": false,
			"id": "-yBAuczxRNTnkbBWW50z_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 604.1537623386716,
			"y": -295.76290102410496,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.968540570222615,
			"height": 4.968540570222615,
			"seed": 1096627911,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.23659717001061153,
					0.2365971700105831
				],
				[
					-0.9463886800423893,
					0.9463886800424177
				],
				[
					-0.47319434002122307,
					2.602568870116613
				],
				[
					1.4195830200636124,
					3.3123603801484194
				],
				[
					3.312360380148448,
					2.1293745300954185
				],
				[
					4.022151890180226,
					0
				],
				[
					2.8391660401272247,
					-1.6561801900741955
				],
				[
					0.47319434002122307,
					-0.9463886800424177
				],
				[
					-0.9463886800423893,
					1.4195830200636124
				],
				[
					-0.9463886800423893,
					1.6561801900741955
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08634918183088303,
				0.1553727090358734,
				0.19473452866077423,
				0.20529288053512573,
				0.18379037082195282,
				0.1407143920660019,
				0.0936298817396164,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1312475475,
			"isDeleted": false,
			"id": "vL5PDX_3Yp6orQ6dS_hHM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 607.4661227188201,
			"y": -294.3433180040414,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.5489575501590025,
			"height": 2.3659717001060017,
			"seed": 1333732423,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.2365971700105831
				],
				[
					0,
					0.9463886800424177
				],
				[
					3.0757632101377794,
					2.3659717001060017
				],
				[
					3.5489575501590025,
					2.1293745300954185
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09817599505186081,
				0.10462332516908646,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1588554077,
			"isDeleted": false,
			"id": "afmulk9z4qQ8J9B11pU4u",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 611.7248717790109,
			"y": -296.94588687415796,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.441734910243781,
			"height": 5.441734910243838,
			"seed": 554631943,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.9463886800424461,
					1.892777360084807
				],
				[
					1.656180190074224,
					3.785554720169614
				],
				[
					2.3659717001060017,
					3.548957550159031
				],
				[
					3.312360380148448,
					0.7097915100318062
				],
				[
					4.495346230201449,
					-0.7097915100318062
				],
				[
					4.968540570222672,
					1.419583020063584
				],
				[
					4.968540570222672,
					4.022151890180197
				],
				[
					5.205137740233226,
					4.731943400212032
				],
				[
					5.441734910243781,
					4.49534623020142
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1789814829826355,
				0.178493469953537,
				0.11295605450868607,
				0.051208771765232086,
				0.08277343958616257,
				0.1809622198343277,
				0.2203666716814041,
				0.15203313529491425,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 895231731,
			"isDeleted": false,
			"id": "drLvgNazckv2OjN0KnL_Y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 628.7598680197741,
			"y": -295.9994981941156,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.205137740233226,
			"height": 5.914929250265033,
			"seed": 1679414631,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4731943400211094,
					0.9463886800423893
				],
				[
					-0.7097915100317778,
					1.8927773600847786
				],
				[
					-0.4731943400211094,
					3.0757632101377794
				],
				[
					1.656180190074224,
					4.022151890180197
				],
				[
					3.785554720169671,
					2.8391660401271963
				],
				[
					4.495346230201449,
					0.4731943400211662
				],
				[
					3.075763210137893,
					-1.8927773600848354
				],
				[
					0.7097915100318914,
					-1.656180190074224
				],
				[
					-0.2365971700105547,
					0.2365971700105831
				],
				[
					1.656180190074224,
					1.419583020063584
				],
				[
					2.129374530095447,
					1.419583020063584
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05036798119544983,
				0.07129129022359848,
				0.1302221119403839,
				0.1813270002603531,
				0.20499923825263977,
				0.18509957194328308,
				0.15191997587680817,
				0.12058813124895096,
				0.07726019620895386,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 2064922045,
			"isDeleted": false,
			"id": "jZ3_OYWCAqoxQw8mYACZE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 637.5139633101664,
			"y": -303.57060763445486,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7097915100317778,
			"height": 12.30305284055126,
			"seed": 562683399,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.9463886800424177
				],
				[
					0,
					-1.1829858500530008
				],
				[
					0.4731943400211094,
					1.4195830200636124
				],
				[
					0.7097915100317778,
					6.388123590286256
				],
				[
					0.4731943400211094,
					10.646872650477036
				],
				[
					0.2365971700105547,
					11.120066990498259
				],
				[
					0.2365971700105547,
					10.646872650477036
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0699010044336319,
				0.11129312217235565,
				0.15944592654705048,
				0.21638736128807068,
				0.2195800244808197,
				0.008862304501235485,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 398512275,
			"isDeleted": false,
			"id": "ONwV-GSgQBaHBeaneN77f",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 634.4382001000286,
			"y": -296.94588687415796,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.205137740233226,
			"height": 0.9463886800424177,
			"seed": 111783463,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.23659717001066838,
					0
				],
				[
					0.9463886800424461,
					0.2365971700105831
				],
				[
					1.656180190074224,
					0.47319434002119465
				],
				[
					4.968540570222672,
					0.9463886800424177
				],
				[
					5.205137740233226,
					0.9463886800424177
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08973999321460724,
				0.1803240031003952,
				0.11826245486736298,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 81,
			"versionNonce": 1574991389,
			"isDeleted": false,
			"id": "yiIdfefHF5SSi2o946GNO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 642.7191010503996,
			"y": -305.226787824529,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.6783320802544495,
			"height": 13.249441520593649,
			"seed": 1518956551,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.2365971700105547,
					0
				],
				[
					0.23659717001066838,
					2.3659717001060017
				],
				[
					1.1829858500530008,
					7.80770661034984
				],
				[
					0.9463886800424461,
					11.356664160508842
				],
				[
					0.7097915100318914,
					12.066455670540648
				],
				[
					0.7097915100318914,
					10.646872650477036
				],
				[
					2.129374530095447,
					8.044303780360451
				],
				[
					4.258749060190894,
					6.861317930307422
				],
				[
					5.20513774023334,
					8.280900950371034
				],
				[
					5.441734910243895,
					11.12006699049823
				],
				[
					4.968540570222672,
					13.249441520593649
				],
				[
					4.968540570222672,
					12.066455670540648
				],
				[
					4.968540570222672,
					11.829858500530065
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16202542185783386,
				0.23329666256904602,
				0.22737261652946472,
				0.19076299667358398,
				0.1631781905889511,
				0.14967943727970123,
				0.16731023788452148,
				0.21139287948608398,
				0.26098498702049255,
				0.2982960343360901,
				0.08197998255491257,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 1193231923,
			"isDeleted": false,
			"id": "sTLjsSHPVQ1S9gNkn8tT-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 651.4731963407919,
			"y": -295.5263038540944,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.914929250265004,
			"height": 5.914929250265004,
			"seed": 119961319,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.2365971700105547,
					0
				],
				[
					0.4731943400211094,
					-0.2365971700105831
				],
				[
					0.9463886800423325,
					-0.4731943400211662
				],
				[
					1.6561801900741102,
					-1.419583020063584
				],
				[
					1.4195830200635555,
					-3.0757632101377794
				],
				[
					-0.47319434002122307,
					-3.312360380148391
				],
				[
					-1.8927773600848923,
					-0.9463886800423893
				],
				[
					-0.9463886800424461,
					1.656180190074224
				],
				[
					1.4195830200635555,
					2.602568870116613
				],
				[
					3.785554720169557,
					1.1829858500530293
				],
				[
					4.022151890180112,
					0.9463886800424177
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07182897627353668,
				0.10819299519062042,
				0.20493200421333313,
				0.17506097257137299,
				0.1238999292254448,
				0.1936892718076706,
				0.3187180161476135,
				0.34324026107788086,
				0.008287963457405567,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 839232125,
			"isDeleted": false,
			"id": "hgzXG7iIuKkVLZ3Sw_Eau",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 655.9685425709933,
			"y": -298.36546989422163,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.571109440339114,
			"height": 6.151526420275644,
			"seed": 1092095879,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.2365971700105547,
					0.9463886800424177
				],
				[
					1.1829858500530008,
					4.258749060190809
				],
				[
					1.4195830200635555,
					6.151526420275644
				],
				[
					2.1293745300953333,
					5.914929250265033
				],
				[
					4.022151890180112,
					3.548957550159031
				],
				[
					6.624720760296782,
					2.36597170010603
				],
				[
					7.571109440339114,
					1.892777360084807
				],
				[
					7.571109440339114,
					1.892777360084807
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15378905832767487,
				0.19663672149181366,
				0.1911386102437973,
				0.18697208166122437,
				0.20562347769737244,
				0.20049402117729187,
				0.17075827717781067,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 442370003,
			"isDeleted": false,
			"id": "THCaW7xDG617OdeAHoOHU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 667.0886095614916,
			"y": -298.8386642342428,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.914929250265004,
			"height": 6.624720760296839,
			"seed": 59089607,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.47319434002122307,
					0
				],
				[
					-1.4195830200636692,
					0.23659717001061153
				],
				[
					-2.60256887011667,
					1.4195830200636124
				],
				[
					-1.4195830200636692,
					2.602568870116613
				],
				[
					0.7097915100317778,
					3.785554720169614
				],
				[
					1.4195830200635555,
					4.731943400212003
				],
				[
					-0.23659717001066838,
					5.678332080254421
				],
				[
					-3.075763210137893,
					6.624720760296839
				],
				[
					-4.495346230201449,
					6.388123590286227
				],
				[
					-4.495346230201449,
					6.151526420275616
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08490322530269623,
				0.16157843172550201,
				0.15872009098529816,
				0.15350015461444855,
				0.1529970020055771,
				0.22447292506694794,
				0.2465163916349411,
				0.08833972364664078,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 81,
			"versionNonce": 1212502749,
			"isDeleted": false,
			"id": "Y35tXhpZGQF2hYtSyPZ7X",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 462.3762606938002,
			"y": -239.39861651443843,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.559649168672706,
			"height": 10.559649168672735,
			"seed": 702910535,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.42238596674690143,
					0
				],
				[
					1.6895438669876057,
					0.8447719334938313
				],
				[
					5.4910175677097754,
					2.5343158004814654
				],
				[
					9.292491268431945,
					4.2238596674691
				],
				[
					10.559649168672706,
					4.646245634216001
				],
				[
					10.137263201925748,
					4.646245634216001
				],
				[
					8.870105301685044,
					4.2238596674691
				],
				[
					6.758175467950537,
					4.646245634216001
				],
				[
					3.3790877339752114,
					6.758175467950565
				],
				[
					1.6895438669876057,
					9.292491268432002
				],
				[
					1.6895438669876057,
					10.559649168672735
				],
				[
					2.95670176722831,
					10.559649168672735
				],
				[
					3.3790877339752114,
					10.559649168672735
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.20026397705078125,
				0.24782399833202362,
				0.22953970730304718,
				0.21165746450424194,
				0.16670361161231995,
				0.1594085991382599,
				0.19160225987434387,
				0.2479524165391922,
				0.274167001247406,
				0.22035738825798035,
				0.08675219863653183,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 81,
			"versionNonce": 1200854387,
			"isDeleted": false,
			"id": "sY4XY7MqzvuAWJ0ppaGcC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 482.2284011309049,
			"y": -239.82100248118533,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.292491268431945,
			"height": 16.05066673638254,
			"seed": 370745127,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.42238596674690143,
					1.2671579002407327
				],
				[
					2.5343158004814086,
					8.02533336819127
				],
				[
					2.5343158004814086,
					13.516350935901102
				],
				[
					2.111929833734507,
					14.783508836141806
				],
				[
					0.8447719334938029,
					13.093964969154172
				],
				[
					-1.2671579002407043,
					8.02533336819127
				],
				[
					0.8447719334938029,
					1.6895438669876341
				],
				[
					5.068631600962931,
					-1.2671579002407327
				],
				[
					7.180561434697438,
					-0.8447719334938313
				],
				[
					8.02533336819124,
					1.2671579002407327
				],
				[
					7.180561434697438,
					3.8014737007221697
				],
				[
					5.068631600962931,
					4.646245634216001
				],
				[
					5.068631600962931,
					4.2238596674691
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10848397761583328,
				0.15537410974502563,
				0.1806187778711319,
				0.16645248234272003,
				0.11424670368432999,
				0.07106100767850876,
				0.0469290167093277,
				0.09684155136346817,
				0.14220058917999268,
				0.16676296293735504,
				0.16606049239635468,
				0.04553753510117531,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1563488061,
			"isDeleted": false,
			"id": "ZSWQqYI-2K8WOq0lTE1t1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 491.9432783660838,
			"y": -240.66577441467916,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.913403534456734,
			"height": 6.758175467950565,
			"seed": 732645895,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4223859667469583,
					0
				],
				[
					0,
					2.111929833734564
				],
				[
					0.8447719334938029,
					5.068631600962931
				],
				[
					2.5343158004814654,
					0.8447719334938313
				],
				[
					4.646245634215973,
					-1.6895438669876341
				],
				[
					5.4910175677097754,
					-0.8447719334938029
				],
				[
					5.4910175677097754,
					-0.8447719334938029
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06038198992609978,
				0.15510544180870056,
				0.1471923291683197,
				0.11720861494541168,
				0.11696447432041168,
				0.018023589625954628,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 2114350867,
			"isDeleted": false,
			"id": "TW6MBaEKASza-oI1SYAd3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 498.27906786728744,
			"y": -239.82100248118533,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.223859667469128,
			"height": 8.02533336819127,
			"seed": 504470055,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.42238596674690143,
					-0.42238596674690143
				],
				[
					-0.8447719334938597,
					0
				],
				[
					-1.6895438669876626,
					2.1119298337345356
				],
				[
					-0.8447719334938597,
					4.2238596674691
				],
				[
					0.8447719334938029,
					4.646245634216001
				],
				[
					2.5343158004814654,
					2.1119298337345356
				],
				[
					2.111929833734564,
					-1.6895438669876341
				],
				[
					-0.42238596674690143,
					-3.3790877339752683
				],
				[
					-1.6895438669876626,
					-0.8447719334938313
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06302142143249512,
				0.08675213903188705,
				0.12353949248790741,
				0.13929876685142517,
				0.16489285230636597,
				0.15520785748958588,
				0.12789614498615265,
				0.07979024946689606,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 81,
			"versionNonce": 522846109,
			"isDeleted": false,
			"id": "FZKT59FOxaE14SH1sEdgk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 505.037243335238,
			"y": -250.80303761660497,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.758175467950537,
			"height": 15.628280769635637,
			"seed": 287697607,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.42238596674690143
				],
				[
					-0.42238596674690143,
					3.8014737007221697
				],
				[
					-0.42238596674690143,
					7.180561434697438
				],
				[
					-0.42238596674690143,
					11.404421102166538
				],
				[
					0.42238596674690143,
					11.404421102166538
				],
				[
					0.42238596674690143,
					10.982035135419636
				],
				[
					2.5343158004814654,
					10.559649168672735
				],
				[
					3.8014737007221697,
					12.67157900240727
				],
				[
					3.8014737007221697,
					14.783508836141806
				],
				[
					2.111929833734564,
					15.628280769635637
				],
				[
					-1.6895438669876057,
					14.783508836141806
				],
				[
					-2.956701767228367,
					12.67157900240727
				],
				[
					-2.5343158004814654,
					12.67157900240727
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09560650587081909,
				0.13127176463603973,
				0.16222482919692993,
				0.1189848929643631,
				0.10962793231010437,
				0.12658697366714478,
				0.1501898169517517,
				0.1746354103088379,
				0.19270114600658417,
				0.19791091978549957,
				0.07662567496299744,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 1076696243,
			"isDeleted": false,
			"id": "pnqEv-lGd9OUwhoP4WjRU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 523.622225872102,
			"y": -241.08816038142606,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.6029474014443394,
			"height": 7.180561434697466,
			"seed": 51235239,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.42238596674690143
				],
				[
					-0.42238596674690143,
					1.2671579002407327
				],
				[
					-0.8447719334938029,
					2.1119298337345356
				],
				[
					-0.8447719334938029,
					3.3790877339752683
				],
				[
					2.111929833734564,
					5.491017567709832
				],
				[
					5.491017567709832,
					3.801473700722198
				],
				[
					5.913403534456734,
					0.42238596674690143
				],
				[
					2.5343158004814654,
					-1.6895438669876341
				],
				[
					-0.8447719334938029,
					-0.42238596674690143
				],
				[
					-1.6895438669876057,
					3.3790877339752683
				],
				[
					-1.2671579002407043,
					3.801473700722198
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06790127605199814,
				0.09019149839878082,
				0.116029754281044,
				0.14865295588970184,
				0.1509275883436203,
				0.12763720750808716,
				0.10118041932582855,
				0.09707415848970413,
				0.015008575282990932,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 84,
			"versionNonce": 1952580605,
			"isDeleted": false,
			"id": "lMRQkeoDQ0RKieRD_gka6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 532.0699452070402,
			"y": -238.5538445809446,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.714877235178903,
			"height": 26.187929938308372,
			"seed": 1727851079,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8447719334938029,
					-0.42238596674692985
				],
				[
					2.5343158004814654,
					-1.6895438669876341
				],
				[
					8.02533336819124,
					-7.602947401444368
				],
				[
					8.8701053016851,
					-12.67157900240727
				],
				[
					7.6029474014443394,
					-15.205894802888736
				],
				[
					5.913403534456734,
					-14.783508836141834
				],
				[
					4.223859667469071,
					-11.826807068913467
				],
				[
					3.8014737007221697,
					-6.335789501203635
				],
				[
					5.913403534456734,
					0.8447719334938029
				],
				[
					6.335789501203635,
					6.758175467950537
				],
				[
					5.068631600962874,
					10.137263201925805
				],
				[
					2.956701767228367,
					10.982035135419636
				],
				[
					-0.42238596674690143,
					7.602947401444368
				],
				[
					-0.8447719334938029,
					4.646245634216001
				],
				[
					3.8014737007221697,
					2.1119298337345356
				],
				[
					4.646245634215973,
					1.6895438669876341
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11895318329334259,
				0.1886969953775406,
				0.23620648682117462,
				0.2028123140335083,
				0.1385810524225235,
				0.11879421770572662,
				0.10431631654500961,
				0.11020010709762573,
				0.12931625545024872,
				0.14974486827850342,
				0.16175460815429688,
				0.16307662427425385,
				0.12486816197633743,
				0.09918499737977982,
				0.02046273835003376,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 2108556883,
			"isDeleted": false,
			"id": "DiU8ccb600xPjW50JmGwK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 546.853454043182,
			"y": -241.51054634817297,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.335789501203635,
			"height": 8.02533336819127,
			"seed": 874567303,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.42238596674690143,
					0
				],
				[
					1.2671579002407043,
					-0.42238596674690143
				],
				[
					3.3790877339752683,
					-1.2671579002407327
				],
				[
					4.646245634215973,
					-2.956701767228367
				],
				[
					2.5343158004814086,
					-4.2238596674691
				],
				[
					-0.4223859667469583,
					-2.5343158004814654
				],
				[
					-1.6895438669876626,
					0.8447719334938029
				],
				[
					0,
					3.8014737007221697
				],
				[
					3.8014737007221697,
					2.534315800481437
				],
				[
					4.223859667469071,
					2.1119298337345356
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07962048053741455,
				0.12693798542022705,
				0.20197197794914246,
				0.18349771201610565,
				0.09761706739664078,
				0.11964605748653412,
				0.1973426789045334,
				0.23227807879447937,
				0.08561846613883972,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 14318685,
			"isDeleted": false,
			"id": "BHayWmhMOuIvgunapvOyA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 554.4564014446264,
			"y": -245.31202004889516,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.758175467950537,
			"height": 8.025333368191298,
			"seed": 1896424455,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.42238596674690143,
					0
				],
				[
					-0.42238596674690143,
					0.8447719334938313
				],
				[
					0,
					4.646245634216001
				],
				[
					0,
					8.025333368191298
				],
				[
					0.42238596674690143,
					7.602947401444368
				],
				[
					2.5343158004814654,
					3.801473700722198
				],
				[
					5.068631600962931,
					0.8447719334938313
				],
				[
					6.335789501203635,
					0
				],
				[
					6.335789501203635,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10053106397390366,
				0.15376535058021545,
				0.17245343327522278,
				0.16333776712417603,
				0.14636489748954773,
				0.14460159838199615,
				0.1276138871908188,
				0.007319732569158077,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1834992627,
			"isDeleted": false,
			"id": "DSGW76_MNAKfB0DOYe4N-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 560.79219094583,
			"y": -244.88963408214823,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.646245634216029,
			"height": 7.180561434697438,
			"seed": 1456117351,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.2671579002407043
				],
				[
					0,
					2.534315800481437
				],
				[
					0,
					3.8014737007221697
				],
				[
					0,
					5.913403534456705
				],
				[
					0,
					5.491017567709804
				],
				[
					2.111929833734564,
					1.6895438669876341
				],
				[
					4.223859667469071,
					-1.2671579002407327
				],
				[
					4.646245634216029,
					-1.2671579002407327
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.05415106192231178,
				0.10611004382371902,
				0.1138220801949501,
				0.10704028606414795,
				0.10962741076946259,
				0.04746389761567116,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1818552509,
			"isDeleted": false,
			"id": "Lc58vvG14neubRuwCcg_9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 567.5503664137805,
			"y": -243.62247618190753,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.4910175677097754,
			"height": 5.491017567709832,
			"seed": 1934037415,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.42238596674690143,
					0.42238596674692985
				],
				[
					-1.6895438669876057,
					1.6895438669876626
				],
				[
					-0.8447719334938029,
					3.3790877339752967
				],
				[
					1.6895438669876626,
					3.801473700722198
				],
				[
					3.8014737007221697,
					2.111929833734564
				],
				[
					3.8014737007221697,
					-0.42238596674690143
				],
				[
					1.6895438669876626,
					-1.6895438669876341
				],
				[
					-1.2671579002407043,
					0.8447719334938313
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08043060451745987,
				0.14920730888843536,
				0.1900341808795929,
				0.20405313372612,
				0.14693590998649597,
				0.06716582924127579,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 659082643,
			"isDeleted": false,
			"id": "fP2D6zUHBsKW1rcx8-MwL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 573.8861559149841,
			"y": -244.88963408214823,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.602947401444396,
			"height": 9.292491268432002,
			"seed": 1064546087,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.42238596674690143,
					4.223859667469071
				],
				[
					0.8447719334938597,
					8.02533336819127
				],
				[
					1.6895438669876626,
					6.335789501203635
				],
				[
					4.646245634216029,
					1.2671579002407043
				],
				[
					7.180561434697495,
					-1.2671579002407327
				],
				[
					7.602947401444396,
					-1.2671579002407327
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17552298307418823,
				0.20199081301689148,
				0.17381851375102997,
				0.16626693308353424,
				0.06367120146751404,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 1755498781,
			"isDeleted": false,
			"id": "k7nbr4u9YN-s59hWEkchf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 516.0192784706576,
			"y": -218.70170414383986,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.025333368191298,
			"height": 12.671579002407299,
			"seed": 839178279,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4223859667469583,
					0
				],
				[
					-0.4223859667469583,
					0.42238596674690143
				],
				[
					2.956701767228367,
					-0.42238596674692985
				],
				[
					6.758175467950537,
					-3.3790877339752967
				],
				[
					7.6029474014443394,
					-5.913403534456734
				],
				[
					6.758175467950537,
					-6.335789501203664
				],
				[
					5.4910175677097754,
					-3.801473700722198
				],
				[
					4.646245634215973,
					1.6895438669876341
				],
				[
					4.223859667469071,
					5.913403534456705
				],
				[
					5.4910175677097754,
					6.335789501203635
				],
				[
					5.913403534456734,
					5.913403534456705
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08886334300041199,
				0.18571698665618896,
				0.25962701439857483,
				0.2554682493209839,
				0.19091516733169556,
				0.15097537636756897,
				0.19016830623149872,
				0.25990375876426697,
				0.2792333960533142,
				0.0776936337351799,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 2124391219,
			"isDeleted": false,
			"id": "w4M2CQsGPMC04Qa_2NJrF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 528.6908574730649,
			"y": -219.5464760773337,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.758175467950537,
			"height": 1.2671579002407327,
			"seed": 477391047,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.42238596674690143,
					0.42238596674690143
				],
				[
					0,
					1.2671579002407327
				],
				[
					3.3790877339752683,
					1.2671579002407327
				],
				[
					6.335789501203635,
					0.8447719334938313
				],
				[
					6.335789501203635,
					0.8447719334938313
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.20569336414337158,
				0.263498991727829,
				0.1499967724084854,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1996856701,
			"isDeleted": false,
			"id": "TWR3PsY85NK_v_ap0Nyp6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 541.3624364754721,
			"y": -223.7703357448028,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.335789501203635,
			"height": 5.491017567709832,
			"seed": 558784167,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.42238596674692985
				],
				[
					3.8014737007221697,
					0.8447719334938313
				],
				[
					6.335789501203635,
					1.2671579002407327
				],
				[
					5.913403534456734,
					2.111929833734564
				],
				[
					2.956701767228367,
					4.2238596674691
				],
				[
					1.2671579002407043,
					5.491017567709832
				],
				[
					2.111929833734507,
					5.491017567709832
				],
				[
					2.5343158004814654,
					5.491017567709832
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1968259960412979,
				0.2766770124435425,
				0.2607404291629791,
				0.22892993688583374,
				0.28448036313056946,
				0.33968865871429443,
				0.11229141056537628,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 466273491,
			"isDeleted": false,
			"id": "Cz9irRVa_1NbNBCfsI3Po",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 553.1892435443856,
			"y": -224.1927217115497,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.913403534456734,
			"height": 10.982035135419636,
			"seed": 2025425383,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4223859667469583,
					0
				],
				[
					-1.6895438669876626,
					2.1119298337345356
				],
				[
					-1.2671579002407611,
					7.602947401444368
				],
				[
					0.8447719334938029,
					8.8701053016851
				],
				[
					3.8014737007221697,
					6.335789501203635
				],
				[
					4.223859667469071,
					1.2671579002407327
				],
				[
					2.111929833734507,
					-2.1119298337345356
				],
				[
					-0.8447719334938597,
					-1.2671579002407327
				],
				[
					-1.2671579002407611,
					1.6895438669876341
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11587020754814148,
				0.204165980219841,
				0.22168976068496704,
				0.20125000178813934,
				0.18624866008758545,
				0.17847393453121185,
				0.12428906559944153,
				0.03721194341778755,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1859053021,
			"isDeleted": false,
			"id": "VKhUGEYWqpoGH-Dz9UZMT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 568.3951383472744,
			"y": -232.21805507974096,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.6895438669876057,
			"height": 18.162596570117103,
			"seed": 79446663,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.42238596674690143
				],
				[
					0,
					0.8447719334938029
				],
				[
					0,
					3.3790877339752683
				],
				[
					0.8447719334938029,
					12.67157900240727
				],
				[
					1.2671579002407043,
					18.162596570117103
				],
				[
					1.6895438669876057,
					18.162596570117103
				],
				[
					1.6895438669876057,
					17.740210603370173
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1445319801568985,
				0.19679397344589233,
				0.32506200671195984,
				0.3640735447406769,
				0.14420968294143677,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1449177715,
			"isDeleted": false,
			"id": "4fGmQJ52ralAzmken0xj2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 580.6443313829348,
			"y": -223.7703357448028,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.8701053016851,
			"height": 10.982035135419636,
			"seed": 1486815911,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.42238596674690143,
					0.42238596674692985
				],
				[
					-0.8447719334938029,
					2.111929833734564
				],
				[
					1.2671579002407611,
					5.913403534456734
				],
				[
					5.491017567709832,
					6.758175467950565
				],
				[
					8.025333368191298,
					3.801473700722198
				],
				[
					8.025333368191298,
					-0.8447719334938029
				],
				[
					5.068631600962931,
					-4.223859667469071
				],
				[
					1.2671579002407611,
					-2.956701767228367
				],
				[
					2.5343158004814654,
					0.8447719334938313
				],
				[
					3.379087733975325,
					0.8447719334938313
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13863399624824524,
				0.23277398943901062,
				0.2827000021934509,
				0.277146577835083,
				0.23695312440395355,
				0.19579143822193146,
				0.15816693007946014,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1125130813,
			"isDeleted": false,
			"id": "UmZ2BUnBi96DZ74IwyK4_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 595.4278402190765,
			"y": -223.34794977805586,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.180561434697495,
			"height": 0.42238596674692985,
			"seed": 562700327,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.42238596674692985
				],
				[
					0.42238596674690143,
					-0.42238596674692985
				],
				[
					2.956701767228367,
					-0.42238596674692985
				],
				[
					5.068631600962931,
					-0.42238596674692985
				],
				[
					6.758175467950537,
					-0.42238596674692985
				],
				[
					7.180561434697495,
					-0.42238596674692985
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11499636620283127,
				0.20386792719364166,
				0.31523600220680237,
				0.31197601556777954,
				0.0712113305926323,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1328016403,
			"isDeleted": false,
			"id": "gS7VSy8L7GIs_VS_M-s22",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 609.3665771217245,
			"y": -227.14942347877806,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.913403534456847,
			"height": 6.335789501203635,
			"seed": 836389159,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4223859667470151,
					0.42238596674690143
				],
				[
					2.111929833734621,
					0.8447719334938313
				],
				[
					5.068631600962931,
					1.6895438669876341
				],
				[
					5.913403534456847,
					1.6895438669876341
				],
				[
					3.379087733975325,
					3.3790877339752683
				],
				[
					0.4223859667470151,
					5.491017567709832
				],
				[
					2.111929833734621,
					6.335789501203635
				],
				[
					2.5343158004815223,
					6.335789501203635
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1466199904680252,
				0.2144320011138916,
				0.22947774827480316,
				0.22806420922279358,
				0.2962741553783417,
				0.12678571045398712,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 145412765,
			"isDeleted": false,
			"id": "jQt6a3Iya5t9Ntr_w0JIo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 622.4605420908788,
			"y": -230.10612524600643,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2671579002405906,
			"height": 9.292491268432002,
			"seed": 1113216103,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.42238596674690143
				],
				[
					0.42238596674678774,
					1.6895438669876341
				],
				[
					0.8447719334938029,
					6.335789501203635
				],
				[
					1.2671579002405906,
					9.292491268432002
				],
				[
					1.2671579002405906,
					9.292491268432002
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11296597123146057,
				0.22573450207710266,
				0.31199198961257935,
				0.13217850029468536,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 1243017651,
			"isDeleted": false,
			"id": "txDQ5DPaR7orvXtHttOlW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 424.3615236865783,
			"y": -254.18212535058024,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.05066673638254,
			"height": 18.584982536863976,
			"seed": 283090503,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4223859667469583,
					-0.42238596674690143
				],
				[
					3.3790877339752683,
					0.42238596674690143
				],
				[
					6.758175467950593,
					3.8014737007221697
				],
				[
					7.180561434697495,
					7.180561434697438
				],
				[
					5.491017567709832,
					10.982035135419636
				],
				[
					5.068631600962931,
					14.783508836141806
				],
				[
					7.602947401444396,
					17.740210603370173
				],
				[
					10.982035135419608,
					18.162596570117074
				],
				[
					13.51635093590113,
					17.31782463662327
				],
				[
					15.628280769635637,
					16.89543866987637
				],
				[
					16.05066673638254,
					17.31782463662327
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09448287636041641,
				0.20042797923088074,
				0.24026401340961456,
				0.2362789660692215,
				0.24315905570983887,
				0.27990010380744934,
				0.31830474734306335,
				0.32460615038871765,
				0.3022216260433197,
				0.05335796996951103,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 1011906301,
			"isDeleted": false,
			"id": "b3oClk_kIF0lb2MBlKyCB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 448.43752379115216,
			"y": -238.5538445809446,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.758175467950593,
			"height": 7.180561434697438,
			"seed": 1837316839,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4223859667469583,
					0
				],
				[
					-0.4223859667469583,
					0.42238596674690143
				],
				[
					2.111929833734564,
					2.1119298337345356
				],
				[
					5.068631600962874,
					3.8014737007221697
				],
				[
					6.335789501203635,
					4.646245634216001
				],
				[
					4.646245634215973,
					5.068631600962902
				],
				[
					2.5343158004814654,
					5.913403534456734
				],
				[
					0.42238596674690143,
					6.758175467950537
				],
				[
					0,
					6.758175467950537
				],
				[
					1.6895438669876626,
					7.180561434697438
				],
				[
					1.6895438669876626,
					7.180561434697438
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0900493785738945,
				0.24500997364521027,
				0.32799002528190613,
				0.3315899074077606,
				0.3053867220878601,
				0.32460758090019226,
				0.3487495481967926,
				0.3913927674293518,
				0.3461087644100189,
				0.13001935184001923,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1213481811,
			"isDeleted": false,
			"id": "Gzj_cXagxi6WQC9_FzbUy",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 514.4134130304002,
			"y": -328.5083062867026,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.744167183795412,
			"height": 14.109613667773516,
			"seed": 1198936967,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.45514882799261613,
					-1.8205953119707772
				],
				[
					1.820595311970692,
					-3.6411906239415543
				],
				[
					8.192678903868455,
					-9.558125387846559
				],
				[
					11.378720699817336,
					-12.74416718379544
				],
				[
					12.744167183795412,
					-13.654464839780815
				],
				[
					12.744167183795412,
					-14.109613667773516
				],
				[
					12.744167183795412,
					-14.109613667773516
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07295998930931091,
				0.07897280901670456,
				0.17847873270511627,
				0.21456067264080048,
				0.22386550903320312,
				0.17546594142913818,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1216515933,
			"isDeleted": false,
			"id": "2wT9F8QPPRx63oIxKM6eZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 530.7987708381371,
			"y": -349.44515237436644,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.372083591897649,
			"height": 7.28238124788308,
			"seed": 1747841959,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.45514882799261613,
					0
				],
				[
					0.9102976559854596,
					-0.4551488279927014
				],
				[
					4.096339451934227,
					-1.8205953119707772
				],
				[
					5.916934763905033,
					-2.27574413996345
				],
				[
					5.006637107919687,
					0.9102976559853744
				],
				[
					3.641190623941611,
					4.551488279926929
				],
				[
					3.641190623941611,
					5.00663710791963
				],
				[
					4.096339451934227,
					4.551488279926929
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06453555077314377,
				0.20463000237941742,
				0.22693298757076263,
				0.20926013588905334,
				0.22799664735794067,
				0.28390616178512573,
				0.14159753918647766,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 81,
			"versionNonce": 1647730931,
			"isDeleted": false,
			"id": "ML-OX2K6J-5DK51hf0JtL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 536.7157056020421,
			"y": -361.7341707301692,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.192678903868568,
			"height": 7.737530075875782,
			"seed": 252894951,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.4551488279927298
				],
				[
					-0.4551488279927298,
					-1.3654464839780758
				],
				[
					0,
					-1.3654464839780758
				],
				[
					1.3654464839780758,
					1.8205953119707488
				],
				[
					2.2757441399635354,
					5.00663710791963
				],
				[
					2.7308929679561516,
					5.461785935912303
				],
				[
					3.1860417959488814,
					2.7308929679561516
				],
				[
					5.006637107919687,
					-0.4551488279927298
				],
				[
					7.282381247883109,
					-2.2757441399634786
				],
				[
					7.7375300758758385,
					0
				],
				[
					7.7375300758758385,
					4.096339451934227
				],
				[
					7.282381247883109,
					4.096339451934227
				],
				[
					7.282381247883109,
					3.6411906239415543
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08945635706186295,
				0.13887222111225128,
				0.16782251000404358,
				0.14792414009571075,
				0.10864218324422836,
				0.09209149330854416,
				0.08802960067987442,
				0.11847372353076935,
				0.15457116067409515,
				0.17593474686145782,
				0.025372039526700974,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 1267899325,
			"isDeleted": false,
			"id": "oCvZ5Vb0fXQaAKHx5FdYY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 548.5495751298522,
			"y": -361.2790219021765,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.006637107919573,
			"height": 6.827232419890436,
			"seed": 1653244359,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.910297655985346,
					0.4551488279927014
				],
				[
					-1.3654464839780758,
					1.8205953119707772
				],
				[
					-1.3654464839780758,
					3.1860417959488814
				],
				[
					0,
					4.551488279926957
				],
				[
					2.2757441399634217,
					3.1860417959488814
				],
				[
					3.6411906239414975,
					0
				],
				[
					2.2757441399634217,
					-2.2757441399634786
				],
				[
					-0.4551488279927298,
					-1.8205953119707488
				],
				[
					-1.3654464839780758,
					2.2757441399634786
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0738874226808548,
				0.11238900572061539,
				0.11747186630964279,
				0.122267946600914,
				0.11847155541181564,
				0.12382235378026962,
				0.11674163490533829,
				0.01325207483023405,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1631832723,
			"isDeleted": false,
			"id": "L8Mvp_9FAmYq3uSgkE0Vm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 554.9216587217498,
			"y": -363.09961721414726,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3654464839780758,
			"height": 5.461785935912303,
			"seed": 535064167,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.455148827992673
				],
				[
					-0.45514882799261613,
					1.3654464839780758
				],
				[
					0,
					4.096339451934227
				],
				[
					0.4551488279927298,
					5.461785935912303
				],
				[
					0.9102976559854596,
					5.461785935912303
				],
				[
					0.9102976559854596,
					5.00663710791963
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12098999321460724,
				0.16483700275421143,
				0.15581558644771576,
				0.024096496403217316,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 497163293,
			"isDeleted": false,
			"id": "eSsHr-CFlgUP0_3KlMcIP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 556.287105205728,
			"y": -366.7408078380888,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.9102976559854596,
			"height": 0.455148827992673,
			"seed": 1381128039,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4551488279927298,
					0
				],
				[
					-0.9102976559854596,
					0
				],
				[
					-0.9102976559854596,
					0.455148827992673
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09729599207639694,
				0.12462320178747177,
				0.0660952478647232,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 439550003,
			"isDeleted": false,
			"id": "EdN-yu4lkqiDkFlQ3jSVb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 562.6591887976257,
			"y": -365.37536135411074,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.551488279926957,
			"height": 8.192678903868483,
			"seed": 730399047,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4551488279927298,
					0
				],
				[
					-0.910297655985346,
					0.455148827992673
				],
				[
					-1.3654464839780758,
					0.9102976559853744
				],
				[
					-0.910297655985346,
					3.1860417959488245
				],
				[
					0.4551488279927298,
					5.9169347639050045
				],
				[
					0.4551488279927298,
					7.737530075875782
				],
				[
					-1.3654464839780758,
					8.192678903868483
				],
				[
					-4.096339451934227,
					8.192678903868483
				],
				[
					-3.6411906239414975,
					7.282381247883109
				],
				[
					-3.1860417959488814,
					7.282381247883109
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06410952657461166,
				0.10109420865774155,
				0.10540704429149628,
				0.09616247564554214,
				0.10942312330007553,
				0.14147305488586426,
				0.13990329205989838,
				0.044470611959695816,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 379752573,
			"isDeleted": false,
			"id": "Gdfov9M6lTuarKCnNEOgQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 568.5761235615307,
			"y": -362.1893195581619,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.46842304383199,
			"height": 7.737530075875782,
			"seed": 1193225927,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.910297655985346,
					-0.455148827992673
				],
				[
					2.7308929679561516,
					-0.910297655985346
				],
				[
					3.1860417959488814,
					-2.7308929679561516
				],
				[
					1.3654464839780758,
					-3.1860417959488245
				],
				[
					-1.8205953119708056,
					-0.910297655985346
				],
				[
					-1.3654464839780758,
					2.73089296795618
				],
				[
					2.2757441399634217,
					4.551488279926957
				],
				[
					8.192678903868455,
					2.73089296795618
				],
				[
					8.647827731861184,
					2.2757441399634786
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14722000062465668,
				0.22482599318027496,
				0.20486892759799957,
				0.12645593285560608,
				0.14928101003170013,
				0.25030094385147095,
				0.2719569206237793,
				0.06815719604492188,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 100,
			"versionNonce": 116031955,
			"isDeleted": false,
			"id": "4h3yqJZPxx962fkMbw94Q",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 354.9031502579802,
			"y": -110.17366465786164,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 21.134222572278418,
			"height": 25.977481911758872,
			"seed": 1235168073,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.4402963035891361
				],
				[
					0,
					-1.3208889107674082
				],
				[
					0,
					-2.6417778215348022
				],
				[
					0,
					-3.0820741251239383
				],
				[
					0.8805926071782437,
					0
				],
				[
					1.7611852143564874,
					10.567111286139195
				],
				[
					1.7611852143564874,
					19.813333661510995
				],
				[
					2.641777821534788,
					20.693926268689268
				],
				[
					3.0820741251239383,
					18.052148447154465
				],
				[
					2.2014815179456377,
					12.328296500495739
				],
				[
					1.320888910767394,
					5.723851946658726
				],
				[
					0,
					0
				],
				[
					-0.8805926071783006,
					-3.0820741251239383
				],
				[
					-2.2014815179456946,
					-4.402963035891332
				],
				[
					-2.2014815179456946,
					-4.843259339480468
				],
				[
					-2.2014815179456946,
					-5.2835556430696045
				],
				[
					0.44029630358909344,
					-5.2835556430696045
				],
				[
					7.04474085742612,
					-4.402963035891332
				],
				[
					13.208889107673997,
					-0.4402963035891361
				],
				[
					14.970074322030484,
					3.52237042871306
				],
				[
					13.64918541126309,
					5.723851946658726
				],
				[
					11.007407589728302,
					5.723851946658726
				],
				[
					10.126814982550059,
					4.843259339480468
				],
				[
					11.888000196906603,
					5.2835556430696045
				],
				[
					15.850666929208785,
					7.9253334646043925
				],
				[
					18.492444750743573,
					11.888000196906603
				],
				[
					18.932741054332723,
					14.970074322030527
				],
				[
					17.17155583997618,
					17.171555839976207
				],
				[
					12.328296500495696,
					18.4924447507436
				],
				[
					7.485037161015271,
					19.373037357921874
				],
				[
					7.925333464604364,
					17.171555839976207
				],
				[
					8.365629768193514,
					16.290963232797935
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.05021188408136368,
				0.07638885825872421,
				0.16184906661510468,
				0.195952907204628,
				0.20382466912269592,
				0.19206345081329346,
				0.1556619256734848,
				0.1316033899784088,
				0.11362896859645844,
				0.08785006403923035,
				0.08322207629680634,
				0.10127618163824081,
				0.12430087476968765,
				0.15496686100959778,
				0.1806698888540268,
				0.20118515193462372,
				0.2017446905374527,
				0.1837521344423294,
				0.15717779099941254,
				0.17275168001651764,
				0.17987573146820068,
				0.16160044074058533,
				0.15126843750476837,
				0.17384649813175201,
				0.1869240403175354,
				0.20026671886444092,
				0.25670382380485535,
				0.27715298533439636,
				0.2709178030490875,
				0.029109984636306763,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 341145821,
			"isDeleted": false,
			"id": "uuce6uN4W98W-JVUneYTM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 376.91796543743686,
			"y": -116.77810921169863,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.0820741251239383,
			"height": 24.656593000991464,
			"seed": 692472073,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4402963035891503,
					0
				],
				[
					-0.8805926071783006,
					0.8805926071782579
				],
				[
					0,
					7.485037161015256
				],
				[
					1.320888910767394,
					19.813333661510995
				],
				[
					2.2014815179456377,
					24.656593000991464
				],
				[
					2.2014815179456377,
					24.216296697402328
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07982479780912399,
				0.16254442930221558,
				0.17421823740005493,
				0.007326965220272541,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 545312627,
			"isDeleted": false,
			"id": "7s_RPaok3E174BQGLRt4f",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 382.6418173840956,
			"y": -99.1662570681333,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.04474085742612,
			"height": 9.2462223753718,
			"seed": 269873161,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4402963035891503,
					0.4402963035891361
				],
				[
					-1.7611852143565443,
					2.201481517945666
				],
				[
					-1.7611852143565443,
					5.2835556430696045
				],
				[
					0.8805926071782437,
					7.485037161015271
				],
				[
					3.962666732302182,
					5.7238519466587405
				],
				[
					5.283555643069576,
					1.3208889107674082
				],
				[
					2.2014815179456377,
					-1.76118521435653
				],
				[
					-1.320888910767394,
					-0.8805926071782579
				],
				[
					-0.8805926071783006,
					3.5223704287130744
				],
				[
					-0.4402963035891503,
					3.9626667323021962
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06800763309001923,
				0.13719677925109863,
				0.16129253804683685,
				0.1557844579219818,
				0.1558217704296112,
				0.14687711000442505,
				0.10019268840551376,
				0.006673858501017094,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1078744381,
			"isDeleted": false,
			"id": "2_HB5Lyiwb0LyypT3qJjJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 391.88803975946735,
			"y": -99.60655337172244,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.485037161015271,
			"height": 6.604444553837013,
			"seed": 1656375945,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.320888910767394,
					0.4402963035891361
				],
				[
					-2.2014815179456377,
					0.8805926071782721
				],
				[
					-3.0820741251238815,
					1.7611852143565443
				],
				[
					-3.962666732302182,
					4.402963035891332
				],
				[
					-1.7611852143564874,
					6.604444553837013
				],
				[
					3.0820741251239383,
					5.2835556430696045
				],
				[
					3.5223704287130886,
					4.843259339480468
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.03880148380994797,
				0.08599597215652466,
				0.1466199904680252,
				0.20850399136543274,
				0.22890399396419525,
				0.09457177668809891,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 81,
			"versionNonce": 2034002195,
			"isDeleted": false,
			"id": "Y2hArvNYtVfJRjiI6PqhL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 399.81337322407177,
			"y": -113.25573878298557,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.485037161015271,
			"height": 20.25362996510013,
			"seed": 775641193,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4402963035891503,
					-0.4402963035891361
				],
				[
					-0.8805926071782437,
					-1.320888910767394
				],
				[
					-0.8805926071782437,
					-0.4402963035891361
				],
				[
					-0.4402963035891503,
					4.843259339480468
				],
				[
					0,
					11.888000196906603
				],
				[
					-0.4402963035891503,
					18.052148447154465
				],
				[
					-0.4402963035891503,
					18.932741054332737
				],
				[
					0.4402963035891503,
					17.171555839976207
				],
				[
					1.7611852143565443,
					13.649185411263133
				],
				[
					4.402963035891332,
					10.126814982550073
				],
				[
					6.604444553837027,
					8.365629768193543
				],
				[
					6.604444553837027,
					9.686518678960937
				],
				[
					6.164148250247877,
					10.126814982550073
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05716998130083084,
				0.06773797422647476,
				0.18591000139713287,
				0.251910001039505,
				0.25018540024757385,
				0.14798223972320557,
				0.1160484030842781,
				0.1243317574262619,
				0.14762969315052032,
				0.15863458812236786,
				0.0650576800107956,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 367568285,
			"isDeleted": false,
			"id": "Fs4D8_YYGVGKTJvDPfb4N",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 401.5745584384283,
			"y": -98.72596076454417,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.402963035891332,
			"height": 3.9626667323021962,
			"seed": 620216201,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4402963035891503,
					0.8805926071782721
				],
				[
					0,
					2.201481517945666
				],
				[
					3.5223704287130317,
					3.9626667323021962
				],
				[
					3.962666732302182,
					3.9626667323021962
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0494999997317791,
				0.21238000690937042,
				0.09674417227506638,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 378785459,
			"isDeleted": false,
			"id": "bpXYQD6c60N9zodIWI7-l",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 409.49989190303273,
			"y": -98.28566446095503,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8805926071782437,
			"height": 5.723851946658726,
			"seed": 503235785,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4402963035891503,
					0.4402963035891361
				],
				[
					-0.4402963035891503,
					1.76118521435653
				],
				[
					-0.4402963035891503,
					4.402963035891332
				],
				[
					0.44029630358909344,
					5.723851946658726
				],
				[
					0.44029630358909344,
					5.723851946658726
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13821664452552795,
				0.15613208711147308,
				0.0364605113863945,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 677112317,
			"isDeleted": false,
			"id": "UaseoCuMqV7ZEyGASETFi",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 409.9401882066218,
			"y": -102.68862749684637,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.320888910767394,
			"height": 0.4402963035891361,
			"seed": 1251651817,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8805926071782437,
					-0.4402963035891361
				],
				[
					-1.320888910767394,
					-0.4402963035891361
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06803417950868607,
				0.039365265518426895,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 187531347,
			"isDeleted": false,
			"id": "WXTxtD2Sq4BVUJ-SbagR3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 413.02226233174576,
			"y": -97.40507185377678,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.843259339480483,
			"height": 6.6044445538369985,
			"seed": 315960873,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.44029630358912186
				],
				[
					0.4402963035891503,
					-0.44029630358912186
				],
				[
					1.320888910767394,
					0
				],
				[
					2.2014815179456946,
					0.8805926071782721
				],
				[
					3.0820741251239383,
					-0.44029630358912186
				],
				[
					3.962666732302182,
					-3.52237042871306
				],
				[
					3.962666732302182,
					-3.082074125123924
				],
				[
					3.962666732302182,
					0.8805926071782721
				],
				[
					4.402963035891332,
					3.0820741251239383
				],
				[
					4.843259339480483,
					3.0820741251239383
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10792797803878784,
				0.13960272073745728,
				0.1291690617799759,
				0.09000986069440842,
				0.04164138808846474,
				0.055352356284856796,
				0.18138998746871948,
				0.21760506927967072,
				0.050322938710451126,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 682074717,
			"isDeleted": false,
			"id": "ha0EkxSo5I-90TJ2D3wa5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 421.38789209993934,
			"y": -98.72596076454417,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.164148250247877,
			"height": 6.164148250247862,
			"seed": 1353799849,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4402963035891503,
					0.4402963035891361
				],
				[
					-1.3208889107674509,
					1.320888910767394
				],
				[
					-1.7611852143565443,
					3.0820741251239383
				],
				[
					0,
					3.9626667323021962
				],
				[
					3.0820741251238815,
					3.0820741251239383
				],
				[
					4.402963035891332,
					-0.4402963035891361
				],
				[
					2.2014815179456377,
					-2.201481517945666
				],
				[
					-0.4402963035891503,
					0.4402963035891361
				],
				[
					-0.8805926071783006,
					3.52237042871306
				],
				[
					-0.4402963035891503,
					3.52237042871306
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1129172071814537,
				0.14969277381896973,
				0.1479284018278122,
				0.16580352187156677,
				0.19640789926052094,
				0.21295206248760223,
				0.09024417400360107,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1356856819,
			"isDeleted": false,
			"id": "2Me1jwFq6IdPSNXf0fH-u",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 424.91026252865237,
			"y": -100.4871459789007,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.365629768193514,
			"height": 20.25362996510013,
			"seed": 1114751785,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8805926071782437,
					0.4402963035891361
				],
				[
					-1.320888910767394,
					1.320888910767394
				],
				[
					-0.8805926071782437,
					3.52237042871306
				],
				[
					0.8805926071783006,
					7.0447408574261345
				],
				[
					2.641777821534788,
					11.888000196906603
				],
				[
					1.320888910767394,
					17.171555839976193
				],
				[
					-2.2014815179456377,
					20.25362996510013
				],
				[
					-5.283555643069576,
					20.25362996510013
				],
				[
					-5.723851946658726,
					19.37303735792186
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07217898219823837,
				0.08498486131429672,
				0.1408519297838211,
				0.13643670082092285,
				0.14565542340278625,
				0.18266305327415466,
				0.20546108484268188,
				0.09515909105539322,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 85,
			"versionNonce": 731729597,
			"isDeleted": false,
			"id": "H2EnVA0v1wNBmg4moAuxW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 454.40124134951435,
			"y": -148.10438312611367,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.320608610045724,
			"height": 7.444755072146165,
			"seed": 1725247177,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.43792676894977944
				],
				[
					0,
					-0.8758535378995305
				],
				[
					0,
					-1.7517070757990894
				],
				[
					0,
					-2.189633844748869
				],
				[
					0,
					-0.43792676894977944
				],
				[
					0.8758535378995589,
					2.6275606136986482
				],
				[
					1.7517070757991178,
					3.503414151598207
				],
				[
					3.5034141515982355,
					0.43792676894977944
				],
				[
					3.9413409205479866,
					-1.7517070757990894
				],
				[
					3.5034141515982355,
					-0.8758535378995305
				],
				[
					3.0654873826484277,
					2.6275606136986482
				],
				[
					4.8171944584475455,
					5.2551212273972965
				],
				[
					6.568901534246606,
					4.817194458447517
				],
				[
					8.320608610045724,
					0.43792676894977944
				],
				[
					8.320608610045724,
					-2.189633844748869
				],
				[
					7.444755072146165,
					-2.189633844748869
				],
				[
					7.444755072146165,
					-1.7517070757990894
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.03108169510960579,
				0.063295379281044,
				0.1513134092092514,
				0.19456499814987183,
				0.19727081060409546,
				0.15264301002025604,
				0.11732476949691772,
				0.11147607117891312,
				0.12355447560548782,
				0.1462792605161667,
				0.16884884238243103,
				0.17526932060718536,
				0.17186285555362701,
				0.13277798891067505,
				0.03175555542111397,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 86,
			"versionNonce": 1655818131,
			"isDeleted": false,
			"id": "LUCTGMru35--vBMIM2fhg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 465.7873373422085,
			"y": -147.22852958821412,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.9481692237444,
			"height": 7.882681841095945,
			"seed": 1996711273,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.437926768949751,
					-0.43792676894977944
				],
				[
					1.31378030684931,
					-0.8758535378995589
				],
				[
					3.0654873826484277,
					-2.6275606136986482
				],
				[
					2.6275606136986767,
					-3.9413409205479866
				],
				[
					0,
					-3.0654873826484277
				],
				[
					-1.7517070757991178,
					0.43792676894977944
				],
				[
					-0.437926768949751,
					3.503414151598207
				],
				[
					3.0654873826484277,
					2.6275606136986482
				],
				[
					4.8171944584475455,
					0.43792676894977944
				],
				[
					4.379267689497738,
					0.8758535378995589
				],
				[
					3.9413409205479866,
					3.0654873826484277
				],
				[
					5.6930479963470475,
					3.941340920547958
				],
				[
					7.882681841095973,
					3.0654873826484277
				],
				[
					9.196462147945283,
					0
				],
				[
					8.320608610045724,
					-2.6275606136986482
				],
				[
					6.130974765296855,
					-2.6275606136986482
				],
				[
					3.5034141515981787,
					0.8758535378995589
				],
				[
					3.5034141515981787,
					1.31378030684931
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08433087170124054,
				0.1266390085220337,
				0.17451107501983643,
				0.16020368039608002,
				0.13140758872032166,
				0.14446331560611725,
				0.1729489415884018,
				0.1570761352777481,
				0.08366800099611282,
				0.06634518504142761,
				0.12456338852643967,
				0.1559494286775589,
				0.16608190536499023,
				0.1808938831090927,
				0.1910063773393631,
				0.16718970239162445,
				0.006619506981223822,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 803106589,
			"isDeleted": false,
			"id": "k8d3CCq8O_inkyhHmBluQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 474.1079459522542,
			"y": -145.03889574346525,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.31378030684931,
			"height": 0.43792676894977944,
			"seed": 1455519465,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.43792676894977944
				],
				[
					1.31378030684931,
					0.43792676894977944
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06624399125576019,
				0.023027649149298668,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 383343923,
			"isDeleted": false,
			"id": "w7_AOXbYOP5hZBcS8AmQU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 481.5527010244004,
			"y": -158.61462558090827,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.568901534246606,
			"height": 14.451583375342551,
			"seed": 11498537,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.437926768949751
				],
				[
					0,
					2.189633844748869
				],
				[
					0,
					9.634388916895062
				],
				[
					-0.437926768949751,
					14.0136566063928
				],
				[
					0.8758535378995589,
					10.072315685844814
				],
				[
					3.9413409205479866,
					5.2551212273972965
				],
				[
					6.130974765296855,
					3.503414151598207
				],
				[
					5.6930479963470475,
					4.817194458447517
				],
				[
					5.6930479963470475,
					5.2551212273972965
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08956115692853928,
				0.13369689881801605,
				0.13424429297447205,
				0.0856499969959259,
				0.1284025013446808,
				0.11593780666589737,
				0.012575073167681694,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1675395965,
			"isDeleted": false,
			"id": "cDJ5eOfPVAZI-66jzQAZt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 482.8664813312497,
			"y": -146.35267605031456,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.9413409205479866,
			"height": 2.6275606136986482,
			"seed": 186875849,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8758535378995305
				],
				[
					0.43792676894980787,
					2.189633844748869
				],
				[
					3.0654873826484277,
					2.6275606136986482
				],
				[
					3.9413409205479866,
					2.189633844748869
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10256988555192947,
				0.09850262105464935,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 951926483,
			"isDeleted": false,
			"id": "1QH4Hts-Kfcb6-c0jltvo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 492.93879701709454,
			"y": -148.54230989506345,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.444755072146165,
			"height": 7.882681841095945,
			"seed": 1257067785,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8758535378995589,
					-0.437926768949751
				],
				[
					1.751707075799061,
					-2.189633844748869
				],
				[
					0.8758535378995589,
					-3.0654873826483993
				],
				[
					-1.7517070757991178,
					-1.31378030684931
				],
				[
					-2.189633844748869,
					3.0654873826484277
				],
				[
					0,
					4.8171944584475455
				],
				[
					4.817194458447489,
					3.9413409205479866
				],
				[
					5.2551212273972965,
					3.503414151598207
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14876914024353027,
				0.155506893992424,
				0.11907418817281723,
				0.14870251715183258,
				0.2065238058567047,
				0.2149818390607834,
				0.031517792493104935,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 735644637,
			"isDeleted": false,
			"id": "99YDl8W4fQjZpO_qs6zSk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 499.0697717823914,
			"y": -149.41816343296298,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.444755072146165,
			"height": 5.2551212273972965,
			"seed": 1153846729,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.43792676894980787,
					0.43792676894977944
				],
				[
					-0.43792676894980787,
					1.7517070757990894
				],
				[
					0,
					3.5034141515981787
				],
				[
					1.31378030684931,
					4.817194458447517
				],
				[
					3.5034141515981787,
					2.189633844748869
				],
				[
					5.25512122739724,
					-0.43792676894977944
				],
				[
					6.1309747652967985,
					1.7517070757990894
				],
				[
					6.1309747652967985,
					4.817194458447517
				],
				[
					6.568901534246606,
					4.379267689497738
				],
				[
					7.006828303196357,
					3.941340920547958
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04327999800443649,
				0.11560799926519394,
				0.1517299860715866,
				0.12902098894119263,
				0.08452633768320084,
				0.08674304187297821,
				0.17299185693264008,
				0.1981944888830185,
				0.03260299563407898,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1660152947,
			"isDeleted": false,
			"id": "ynOG_JxXLxSiLmYhPBMvM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 508.70416069928643,
			"y": -148.54230989506345,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.875853537899502,
			"height": 4.8171944584475455,
			"seed": 985925705,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.437926768949751,
					1.7517070757991178
				],
				[
					0.437926768949751,
					3.503414151598207
				],
				[
					0.437926768949751,
					4.8171944584475455
				],
				[
					0.875853537899502,
					4.8171944584475455
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15999798476696014,
				0.12551215291023254,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1743095869,
			"isDeleted": false,
			"id": "ufcbsviibLD-6qQIhfLzA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 510.4558677750855,
			"y": -152.9215775845612,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.31378030684931,
			"height": 0,
			"seed": 263028105,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8758535378995589,
					0
				],
				[
					-1.31378030684931,
					0
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11443847417831421,
				0.013167999684810638,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 423880211,
			"isDeleted": false,
			"id": "6NjFGOL2elil32ILShZuX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 513.0834283887841,
			"y": -148.9802366640132,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.2551212273972965,
			"height": 5.6930479963470475,
			"seed": 550372041,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8758535378995305
				],
				[
					0,
					1.7517070757990894
				],
				[
					0,
					4.817194458447517
				],
				[
					1.31378030684931,
					5.6930479963470475
				],
				[
					3.9413409205479297,
					2.189633844748869
				],
				[
					5.2551212273972965,
					0.8758535378995305
				],
				[
					5.2551212273972965,
					2.6275606136986482
				],
				[
					4.817194458447489,
					4.817194458447517
				],
				[
					4.817194458447489,
					5.2551212273972965
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06787948310375214,
				0.1501091867685318,
				0.11833789199590683,
				0.06507831066846848,
				0.0793687105178833,
				0.1267976015806198,
				0.011473937891423702,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 2044950685,
			"isDeleted": false,
			"id": "Wx8HIwfhvvXuedvfPxk-c",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 520.9661102298801,
			"y": -146.79060281926434,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.2551212273972965,
			"height": 7.444755072146165,
			"seed": 1846309481,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8758535378995589,
					0.8758535378995305
				],
				[
					-0.8758535378995589,
					2.189633844748869
				],
				[
					0,
					4.379267689497738
				],
				[
					3.0654873826484277,
					3.0654873826484277
				],
				[
					3.9413409205479866,
					-0.8758535378995589
				],
				[
					2.6275606136986767,
					-3.0654873826484277
				],
				[
					-1.31378030684931,
					1.31378030684931
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.05238461121916771,
				0.15566498041152954,
				0.1623244285583496,
				0.16987167298793793,
				0.19568264484405518,
				0.020467467606067657,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 581151667,
			"isDeleted": false,
			"id": "AssuW_EPoJ9MIi0zZzhe5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 524.4695243814783,
			"y": -146.35267605031456,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.568901534246606,
			"height": 12.699876299543462,
			"seed": 1541662217,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.437926768949751
				],
				[
					0,
					1.31378030684931
				],
				[
					0.875853537899502,
					4.817194458447517
				],
				[
					1.751707075799061,
					9.196462147945255
				],
				[
					-0.43792676894980787,
					12.699876299543462
				],
				[
					-4.379267689497794,
					12.261949530593682
				],
				[
					-4.8171944584475455,
					11.824022761643903
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07592999190092087,
				0.07592999190092087,
				0.14287488162517548,
				0.19716018438339233,
				0.24118545651435852,
				0.08624698221683502,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 81,
			"versionNonce": 193223933,
			"isDeleted": false,
			"id": "4uPKHtW1GCK_fdq7HCZtQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 451.04478080887725,
			"y": -54.227940466728796,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.381316299402101,
			"height": 13.65757955928251,
			"seed": 824312809,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.4552526519760818
				],
				[
					0,
					-1.8210106079043271
				],
				[
					0,
					-3.6420212158086542
				],
				[
					0,
					-4.552526519760846
				],
				[
					0.9105053039521636,
					-3.6420212158086542
				],
				[
					2.276263259880352,
					1.3657579559282453
				],
				[
					2.7315159118564907,
					6.373537127665173
				],
				[
					2.7315159118564907,
					7.284042431617337
				],
				[
					2.276263259880352,
					4.552526519760846
				],
				[
					3.6420212158086542,
					0
				],
				[
					8.64980038754561,
					-5.9182844756890916
				],
				[
					10.926063647425963,
					-6.373537127665173
				],
				[
					11.381316299402101,
					-6.373537127665173
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.01176083367317915,
				0.017860230058431625,
				0.08506903052330017,
				0.19220998883247375,
				0.2107716053724289,
				0.18116290867328644,
				0.1550702154636383,
				0.12193911522626877,
				0.1576458364725113,
				0.19934500753879547,
				0.006836151238530874,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 590986579,
			"isDeleted": false,
			"id": "xHqEmccEsJ_ediEQfDi3m",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 456.0525599806141,
			"y": -53.31743516277663,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.1867685638326293,
			"height": 5.46303182371301,
			"seed": 1892080393,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4552526519760818
				],
				[
					0.4552526519761386,
					1.3657579559282453
				],
				[
					3.1867685638326293,
					5.007779171736928
				],
				[
					3.1867685638326293,
					5.46303182371301
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08388897776603699,
				0.14838799834251404,
				0.0742398053407669,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 340374877,
			"isDeleted": false,
			"id": "YT8oc74N_wqd50OwIJ3NU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 465.15761302013584,
			"y": -51.041171902896195,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3657579559281885,
			"height": 5.0077791717369,
			"seed": 1302544457,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4552526519760818
				],
				[
					0.45525265197602494,
					1.8210106079043271
				],
				[
					1.3657579559281885,
					4.552526519760818
				],
				[
					1.3657579559281885,
					5.0077791717369
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12759798765182495,
				0.1706799864768982,
				0.031663209199905396,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1985780467,
			"isDeleted": false,
			"id": "4jLybaJOLLu3RXoGCgVHf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 466.52337097606403,
			"y": -58.32521433451356,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.9105053039521636,
			"height": 2.2762632598804373,
			"seed": 1875031433,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.45525265197602494,
					0.910505303952192
				],
				[
					-0.9105053039521636,
					2.2762632598804373
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11104598641395569,
				0.1389588564634323,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 528810429,
			"isDeleted": false,
			"id": "hYyW4vslKSfjaU0Y5JNE4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 472.8969081037293,
			"y": -63.33299350625046,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.8210106079043271,
			"height": 17.299600775091164,
			"seed": 1838758601,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4552526519760818
				],
				[
					0,
					3.6420212158086542
				],
				[
					0.9105053039521636,
					12.291821603354265
				],
				[
					0.9105053039521636,
					17.299600775091164
				],
				[
					1.8210106079043271,
					15.023337515210756
				],
				[
					1.8210106079043271,
					14.112832211258592
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1472260057926178,
				0.19241997599601746,
				0.17435809969902039,
				0.006308807525783777,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1217578131,
			"isDeleted": false,
			"id": "T0uunTPy0fADRCR1YlHzH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 477.4494346234901,
			"y": -67.43026737403522,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3657579559281885,
			"height": 21.39687464287593,
			"seed": 1091248585,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					2.7315159118564907
				],
				[
					0.45525265197602494,
					10.92606364742602
				],
				[
					0.45525265197602494,
					19.12061138299552
				],
				[
					1.3657579559281885,
					21.39687464287593
				],
				[
					1.3657579559281885,
					21.39687464287593
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.23688800632953644,
				0.2914150059223175,
				0.09182992577552795,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1381483037,
			"isDeleted": false,
			"id": "dqfJdvMK8mQiBfyzgJzfm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 485.6439823590596,
			"y": -53.31743516277663,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.45525265197602494,
			"height": 6.373537127665173,
			"seed": 631352809,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.45525265197602494,
					0.4552526519760818
				],
				[
					-0.45525265197602494,
					0.9105053039521636
				],
				[
					0,
					5.9182844756890916
				],
				[
					0,
					6.373537127665173
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1679176688194275,
				0.14548349380493164,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1905441331,
			"isDeleted": false,
			"id": "TUhGm5IJfCkB4WubD2FbR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 486.55448766301174,
			"y": -57.41470903056137,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.9105053039521636,
			"height": 0,
			"seed": 1035627305,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.45525265197602494,
					0
				],
				[
					-0.9105053039521636,
					0
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1110759899020195,
				0.043953828513622284,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 833844861,
			"isDeleted": false,
			"id": "J2Q1jJ4cIF4RnsQeqIzH5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 492.0175194867247,
			"y": -53.31743516277663,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.642021215808768,
			"height": 6.373537127665173,
			"seed": 133445737,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.9105053039521636
				],
				[
					0,
					1.3657579559282453
				],
				[
					0,
					2.2762632598804373
				],
				[
					0.4552526519761386,
					3.6420212158086827
				],
				[
					1.3657579559283022,
					2.2762632598804373
				],
				[
					2.2762632598804657,
					-0.4552526519760818
				],
				[
					3.1867685638326293,
					0
				],
				[
					3.642021215808768,
					4.097273867784764
				],
				[
					3.642021215808768,
					5.9182844756890916
				],
				[
					3.642021215808768,
					5.9182844756890916
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08235897868871689,
				0.10271600633859634,
				0.13362596929073334,
				0.14827169477939606,
				0.09145956486463547,
				0.10667135566473007,
				0.2152896374464035,
				0.18241381645202637,
				0.057297851890325546,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 239270867,
			"isDeleted": false,
			"id": "25WH8O3msAAyIuYSHRMW3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 498.39105661439,
			"y": -52.86218251080055,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.552526519760818,
			"height": 5.46303182371301,
			"seed": 194708201,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4552526519760818
				],
				[
					-0.4552526519761386,
					0.9105053039521636
				],
				[
					-0.4552526519761386,
					1.3657579559282738
				],
				[
					0.45525265197602494,
					4.097273867784764
				],
				[
					3.1867685638325156,
					5.007779171736928
				],
				[
					4.097273867784679,
					1.8210106079043555
				],
				[
					3.6420212158086542,
					-0.4552526519760818
				],
				[
					0.9105053039521636,
					-0.4552526519760818
				],
				[
					0,
					2.2762632598804373
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09569375962018967,
				0.1438779979944229,
				0.22825799882411957,
				0.24502280354499817,
				0.20351116359233856,
				0.2228020280599594,
				0.1771525889635086,
				0.01167221087962389,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 676962013,
			"isDeleted": false,
			"id": "Hkb1OWc2wAuO50Rlc4-TJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 502.48833048217466,
			"y": -53.772687814752715,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.8210106079043271,
			"height": 13.65757955928251,
			"seed": 448952393,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.9105053039521636
				],
				[
					0,
					1.8210106079043271
				],
				[
					0.9105053039521636,
					5.007779171736928
				],
				[
					1.8210106079043271,
					10.015558343473856
				],
				[
					0.4552526519761386,
					13.65757955928251
				],
				[
					0,
					13.202326907306428
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10815399140119553,
				0.16774798929691315,
				0.2138388305902481,
				0.11004620045423508,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 1522141555,
			"isDeleted": false,
			"id": "M717mt8H87OxhEaqj_k2J",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 469.53606455223303,
			"y": -185.20978197799278,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.426973329132352,
			"height": 11.469670662045644,
			"seed": 1795088201,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5213486664566176
				],
				[
					3.6494406651962663,
					3.1280919987397056
				],
				[
					8.862927329762556,
					4.692137998109558
				],
				[
					10.426973329132352,
					5.213486664566176
				],
				[
					8.862927329762556,
					5.734835331022822
				],
				[
					6.777532663935972,
					6.777532663936057
				],
				[
					3.6494406651962663,
					8.862927329762528
				],
				[
					1.0426973329132352,
					10.948321995589026
				],
				[
					1.0426973329132352,
					11.469670662045644
				],
				[
					2.0853946658264704,
					9.384275996219145
				],
				[
					2.606743332283031,
					9.384275996219145
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15820781886577606,
				0.20891283452510834,
				0.19625912606716156,
				0.17641763389110565,
				0.19371697306632996,
				0.2156786173582077,
				0.2735876441001892,
				0.3122708797454834,
				0.2978793978691101,
				0.10013274848461151,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1289468733,
			"isDeleted": false,
			"id": "KbYjgmcT5wcTWqiwiNrb6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 468.4933672193198,
			"y": -156.01425665642205,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.6494406651962663,
			"height": 12.512367994958879,
			"seed": 1608661161,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5213486664565607,
					-2.085394665826499
				],
				[
					2.0853946658264704,
					-6.777532663936057
				],
				[
					3.1280919987397056,
					-11.469670662045644
				],
				[
					3.6494406651962663,
					-12.512367994958879
				],
				[
					3.1280919987397056,
					-11.991019328502261
				],
				[
					2.606743332283031,
					-9.905624662675791
				],
				[
					2.0853946658264704,
					-9.905624662675791
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19653399288654327,
				0.23077048361301422,
				0.23261773586273193,
				0.2474530041217804,
				0.21770596504211426,
				0.03965561091899872,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1279157011,
			"isDeleted": false,
			"id": "7YYbptTfmCyBdSHrwUeSc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 474.22820255034253,
			"y": -194.59405797421195,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.7775326639360856,
			"height": 11.991019328502276,
			"seed": 1058824841,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5213486664565607,
					0
				],
				[
					-1.0426973329132352,
					-0.5213486664566318
				],
				[
					0,
					-2.606743332283102
				],
				[
					1.5640459993699096,
					-5.213486664566204
				],
				[
					4.170789331653054,
					-8.862927329762556
				],
				[
					5.73483533102285,
					-10.948321995589026
				],
				[
					5.21348666456629,
					-11.469670662045644
				],
				[
					4.170789331653054,
					-11.991019328502276
				],
				[
					3.64944066519638,
					-11.991019328502276
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.02867947332561016,
				0.134443998336792,
				0.19119000434875488,
				0.21647708117961884,
				0.21754248440265656,
				0.23835192620754242,
				0.20199847221374512,
				0.017472412437200546,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1738230685,
			"isDeleted": false,
			"id": "rHQc3MEnMhqni-t10YyXv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 476.313597216169,
			"y": -209.71316930145395,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.38427599621923,
			"height": 7.8202299968493065,
			"seed": 445524521,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5213486664566744,
					0
				],
				[
					1.0426973329132352,
					-0.5213486664566176
				],
				[
					3.64944066519638,
					-2.606743332283102
				],
				[
					7.29888133039276,
					-5.213486664566204
				],
				[
					8.341578663305995,
					-5.213486664566204
				],
				[
					8.341578663305995,
					-3.6494406651963374
				],
				[
					8.341578663305995,
					0
				],
				[
					9.38427599621923,
					2.606743332283102
				],
				[
					9.38427599621923,
					2.606743332283102
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06828998029232025,
				0.11934716999530792,
				0.11977377533912659,
				0.12570711970329285,
				0.16067355871200562,
				0.21743926405906677,
				0.10027115046977997,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1799784627,
			"isDeleted": false,
			"id": "Blk8WgdIkUZ0bcXIuLtie",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 428.00996874517756,
			"y": -107.73082578617081,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.068725846678035,
			"height": 15.682471016013693,
			"seed": 408942025,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5227490338671146
				],
				[
					-0.5227490338671146,
					-1.0454980677342292
				],
				[
					-0.5227490338671146,
					-1.5682471016013722
				],
				[
					2.613745169335573,
					-4.704741304804088
				],
				[
					8.363984541873947,
					-10.977729711209577
				],
				[
					11.500478745076691,
					-15.15972198214655
				],
				[
					12.023227778943863,
					-15.682471016013693
				],
				[
					12.54597681281092,
					-15.15972198214655
				],
				[
					12.54597681281092,
					-14.636972948279436
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09586083889007568,
				0.13761068880558014,
				0.18412365019321442,
				0.21248669922351837,
				0.21837671101093292,
				0.1796850860118866,
				0.04064157232642174,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 952750077,
			"isDeleted": false,
			"id": "zPlPs8HK3Tw_QdupyxUZG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 442.1241926595899,
			"y": -127.59528907312148,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.886733575741118,
			"height": 7.318486474139718,
			"seed": 756827497,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5227490338671714,
					0
				],
				[
					1.0454980677342292,
					-1.0454980677342576
				],
				[
					5.750239372538317,
					-3.1364942032027443
				],
				[
					8.363984541873947,
					-3.1364942032027443
				],
				[
					7.318486474139718,
					-0.5227490338671146
				],
				[
					4.704741304804088,
					3.1364942032027443
				],
				[
					4.1819922709369735,
					4.1819922709369735
				],
				[
					4.704741304804088,
					4.1819922709369735
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.2042199969291687,
				0.23589688539505005,
				0.20447024703025818,
				0.2500176727771759,
				0.2894248068332672,
				0.06871530413627625,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1836644947,
			"isDeleted": false,
			"id": "pg6XJDTyVXuIH5RflEp-m",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 434.80570618545016,
			"y": -83.68437022828314,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.2274903386712595,
			"height": 7.841235508006832,
			"seed": 22431273,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5227490338671146
				],
				[
					2.6137451693356297,
					4.1819922709369735
				],
				[
					4.704741304804088,
					7.841235508006832
				],
				[
					5.2274903386712595,
					7.841235508006832
				],
				[
					5.2274903386712595,
					7.841235508006832
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.18462799489498138,
				0.2477639764547348,
				0.2284497618675232,
				0.11874526739120483,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 2120796253,
			"isDeleted": false,
			"id": "CkdC8iegJDuSi5YDUl8RH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 443.6924397611913,
			"y": -78.45687988961191,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.79573744027266,
			"height": 7.841235508006832,
			"seed": 1091796553,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5227490338671714,
					0.5227490338671146
				],
				[
					-0.5227490338671714,
					2.0909961354684867
				],
				[
					1.0454980677342292,
					4.7047413048041165
				],
				[
					3.659243237069859,
					6.795737440272603
				],
				[
					4.704741304804088,
					7.841235508006832
				],
				[
					4.181992270936917,
					7.841235508006832
				],
				[
					0.5227490338670577,
					6.272988406405489
				],
				[
					-2.090996135468572,
					5.750239372538346
				],
				[
					-1.5682471016014006,
					6.272988406405489
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11897100508213043,
				0.1604350209236145,
				0.15118682384490967,
				0.1365610659122467,
				0.20810547471046448,
				0.29675599932670593,
				0.3674840033054352,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 103,
			"versionNonce": 262944755,
			"isDeleted": false,
			"id": "c6FtZ7leMVwOnp_JVYk6Y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 538.088290309573,
			"y": -150.56646310754996,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 23.66649978584809,
			"height": 102.55483240534167,
			"seed": 623255017,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5634880901392307
				],
				[
					0,
					-1.1269761802784615
				],
				[
					4.50790472111396,
					1.12697618027849
				],
				[
					10.706273712645554,
					8.452321352088603
				],
				[
					12.960226073202534,
					16.904642704177206
				],
				[
					12.960226073202534,
					25.92045214640504
				],
				[
					10.142785622506324,
					34.37277349849364
				],
				[
					6.7618570816708825,
					40.571142490025295
				],
				[
					3.3809285408354413,
					43.38858294072148
				],
				[
					3.944416630974729,
					44.51555912099997
				],
				[
					6.198368991531652,
					45.64253530127846
				],
				[
					8.452321352088632,
					47.33299957169618
				],
				[
					9.579297532367093,
					48.45997575197464
				],
				[
					7.888833261949401,
					47.89648766183541
				],
				[
					6.7618570816708825,
					47.33299957169618
				],
				[
					5.634880901392421,
					46.76951148155692
				],
				[
					5.07139281125319,
					46.20602339141769
				],
				[
					6.198368991531652,
					46.76951148155692
				],
				[
					9.015809442227862,
					48.45997575197464
				],
				[
					11.269761802784842,
					50.71392811253162
				],
				[
					12.396737983063304,
					52.40439238294931
				],
				[
					12.396737983063304,
					52.96788047308857
				],
				[
					11.269761802784842,
					53.5313685632278
				],
				[
					7.325345171810113,
					55.78532092378475
				],
				[
					1.690464270417749,
					59.72973755475945
				],
				[
					0,
					65.36461845615185
				],
				[
					0,
					70.43601126740501
				],
				[
					0.5634880901392876,
					76.0708921687974
				],
				[
					1.690464270417749,
					81.70577307018979
				],
				[
					2.8174404506962105,
					86.77716588144298
				],
				[
					2.8174404506962105,
					92.41204678283535
				],
				[
					1.1269761802785183,
					98.04692768422777
				],
				[
					-1.1269761802784615,
					100.86436813492398
				],
				[
					-10.142785622506324,
					101.42785622506321
				],
				[
					-10.706273712645554,
					101.42785622506321
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14764200150966644,
				0.21166199445724487,
				0.2466503232717514,
				0.22182080149650574,
				0.21050311625003815,
				0.23332446813583374,
				0.2595822513103485,
				0.2717384994029999,
				0.2752251625061035,
				0.23727743327617645,
				0.23262740671634674,
				0.2645745575428009,
				0.3065931797027588,
				0.33598092198371887,
				0.36397141218185425,
				0.3618681728839874,
				0.3689468502998352,
				0.3985331952571869,
				0.4317314028739929,
				0.45424869656562805,
				0.4590945839881897,
				0.4893283545970917,
				0.5017076134681702,
				0.5260300636291504,
				0.5507063269615173,
				0.5342828035354614,
				0.5258832573890686,
				0.5292778611183167,
				0.5290641188621521,
				0.5410208702087402,
				0.5351490378379822,
				0.4412786364555359,
				0.08939486742019653,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 977908925,
			"isDeleted": false,
			"id": "bdphWsWED-n9k5YIT4aDp",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 558.9373496447249,
			"y": -146.62204647657526,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 0.5634880901392592,
			"seed": 1673586761,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5634880901392592
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0039174193516373634,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 84,
			"versionNonce": 803651987,
			"isDeleted": false,
			"id": "DAkupa4agnRHX40Osll1y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 558.3738615545857,
			"y": -147.74902265685375,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.396737983063304,
			"height": 9.015809442227834,
			"seed": 1750702761,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5634880901392307
				],
				[
					-0.5634880901392307,
					-0.5634880901392307
				],
				[
					0,
					-0.5634880901392307
				],
				[
					2.25395236055698,
					3.944416630974672
				],
				[
					3.944416630974672,
					8.452321352088603
				],
				[
					3.944416630974672,
					3.3809285408354413
				],
				[
					5.07139281125319,
					0.5634880901392307
				],
				[
					6.198368991531652,
					2.2539523605569514
				],
				[
					7.325345171810113,
					4.507904721113931
				],
				[
					7.888833261949401,
					5.071392811253162
				],
				[
					9.015809442227862,
					1.6904642704177206
				],
				[
					10.706273712645554,
					0.5634880901392307
				],
				[
					11.833249892924073,
					2.8174404506962105
				],
				[
					11.833249892924073,
					4.507904721113931
				],
				[
					10.142785622506324,
					7.325345171810113
				],
				[
					10.142785622506324,
					7.325345171810113
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08241283893585205,
				0.11625244468450546,
				0.15394574403762817,
				0.15923798084259033,
				0.08694375306367874,
				0.12138137966394424,
				0.16680611670017242,
				0.17901413142681122,
				0.16147494316101074,
				0.12734411656856537,
				0.16224245727062225,
				0.22096151113510132,
				0.24425600469112396,
				0.0686546042561531,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 940447005,
			"isDeleted": false,
			"id": "48VUz4G6yomWGaBc-qBmz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 574.1515280784845,
			"y": -142.11414175546136,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.142785622506324,
			"height": 8.452321352088603,
			"seed": 1619350121,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5634880901392307,
					0
				],
				[
					1.6904642704176922,
					0
				],
				[
					4.507904721113903,
					0
				],
				[
					7.325345171810113,
					-1.1269761802784615
				],
				[
					8.452321352088575,
					-4.507904721113903
				],
				[
					6.7618570816708825,
					-5.634880901392393
				],
				[
					3.3809285408354413,
					-3.944416630974672
				],
				[
					1.1269761802784615,
					-0.5634880901392307
				],
				[
					2.8174404506962105,
					2.8174404506962105
				],
				[
					9.579297532367093,
					2.2539523605569514
				],
				[
					10.142785622506324,
					1.6904642704177206
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0319100022315979,
				0.04371041804552078,
				0.10392855852842331,
				0.20238535106182098,
				0.21247313916683197,
				0.16638348996639252,
				0.12738199532032013,
				0.17318740487098694,
				0.26662662625312805,
				0.11549744009971619,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 660543283,
			"isDeleted": false,
			"id": "u5uVvBJ2BUsnsYkqTDHBZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 589.3657065122438,
			"y": -155.63785591880313,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.253952360556923,
			"height": 15.777666523898716,
			"seed": 865310665,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5634880901392307,
					0.5634880901392592
				],
				[
					1.1269761802784615,
					6.7618570816708825
				],
				[
					0,
					14.650690343620255
				],
				[
					-1.1269761802784615,
					15.777666523898716
				],
				[
					-1.1269761802784615,
					15.214178433759486
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.3005419969558716,
				0.32180601358413696,
				0.24757696688175201,
				0.010401977226138115,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1395091837,
			"isDeleted": false,
			"id": "--fB133zankapZzV2lCwz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 583.1673375207122,
			"y": -148.31251074699298,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.087202253480996,
			"height": 2.817440450696182,
			"seed": 308995049,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5634880901392592
				],
				[
					4.50790472111396,
					-1.6904642704177206
				],
				[
					13.523714163341765,
					0.5634880901392307
				],
				[
					14.087202253480996,
					1.1269761802784615
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0943799763917923,
				0.23256255686283112,
				0.035031404346227646,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1685829843,
			"isDeleted": false,
			"id": "wg2BxfCbdoFszAk8dKrVq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 596.1275635939148,
			"y": -140.42367748504364,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.325345171810113,
			"height": 9.015809442227834,
			"seed": 732111145,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5634880901392307
				],
				[
					0,
					2.2539523605569514
				],
				[
					2.25395236055698,
					2.8174404506962105
				],
				[
					4.507904721113903,
					1.12697618027849
				],
				[
					5.634880901392421,
					-2.2539523605569514
				],
				[
					5.634880901392421,
					-5.071392811253162
				],
				[
					3.3809285408354413,
					-6.198368991531623
				],
				[
					-1.6904642704176922,
					-3.3809285408354413
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09502185136079788,
				0.16203197836875916,
				0.18094460666179657,
				0.17870275676250458,
				0.18617717921733856,
				0.21326473355293274,
				0.04650131240487099,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 2094477789,
			"isDeleted": false,
			"id": "nzSCQftUvn1RtPbBKeAU2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 598.3815159544718,
			"y": -139.29670130476515,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.7618570816708825,
			"height": 2.2539523605569514,
			"seed": 193645481,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5634880901392307
				],
				[
					1.1269761802784615,
					1.6904642704177206
				],
				[
					2.253952360556923,
					2.2539523605569514
				],
				[
					6.7618570816708825,
					1.6904642704177206
				],
				[
					6.7618570816708825,
					1.1269761802784615
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.051511991769075394,
				0.1422005295753479,
				0.09168847650289536,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1154688627,
			"isDeleted": false,
			"id": "dqdu6ZVQfCDDyR4t4pMJ0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 614.7226705685097,
			"y": -164.09017727089173,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1269761802785752,
			"height": 24.79347596612658,
			"seed": 572339145,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					3.3809285408354413
				],
				[
					0,
					9.015809442227862
				],
				[
					0,
					15.777666523898745
				],
				[
					0.5634880901392307,
					23.66649978584809
				],
				[
					1.1269761802785752,
					24.79347596612658
				],
				[
					1.1269761802785752,
					24.79347596612658
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0747779831290245,
				0.20882974565029144,
				0.2695460021495819,
				0.3252260088920593,
				0.060822419822216034,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 36630077,
			"isDeleted": false,
			"id": "5mpQ419IgmsqYQvireb34",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 637.8256822642186,
			"y": -161.83622491033475,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.452321352088575,
			"height": 27.61091641682276,
			"seed": 658905801,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.563488090139117,
					-1.6904642704177206
				],
				[
					0.563488090139117,
					-2.25395236055698
				],
				[
					0,
					2.2539523605569514
				],
				[
					-3.380928540835498,
					13.523714163341765
				],
				[
					-7.888833261949458,
					24.79347596612655
				],
				[
					-6.198368991531652,
					25.35696405626578
				],
				[
					-5.634880901392535,
					24.79347596612655
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08056500554084778,
				0.10117898881435394,
				0.16644831001758575,
				0.19766229391098022,
				0.18307675421237946,
				0.06982427835464478,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 84,
			"versionNonce": 791404563,
			"isDeleted": false,
			"id": "yxHCelarqUxf89DcDB9a9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 646.9233044411473,
			"y": -148.63205419619572,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.499126153330053,
			"height": 7.953989370300889,
			"seed": 182902953,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5681420978786491,
					0
				],
				[
					-1.1362841957572982,
					0
				],
				[
					-2.8407104893932456,
					0.5681420978786491
				],
				[
					-3.9769946851505438,
					3.4088525872718094
				],
				[
					-2.2725683915145964,
					7.385847272422268
				],
				[
					1.1362841957571845,
					7.385847272422268
				],
				[
					2.840710489393132,
					3.9769946851504585
				],
				[
					3.408852587271781,
					3.4088525872718094
				],
				[
					4.545136783029079,
					5.681420978786349
				],
				[
					6.817705174543562,
					6.249563076664998
				],
				[
					8.52213146817951,
					4.545136783029079
				],
				[
					8.52213146817951,
					0.5681420978786491
				],
				[
					6.249563076664913,
					-0.5681420978786207
				],
				[
					3.408852587271781,
					0.5681420978786491
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07751598954200745,
				0.19265517592430115,
				0.21313336491584778,
				0.16402554512023926,
				0.11915262043476105,
				0.10490506142377853,
				0.12773193418979645,
				0.15101327002048492,
				0.1628563553094864,
				0.16504010558128357,
				0.16505062580108643,
				0.15935754776000977,
				0.044642455875873566,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 303046301,
			"isDeleted": false,
			"id": "-Z1S1uS3qCM0bhFrbXv-c",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 659.4224305944772,
			"y": -151.47276468558888,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.681420978786377,
			"height": 10.794699859694077,
			"seed": 95230057,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5681420978786207
				],
				[
					0,
					1.1362841957572698
				],
				[
					0,
					2.8407104893931603
				],
				[
					0.5681420978786491,
					7.3858472724222395
				],
				[
					0.5681420978786491,
					6.817705174543619
				],
				[
					2.2725683915145964,
					1.1362841957572698
				],
				[
					4.545136783029079,
					-2.8407104893931887
				],
				[
					5.681420978786377,
					0.5681420978786207
				],
				[
					5.681420978786377,
					6.817705174543619
				],
				[
					5.681420978786377,
					7.953989370300889
				],
				[
					5.681420978786377,
					7.3858472724222395
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08446508646011353,
				0.11151549965143204,
				0.13579025864601135,
				0.12573818862438202,
				0.09545141458511353,
				0.12770706415176392,
				0.181866854429245,
				0.19722089171409607,
				0.07121551781892776,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1836869043,
			"isDeleted": false,
			"id": "xxX-NVZd-IdCiIM5KXiHE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 673.0578409435644,
			"y": -146.9276279025598,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.090273566058158,
			"height": 11.930984055451347,
			"seed": 1480170953,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5681420978786491
				],
				[
					-0.5681420978786491,
					-1.704426293635919
				],
				[
					-0.5681420978786491,
					-2.8407104893931887
				],
				[
					-1.7044262936359473,
					-3.4088525872718094
				],
				[
					-3.97699468515043,
					-0.5681420978786491
				],
				[
					-4.545136783029079,
					5.1132788809077
				],
				[
					-1.7044262936359473,
					8.522131468179538
				],
				[
					3.97699468515043,
					5.1132788809077
				],
				[
					4.545136783029079,
					4.545136783029079
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.03523498401045799,
				0.07372015714645386,
				0.10955657809972763,
				0.1440473049879074,
				0.15944188833236694,
				0.19489654898643494,
				0.19637362658977509,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 53232381,
			"isDeleted": false,
			"id": "TbYA-DM3zpr29BLX-laMS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 678.1711198244722,
			"y": -149.768338391953,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.681420978786377,
			"height": 9.658415663936808,
			"seed": 1833889129,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5681420978786491
				],
				[
					0,
					2.8407104893931887
				],
				[
					1.1362841957572982,
					7.953989370300889
				],
				[
					1.1362841957572982,
					9.658415663936808
				],
				[
					2.840710489393132,
					5.681420978786349
				],
				[
					5.681420978786377,
					0
				],
				[
					5.681420978786377,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09289798140525818,
				0.125931978225708,
				0.13789230585098267,
				0.1281857043504715,
				0.09849072247743607,
				0.029957061633467674,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 1189820243,
			"isDeleted": false,
			"id": "BeGavcbiAgFcboF89_GJB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 688.3976775862876,
			"y": -145.22320160892392,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.090273566058158,
			"height": 3.9769946851504585,
			"seed": 1931198281,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5681420978786491,
					0
				],
				[
					2.840710489393132,
					0.5681420978786491
				],
				[
					5.681420978786377,
					-0.5681420978786207
				],
				[
					6.817705174543562,
					-1.7044262936358905
				],
				[
					4.545136783029079,
					-2.2725683915145396
				],
				[
					1.1362841957572982,
					-1.1362841957572698
				],
				[
					0,
					0.5681420978786491
				],
				[
					1.7044262936359473,
					1.704426293635919
				],
				[
					3.97699468515043,
					1.704426293635919
				],
				[
					8.52213146817951,
					0
				],
				[
					9.090273566058158,
					-0.5681420978786207
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09975998103618622,
				0.13627612590789795,
				0.13703979551792145,
				0.1277851015329361,
				0.1304781436920166,
				0.15733160078525543,
				0.2118329107761383,
				0.19423800706863403,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1510267741,
			"isDeleted": false,
			"id": "inmHElG9Orfmkyk2JOXQ0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 701.4649458374962,
			"y": -163.40374874104023,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1362841957572982,
			"height": 22.157541817266775,
			"seed": 320018601,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5681420978786491,
					0
				],
				[
					-1.1362841957572982,
					0.5681420978786207
				],
				[
					-1.1362841957572982,
					3.4088525872718094
				],
				[
					0,
					13.067268251208617
				],
				[
					0,
					21.589399719388126
				],
				[
					-0.5681420978786491,
					22.157541817266775
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11811511218547821,
				0.15424130856990814,
				0.18458519876003265,
				0.022620484232902527,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1506727155,
			"isDeleted": false,
			"id": "ic8CLMg1IBIjsR3jjafq4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 695.7835248587098,
			"y": -153.1771909792248,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.226557761815457,
			"height": 0.5681420978786491,
			"seed": 1784749993,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5681420978786491,
					0
				],
				[
					2.8407104893932456,
					-0.5681420978786491
				],
				[
					9.090273566058158,
					-0.5681420978786491
				],
				[
					9.658415663936808,
					-0.5681420978786491
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.2488119751214981,
				0.05751593038439751,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 80,
			"versionNonce": 250308541,
			"isDeleted": false,
			"id": "Vn3h9mXxFHSXuKvy2gBby",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 710.5552194035544,
			"y": -148.06391209831708,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.658415663936808,
			"height": 8.522131468179538,
			"seed": 304712937,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5681420978786207
				],
				[
					1.1362841957572982,
					1.7044262936358905
				],
				[
					2.8407104893932456,
					2.8407104893931603
				],
				[
					7.385847272422325,
					3.97699468515043
				],
				[
					8.52213146817951,
					1.7044262936358905
				],
				[
					5.681420978786377,
					-1.704426293635919
				],
				[
					1.1362841957572982,
					-2.8407104893931887
				],
				[
					-0.5681420978786491,
					-1.1362841957572698
				],
				[
					0.5681420978786491,
					2.8407104893931603
				],
				[
					3.97699468515043,
					5.1132788809077
				],
				[
					8.52213146817951,
					5.681420978786349
				],
				[
					9.090273566058158,
					5.1132788809077
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06407299637794495,
				0.07763513177633286,
				0.1431366205215454,
				0.2256380021572113,
				0.237745001912117,
				0.14527328312397003,
				0.08899819850921631,
				0.12143679708242416,
				0.19816158711910248,
				0.2039087563753128,
				0.07081686705350876,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 900578963,
			"isDeleted": false,
			"id": "4hu0Gs2n6KzHeI_teOe2x",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 748.0525978635443,
			"y": -150.33648048983162,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.681420978786377,
			"height": 14.203552446965887,
			"seed": 1068732713,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.1362841957572982,
					-0.5681420978786491
				],
				[
					1.7044262936359473,
					-1.704426293635919
				],
				[
					2.8407104893932456,
					-2.8407104893931887
				],
				[
					5.113278880907728,
					-6.249563076664998
				],
				[
					5.681420978786377,
					-7.953989370300917
				],
				[
					4.545136783029079,
					-6.817705174543647
				],
				[
					2.8407104893932456,
					-2.272568391514568
				],
				[
					1.7044262936359473,
					4.545136783029079
				],
				[
					3.9769946851505438,
					6.24956307666497
				],
				[
					3.9769946851505438,
					6.24956307666497
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07035498321056366,
				0.06925744563341141,
				0.08189007639884949,
				0.11320959776639938,
				0.12081475555896759,
				0.16167612373828888,
				0.19084662199020386,
				0.19971612095832825,
				0.03163671866059303,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 80,
			"versionNonce": 335636509,
			"isDeleted": false,
			"id": "uhNWqna-JHPT_k3N2b6vZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 748.6207399614229,
			"y": -162.8356066431616,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 21.589399719388098,
			"height": 31.247815383324962,
			"seed": 1752382377,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.7044262936358336,
					0
				],
				[
					-3.408852587271781,
					0.5681420978786491
				],
				[
					-5.113278880907728,
					1.704426293635919
				],
				[
					-7.385847272422211,
					11.362841957572726
				],
				[
					-4.545136783029079,
					19.884973425752236
				],
				[
					1.1362841957572982,
					22.725683915145424
				],
				[
					8.52213146817951,
					21.021257621509505
				],
				[
					13.067268251208702,
					13.635410349087266
				],
				[
					14.203552446965887,
					3.4088525872718094
				],
				[
					10.794699859694106,
					-8.522131468179538
				],
				[
					-3.97699468515043,
					1.1362841957572698
				],
				[
					-3.97699468515043,
					2.8407104893931887
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10447198152542114,
				0.1272919923067093,
				0.2215220034122467,
				0.25895214080810547,
				0.2633001208305359,
				0.2347916215658188,
				0.20881786942481995,
				0.18368029594421387,
				0.12285040318965912,
				0.022845489904284477,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 893285427,
			"isDeleted": false,
			"id": "hhXcTuoqpRL9BRhndclxL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 603.5916781579779,
			"y": -170.8140863421433,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.284150898307757,
			"height": 9.54798345815874,
			"seed": 1166045161,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4151297155721636,
					0
				],
				[
					-0.8302594311442704,
					0
				],
				[
					-1.245389146716434,
					0.41512971557212097
				],
				[
					-1.6605188622885407,
					0.8302594311442419
				],
				[
					-1.6605188622885407,
					1.245389146716363
				],
				[
					-0.4151297155721636,
					0.41512971557212097
				],
				[
					4.566426871293288,
					-4.151297155721181
				],
				[
					10.793372604875003,
					-8.302594311442377
				],
				[
					11.623632036019217,
					-8.302594311442377
				],
				[
					11.623632036019217,
					-8.302594311442377
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.02803240902721882,
				0.01608663983643055,
				0.02390335127711296,
				0.028588196262717247,
				0.12888135015964508,
				0.19329248368740082,
				0.19965697824954987,
				0.04239053279161453,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 456678525,
			"isDeleted": false,
			"id": "tJO4wjYuyYMVe9s0MZzJx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 618.5363479185742,
			"y": -183.68310752487898,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.71772402701447,
			"height": 7.887464595870256,
			"seed": 1308621417,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.41512971557212097
				],
				[
					1.2453891467163203,
					0.41512971557212097
				],
				[
					6.642075449153822,
					0.8302594311442419
				],
				[
					8.71772402701447,
					0.8302594311442419
				],
				[
					8.302594311442363,
					2.4907782934327116
				],
				[
					5.396686302437502,
					5.811816018009665
				],
				[
					4.151297155721068,
					7.887464595870256
				],
				[
					4.981556586865395,
					7.057205164726014
				],
				[
					5.811816018009608,
					6.642075449153907
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07216335833072662,
				0.14588391780853271,
				0.17466039955615997,
				0.17396102845668793,
				0.1925579458475113,
				0.2698059678077698,
				0.27981066703796387,
				0.13963967561721802,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 86,
			"versionNonce": 409433555,
			"isDeleted": false,
			"id": "fJemnUx_MzhfQX9fDeJN8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 634.7264068258867,
			"y": -182.85284809373474,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.717724027014583,
			"height": 25.322912649899237,
			"seed": 2082237961,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.41512971557222045,
					-0.41512971557212097
				],
				[
					1.245389146716434,
					-1.245389146716363
				],
				[
					3.7361674401490745,
					-4.1512971557211955
				],
				[
					6.226945733581829,
					-7.057205164726014
				],
				[
					8.717724027014583,
					-12.038761751591451
				],
				[
					8.302594311442476,
					-15.35979947616839
				],
				[
					6.226945733581829,
					-16.190058907312633
				],
				[
					4.151297155721295,
					-14.114410329452042
				],
				[
					3.7361674401490745,
					-10.378242889302967
				],
				[
					5.396686302437615,
					-4.566426871293302
				],
				[
					7.8874645958703695,
					2.0756485778605906
				],
				[
					8.302594311442476,
					6.226945733581772
				],
				[
					7.057205164726042,
					8.717724027014498
				],
				[
					4.151297155721295,
					9.132853742586605
				],
				[
					1.245389146716434,
					8.717724027014498
				],
				[
					0,
					7.057205164726014
				],
				[
					0.8302594311443272,
					4.566426871293302
				],
				[
					1.245389146716434,
					4.151297155721181
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10741198807954788,
				0.12676623463630676,
				0.12438803166151047,
				0.06782528758049011,
				0.027227630838751793,
				0.0480014942586422,
				0.09388861060142517,
				0.10028631240129471,
				0.08594568073749542,
				0.07878360152244568,
				0.08084765821695328,
				0.09400931000709534,
				0.10606426745653152,
				0.1279844343662262,
				0.10374213010072708,
				0.034353941679000854,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 475120861,
			"isDeleted": false,
			"id": "nmDST4RU-JhIFbUFbBiEX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 647.5954280086224,
			"y": -187.00414524945592,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.566426871293288,
			"height": 6.226945733581786,
			"seed": 1819013001,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.2453891467163203,
					0.41512971557212097
				],
				[
					-1.6605188622885407,
					1.245389146716363
				],
				[
					-1.6605188622885407,
					2.9059080090048326
				],
				[
					-0.41512971557210676,
					4.5664268712933165
				],
				[
					1.6605188622885407,
					3.7361674401490745
				],
				[
					2.9059080090047473,
					0.8302594311442419
				],
				[
					2.075648577860534,
					-1.6605188622884697
				],
				[
					-0.41512971557210676,
					-0.8302594311442277
				],
				[
					-0.8302594311443272,
					3.7361674401490745
				],
				[
					-0.41512971557210676,
					3.7361674401490745
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05803997814655304,
				0.10749953985214233,
				0.1477239429950714,
				0.16785643994808197,
				0.1647244542837143,
				0.13460427522659302,
				0.12160009890794754,
				0.11940426379442215,
				0.0057902527041733265,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1581204339,
			"isDeleted": false,
			"id": "hKLU00i6NgraLL6JK9PCW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 652.1618548799157,
			"y": -187.00414524945592,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.660518862288427,
			"height": 4.1512971557211955,
			"seed": 1954351625,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.41512971557212097
				],
				[
					-0.41512971557210676,
					0.8302594311442419
				],
				[
					-0.41512971557210676,
					2.075648577860605
				],
				[
					-0.41512971557210676,
					3.7361674401490745
				],
				[
					0.8302594311442135,
					4.1512971557211955
				],
				[
					1.2453891467163203,
					3.7361674401490745
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.13843201100826263,
				0.15189702808856964,
				0.041810210794210434,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 450830653,
			"isDeleted": false,
			"id": "6lJz663Xl5qgWs_Ad3Le8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 654.6526331733485,
			"y": -188.6646641117444,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.245389146716434,
			"height": 0,
			"seed": 398176521,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.41512971557222045,
					0
				],
				[
					-1.245389146716434,
					0
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07111600041389465,
				0.08124648779630661,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1594645779,
			"isDeleted": false,
			"id": "-JOXFRAtJIrRVlwr-xsoQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 658.8039303290695,
			"y": -200.28829614776373,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8302594311442135,
			"height": 18.680837200745344,
			"seed": 142579273,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.41512971557210676
				],
				[
					-0.4151297155719931,
					-0.8302594311442277
				],
				[
					-0.4151297155719931,
					-0.41512971557210676
				],
				[
					0.41512971557222045,
					4.5664268712933165
				],
				[
					0.41512971557222045,
					13.699280613879921
				],
				[
					0.41512971557222045,
					17.850577769601117
				],
				[
					0.41512971557222045,
					17.850577769601117
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07239880412817001,
				0.09484735131263733,
				0.2101120948791504,
				0.26139017939567566,
				0.07203088700771332,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 742519197,
			"isDeleted": false,
			"id": "rjzzSrPdgvKyl0eCYk-SV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 671.2578217962332,
			"y": -199.4580367166195,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.6605188622885407,
			"height": 16.190058907312633,
			"seed": 1862364201,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.41512971557222045,
					0.41512971557212097
				],
				[
					-0.41512971557222045,
					1.245389146716363
				],
				[
					0.8302594311442135,
					9.963113173730846
				],
				[
					1.2453891467163203,
					16.190058907312633
				],
				[
					1.2453891467163203,
					16.190058907312633
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11019345372915268,
				0.14262570440769196,
				0.17419128119945526,
				0.03797769173979759,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 642073267,
			"isDeleted": false,
			"id": "eXDBpXYzJXDOPnpVNHzVf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 674.57885952081,
			"y": -186.1738858183117,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8302594311442135,
			"height": 3.3210377245769536,
			"seed": 1004889161,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4151297155719931,
					1.6605188622884697
				],
				[
					-0.4151297155719931,
					2.4907782934327116
				],
				[
					0.41512971557222045,
					3.3210377245769536
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11247598379850388,
				0.13304001092910767,
				0.06333773583173752,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1034663421,
			"isDeleted": false,
			"id": "tTR4v1bsNjiEs-oWU9WYB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 677.0696378142429,
			"y": -191.1554424051771,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8302594311443272,
			"height": 0,
			"seed": 462930025,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.41512971557222045,
					0
				],
				[
					-0.8302594311443272,
					0
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07521301507949829,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 84,
			"versionNonce": 210793555,
			"isDeleted": false,
			"id": "no8kyE7SuZo9CnwftIe_6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 678.7301566765314,
			"y": -189.0797938273165,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.208502320447224,
			"height": 5.811816018009665,
			"seed": 295738793,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.41512971557212097
				],
				[
					0,
					1.245389146716363
				],
				[
					1.2453891467163203,
					4.981556586865423
				],
				[
					2.4907782934326406,
					5.811816018009665
				],
				[
					3.7361674401490745,
					2.9059080090048326
				],
				[
					4.981556586865395,
					0.41512971557212097
				],
				[
					5.811816018009608,
					0.8302594311442419
				],
				[
					6.226945733581715,
					4.1512971557211955
				],
				[
					6.6420754491539356,
					5.811816018009665
				],
				[
					7.887464595870142,
					4.1512971557211955
				],
				[
					9.547983458158683,
					1.6605188622884839
				],
				[
					10.793372604875003,
					0.8302594311442419
				],
				[
					11.208502320447224,
					2.9059080090048326
				],
				[
					10.793372604875003,
					5.811816018009665
				],
				[
					10.37824288930301,
					5.811816018009665
				],
				[
					10.37824288930301,
					5.396686302437544
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1100359782576561,
				0.14580200612545013,
				0.1527414172887802,
				0.14077936112880707,
				0.0872313529253006,
				0.07506387680768967,
				0.18847618997097015,
				0.24334676563739777,
				0.2117791771888733,
				0.09765805304050446,
				0.08257210999727249,
				0.1672903150320053,
				0.2359490990638733,
				0.23172061145305634,
				0.04693426564335823,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 438169181,
			"isDeleted": false,
			"id": "MFGdhhFjVsh10LHa4Vrr3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 692.0143075748391,
			"y": -193.64622069860982,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2453891467163203,
			"height": 0,
			"seed": 1103205737,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.41512971557210676,
					0
				],
				[
					-0.8302594311442135,
					0
				],
				[
					-1.2453891467163203,
					0
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14235474169254303,
				0.10557116568088531,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 298086899,
			"isDeleted": false,
			"id": "5poShEHb4LWUAb4aynvpj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 694.0899561526996,
			"y": -187.41927496502802,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.4907782934327543,
			"height": 3.3210377245769394,
			"seed": 1634497929,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4151297155719931,
					0.41512971557210676
				],
				[
					-0.8302594311442135,
					1.2453891467163487
				],
				[
					-0.8302594311442135,
					2.9059080090048184
				],
				[
					0.41512971557222045,
					3.3210377245769394
				],
				[
					1.245389146716434,
					2.9059080090048184
				],
				[
					1.6605188622885407,
					2.0756485778605906
				],
				[
					1.6605188622885407,
					1.2453891467163487
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07998797297477722,
				0.0969410091638565,
				0.14257532358169556,
				0.13690036535263062,
				0.14066562056541443,
				0.10745929181575775,
				0.01823519915342331,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 80,
			"versionNonce": 812260029,
			"isDeleted": false,
			"id": "gUytMR5TgX-b4ApBUzUFv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 694.5050858682719,
			"y": -189.49492354288864,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.811816018009722,
			"height": 7.472334880298149,
			"seed": 997203241,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.41512971557212097
				],
				[
					-0.41512971557222045,
					0.41512971557212097
				],
				[
					0,
					2.9059080090048326
				],
				[
					0.41512971557210676,
					6.226945733581786
				],
				[
					1.2453891467163203,
					7.472334880298149
				],
				[
					2.0756485778606475,
					4.5664268712933165
				],
				[
					3.321037724576854,
					1.245389146716363
				],
				[
					4.151297155721181,
					0.41512971557212097
				],
				[
					4.981556586865395,
					2.075648577860605
				],
				[
					4.566426871293288,
					6.642075449153907
				],
				[
					4.981556586865395,
					6.642075449153907
				],
				[
					5.396686302437502,
					6.226945733581786
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07273376733064651,
				0.18636398017406464,
				0.23312601447105408,
				0.17846563458442688,
				0.126475527882576,
				0.09369305521249771,
				0.16435885429382324,
				0.2301255464553833,
				0.207781121134758,
				0.046334899961948395,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1994898323,
			"isDeleted": false,
			"id": "A0fLK4R67L5y4MoDpI5zm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 703.6379396108584,
			"y": -187.41927496502802,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.151297155721068,
			"height": 5.396686302437544,
			"seed": 567062889,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8302594311442135,
					1.2453891467163487
				],
				[
					-1.245389146716434,
					2.0756485778605906
				],
				[
					-0.41512971557210676,
					4.981556586865423
				],
				[
					0.8302594311442135,
					4.981556586865423
				],
				[
					2.4907782934326406,
					2.0756485778605906
				],
				[
					2.0756485778606475,
					-0.41512971557212097
				],
				[
					-1.660518862288427,
					2.4907782934327116
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.059487976133823395,
				0.12177956849336624,
				0.19841620326042175,
				0.19954660534858704,
				0.2115384191274643,
				0.22240008413791656,
				0.007909851148724556,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 422689565,
			"isDeleted": false,
			"id": "VvkaamGqxXzGycLKAcIAi",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 705.7135881887191,
			"y": -187.41927496502802,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.547983458158797,
			"height": 13.2841508983078,
			"seed": 1110017289,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.41512971557222045,
					0.41512971557210676
				],
				[
					-0.8302594311442135,
					0.8302594311442277
				],
				[
					0,
					4.566426871293302
				],
				[
					0.8302594311442135,
					8.717724027014484
				],
				[
					-1.245389146716434,
					12.453891467163558
				],
				[
					-5.396686302437615,
					13.2841508983078
				],
				[
					-8.302594311442363,
					9.963113173730846
				],
				[
					-8.717724027014583,
					9.132853742586605
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08001305907964706,
				0.09504098445177078,
				0.14729702472686768,
				0.15806171298027039,
				0.21679510176181793,
				0.23327407240867615,
				0.11218283325433731,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 101,
			"versionNonce": 405852467,
			"isDeleted": false,
			"id": "17Ur8qHESnPcpm5j6bkZS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 718.1674796558825,
			"y": -197.79751785433103,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.605188622884725,
			"height": 13.699280613879921,
			"seed": 1199996361,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8302594311443272,
					0
				],
				[
					5.396686302437615,
					0.41512971557212097
				],
				[
					9.963113173731017,
					0.41512971557212097
				],
				[
					13.284150898307871,
					0.41512971557212097
				],
				[
					14.529540045024305,
					0.41512971557212097
				],
				[
					14.944669760596298,
					0
				],
				[
					15.359799476168519,
					0
				],
				[
					14.944669760596298,
					0
				],
				[
					14.529540045024305,
					2.075648577860605
				],
				[
					14.529540045024305,
					5.396686302437544
				],
				[
					14.529540045024305,
					9.132853742586619
				],
				[
					14.529540045024305,
					11.62363203601933
				],
				[
					14.944669760596298,
					12.869021182735693
				],
				[
					14.944669760596298,
					13.699280613879921
				],
				[
					14.529540045024305,
					13.2841508983078
				],
				[
					13.699280613879978,
					13.2841508983078
				],
				[
					12.03876175159155,
					12.869021182735693
				],
				[
					9.13285374258669,
					13.2841508983078
				],
				[
					6.2269457335819425,
					13.699280613879921
				],
				[
					4.151297155721295,
					13.699280613879921
				],
				[
					2.905908009004861,
					13.699280613879921
				],
				[
					2.0756485778606475,
					13.699280613879921
				],
				[
					1.245389146716434,
					13.699280613879921
				],
				[
					0.8302594311443272,
					13.699280613879921
				],
				[
					0,
					13.699280613879921
				],
				[
					-0.4151297155719931,
					13.699280613879921
				],
				[
					-0.4151297155719931,
					12.038761751591451
				],
				[
					-0.8302594311442135,
					7.88746459587027
				],
				[
					-0.8302594311442135,
					4.9815565868654375
				],
				[
					-1.2453891467162066,
					4.1512971557211955
				],
				[
					-1.2453891467162066,
					2.9059080090048326
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10061651468276978,
				0.13049817085266113,
				0.12806347012519836,
				0.1119716465473175,
				0.10648123174905777,
				0.09313467144966125,
				0.08965899795293808,
				0.08688009530305862,
				0.09964428842067719,
				0.11003357172012329,
				0.11497900635004044,
				0.11665362864732742,
				0.10551794618368149,
				0.09941937029361725,
				0.09211065620183945,
				0.09432397782802582,
				0.12005902081727982,
				0.13304181396961212,
				0.15516583621501923,
				0.17805472016334534,
				0.17528539896011353,
				0.18629108369350433,
				0.1898641735315323,
				0.1975773274898529,
				0.19361795485019684,
				0.20312091708183289,
				0.17241641879081726,
				0.15807799994945526,
				0.15181021392345428,
				0.15222223103046417,
				0.032229065895080566,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1558597501,
			"isDeleted": false,
			"id": "o0h2C19ApLLMnmjyVowci",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 721.9036470960316,
			"y": -196.55212870761466,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.245389146716434,
			"height": 11.20850232044721,
			"seed": 263889513,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.41512971557212097
				],
				[
					0,
					1.245389146716363
				],
				[
					0.41512971557222045,
					6.226945733581786
				],
				[
					1.245389146716434,
					11.20850232044721
				],
				[
					1.245389146716434,
					10.793372604875088
				],
				[
					1.245389146716434,
					10.793372604875088
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.062198638916015625,
				0.07100262492895126,
				0.11766311526298523,
				0.11269216984510422,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 117846739,
			"isDeleted": false,
			"id": "UDB35N_GmZrDrANRlwbEC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 725.6398145361807,
			"y": -196.13699899204255,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.490778293432868,
			"height": 11.20850232044721,
			"seed": 1133701481,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.41512971557222045,
					0
				],
				[
					0.8302594311443272,
					0.41512971557212097
				],
				[
					1.245389146716434,
					2.0756485778605906
				],
				[
					1.6605188622885407,
					7.472334880298135
				],
				[
					2.0756485778606475,
					11.20850232044721
				],
				[
					2.490778293432868,
					11.20850232044721
				],
				[
					2.490778293432868,
					11.20850232044721
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.043829530477523804,
				0.0626385509967804,
				0.12792938947677612,
				0.19070737063884735,
				0.13762903213500977,
				0.007134613115340471,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 2043238365,
			"isDeleted": false,
			"id": "vRQQ2KglMAPpKqQoaTWEn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 719.412868802599,
			"y": -192.40083155189348,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.453891467163544,
			"height": 0.41512971557210676,
			"seed": 239352649,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.41512971557210676,
					-0.41512971557210676
				],
				[
					0.41512971557210676,
					-0.41512971557210676
				],
				[
					4.566426871293288,
					0
				],
				[
					10.37824288930301,
					0
				],
				[
					12.038761751591437,
					-0.41512971557210676
				],
				[
					11.62363203601933,
					-0.41512971557210676
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04079647734761238,
				0.11648767441511154,
				0.16061142086982727,
				0.15509670972824097,
				0.028543883934617043,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1677615219,
			"isDeleted": false,
			"id": "mQkjsepwXg61yuLGez7zM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 720.2431282337432,
			"y": -189.91005325846075,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.793372604875117,
			"height": 2.0756485778605906,
			"seed": 1045275209,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.41512971557222045,
					0.8302594311442277
				],
				[
					4.566426871293288,
					2.0756485778605906
				],
				[
					8.717724027014583,
					1.6605188622884697
				],
				[
					10.793372604875117,
					0.8302594311442277
				],
				[
					10.37824288930301,
					0.41512971557210676
				],
				[
					9.963113173730903,
					0.41512971557210676
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12006369233131409,
				0.21000997722148895,
				0.24688738584518433,
				0.20175503194332123,
				0.030622588470578194,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 703353917,
			"isDeleted": false,
			"id": "tdy5VW2JHa94O0ke7_V9g",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 718.9977390870268,
			"y": -200.70342586333584,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.642075449153822,
			"height": 4.566426871293302,
			"seed": 1363151177,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.41512971557210676
				],
				[
					0.8302594311442135,
					-0.41512971557212097
				],
				[
					4.151297155721181,
					-2.4907782934327116
				],
				[
					6.642075449153822,
					-3.7361674401490745
				],
				[
					6.642075449153822,
					-4.1512971557211955
				],
				[
					6.642075449153822,
					-4.1512971557211955
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.009999999776482582,
				0.10908745974302292,
				0.12049926817417145,
				0.10299579054117203,
				0.015237243846058846,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 2027936275,
			"isDeleted": false,
			"id": "X9hoCX08swWyWXPdIsYZY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 731.8667602697625,
			"y": -199.87316643219162,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.057205164726042,
			"height": 8.302594311442377,
			"seed": 236679241,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.41512971557210676,
					0
				],
				[
					-0.8302594311442135,
					-0.41512971557212097
				],
				[
					-0.41512971557210676,
					-1.2453891467163487
				],
				[
					2.0756485778606475,
					-4.151297155721181
				],
				[
					4.981556586865395,
					-7.887464595870256
				],
				[
					5.811816018009608,
					-8.302594311442377
				],
				[
					6.226945733581829,
					-7.887464595870256
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10974197089672089,
				0.17767199873924255,
				0.22938598692417145,
				0.20403435826301575,
				0.0458192452788353,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1764803741,
			"isDeleted": false,
			"id": "01uEs30K9I9SYl_LL8zKJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 740.169354581205,
			"y": -207.76063102806188,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8302594311442135,
			"height": 17.020318338456875,
			"seed": 441976361,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.41512971557212097
				],
				[
					0.4151297155719931,
					4.981556586865423
				],
				[
					0.4151297155719931,
					10.378242889302967
				],
				[
					0.8302594311442135,
					14.529540045024163
				],
				[
					0.8302594311442135,
					17.020318338456875
				],
				[
					0.8302594311442135,
					16.190058907312633
				],
				[
					0.8302594311442135,
					15.774929191740512
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11758236587047577,
				0.16273096203804016,
				0.16440734267234802,
				0.16027669608592987,
				0.16012853384017944,
				0.045126281678676605,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 312549299,
			"isDeleted": false,
			"id": "DyPqUVO1asFI4IC9rMAD-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 733.9424088476231,
			"y": -186.1738858183117,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.472334880298149,
			"height": 6.226945733581786,
			"seed": 1147600905,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.41512971557210676,
					0
				],
				[
					2.075648577860534,
					-1.6605188622884697
				],
				[
					7.057205164726042,
					-5.811816018009665
				],
				[
					7.057205164726042,
					-6.226945733581786
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.040219999849796295,
				0.17507794499397278,
				0.05242367461323738,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 994584829,
			"isDeleted": false,
			"id": "1lqUFkEYJSOT7_KcbolXL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 724.8095551050365,
			"y": -208.5908904592061,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 1.245389146716363,
			"seed": 102999369,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.41512971557212097
				],
				[
					0,
					-0.8302594311442419
				],
				[
					0,
					-1.245389146716363
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.025248778983950615,
				0.00908343493938446,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 459845971,
			"isDeleted": false,
			"id": "O3OtmSFm19JtNM2ZKsg0s",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 724.3944253894645,
			"y": -206.1001121657734,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.302594311442363,
			"height": 1.6605188622884839,
			"seed": 1738088809,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.4907782934326406,
					-1.245389146716363
				],
				[
					5.811816018009608,
					-1.6605188622884839
				],
				[
					7.887464595870142,
					-0.8302594311442419
				],
				[
					8.302594311442363,
					-0.41512971557212097
				],
				[
					8.302594311442363,
					-0.8302594311442419
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.24163198471069336,
				0.25938910245895386,
				0.20819516479969025,
				0.04700372368097305,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 69,
			"versionNonce": 833880413,
			"isDeleted": false,
			"id": "JQWshzwk9bTqh64jkpzrs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 723.5641659583201,
			"y": -204.85472301905702,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.0001,
			"height": 0.0001,
			"seed": 2071560585,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.0001,
					0.0001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1955401459,
			"isDeleted": false,
			"id": "HWcwZDhSOpFPtoj8uVmQU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 722.3187768116038,
			"y": -201.94881501005221,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.887464595870256,
			"height": 1.2453891467163487,
			"seed": 1991254569,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.41512971557212097
				],
				[
					0.41512971557210676,
					-0.41512971557212097
				],
				[
					0.8302594311442135,
					-0.41512971557212097
				],
				[
					2.0756485778606475,
					-0.41512971557212097
				],
				[
					4.151297155721181,
					-0.41512971557212097
				],
				[
					6.226945733581715,
					-0.41512971557212097
				],
				[
					7.887464595870256,
					-1.2453891467163487
				],
				[
					7.887464595870256,
					-1.2453891467163487
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0,
				0.06548510491847992,
				0.09542977809906006,
				0.10877124220132828,
				0.11972662061452866,
				0.10553466528654099,
				0.01982376165688038,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 835046845,
			"isDeleted": false,
			"id": "LLnOMbILjQAQnl-k58z1s",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 735.1877979943395,
			"y": -203.60933387234067,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.41512971557210676,
			"height": 10.793372604875088,
			"seed": 463549161,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.41512971557212097
				],
				[
					0,
					0.8302594311442277
				],
				[
					0.41512971557210676,
					2.4907782934327116
				],
				[
					0.41512971557210676,
					6.642075449153893
				],
				[
					0.41512971557210676,
					9.963113173730846
				],
				[
					0.41512971557210676,
					10.793372604875088
				],
				[
					0.41512971557210676,
					10.378242889302967
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05699612572789192,
				0.07573501765727997,
				0.11654067784547806,
				0.1282448172569275,
				0.12040740996599197,
				0.07149792462587357,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 98,
			"versionNonce": 278182035,
			"isDeleted": false,
			"id": "VO2I_dJ7_odEJfa0XNNJZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 561.8470042706456,
			"y": -116.75375565142876,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.200770367659516,
			"height": 14.200770367659572,
			"seed": 721147081,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.37370448335946094,
					-1.1211134500783828
				],
				[
					-0.37370448335946094,
					-1.4948179334378437
				],
				[
					-0.37370448335946094,
					-1.868522416797319
				],
				[
					0,
					-1.1211134500783828
				],
				[
					1.1211134500783828,
					2.9896358668757017
				],
				[
					1.8685224167973047,
					7.847794150548722
				],
				[
					2.2422269001567656,
					8.595203117267644
				],
				[
					2.2422269001567656,
					5.979271733751389
				],
				[
					1.4948179334378437,
					1.8685224167973047
				],
				[
					0.37370448335946094,
					-1.4948179334378437
				],
				[
					-0.37370448335946094,
					-2.24222690015678
				],
				[
					-0.7474089667189219,
					-2.6159313835162408
				],
				[
					0.37370448335946094,
					-3.7370448335946236
				],
				[
					4.11074931695407,
					-4.4844538003135455
				],
				[
					8.968907600627062,
					-2.9896358668757017
				],
				[
					10.837430017424367,
					-0.7474089667189219
				],
				[
					10.090021050705445,
					1.4948179334378437
				],
				[
					8.595203117267602,
					2.6159313835162408
				],
				[
					7.100385183829758,
					2.24222690015678
				],
				[
					7.474089667189219,
					1.8685224167973047
				],
				[
					9.342612083986523,
					1.4948179334378437
				],
				[
					11.95854346750275,
					2.6159313835162408
				],
				[
					13.453361400940594,
					4.1107493169540845
				],
				[
					13.079656917581133,
					5.979271733751389
				],
				[
					11.584838984143289,
					7.474089667189233
				],
				[
					9.342612083986523,
					8.968907600627105
				],
				[
					7.474089667189219,
					9.716316567346027
				],
				[
					5.231862767032453,
					8.595203117267644
				],
				[
					4.11074931695407,
					7.474089667189233
				],
				[
					4.11074931695407,
					7.100385183829772
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07156698405742645,
				0.09516598284244537,
				0.13713198900222778,
				0.17805463075637817,
				0.18402093648910522,
				0.1801425814628601,
				0.14149713516235352,
				0.07639468461275101,
				0.04164596647024155,
				0.05191519111394882,
				0.08251321315765381,
				0.1234336569905281,
				0.16628359258174896,
				0.2032044678926468,
				0.1946134716272354,
				0.15830297768115997,
				0.1529657244682312,
				0.14041857421398163,
				0.10306011885404587,
				0.08124090731143951,
				0.10943496972322464,
				0.14564593136310577,
				0.17332620918750763,
				0.2241356521844864,
				0.28589263558387756,
				0.32611241936683655,
				0.3415359854698181,
				0.24757952988147736,
				0.061349090188741684,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 2057244189,
			"isDeleted": false,
			"id": "wxT2evnh0b9eNW0rp1DUR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 577.542592571743,
			"y": -111.89559736775576,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.605567250391971,
			"height": 6.352976217110864,
			"seed": 542208201,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.37370448335946094,
					0.37370448335946094
				],
				[
					-0.37370448335946094,
					1.1211134500783828
				],
				[
					-0.37370448335946094,
					3.737044833594638
				],
				[
					1.4948179334378437,
					6.352976217110864
				],
				[
					3.7370448335946094,
					6.352976217110864
				],
				[
					4.858158283673049,
					3.737044833594638
				],
				[
					5.23186276703251,
					1.4948179334378437
				],
				[
					4.858158283673049,
					1.4948179334378437
				],
				[
					4.484453800313531,
					1.4948179334378437
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.051968809217214584,
				0.07594000548124313,
				0.1345083862543106,
				0.1742776781320572,
				0.15244832634925842,
				0.16396307945251465,
				0.11861575394868851,
				0.008749419823288918,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1295396403,
			"isDeleted": false,
			"id": "hFf77UxlNLhb55-9UUO-m",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 586.1377956890105,
			"y": -111.14818840103683,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.37370448335946094,
			"height": 4.48445380031356,
			"seed": 1481678953,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7474089667189219
				],
				[
					0,
					1.4948179334378437
				],
				[
					-0.37370448335946094,
					3.737044833594638
				],
				[
					-0.37370448335946094,
					4.48445380031356
				],
				[
					0,
					4.48445380031356
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08699200302362442,
				0.10985998809337616,
				0.17762398719787598,
				0.08626110851764679,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1798390397,
			"isDeleted": false,
			"id": "ILIA3XY_bEOEyQPQ6c1Rw",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 586.8852046557295,
			"y": -116.00634668470984,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.37370448335946094,
			"height": 0.7474089667189219,
			"seed": 744874121,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.37370448335946094,
					-0.37370448335946094
				],
				[
					-0.37370448335946094,
					-0.7474089667189219
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07810656726360321,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 223866835,
			"isDeleted": false,
			"id": "ovRJmVlk55UVcqXYyYWRg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 592.864476389481,
			"y": -121.61191393510177,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7474089667189219,
			"height": 13.827065884300112,
			"seed": 782247369,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.37370448335946094,
					2.2422269001567656
				],
				[
					0.7474089667189219,
					10.090021050705474
				],
				[
					0.37370448335946094,
					13.827065884300112
				],
				[
					0.7474089667189219,
					13.45336140094065
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15766198933124542,
				0.18718111515045166,
				0.05049706995487213,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 83,
			"versionNonce": 138275549,
			"isDeleted": false,
			"id": "Cvr-a1qlfGcN2moYEdG2D",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 601.833383990108,
			"y": -120.49080048502339,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.463725534064906,
			"height": 13.45336140094065,
			"seed": 238385929,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7474089667189219
				],
				[
					0.7474089667189219,
					6.726680700470325
				],
				[
					1.1211134500783828,
					9.342612083986552
				],
				[
					0.7474089667189219,
					8.59520311726763
				],
				[
					-1.1211134500783828,
					7.100385183829786
				],
				[
					-3.7370448335946094,
					7.847794150548708
				],
				[
					-4.858158283672992,
					10.463725534064935
				],
				[
					-3.3633403502351484,
					12.332247950862268
				],
				[
					-0.37370448335946094,
					11.958543467502807
				],
				[
					2.2422269001567656,
					10.463725534064935
				],
				[
					2.9896358668756875,
					10.463725534064935
				],
				[
					3.3633403502351484,
					12.705952434221729
				],
				[
					4.11074931695407,
					13.45336140094065
				],
				[
					5.605567250391914,
					11.584838984143346
				],
				[
					5.605567250391914,
					10.837430017424396
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.042796965688467026,
				0.12901385128498077,
				0.14317528903484344,
				0.12465213239192963,
				0.08980575203895569,
				0.11282595992088318,
				0.1691754162311554,
				0.20531338453292847,
				0.19195076823234558,
				0.1449383795261383,
				0.16230447590351105,
				0.19876815378665924,
				0.1589464694261551,
				0.024662170559167862,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 319847795,
			"isDeleted": false,
			"id": "D5TewhoZ7LKG5KZ3noKjB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 607.4389512404999,
			"y": -114.13782426791252,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7474089667189219,
			"height": 1.121113450078397,
			"seed": 1554890729,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.37370448335946094,
					-0.7474089667189361
				],
				[
					-0.7474089667189219,
					-1.121113450078397
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08321667462587357,
				0.07828643918037415,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1112966973,
			"isDeleted": false,
			"id": "Isox-O3TKLmpMIQZuK9Rm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 610.0548826240162,
			"y": -113.3904153011936,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.231862767032567,
			"height": 5.2318627670324815,
			"seed": 890305833,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.37370448335946094,
					0.37370448335946094
				],
				[
					0.7474089667189219,
					1.4948179334378437
				],
				[
					1.4948179334378437,
					4.11074931695407
				],
				[
					2.2422269001568793,
					4.858158283673021
				],
				[
					3.363340350235262,
					2.2422269001567656
				],
				[
					4.484453800313645,
					0.7474089667189219
				],
				[
					4.858158283673106,
					2.2422269001567656
				],
				[
					4.484453800313645,
					4.858158283673021
				],
				[
					4.858158283673106,
					5.2318627670324815
				],
				[
					5.231862767032567,
					5.2318627670324815
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09158200025558472,
				0.12520797550678253,
				0.15432174503803253,
				0.12888872623443604,
				0.10310986638069153,
				0.1384035348892212,
				0.17552828788757324,
				0.1363053023815155,
				0.009618316777050495,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 430331667,
			"isDeleted": false,
			"id": "WtoBfIFkGL8goNpyot8-5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 619.0237902246433,
			"y": -112.26930185111522,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.231862767032453,
			"height": 5.2318627670324815,
			"seed": 1854842793,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.37370448335946094,
					0.37370448335946094
				],
				[
					-1.1211134500783828,
					0.7474089667189219
				],
				[
					-1.8685224167973047,
					1.8685224167973047
				],
				[
					-1.8685224167973047,
					4.48445380031356
				],
				[
					0.7474089667189219,
					5.2318627670324815
				],
				[
					3.3633403502351484,
					4.110749316954099
				],
				[
					3.3633403502351484,
					2.6159313835162266
				],
				[
					1.8685224167973047,
					1.4948179334378437
				],
				[
					-0.7474089667189219,
					2.9896358668756875
				],
				[
					-0.7474089667189219,
					3.363340350235177
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06829953193664551,
				0.11637783795595169,
				0.15862765908241272,
				0.14114467799663544,
				0.12032806128263474,
				0.17697195708751678,
				0.18974924087524414,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 2078054301,
			"isDeleted": false,
			"id": "mtjOv21wQD95_G7nb_0Bt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 622.013426091519,
			"y": -111.89559736775576,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.474089667189219,
			"height": 13.07965691758119,
			"seed": 632328745,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.1211134500783828
				],
				[
					0,
					1.8685224167973047
				],
				[
					0,
					5.979271733751403
				],
				[
					0.37370448335946094,
					10.090021050705474
				],
				[
					-1.1211134500783828,
					13.07965691758119
				],
				[
					-6.352976217110836,
					11.958543467502807
				],
				[
					-7.100385183829758,
					11.211134500783885
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09217599779367447,
				0.192811980843544,
				0.267239511013031,
				0.24015380442142487,
				0.009509887546300888,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 797965491,
			"isDeleted": false,
			"id": "cA4fEx-MPmHMWT8T5taoA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 627.2452888585515,
			"y": -112.26930185111522,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.979271733751375,
			"height": 7.474089667189247,
			"seed": 201460745,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.37370448335946094,
					0
				],
				[
					-0.7474089667189219,
					-0.37370448335946094
				],
				[
					-1.8685224167973047,
					-0.37370448335946094
				],
				[
					-2.6159313835162266,
					0.7474089667189219
				],
				[
					-1.4948179334378437,
					2.9896358668756875
				],
				[
					1.8685224167973047,
					5.2318627670324815
				],
				[
					2.9896358668756875,
					6.726680700470325
				],
				[
					0.7474089667189219,
					7.100385183829786
				],
				[
					-2.2422269001567656,
					6.352976217110864
				],
				[
					-2.9896358668756875,
					5.2318627670324815
				],
				[
					-2.9896358668756875,
					4.858158283673021
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06737899780273438,
				0.10908297449350357,
				0.1652519851922989,
				0.17555542290210724,
				0.16462616622447968,
				0.18226923048496246,
				0.20722128450870514,
				0.254215270280838,
				0.20277389883995056,
				0.02433612011373043,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 86,
			"versionNonce": 1325505533,
			"isDeleted": false,
			"id": "ZNUK_APisiAXKwo6IxcDh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 561.8470042706456,
			"y": -93.58407768314208,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.332247950862211,
			"height": 10.463725534064963,
			"seed": 2072030569,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.37370448335946094,
					-0.7474089667189219
				],
				[
					0.37370448335946094,
					-1.1211134500784112
				],
				[
					0.7474089667189219,
					-1.868522416797333
				],
				[
					0.7474089667189219,
					-2.242226900156794
				],
				[
					1.1211134500783828,
					-0.7474089667189219
				],
				[
					2.2422269001567656,
					4.484453800313531
				],
				[
					3.7370448335946094,
					6.726680700470325
				],
				[
					5.605567250391914,
					4.484453800313531
				],
				[
					6.352976217110836,
					0.7474089667189219
				],
				[
					5.979271733751375,
					0.7474089667189219
				],
				[
					6.352976217110836,
					3.7370448335946094
				],
				[
					8.22149863390814,
					6.726680700470325
				],
				[
					10.090021050705445,
					6.726680700470325
				],
				[
					11.584838984143289,
					2.2422269001567656
				],
				[
					12.332247950862211,
					-2.989635866875716
				],
				[
					12.332247950862211,
					-3.737044833594638
				],
				[
					11.584838984143289,
					-1.4948179334378722
				],
				[
					11.211134500783828,
					-1.1211134500784112
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.018011383712291718,
				0.02917938306927681,
				0.046929627656936646,
				0.10883630067110062,
				0.1322837769985199,
				0.12419223040342331,
				0.11612045019865036,
				0.08018853515386581,
				0.0395975336432457,
				0.050740599632263184,
				0.09707360714673996,
				0.16623914241790771,
				0.22995007038116455,
				0.2621830105781555,
				0.24359329044818878,
				0.12023474276065826,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1349774931,
			"isDeleted": false,
			"id": "wXbpHtB3R8BFtUPrT23_A",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 577.1688880883835,
			"y": -87.97851043275017,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.858158283672992,
			"height": 4.858158283673021,
			"seed": 785039081,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.37370448335946094,
					1.1211134500784112
				],
				[
					-0.7474089667189219,
					2.242226900156794
				],
				[
					-0.37370448335946094,
					2.989635866875716
				],
				[
					1.4948179334378437,
					3.363340350235177
				],
				[
					3.7370448335946094,
					1.868522416797333
				],
				[
					4.11074931695407,
					-0.7474089667189219
				],
				[
					2.9896358668756875,
					-1.4948179334378437
				],
				[
					1.4948179334378437,
					-0.7474089667189219
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05872076377272606,
				0.06526193022727966,
				0.10847454518079758,
				0.16313861310482025,
				0.22935351729393005,
				0.2470061033964157,
				0.1720888912677765,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 331813981,
			"isDeleted": false,
			"id": "ADx2gPsCHLRXtvN9W8tht",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 579.0374105051808,
			"y": -86.85739698267176,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.605567250391971,
			"height": 1.1211134500784112,
			"seed": 1630259561,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.37370448335946094,
					0.37370448335946094
				],
				[
					1.4948179334378437,
					0.37370448335946094
				],
				[
					2.2422269001567656,
					0.37370448335946094
				],
				[
					5.23186276703251,
					-0.37370448335948936
				],
				[
					5.605567250391971,
					-0.7474089667189503
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.078264981508255,
				0.1482589989900589,
				0.11329659819602966,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1059630067,
			"isDeleted": false,
			"id": "rOzQpG-AFbFbOjziKyjPC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 587.2589091390889,
			"y": -97.32112251673672,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1211134500783828,
			"height": 12.705952434221729,
			"seed": 471411081,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.37370448335946094
				],
				[
					0.37370448335946094,
					4.858158283673021
				],
				[
					0.37370448335946094,
					11.584838984143346
				],
				[
					0.7474089667189219,
					12.705952434221729
				],
				[
					1.1211134500783828,
					12.332247950862268
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11347207427024841,
				0.16099126636981964,
				0.16115841269493103,
				0.0069337766617536545,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 637436093,
			"isDeleted": false,
			"id": "gqmFtjmEK-iz9LeA5Whqw",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 589.8748405226053,
			"y": -97.32112251673672,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.37370448335946094,
			"height": 16.442997267816338,
			"seed": 1039789481,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.37370448335946094
				],
				[
					0,
					-0.7474089667189219
				],
				[
					0.37370448335946094,
					2.6159313835162266
				],
				[
					0.37370448335946094,
					11.211134500783885
				],
				[
					0.37370448335946094,
					15.695588301097416
				],
				[
					0.37370448335946094,
					15.695588301097416
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.112574003636837,
				0.22347497940063477,
				0.25894901156425476,
				0.06988928467035294,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 531936659,
			"isDeleted": false,
			"id": "hJQwj5cduQT4Kgz_mZN48",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 596.975225706435,
			"y": -87.23110146603125,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.605567250391914,
			"height": 7.474089667189247,
			"seed": 1365439657,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.37370448335946094,
					-0.37370448335946094
				],
				[
					0.37370448335946094,
					-1.1211134500783828
				],
				[
					-0.7474089667189219,
					-1.4948179334378437
				],
				[
					-2.6159313835162266,
					0.37370448335948936
				],
				[
					-1.1211134500783828,
					3.363340350235177
				],
				[
					1.4948179334378437,
					5.2318627670324815
				],
				[
					1.4948179334378437,
					5.979271733751403
				],
				[
					-1.8685224167973047,
					5.979271733751403
				],
				[
					-4.11074931695407,
					4.858158283673021
				],
				[
					-3.7370448335946094,
					4.858158283673021
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04160800203680992,
				0.15507598221302032,
				0.21160800755023956,
				0.18873654305934906,
				0.16217367351055145,
				0.14799191057682037,
				0.18460187315940857,
				0.2180638164281845,
				0.03921929746866226,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 100,
			"versionNonce": 1799971101,
			"isDeleted": false,
			"id": "ZsQ3CMqh3J78yjY8iCNRh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 608.9337691739378,
			"y": -90.22073733290694,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.432633134692082,
			"height": 18.311519684613643,
			"seed": 219766569,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7474089667189219,
					0
				],
				[
					2.2422269001567656,
					0
				],
				[
					4.858158283673106,
					0
				],
				[
					10.46372553406502,
					0
				],
				[
					14.20077036765963,
					-1.1211134500783828
				],
				[
					16.069292784456934,
					-1.8685224167973047
				],
				[
					16.816701751175856,
					-2.2422269001567656
				],
				[
					17.190406234535317,
					-2.2422269001567656
				],
				[
					16.816701751175856,
					-1.4948179334378437
				],
				[
					16.442997267816395,
					1.4948179334378437
				],
				[
					16.442997267816395,
					6.352976217110864
				],
				[
					16.069292784456934,
					10.090021050705474
				],
				[
					16.442997267816395,
					11.958543467502807
				],
				[
					16.442997267816395,
					13.07965691758119
				],
				[
					16.442997267816395,
					13.45336140094065
				],
				[
					16.069292784456934,
					13.827065884300112
				],
				[
					14.948179334378551,
					14.200770367659572
				],
				[
					11.958543467502864,
					14.948179334378494
				],
				[
					7.474089667189332,
					14.948179334378494
				],
				[
					3.363340350235262,
					14.948179334378494
				],
				[
					1.1211134500783828,
					15.321883817737955
				],
				[
					0.37370448335946094,
					15.695588301097416
				],
				[
					0,
					16.069292784456877
				],
				[
					0.37370448335946094,
					16.069292784456877
				],
				[
					0.7474089667189219,
					14.200770367659572
				],
				[
					0.37370448335946094,
					8.59520311726763
				],
				[
					0.37370448335946094,
					4.110749316954099
				],
				[
					0,
					2.6159313835162266
				],
				[
					-1.4948179334378437,
					1.8685224167973047
				],
				[
					-2.2422269001567656,
					1.1211134500783828
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06431298702955246,
				0.07184375077486038,
				0.12174288928508759,
				0.16325335204601288,
				0.1593257188796997,
				0.1497766077518463,
				0.1573103666305542,
				0.15481223165988922,
				0.13543954491615295,
				0.1540108323097229,
				0.1886672079563141,
				0.20176245272159576,
				0.20239508152008057,
				0.19906191527843475,
				0.19359542429447174,
				0.1871682107448578,
				0.19793619215488434,
				0.21832290291786194,
				0.227824404835701,
				0.24419143795967102,
				0.23992855846881866,
				0.21010959148406982,
				0.20975078642368317,
				0.2532227039337158,
				0.24108999967575073,
				0.23431603610515594,
				0.23486462235450745,
				0.2116706818342209,
				0.1616276502609253,
				0.03043386898934841,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 81,
			"versionNonce": 1364101939,
			"isDeleted": false,
			"id": "3H92lvUlqh8Vq52eREGwP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 610.0548826240162,
			"y": -84.615170082515,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.858158283673106,
			"height": 4.858158283673021,
			"seed": 1587905769,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.37370448335946094
				],
				[
					0.7474089667189219,
					0.37370448335946094
				],
				[
					2.2422269001568793,
					0.7474089667189219
				],
				[
					3.363340350235262,
					0.7474089667189219
				],
				[
					4.110749316954184,
					1.1211134500783828
				],
				[
					4.484453800313645,
					0.7474089667189219
				],
				[
					4.484453800313645,
					0.37370448335946094
				],
				[
					4.484453800313645,
					0
				],
				[
					4.484453800313645,
					-0.7474089667189219
				],
				[
					4.858158283673106,
					-1.8685224167973047
				],
				[
					4.858158283673106,
					-3.363340350235177
				],
				[
					4.858158283673106,
					-3.737044833594638
				],
				[
					4.484453800313645,
					-3.363340350235177
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09282147139310837,
				0.1295466274023056,
				0.13367022573947906,
				0.12107281386852264,
				0.10764434933662415,
				0.10508694499731064,
				0.09877615422010422,
				0.0989949032664299,
				0.10408861935138702,
				0.11660290509462357,
				0.12204919755458832,
				0.11929638683795929,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 81,
			"versionNonce": 421082493,
			"isDeleted": false,
			"id": "gUE7U1s2oxliQmSnsl1bH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 614.1656319409703,
			"y": -84.615170082515,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.605567250391914,
			"height": 5.6055672503919425,
			"seed": 486833161,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.37370448335946094,
					0.37370448335946094
				],
				[
					1.8685224167973047,
					0.37370448335946094
				],
				[
					3.7370448335946094,
					0.37370448335946094
				],
				[
					4.484453800313531,
					0.37370448335946094
				],
				[
					4.858158283672992,
					0.37370448335946094
				],
				[
					4.858158283672992,
					0
				],
				[
					5.231862767032453,
					-0.37370448335946094
				],
				[
					5.231862767032453,
					-1.1211134500783828
				],
				[
					5.605567250391914,
					-2.989635866875716
				],
				[
					5.605567250391914,
					-4.858158283673021
				],
				[
					5.231862767032453,
					-5.2318627670324815
				],
				[
					4.858158283672992,
					-3.737044833594638
				],
				[
					4.858158283672992,
					-3.737044833594638
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1191980317234993,
				0.13685092329978943,
				0.1130707710981369,
				0.08277584612369537,
				0.08223751932382584,
				0.07361352443695068,
				0.11311538517475128,
				0.13221246004104614,
				0.1492338329553604,
				0.15182361006736755,
				0.12172576785087585,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 80,
			"versionNonce": 140291283,
			"isDeleted": false,
			"id": "FtpXKJKm_oTfbKRyp1Kp6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 619.0237902246433,
			"y": -84.615170082515,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.979271733751375,
			"height": 2.615931383516255,
			"seed": 554800937,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.37370448335946094
				],
				[
					0.37370448335946094,
					-0.37370448335946094
				],
				[
					1.8685224167973047,
					-0.37370448335946094
				],
				[
					3.3633403502351484,
					0
				],
				[
					4.484453800313531,
					0
				],
				[
					4.858158283672992,
					0
				],
				[
					5.231862767032453,
					-0.37370448335946094
				],
				[
					5.605567250391914,
					-0.7474089667189219
				],
				[
					5.605567250391914,
					-1.4948179334378437
				],
				[
					5.979271733751375,
					-2.2422269001567656
				],
				[
					5.979271733751375,
					-2.615931383516255
				],
				[
					5.605567250391914,
					-2.2422269001567656
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11298205703496933,
				0.1304934024810791,
				0.15001751482486725,
				0.1600261777639389,
				0.15022878348827362,
				0.14298999309539795,
				0.13931973278522491,
				0.14052045345306396,
				0.16243332624435425,
				0.1620110720396042,
				0.16036075353622437,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 82,
			"versionNonce": 984579549,
			"isDeleted": false,
			"id": "UfiNsW5CyfYsBtLAuzpFH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 612.297109524173,
			"y": -83.49405663243661,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.7370448335946094,
			"height": 4.11074931695407,
			"seed": 158378857,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.37370448335946094
				],
				[
					0,
					0.7474089667189219
				],
				[
					0.37370448335946094,
					2.2422269001567656
				],
				[
					1.1211134500783828,
					2.9896358668756875
				],
				[
					1.4948179334378437,
					3.3633403502351484
				],
				[
					2.2422269001567656,
					2.9896358668756875
				],
				[
					2.9896358668756875,
					2.9896358668756875
				],
				[
					3.3633403502351484,
					2.9896358668756875
				],
				[
					3.7370448335946094,
					2.6159313835162266
				],
				[
					3.7370448335946094,
					2.2422269001567656
				],
				[
					3.7370448335946094,
					1.1211134500783828
				],
				[
					3.3633403502351484,
					0
				],
				[
					3.3633403502351484,
					-0.7474089667189219
				],
				[
					3.7370448335946094,
					-0.7474089667189219
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06309670954942703,
				0.08160946518182755,
				0.08721600472927094,
				0.08586905151605606,
				0.08881140500307083,
				0.09361657500267029,
				0.08896008133888245,
				0.0880202054977417,
				0.08877597004175186,
				0.08694195747375488,
				0.09472458064556122,
				0.09239434450864792,
				0.014422210864722729,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 82,
			"versionNonce": 678795891,
			"isDeleted": false,
			"id": "hJHRlPkLhTDGQ4A0dFpzg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 616.4078588411271,
			"y": -80.87812524892038,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.979271733751375,
			"height": 4.858158283672992,
			"seed": 1031289193,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.37370448335946094,
					0
				],
				[
					1.4948179334378437,
					0
				],
				[
					2.6159313835162266,
					0
				],
				[
					3.7370448335946094,
					0
				],
				[
					4.484453800313531,
					0
				],
				[
					4.858158283672992,
					0
				],
				[
					5.231862767032453,
					-0.37370448335946094
				],
				[
					5.231862767032453,
					-0.7474089667189219
				],
				[
					5.605567250391914,
					-1.4948179334378437
				],
				[
					5.605567250391914,
					-2.6159313835162266
				],
				[
					5.979271733751375,
					-4.11074931695407
				],
				[
					5.979271733751375,
					-4.858158283672992
				],
				[
					5.979271733751375,
					-4.484453800313531
				],
				[
					5.605567250391914,
					-4.11074931695407
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10238540917634964,
				0.11704443395137787,
				0.1071215495467186,
				0.10228405892848969,
				0.09807446599006653,
				0.09203305095434189,
				0.0919344499707222,
				0.09436126798391342,
				0.09484442323446274,
				0.10956350713968277,
				0.12864120304584503,
				0.12766458094120026,
				0.028840363025665283,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 82,
			"versionNonce": 1998436925,
			"isDeleted": false,
			"id": "y-HoZofHXegAqelGt7OLz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 610.4285871073756,
			"y": -79.00960283212305,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.979271733751489,
			"height": 2.989635866875716,
			"seed": 698599273,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.37370448335946094,
					0
				],
				[
					-0.37370448335946094,
					0.37370448335946094
				],
				[
					0,
					0.37370448335946094
				],
				[
					0.7474089667189219,
					0.37370448335946094
				],
				[
					2.2422269001568793,
					0.37370448335946094
				],
				[
					3.737044833594723,
					0.37370448335946094
				],
				[
					4.484453800313645,
					0.7474089667189219
				],
				[
					4.858158283673106,
					0.7474089667189219
				],
				[
					5.231862767032567,
					0
				],
				[
					5.231862767032567,
					-1.1211134500784112
				],
				[
					5.605567250392028,
					-1.868522416797333
				],
				[
					5.605567250392028,
					-2.242226900156794
				],
				[
					5.231862767032567,
					-1.868522416797333
				],
				[
					5.231862767032567,
					-1.4948179334378722
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06284451484680176,
				0.05337445065379143,
				0.10784820467233658,
				0.11981576681137085,
				0.13464532792568207,
				0.1359371393918991,
				0.12927065789699554,
				0.1231713593006134,
				0.13798534870147705,
				0.1397848278284073,
				0.12419921904802322,
				0.060520295053720474,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 85,
			"versionNonce": 1583338515,
			"isDeleted": false,
			"id": "pC2HkNf2Lp3wrXhfp1baJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 618.6500857412839,
			"y": -80.13071628220146,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.726680700470297,
			"height": 3.363340350235177,
			"seed": 99833193,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.37370448335946094,
					0
				],
				[
					-0.37370448335946094,
					0.37370448335946094
				],
				[
					-0.7474089667189219,
					0.7474089667189503
				],
				[
					-0.37370448335946094,
					1.4948179334378722
				],
				[
					0.37370448335946094,
					1.868522416797333
				],
				[
					0.7474089667189219,
					1.868522416797333
				],
				[
					1.8685224167973047,
					1.868522416797333
				],
				[
					2.6159313835162266,
					1.4948179334378722
				],
				[
					3.7370448335946094,
					1.1211134500784112
				],
				[
					4.858158283672992,
					0.7474089667189503
				],
				[
					5.605567250391914,
					1.1211134500784112
				],
				[
					5.979271733751375,
					1.1211134500784112
				],
				[
					5.979271733751375,
					0
				],
				[
					5.979271733751375,
					-1.1211134500783828
				],
				[
					5.979271733751375,
					-1.4948179334378437
				],
				[
					5.605567250391914,
					-1.4948179334378437
				],
				[
					5.605567250391914,
					-1.4948179334378437
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06879647821187973,
				0.0608442984521389,
				0.07301748543977737,
				0.0796159952878952,
				0.08323092758655548,
				0.08775351196527481,
				0.09434188902378082,
				0.10336941480636597,
				0.10092297196388245,
				0.10082662850618362,
				0.10257528722286224,
				0.10985968261957169,
				0.0907420963048935,
				0.05141375586390495,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 390425245,
			"isDeleted": false,
			"id": "znghKEJnm013XtIDdmuhL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 614.1656319409703,
			"y": -78.26219386540413,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.231862767032453,
			"height": 1.4948179334378437,
			"seed": 2024689673,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.37370448335946094,
					0
				],
				[
					-0.37370448335946094,
					-0.37370448335946094
				],
				[
					-0.37370448335946094,
					0
				],
				[
					0.37370448335946094,
					0.7474089667189219
				],
				[
					2.2422269001567656,
					1.1211134500783828
				],
				[
					4.858158283672992,
					0.37370448335946094
				],
				[
					4.858158283672992,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0041014100424945354,
				0.03504299744963646,
				0.0723971575498581,
				0.0808061808347702,
				0.09351076930761337,
				0.021469848230481148,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 2047990195,
			"isDeleted": false,
			"id": "hallRVzcNxxkRi0A3XHAk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 645.3997229118148,
			"y": -123.35120656148511,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.8455723765811172,
			"height": 21.777754043656884,
			"seed": 499461609,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.3691144753162092
				],
				[
					0,
					1.4764579012648653
				],
				[
					1.4764579012648937,
					7.013175031008146
				],
				[
					1.8455723765811172,
					14.764579012648724
				],
				[
					1.4764579012648937,
					20.30129614239202
				],
				[
					1.4764579012648937,
					21.777754043656884
				],
				[
					1.4764579012648937,
					19.19395271644335
				],
				[
					1.4764579012648937,
					18.4557237658109
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08006018400192261,
				0.11941729485988617,
				0.1570243537425995,
				0.171220064163208,
				0.16313599050045013,
				0.11075320094823837,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1272450813,
			"isDeleted": false,
			"id": "fm2kmAAhEI3zsrztvwJ4C",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 644.2923794858661,
			"y": -123.72032103680134,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.241036913913604,
			"height": 1.107343425948656,
			"seed": 1586400937,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.36911447531622343,
					-0.36911447531622343
				],
				[
					1.1073434259486703,
					-0.7382289506324327
				],
				[
					2.9529158025297875,
					-1.107343425948656
				],
				[
					9.596976358221696,
					-1.107343425948656
				],
				[
					14.3954645373326,
					-1.107343425948656
				],
				[
					16.241036913913604,
					-0.36911447531622343
				],
				[
					16.241036913913604,
					-0.36911447531622343
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08204199373722076,
				0.10877200216054916,
				0.12874749302864075,
				0.10590432584285736,
				0.005822448525577784,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 145894227,
			"isDeleted": false,
			"id": "OMIXCcEDEDqp3TpilftWT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 660.5334163997798,
			"y": -124.08943551211756,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.8455723765811172,
			"height": 21.039525093024466,
			"seed": 911734921,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.36911447531622343
				],
				[
					0.36911447531622343,
					3.6911447531621917
				],
				[
					1.4764579012648937,
					8.858747407589249
				],
				[
					1.8455723765811172,
					14.026350062016306
				],
				[
					1.8455723765811172,
					18.086609290494707
				],
				[
					1.4764579012648937,
					20.670410617708242
				],
				[
					0.36911447531622343,
					21.039525093024466
				],
				[
					0,
					21.039525093024466
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11330999433994293,
				0.16436801850795746,
				0.15645980834960938,
				0.13843826949596405,
				0.10029791295528412,
				0.013408904895186424,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 861349725,
			"isDeleted": false,
			"id": "pk49sV9Olp9OA9098rdct",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 647.6144097637122,
			"y": -100.46610909187959,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.07343425948659,
			"height": 0.369114475316195,
			"seed": 1390580041,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.36911447531622343,
					0
				],
				[
					5.536717129743238,
					-0.369114475316195
				],
				[
					9.966090833537805,
					-0.369114475316195
				],
				[
					11.07343425948659,
					0
				],
				[
					10.704319784170252,
					-0.369114475316195
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09475301951169968,
				0.2147420048713684,
				0.23889020085334778,
				0.05225637927651405,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 91,
			"versionNonce": 781666547,
			"isDeleted": false,
			"id": "oIT33SS_ER9aRbSXJy8Ww",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 648.3526387143445,
			"y": -120.76740523427159,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.167602654427128,
			"height": 5.167602654427057,
			"seed": 949587305,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.36911447531622343
				],
				[
					0,
					0.7382289506324327
				],
				[
					0,
					1.4764579012648795
				],
				[
					0.3691144753163371,
					2.952915802529745
				],
				[
					1.107343425948784,
					3.6911447531621917
				],
				[
					1.107343425948784,
					3.3220302778459683
				],
				[
					0.7382289506324469,
					1.4764579012648795
				],
				[
					0.3691144753163371,
					0
				],
				[
					0,
					-0.7382289506324327
				],
				[
					0,
					-1.107343425948656
				],
				[
					1.4764579012648937,
					-1.107343425948656
				],
				[
					3.322030277846011,
					-1.107343425948656
				],
				[
					4.798488179110905,
					-0.36911447531622343
				],
				[
					4.798488179110905,
					0.36911447531622343
				],
				[
					4.798488179110905,
					1.4764579012648795
				],
				[
					4.798488179110905,
					2.952915802529745
				],
				[
					4.798488179110905,
					3.6911447531621917
				],
				[
					5.167602654427128,
					3.6911447531621917
				],
				[
					4.798488179110905,
					3.6911447531621917
				],
				[
					3.322030277846011,
					4.060259228478401
				],
				[
					1.8455723765812309,
					4.060259228478401
				],
				[
					1.107343425948784,
					3.3220302778459683
				],
				[
					1.4764579012648937,
					3.3220302778459683
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.03926898166537285,
				0.04724743589758873,
				0.07403439283370972,
				0.07553375512361526,
				0.06405597180128098,
				0.05514843761920929,
				0.04239172488451004,
				0.03802795335650444,
				0.054529204964637756,
				0.08529043942689896,
				0.10918240249156952,
				0.11416445672512054,
				0.10721252113580704,
				0.09275030344724655,
				0.09096987545490265,
				0.08367343246936798,
				0.08702865242958069,
				0.09567129611968994,
				0.10733374208211899,
				0.12904275953769684,
				0.14431165158748627,
				0.029388427734375,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 88,
			"versionNonce": 538194877,
			"isDeleted": false,
			"id": "jUuvc84Ke7cMT1Z7EF2w1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 655.3658137453527,
			"y": -120.39829075895537,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.060259228478344,
			"height": 5.167602654427071,
			"seed": 1940270409,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.3691144753162092
				],
				[
					0,
					0.7382289506324327
				],
				[
					0.36911447531622343,
					2.5838013272135214
				],
				[
					0.7382289506324469,
					3.3220302778459683
				],
				[
					0.7382289506324469,
					2.5838013272135214
				],
				[
					0.36911447531622343,
					0.7382289506324327
				],
				[
					0,
					-0.7382289506324469
				],
				[
					-0.36911447531622343,
					-1.4764579012648795
				],
				[
					0.36911447531622343,
					-1.845572376581103
				],
				[
					1.47645790126478,
					-1.4764579012648795
				],
				[
					2.583801327213564,
					-0.7382289506324469
				],
				[
					3.322030277846011,
					0
				],
				[
					3.6911447531621207,
					0.7382289506324327
				],
				[
					3.322030277846011,
					1.4764579012648653
				],
				[
					2.952915802529674,
					2.5838013272135214
				],
				[
					2.583801327213564,
					3.3220302778459683
				],
				[
					2.214686851897227,
					3.3220302778459683
				],
				[
					1.1073434259486703,
					2.214686851897312
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04538601636886597,
				0.05143924057483673,
				0.04919329658150673,
				0.041547760367393494,
				0.0209424439817667,
				0.02232571318745613,
				0.02433187887072563,
				0.047348082065582275,
				0.07614398002624512,
				0.08509774506092072,
				0.08196258544921875,
				0.07344662398099899,
				0.07159020751714706,
				0.07310137897729874,
				0.08356765657663345,
				0.09383053332567215,
				0.09440969675779343,
				0.025044891983270645,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 89,
			"versionNonce": 1095217811,
			"isDeleted": false,
			"id": "YO-0yjmPE9nPFyyh-UM9n",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 649.4599821402933,
			"y": -114.12334467857966,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.536717129743238,
			"height": 4.798488179110834,
			"seed": 387264649,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.107343425948656
				],
				[
					1.1073434259485566,
					2.5838013272135356
				],
				[
					1.1073434259485566,
					2.9529158025297306
				],
				[
					0.7382289506324469,
					1.107343425948656
				],
				[
					0,
					0
				],
				[
					-0.7382289506324469,
					-1.107343425948656
				],
				[
					0.36911447531610975,
					-1.107343425948656
				],
				[
					2.5838013272134503,
					-1.107343425948656
				],
				[
					4.060259228478344,
					-0.7382289506324469
				],
				[
					4.798488179110791,
					-0.36911447531622343
				],
				[
					4.4293737037945675,
					-0.36911447531622343
				],
				[
					4.060259228478344,
					0
				],
				[
					3.6911447531621207,
					1.107343425948656
				],
				[
					3.6911447531621207,
					2.5838013272135356
				],
				[
					4.4293737037945675,
					3.322030277845954
				],
				[
					4.4293737037945675,
					3.6911447531621775
				],
				[
					2.952915802529674,
					3.6911447531621775
				],
				[
					1.47645790126478,
					3.6911447531621775
				],
				[
					0.36911447531610975,
					3.6911447531621775
				],
				[
					1.1073434259485566,
					3.322030277845954
				],
				[
					1.47645790126478,
					3.322030277845954
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10740014910697937,
				0.09614501893520355,
				0.07620123028755188,
				0.05668795853853226,
				0.057561371475458145,
				0.06692413240671158,
				0.11190609633922577,
				0.12393166869878769,
				0.11472665518522263,
				0.11037011444568634,
				0.10312613099813461,
				0.09816689789295197,
				0.09713989496231079,
				0.09924902021884918,
				0.11024569720029831,
				0.12142321467399597,
				0.13690240681171417,
				0.15149915218353271,
				0.14685370028018951,
				0.009138640947639942,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 91,
			"versionNonce": 506508317,
			"isDeleted": false,
			"id": "sIxSPns5ZyGjsW9udU84a",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 655.734928220669,
			"y": -113.75423020326345,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.6911447531621207,
			"height": 5.5367171297432805,
			"seed": 687923881,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.36911447531622343
				],
				[
					0,
					1.107343425948656
				],
				[
					0,
					1.4764579012648795
				],
				[
					0,
					2.952915802529745
				],
				[
					0.36911447531622343,
					3.6911447531621917
				],
				[
					0.36911447531622343,
					2.952915802529745
				],
				[
					0,
					1.107343425948656
				],
				[
					-0.36911447531622343,
					-0.3691144753162092
				],
				[
					-0.36911447531622343,
					-1.4764579012648653
				],
				[
					0,
					-1.4764579012648653
				],
				[
					0.7382289506324469,
					-1.4764579012648653
				],
				[
					2.2146868518973406,
					-0.7382289506324327
				],
				[
					2.9529158025297875,
					0
				],
				[
					3.322030277845897,
					0
				],
				[
					2.9529158025297875,
					0.36911447531622343
				],
				[
					2.2146868518973406,
					1.107343425948656
				],
				[
					2.2146868518973406,
					1.845572376581103
				],
				[
					2.2146868518973406,
					2.952915802529745
				],
				[
					2.5838013272134503,
					3.3220302778459683
				],
				[
					1.8455723765810035,
					3.3220302778459683
				],
				[
					0.7382289506324469,
					3.6911447531621917
				],
				[
					0,
					4.060259228478415
				],
				[
					-0.36911447531622343,
					4.060259228478415
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.04128536954522133,
				0.06660305708646774,
				0.07073916494846344,
				0.06732586771249771,
				0.051932647824287415,
				0.04511822387576103,
				0.05262100324034691,
				0.07641183584928513,
				0.09543487429618835,
				0.10855447500944138,
				0.10776568949222565,
				0.08872833102941513,
				0.08410366624593735,
				0.0842195451259613,
				0.08558142185211182,
				0.09161199629306793,
				0.09392477571964264,
				0.11577285826206207,
				0.12689465284347534,
				0.12160934507846832,
				0.023419952020049095,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 92,
			"versionNonce": 561637427,
			"isDeleted": false,
			"id": "uRUIfn1cPl00Xf5ObmcXV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 649.0908676649769,
			"y": -107.84839859820394,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.905831605059575,
			"height": 5.90583160505949,
			"seed": 475863689,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7382289506324469,
					1.8455723765810887
				],
				[
					1.4764579012648937,
					3.6911447531621775
				],
				[
					1.8455723765811172,
					4.060259228478401
				],
				[
					1.4764579012648937,
					3.322030277845954
				],
				[
					0.7382289506324469,
					1.8455723765810887
				],
				[
					0,
					0.36911447531622343
				],
				[
					-0.36911447531610975,
					-1.1073434259486703
				],
				[
					-0.7382289506324469,
					-1.4764579012648653
				],
				[
					-0.36911447531610975,
					-1.8455723765810887
				],
				[
					0.7382289506324469,
					-1.8455723765810887
				],
				[
					2.583801327213564,
					-1.1073434259486703
				],
				[
					3.6911447531622343,
					-0.7382289506324469
				],
				[
					4.060259228478458,
					-0.7382289506324469
				],
				[
					4.060259228478458,
					-1.1073434259486703
				],
				[
					4.060259228478458,
					0
				],
				[
					4.798488179110905,
					1.8455723765810887
				],
				[
					5.167602654427128,
					2.5838013272135356
				],
				[
					5.167602654427128,
					2.9529158025297306
				],
				[
					4.798488179110905,
					2.9529158025297306
				],
				[
					3.6911447531622343,
					2.9529158025297306
				],
				[
					2.583801327213564,
					3.322030277845954
				],
				[
					2.2146868518973406,
					3.322030277845954
				],
				[
					2.2146868518973406,
					2.9529158025297306
				],
				[
					2.583801327213564,
					2.9529158025297306
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09885333478450775,
				0.09652868658304214,
				0.08311251550912857,
				0.0715094581246376,
				0.06705700606107712,
				0.06880801171064377,
				0.07493694871664047,
				0.10299627482891083,
				0.11324676871299744,
				0.11886925995349884,
				0.13293993473052979,
				0.1323748528957367,
				0.12725064158439636,
				0.12493634223937988,
				0.130813330411911,
				0.1466241180896759,
				0.14588631689548492,
				0.14099350571632385,
				0.1615474820137024,
				0.19668282568454742,
				0.208309143781662,
				0.1879156529903412,
				0.031114013865590096,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 97,
			"versionNonce": 966666365,
			"isDeleted": false,
			"id": "N0NQKh4rqOrNQ_0NDZJ_i",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 655.3658137453527,
			"y": -107.47928412288772,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.4293737037945675,
			"height": 6.274946080375713,
			"seed": 223412553,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.36911447531622343
				],
				[
					0,
					1.4764579012648653
				],
				[
					0.36911447531622343,
					2.9529158025297306
				],
				[
					0.7382289506324469,
					3.6911447531621775
				],
				[
					0.7382289506324469,
					3.322030277845954
				],
				[
					0.36911447531622343,
					2.214686851897312
				],
				[
					0,
					0.7382289506324184
				],
				[
					0,
					-0.7382289506324469
				],
				[
					-0.36911447531622343,
					-1.8455723765810887
				],
				[
					-0.36911447531622343,
					-2.214686851897312
				],
				[
					-0.36911447531622343,
					-1.8455723765810887
				],
				[
					0,
					-1.8455723765810887
				],
				[
					0.36911447531622343,
					-1.4764579012648937
				],
				[
					1.1073434259486703,
					-1.4764579012648937
				],
				[
					1.8455723765811172,
					-1.1073434259486703
				],
				[
					2.214686851897227,
					-1.1073434259486703
				],
				[
					2.583801327213564,
					-1.1073434259486703
				],
				[
					2.952915802529674,
					-0.7382289506324469
				],
				[
					3.6911447531621207,
					0.36911447531622343
				],
				[
					4.060259228478344,
					1.4764579012648653
				],
				[
					4.060259228478344,
					1.8455723765810887
				],
				[
					4.060259228478344,
					2.214686851897312
				],
				[
					4.060259228478344,
					2.583801327213507
				],
				[
					3.6911447531621207,
					2.9529158025297306
				],
				[
					2.952915802529674,
					3.322030277845954
				],
				[
					1.8455723765811172,
					3.6911447531621775
				],
				[
					1.47645790126478,
					4.060259228478401
				],
				[
					1.1073434259486703,
					4.060259228478401
				],
				[
					1.47645790126478,
					4.060259228478401
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09963101148605347,
				0.0997956246137619,
				0.09699895977973938,
				0.0908314511179924,
				0.09296716004610062,
				0.08846249431371689,
				0.09388934075832367,
				0.10190838575363159,
				0.11972299218177795,
				0.1270439773797989,
				0.13140353560447693,
				0.12645544111728668,
				0.12859982252120972,
				0.12815017998218536,
				0.1276908814907074,
				0.12492584437131882,
				0.1235824003815651,
				0.12594293057918549,
				0.12599091231822968,
				0.1253623068332672,
				0.119668148458004,
				0.11817620694637299,
				0.12199243158102036,
				0.1536283940076828,
				0.18872734904289246,
				0.2104596495628357,
				0.2243577539920807,
				0.19510143995285034,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 80,
			"versionNonce": 1427401171,
			"isDeleted": false,
			"id": "IMOodQOnKBs2e97vcERZj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 562.3207213128971,
			"y": -65.66162733193114,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.856676990379981,
			"height": 5.142363872167024,
			"seed": 308859497,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.2856868817870577,
					0
				],
				[
					-0.8570606453611731,
					0.8570606453611731
				],
				[
					-0.8570606453611731,
					1.4284344089352885
				],
				[
					-0.8570606453611731,
					3.1425556996576347
				],
				[
					1.1427475271482308,
					5.142363872167024
				],
				[
					2.856868817870577,
					4.856676990379967
				],
				[
					3.4282425814446924,
					2.856868817870577
				],
				[
					2.2854950542964616,
					0.5713737635741154
				],
				[
					-0.2856868817870577,
					0
				],
				[
					-1.4284344089352885,
					1.999808172509404
				],
				[
					-0.2856868817870577,
					3.71392946323175
				],
				[
					0,
					3.999616345018808
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0819794312119484,
				0.10765466094017029,
				0.12738089263439178,
				0.14755147695541382,
				0.15276947617530823,
				0.14746996760368347,
				0.12114407122135162,
				0.10051263123750687,
				0.08767157047986984,
				0.01968875154852867,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 82,
			"versionNonce": 69079261,
			"isDeleted": false,
			"id": "jvPDRxYLY4ey7XKhBO8xW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 569.7485802393606,
			"y": -69.08986991337584,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.4280507539540395,
			"height": 10.284727744334063,
			"seed": 209925801,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.28568688178711454,
					0.5713737635741154
				],
				[
					-0.28568688178711454,
					1.4284344089352885
				],
				[
					-0.28568688178711454,
					3.1425556996576347
				],
				[
					-0.5713737635741154,
					6.285111399315269
				],
				[
					-0.5713737635741154,
					6.570798281102327
				],
				[
					-0.28568688178711454,
					5.713737635741154
				],
				[
					1.4284344089352317,
					5.428050753954096
				],
				[
					3.7139294632316933,
					7.1421720446764425
				],
				[
					4.285303226805809,
					9.141980217185832
				],
				[
					2.856868817870577,
					9.713353980759948
				],
				[
					0.28568688178700086,
					9.999040862547005
				],
				[
					-1.1427475271482308,
					10.284727744334063
				],
				[
					0.8570606453611163,
					9.713353980759948
				],
				[
					1.1427475271482308,
					9.42766709897289
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06193060427904129,
				0.08000360429286957,
				0.11593084782361984,
				0.1176026314496994,
				0.09385617077350616,
				0.08810129016637802,
				0.11384472995996475,
				0.15252618491649628,
				0.16917940974235535,
				0.161089226603508,
				0.11253588646650314,
				0.02097436599433422,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1630386035,
			"isDeleted": false,
			"id": "5oqvkuw1dKKglp9-ENzce",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 575.7480047568888,
			"y": -62.804758514060566,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.713737635741154,
			"height": 3.71392946323175,
			"seed": 611075241,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.28568688178711454,
					0
				],
				[
					0.5713737635741154,
					0
				],
				[
					3.4282425814446924,
					-1.1427475271482308
				],
				[
					5.713737635741154,
					-2.2854950542964616
				],
				[
					5.428050753954153,
					-1.999808172509404
				],
				[
					3.4282425814446924,
					1.1427475271482308
				],
				[
					3.1425556996576915,
					1.4284344089352885
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.032067473977804184,
				0.14584948122501373,
				0.1722293347120285,
				0.052519042044878006,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 1531047229,
			"isDeleted": false,
			"id": "5PUBMYu1umwxvMA0t90S5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 579.7476211019076,
			"y": -62.804758514060566,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.141980217185846,
			"height": 12.855909680417568,
			"seed": 1681452681,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.28568688178700086,
					0
				],
				[
					-0.5713737635741154,
					0
				],
				[
					-1.1427475271482308,
					0.2856868817870577
				],
				[
					-0.28568688178700086,
					1.9998081725093897
				],
				[
					1.7141212907223462,
					5.428050753954082
				],
				[
					1.9998081725094607,
					8.856293335398775
				],
				[
					-0.28568688178700086,
					11.713162153269337
				],
				[
					-4.285303226805809,
					12.855909680417568
				],
				[
					-7.142172044676386,
					11.427475271482294
				],
				[
					-5.999424517528155,
					8.856293335398775
				],
				[
					-5.4280507539540395,
					8.570606453611717
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.03435598686337471,
				0.07045828551054001,
				0.10918570309877396,
				0.14399303495883942,
				0.17000439763069153,
				0.20894598960876465,
				0.21027593314647675,
				0.1393938958644867,
				0.007829376496374607,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 1678528787,
			"isDeleted": false,
			"id": "i8ZejcbMSVj3oxssSMueY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 585.1756718558618,
			"y": -60.80495034155118,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.285111399315213,
			"height": 5.9994245175281975,
			"seed": 608141289,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8570606453611731,
					0
				],
				[
					1.4284344089352885,
					-0.2856868817870577
				],
				[
					2.2854950542964616,
					-0.8570606453611589
				],
				[
					2.5711819360835193,
					-2.2854950542964474
				],
				[
					0.8570606453611731,
					-2.856868817870563
				],
				[
					-0.5713737635740586,
					-1.714121290722332
				],
				[
					-1.142747527148174,
					1.1427475271482308
				],
				[
					0.2856868817870577,
					2.856868817870577
				],
				[
					2.5711819360835193,
					3.1425556996576347
				],
				[
					4.856676990379981,
					1.7141212907223462
				],
				[
					5.142363872167039,
					1.4284344089352885
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04475497454404831,
				0.10566076636314392,
				0.1610879749059677,
				0.16669170558452606,
				0.10929867625236511,
				0.10620303452014923,
				0.164442777633667,
				0.2021358609199524,
				0.1699891984462738,
				0.03718826174736023,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1852521885,
			"isDeleted": false,
			"id": "347VWMfwRHHigQ1s7z7JC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 595.4603996001958,
			"y": -61.94769786869939,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.999232690037616,
			"height": 5.428050753954082,
			"seed": 973854025,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.2856868817870577,
					0
				],
				[
					-0.8570606453611731,
					0
				],
				[
					-2.5711819360835193,
					0.5713737635741154
				],
				[
					-4.2853032268058655,
					3.1425556996576205
				],
				[
					-3.4282425814446924,
					5.142363872167024
				],
				[
					-0.5713737635741154,
					5.428050753954082
				],
				[
					3.4282425814446924,
					3.1425556996576205
				],
				[
					3.71392946323175,
					2.856868817870563
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.027109986171126366,
				0.10924044996500015,
				0.16553008556365967,
				0.21176299452781677,
				0.22192612290382385,
				0.03869445621967316,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1864808115,
			"isDeleted": false,
			"id": "QmW02bvXMp8SrmT_rvjSi",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 600.8884503541499,
			"y": -68.23280926801466,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.2856868817870577,
			"height": 12.855909680417582,
			"seed": 2135784969,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.2856868817870577
				],
				[
					0,
					-0.5713737635741154
				],
				[
					0,
					0.2856868817870577
				],
				[
					0,
					4.2853032268058655
				],
				[
					0,
					9.999040862547005
				],
				[
					0.2856868817870577,
					12.284535916843467
				],
				[
					0.2856868817870577,
					11.713162153269352
				],
				[
					0.2856868817870577,
					11.427475271482294
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06359240412712097,
				0.07377487421035767,
				0.11482681334018707,
				0.1908549815416336,
				0.2262880504131317,
				0.16623705625534058,
				0.012327605858445168,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 80445949,
			"isDeleted": false,
			"id": "WaYkel98XrkePUPZlOlbY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 596.8888340091311,
			"y": -62.51907163227351,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.999232690037616,
			"height": 1.4284344089352743,
			"seed": 1421293257,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.2856868817870577,
					0
				],
				[
					1.1427475271482308,
					0
				],
				[
					2.2854950542964616,
					0.2856868817870577
				],
				[
					7.4278589264635,
					1.1427475271482308
				],
				[
					7.999232690037616,
					1.4284344089352743
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09631597995758057,
				0.1467359960079193,
				0.15922997891902924,
				0.02315051294863224,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 555968595,
			"isDeleted": false,
			"id": "1l0uuWt6RDQEhe6NZL54v",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 611.173178098484,
			"y": -61.662010986912335,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.4278589264635,
			"height": 7.713545808250544,
			"seed": 212296425,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.85706064536123,
					0
				],
				[
					-1.7141212907223462,
					0
				],
				[
					-2.571181936083576,
					0.5713737635741012
				],
				[
					-2.856868817870577,
					2.2854950542964474
				],
				[
					-0.85706064536123,
					3.9996163450187936
				],
				[
					1.1427475271482308,
					5.142363872167024
				],
				[
					0.5713737635741154,
					5.71373763574114
				],
				[
					-3.1425556996576915,
					6.856485162889371
				],
				[
					-6.285111399315269,
					7.713545808250544
				],
				[
					-5.713737635741154,
					7.713545808250544
				],
				[
					-5.428050753954153,
					7.427858926463486
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08785998821258545,
				0.09955911338329315,
				0.14682146906852722,
				0.17562079429626465,
				0.17363931238651276,
				0.17802740633487701,
				0.17944836616516113,
				0.14519742131233215,
				0.014447998255491257,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 84,
			"versionNonce": 56900189,
			"isDeleted": false,
			"id": "vQF3IoIQXbOzPlm15Ix4T",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 562.8848725627805,
			"y": -36.31580557129334,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.034394600264534,
			"height": 8.487995846357308,
			"seed": 1773328457,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.42439979231784264
				],
				[
					-0.4243997923178995,
					-1.2731993769535848
				],
				[
					-0.4243997923178995,
					0
				],
				[
					0.4243997923178995,
					3.819598130860811
				],
				[
					1.6975991692714842,
					6.790396677085852
				],
				[
					3.8195981308607543,
					5.092797507814396
				],
				[
					4.668397715496553,
					1.6975991692714842
				],
				[
					4.668397715496553,
					0.8487995846357421
				],
				[
					4.243997923178654,
					2.970798546225069
				],
				[
					5.092797507814339,
					5.94159709245011
				],
				[
					7.639196261721565,
					7.214796469403723
				],
				[
					10.185595015628792,
					4.668397715496525
				],
				[
					10.609994807946634,
					0.8487995846357421
				],
				[
					10.185595015628792,
					-0.42439979231784264
				],
				[
					10.185595015628792,
					0.42439979231787106
				],
				[
					10.185595015628792,
					0.8487995846357421
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07776305824518204,
				0.086298368871212,
				0.10981472581624985,
				0.13081543147563934,
				0.12987609207630157,
				0.12192388623952866,
				0.09009823948144913,
				0.07804608345031738,
				0.09594793617725372,
				0.13053745031356812,
				0.17737875878810883,
				0.16763262450695038,
				0.10366647690534592,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 2144921075,
			"isDeleted": false,
			"id": "TzgAFZlpeIYZFK49aZdMJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 577.314465501588,
			"y": -34.19380660970401,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.365996884767981,
			"height": 7.639196261721565,
			"seed": 1131702281,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4243997923178995,
					0.42439979231787106
				],
				[
					-1.2731993769536416,
					0.8487995846357421
				],
				[
					-1.2731993769536416,
					2.121998961589327
				],
				[
					0,
					4.243997923178654
				],
				[
					2.970798546225012,
					5.092797507814396
				],
				[
					5.092797507814339,
					2.970798546225069
				],
				[
					4.66839771549644,
					-0.8487995846357137
				],
				[
					1.6975991692714274,
					-2.5463987539071695
				],
				[
					-0.848799584635799,
					-0.42439979231784264
				],
				[
					0.8487995846356853,
					4.243997923178654
				],
				[
					1.2731993769535848,
					4.243997923178654
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.03124847449362278,
				0.04104684293270111,
				0.05575476214289665,
				0.11219796538352966,
				0.15221133828163147,
				0.18179742991924286,
				0.165782630443573,
				0.11120306700468063,
				0.05331576615571976,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 80,
			"versionNonce": 856090301,
			"isDeleted": false,
			"id": "dXy7zIQM9McjcGjwsxjW8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 583.6804623863559,
			"y": -33.34500702506827,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.941597092450138,
			"height": 6.790396677085852,
			"seed": 140347753,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.42439979231784264,
					0
				],
				[
					-0.8487995846356853,
					-0.42439979231787106
				],
				[
					-1.2731993769535848,
					0
				],
				[
					-1.2731993769535848,
					1.6975991692714558
				],
				[
					0.8487995846357421,
					3.8195981308607827
				],
				[
					3.3951983385429685,
					3.8195981308607827
				],
				[
					4.668397715496553,
					0.8487995846357421
				],
				[
					3.3951983385429685,
					-1.6975991692714558
				],
				[
					0.8487995846357421,
					-2.970798546225069
				],
				[
					0,
					0.8487995846357421
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07236499339342117,
				0.07428793609142303,
				0.09609692543745041,
				0.128581702709198,
				0.16659997403621674,
				0.19248563051223755,
				0.15951327979564667,
				0.09820306301116943,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 80,
			"versionNonce": 307081107,
			"isDeleted": false,
			"id": "x4nm6O-2KhqwSzDxJNzWZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 598.1100553251633,
			"y": -43.955001833014904,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.156393561853804,
			"height": 14.853992731125288,
			"seed": 1998302633,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8487995846357421
				],
				[
					0,
					2.121998961589327
				],
				[
					0.8487995846356853,
					9.33679543099305
				],
				[
					1.2731993769535848,
					11.034394600264505
				],
				[
					0,
					9.761195223310892
				],
				[
					-3.3951983385429685,
					8.063596054039436
				],
				[
					-5.941597092450138,
					9.761195223310892
				],
				[
					-5.941597092450138,
					13.156393561853832
				],
				[
					-3.3951983385429685,
					14.853992731125288
				],
				[
					1.2731993769535848,
					14.853992731125288
				],
				[
					6.365996884767924,
					12.731993769535961
				],
				[
					7.214796469403666,
					12.30759397721809
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06410138309001923,
				0.09080703556537628,
				0.1659439355134964,
				0.18561187386512756,
				0.15817944705486298,
				0.08297308534383774,
				0.09175415337085724,
				0.17608855664730072,
				0.23533779382705688,
				0.20088335871696472,
				0.014415130950510502,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1179977501,
			"isDeleted": false,
			"id": "-myS0JQZBcj_9UIAnHQgE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 622.3008434872816,
			"y": -46.925800379239945,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.365996884767924,
			"height": 23.341988577482567,
			"seed": 1545167337,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.42439979231787106
				],
				[
					0,
					-1.2731993769535848
				],
				[
					-0.8487995846356853,
					0.42439979231787106
				],
				[
					-2.12199896158927,
					6.790396677085823
				],
				[
					-4.66839771549644,
					16.127192108078873
				],
				[
					-6.365996884767924,
					22.068789200528983
				],
				[
					-5.5171973001322385,
					21.64438940821111
				],
				[
					-5.092797507814339,
					21.21998961589324
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.049902770668268204,
				0.07597097754478455,
				0.12927459180355072,
				0.17166626453399658,
				0.13897448778152466,
				0.01913653500378132,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 82,
			"versionNonce": 985154867,
			"isDeleted": false,
			"id": "ftjxvaCzkZzUjci303Iq6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 629.5156399566853,
			"y": -37.589004948246924,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.034394600264477,
			"height": 17.400391485032458,
			"seed": 586269353,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4243997923177858,
					0
				],
				[
					0,
					1.2731993769535848
				],
				[
					1.2731993769535848,
					7.639196261721565
				],
				[
					1.2731993769535848,
					14.005193146489546
				],
				[
					0.4243997923178995,
					16.127192108078873
				],
				[
					-2.1219989615893837,
					13.156393561853804
				],
				[
					-3.395198338542855,
					7.214796469403694
				],
				[
					0.4243997923178995,
					0.8487995846357421
				],
				[
					5.5171973001322385,
					-1.2731993769535848
				],
				[
					7.639196261721622,
					1.2731993769535848
				],
				[
					6.365996884767924,
					5.092797507814396
				],
				[
					3.395198338542855,
					7.639196261721565
				],
				[
					3.395198338542855,
					6.790396677085852
				],
				[
					3.395198338542855,
					6.365996884767981
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04435928165912628,
				0.06814572215080261,
				0.11898653954267502,
				0.14081738889217377,
				0.12658102810382843,
				0.10248660296201706,
				0.07349459826946259,
				0.0722402036190033,
				0.1080356165766716,
				0.1186341866850853,
				0.12852279841899872,
				0.10643173009157181,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 532683645,
			"isDeleted": false,
			"id": "a0JXXeSRX0Hfkl9cFs_gp",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 641.3988341415854,
			"y": -49.04779934082927,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.5463987539071695,
			"height": 17.400391485032458,
			"seed": 1178783913,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.42439979231787106
				],
				[
					0.4243997923178995,
					3.3951983385429116
				],
				[
					1.2731993769536984,
					11.458794392582348
				],
				[
					-0.8487995846355716,
					16.975991692714587
				],
				[
					-1.273199376953471,
					16.975991692714587
				],
				[
					-0.8487995846355716,
					16.551591900396744
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1629265695810318,
				0.1788126826286316,
				0.1526850312948227,
				0.01276416052132845,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1350510291,
			"isDeleted": false,
			"id": "3JCQXnTMmf2qY_U5HMthP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 644.7940324801284,
			"y": -35.042606194339726,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.941597092450138,
			"height": 8.063596054039436,
			"seed": 676911017,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4243997923178995,
					0.42439979231787106
				],
				[
					-1.2731993769535848,
					2.121998961589327
				],
				[
					-0.4243997923178995,
					4.668397715496496
				],
				[
					2.12199896158927,
					5.0927975078143675
				],
				[
					4.668397715496553,
					2.9707985462250406
				],
				[
					4.668397715496553,
					-0.8487995846357421
				],
				[
					1.6975991692714842,
					-2.970798546225069
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.031376250088214874,
				0.08930981159210205,
				0.11235583573579788,
				0.15186429023742676,
				0.1644527018070221,
				0.01325689721852541,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1468638173,
			"isDeleted": false,
			"id": "vjvuL8sDB0FzU1c4-r2vP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 647.7648310263535,
			"y": -35.042606194339726,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.5463987539071695,
			"height": 1.2731993769535848,
			"seed": 1558319945,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4243997923178995,
					0
				],
				[
					1.2731993769535848,
					0.42439979231787106
				],
				[
					2.5463987539071695,
					1.2731993769535848
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0394255667924881,
				0.017668914049863815,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 2050544755,
			"isDeleted": false,
			"id": "P5biUop70qLsRMlb-2fU9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 656.6772266650287,
			"y": -35.89140577897547,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.941597092450138,
			"height": 9.336795430993021,
			"seed": 662654825,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.42439979231787106
				],
				[
					-0.4243997923178995,
					-0.8487995846357137
				],
				[
					-1.2731993769536984,
					-1.2731993769535848
				],
				[
					-2.1219989615893837,
					0.8487995846357421
				],
				[
					-0.4243997923178995,
					3.39519833854294
				],
				[
					1.2731993769535848,
					5.94159709245011
				],
				[
					0.8487995846356853,
					7.639196261721565
				],
				[
					-2.5463987539071695,
					8.063596054039436
				],
				[
					-4.668397715496553,
					6.365996884767981
				],
				[
					-3.819598130860868,
					5.94159709245011
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06570492684841156,
				0.10501791536808014,
				0.11584652960300446,
				0.1218908354640007,
				0.14046160876750946,
				0.17133797705173492,
				0.16369014978408813,
				0.028629180043935776,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 29564989,
			"isDeleted": false,
			"id": "Ei8YLTikNerXyugbWkKCc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 665.5896223037039,
			"y": -47.350200171557816,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.5463987539071695,
			"height": 19.522390446621785,
			"seed": 1796970985,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4243997923178995,
					0.42439979231787106
				],
				[
					-1.2731993769536984,
					0.8487995846357421
				],
				[
					-1.2731993769536984,
					5.94159709245011
				],
				[
					0.4243997923177858,
					13.156393561853804
				],
				[
					0.4243997923177858,
					18.2491910696682
				],
				[
					-1.697599169271598,
					19.522390446621785
				],
				[
					-2.1219989615893837,
					19.522390446621785
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0824589878320694,
				0.11352606117725372,
				0.14532141387462616,
				0.11826352030038834,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1202441747,
			"isDeleted": false,
			"id": "BEaTO7zdpHKuJYmFDweRA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 659.6480252112538,
			"y": -35.89140577897547,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.487995846357308,
			"height": 4.243997923178654,
			"seed": 156916681,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.12199896158927,
					-1.6975991692714558
				],
				[
					5.092797507814339,
					-3.3951983385429116
				],
				[
					8.063596054039408,
					-4.243997923178654
				],
				[
					8.487995846357308,
					-4.243997923178654
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07309475541114807,
				0.015512420795857906,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 877531293,
			"isDeleted": false,
			"id": "do3eUXe07actNvNkoDJjR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 672.8044187731075,
			"y": -34.19380660970401,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.214796469403723,
			"height": 8.063596054039436,
			"seed": 21967113,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.848799584635799,
					0
				],
				[
					2.5463987539071695,
					0
				],
				[
					3.3951983385429685,
					-1.6975991692714558
				],
				[
					1.2731993769535848,
					-2.9707985462250406
				],
				[
					-2.12199896158927,
					-2.121998961589327
				],
				[
					-3.8195981308607543,
					1.6975991692714842
				],
				[
					-1.6975991692713706,
					5.092797507814396
				],
				[
					1.6975991692714842,
					5.092797507814396
				],
				[
					2.12199896158927,
					4.668397715496525
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08445144444704056,
				0.14621658623218536,
				0.10327926278114319,
				0.07254236191511154,
				0.12946847081184387,
				0.14775621891021729,
				0.030783049762248993,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 198087603,
			"isDeleted": false,
			"id": "e7tBukyOW4OvFy-OXzUFW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 677.472816488604,
			"y": -36.31580557129334,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.214796469403723,
			"height": 9.761195223310892,
			"seed": 384764073,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8487995846357421
				],
				[
					0.4243997923177858,
					5.092797507814396
				],
				[
					1.2731993769535848,
					7.639196261721594
				],
				[
					2.12199896158927,
					5.94159709245011
				],
				[
					5.092797507814339,
					0.8487995846357421
				],
				[
					7.214796469403723,
					-2.1219989615892985
				],
				[
					7.214796469403723,
					-2.1219989615892985
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06547311693429947,
				0.08877017349004745,
				0.09472388029098511,
				0.09249084442853928,
				0.11986786127090454,
				0.028710175305604935,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 86,
			"versionNonce": 1289483517,
			"isDeleted": false,
			"id": "3swra7nRxXDB7qVJJR22h",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 718.2151965511191,
			"y": -46.925800379239945,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.156393561853747,
			"height": 14.85399273112526,
			"seed": 1614754441,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4243997923178995,
					0
				],
				[
					-0.848799584635799,
					0.8487995846357137
				],
				[
					-1.2731993769536984,
					1.6975991692714558
				],
				[
					-2.970798546225069,
					6.365996884767981
				],
				[
					-3.3951983385429685,
					11.458794392582348
				],
				[
					-2.5463987539071695,
					14.429592938807417
				],
				[
					0,
					14.85399273112526
				],
				[
					2.970798546225069,
					12.30759397721809
				],
				[
					4.24399792317854,
					10.185595015628763
				],
				[
					3.8195981308607543,
					10.609994807946606
				],
				[
					3.8195981308607543,
					13.580793354171675
				],
				[
					5.092797507814339,
					14.85399273112526
				],
				[
					7.639196261721509,
					13.156393561853804
				],
				[
					9.761195223310779,
					10.185595015628763
				],
				[
					9.336795430992993,
					7.214796469403694
				],
				[
					6.79039667708571,
					6.365996884767981
				],
				[
					2.970798546225069,
					7.639196261721565
				],
				[
					2.5463987539071695,
					8.063596054039436
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06860998272895813,
				0.04179855436086655,
				0.07306244224309921,
				0.11510974168777466,
				0.1381571888923645,
				0.13339684903621674,
				0.12571413815021515,
				0.11164474487304688,
				0.0898316353559494,
				0.080842986702919,
				0.1250782161951065,
				0.16270019114017487,
				0.2052517980337143,
				0.2405676245689392,
				0.23237979412078857,
				0.17954470217227936,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1992795475,
			"isDeleted": false,
			"id": "I0VkSvOOEf7hbemCMwQi6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 725.0055932282048,
			"y": -36.31580557129334,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.3659968847680375,
			"height": 0.8487995846357421,
			"seed": 1424978953,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.546398753907283,
					0.42439979231787106
				],
				[
					3.819598130860868,
					0.8487995846357421
				],
				[
					5.941597092450138,
					0.8487995846357421
				],
				[
					6.3659968847680375,
					0.8487995846357421
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09816817939281464,
				0.1423419564962387,
				0.0709717720746994,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1995328861,
			"isDeleted": false,
			"id": "L4IxDv4LseuPHfGMInfvd",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 737.313187205423,
			"y": -40.984203286789835,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.365996884767924,
			"height": 8.063596054039436,
			"seed": 985995593,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.848799584635799,
					-0.42439979231787106
				],
				[
					-1.6975991692714842,
					-0.42439979231787106
				],
				[
					-4.243997923178654,
					0.42439979231787106
				],
				[
					-4.668397715496553,
					2.121998961589327
				],
				[
					-1.2731993769536984,
					5.0927975078143675
				],
				[
					1.2731993769535848,
					6.365996884767981
				],
				[
					0,
					7.214796469403694
				],
				[
					-3.819598130860868,
					7.639196261721565
				],
				[
					-5.092797507814339,
					7.639196261721565
				],
				[
					-4.668397715496553,
					7.214796469403694
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06348397582769394,
				0.04297628626227379,
				0.0959649384021759,
				0.11617251485586166,
				0.12380017340183258,
				0.1281304955482483,
				0.14831393957138062,
				0.1356278955936432,
				0.007237396202981472,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1877836531,
			"isDeleted": false,
			"id": "EnRHFoSVYeg35cUyW25cm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 748.7719815980054,
			"y": -53.7161970563258,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.5463987539071695,
			"height": 22.068789200528983,
			"seed": 1826460617,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4243997923178995,
					0
				],
				[
					-0.848799584635799,
					0.42439979231787106
				],
				[
					-1.2731993769536984,
					5.94159709245011
				],
				[
					-1.6975991692714842,
					15.27839252344316
				],
				[
					-2.1219989615893837,
					22.068789200528983
				],
				[
					-2.5463987539071695,
					21.64438940821111
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06155325472354889,
				0.16184896230697632,
				0.18044555187225342,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1909889469,
			"isDeleted": false,
			"id": "wMITh43Cc382hGNVzE7dx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 741.9815849209194,
			"y": -42.25740266374342,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.185595015628792,
			"height": 2.5463987539071695,
			"seed": 1671854793,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.5463987539071695,
					0.42439979231784264
				],
				[
					5.5171973001322385,
					0.8487995846357137
				],
				[
					9.761195223311006,
					2.1219989615892985
				],
				[
					10.185595015628792,
					2.5463987539071695
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10043313354253769,
				0.07008731365203857,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 83,
			"versionNonce": 801549459,
			"isDeleted": false,
			"id": "RUxdbioojZ7V0DsG9APkf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 727.5519919821121,
			"y": -60.93099352572949,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 61.96236967840821,
			"height": 46.683977154965135,
			"seed": 1371017225,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.6975991692714842,
					0
				],
				[
					-4.668397715496553,
					0.42439979231787106
				],
				[
					-8.487995846357308,
					2.546398753907198
				],
				[
					-16.55159190039683,
					9.761195223310892
				],
				[
					-19.946790238939684,
					21.21998961589324
				],
				[
					-11.03439460026459,
					35.64958255470066
				],
				[
					2.9707985462249553,
					42.43997923178648
				],
				[
					19.522390446621785,
					40.742380062515025
				],
				[
					34.376383177747016,
					32.254384216157746
				],
				[
					42.015579439468524,
					20.79558982357537
				],
				[
					39.469180685561355,
					5.092797507814396
				],
				[
					28.434786085296878,
					-4.243997923178654
				],
				[
					7.214796469403723,
					-0.8487995846357137
				],
				[
					-17.8247912773503,
					10.609994807946634
				],
				[
					-18.6735908619861,
					11.88319418490022
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.04289394989609718,
				0.045169707387685776,
				0.1119375005364418,
				0.16613350808620453,
				0.21444067358970642,
				0.19213952124118805,
				0.17815682291984558,
				0.1936964988708496,
				0.19771331548690796,
				0.17281365394592285,
				0.15934088826179504,
				0.1302841752767563,
				0.03709036111831665,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 381049373,
			"isDeleted": false,
			"id": "A31QhohzBIR76LliXLV-V",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 358.3184954114023,
			"y": 65.25243871846754,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 3.399648737031157,
			"seed": 1410053353,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.9713282105803387
				],
				[
					0,
					3.399648737031157
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05428598076105118,
				0.00393307488411665,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 436838963,
			"isDeleted": false,
			"id": "lqmv9rurPR4tZDdDlN4ip",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 361.2324800431433,
			"y": 52.13950787563303,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.9713282105803387,
			"height": 27.68285400153954,
			"seed": 1018376745,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.48566410529016935
				],
				[
					-0.48566410529019777,
					3.399648737031157
				],
				[
					-0.9713282105803387,
					11.655938526964007
				],
				[
					-0.9713282105803387,
					23.797541159218184
				],
				[
					-0.9713282105803387,
					27.68285400153954
				],
				[
					-0.48566410529019777,
					27.19718989624934
				],
				[
					-0.48566410529019777,
					26.7115257909592
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15733300149440765,
				0.2312999814748764,
				0.22169271111488342,
				0.16624365746974945,
				0.06897042691707611,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 86,
			"versionNonce": 511643261,
			"isDeleted": false,
			"id": "A54yyzdJLJamURVSCec9U",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 361.71814414843345,
			"y": 56.024820717954356,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.598594948124685,
			"height": 26.7115257909592,
			"seed": 1494264841,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4856641052901409,
					-0.48566410529016935
				],
				[
					-0.9713282105803387,
					-0.48566410529016935
				],
				[
					-0.9713282105803387,
					-0.9713282105803387
				],
				[
					-1.4569923158704796,
					-1.456992315870508
				],
				[
					-0.9713282105803387,
					-2.4283205264508183
				],
				[
					1.9426564211606774,
					-5.342305158191834
				],
				[
					7.284961579352512,
					-6.799297474062342
				],
				[
					9.713282105803387,
					-1.456992315870508
				],
				[
					8.741953895223048,
					5.827969263482004
				],
				[
					6.799297474062371,
					9.713282105803358
				],
				[
					4.8566410529016935,
					8.74195389522302
				],
				[
					4.370976947611496,
					7.770625684642681
				],
				[
					4.370976947611496,
					9.22761800051319
				],
				[
					6.313633368772173,
					13.112930842834515
				],
				[
					10.684610316383669,
					17.96957189573618
				],
				[
					12.141602632254205,
					19.912228316896858
				],
				[
					12.141602632254205,
					19.42656421160669
				],
				[
					11.655938526964007,
					18.94090010631652
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04478698596358299,
				0,
				0.017817169427871704,
				0.0616307370364666,
				0.11140631139278412,
				0.18502536416053772,
				0.22606757283210754,
				0.22361303865909576,
				0.2622639238834381,
				0.2318723499774933,
				0.1579430252313614,
				0.125254824757576,
				0.16730117797851562,
				0.2926149368286133,
				0.296019971370697,
				0.2655665874481201,
				0.09886261075735092,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1469899731,
			"isDeleted": false,
			"id": "tWmFqqP_NaBW_ErRfA6zA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 379.2020519388795,
			"y": 69.62341566607904,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.71328210580333,
			"height": 13.598594948124685,
			"seed": 1427451273,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.9713282105803387,
					0
				],
				[
					1.9426564211606774,
					0
				],
				[
					3.8853128423213548,
					-0.9713282105803387
				],
				[
					4.856641052901637,
					-4.370976947611496
				],
				[
					2.4283205264508183,
					-7.284961579352512
				],
				[
					-0.9713282105803387,
					-3.8853128423213263
				],
				[
					-1.9426564211606774,
					2.913984631741016
				],
				[
					0.9713282105803387,
					6.313633368772173
				],
				[
					7.284961579352512,
					6.313633368772173
				],
				[
					7.770625684642653,
					5.827969263482004
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.017896484583616257,
				0.08788958936929703,
				0.2244039922952652,
				0.20284751057624817,
				0.0830305814743042,
				0.11269088834524155,
				0.2244465947151184,
				0.3075859844684601,
				0.04863864183425903,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 84,
			"versionNonce": 670185181,
			"isDeleted": false,
			"id": "ovk5w7hjY3rjeW07Le7MJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 389.400998149973,
			"y": 72.05173619252989,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.25628978993285,
			"height": 36.91047200205267,
			"seed": 720979977,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.48566410529019777,
					0.48566410529016935
				],
				[
					0,
					0
				],
				[
					1.4569923158704796,
					-1.456992315870508
				],
				[
					4.856641052901637,
					-8.25628978993285
				],
				[
					7.770625684642653,
					-16.5125795798657
				],
				[
					7.284961579352455,
					-20.883556527477197
				],
				[
					4.856641052901637,
					-20.883556527477197
				],
				[
					3.885312842321298,
					-17.96957189573618
				],
				[
					4.370976947611496,
					-14.084259053414854
				],
				[
					6.799297474062314,
					-3.8853128423213548
				],
				[
					7.770625684642653,
					7.770625684642681
				],
				[
					6.799297474062314,
					13.598594948124656
				],
				[
					5.342305158191834,
					16.026915474575475
				],
				[
					1.4569923158704796,
					16.026915474575475
				],
				[
					0,
					10.68461031638364
				],
				[
					-0.48566410529019777,
					9.713282105803302
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13357296586036682,
				0.1568300426006317,
				0.21050824224948883,
				0.17127889394760132,
				0.08587991446256638,
				0.1231338232755661,
				0.15128014981746674,
				0.10409314185380936,
				0.10611794888973236,
				0.14502441883087158,
				0.1933080404996872,
				0.16678939759731293,
				0.1709141582250595,
				0.027027253061532974,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 815198579,
			"isDeleted": false,
			"id": "5ypunGTScAOEDKlEqXPGh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 402.5139289928075,
			"y": 51.16817966505269,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4569923158705365,
			"height": 28.65418221211985,
			"seed": 1935304649,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.48566410529016935
				],
				[
					0.4856641052901409,
					3.8853128423213263
				],
				[
					0.9713282105803387,
					18.45523600102635
				],
				[
					-0.48566410529019777,
					28.16851810682968
				],
				[
					-0.48566410529019777,
					26.22586168566903
				],
				[
					-0.48566410529019777,
					25.254533475088692
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07775998115539551,
				0.20204363763332367,
				0.24826397001743317,
				0.18832755088806152,
				0.033670440316200256,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 2107724605,
			"isDeleted": false,
			"id": "MPYo9vP8-pZnihkFHxdO3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 408.3418982562895,
			"y": 70.10907977136921,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.7706256846427095,
			"height": 9.22761800051316,
			"seed": 1091522249,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.48566410529019777,
					0
				],
				[
					0.9713282105803387,
					0
				],
				[
					2.428320526450875,
					0
				],
				[
					4.8566410529016935,
					0
				],
				[
					5.827969263482032,
					-0.9713282105803387
				],
				[
					4.3709769476115525,
					-4.370976947611496
				],
				[
					1.4569923158705365,
					-4.370976947611496
				],
				[
					0.48566410529019777,
					0.48566410529016935
				],
				[
					2.428320526450875,
					4.856641052901665
				],
				[
					7.284961579352512,
					3.399648737031157
				],
				[
					7.7706256846427095,
					2.9139846317409877
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06064898520708084,
				0.07677673548460007,
				0.11783764511346817,
				0.2166759967803955,
				0.24370886385440826,
				0.16489197313785553,
				0.09116736054420471,
				0.11385620385408401,
				0.1765592098236084,
				0.05653146281838417,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 641616659,
			"isDeleted": false,
			"id": "JcS0Wjsz4wUw95gR20Ce7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 421.94049320441417,
			"y": 68.16642335020853,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.284961579352512,
			"height": 8.25628978993285,
			"seed": 1373993001,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4856641052901409,
					-0.48566410529016935
				],
				[
					-1.4569923158704796,
					-0.9713282105803387
				],
				[
					-2.4283205264508183,
					-0.9713282105803387
				],
				[
					-4.370976947611496,
					1.456992315870508
				],
				[
					-3.885312842321298,
					5.342305158191834
				],
				[
					2.428320526450875,
					7.284961579352512
				],
				[
					2.913984631741016,
					6.799297474062342
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06466897577047348,
				0.1345600038766861,
				0.1959799826145172,
				0.23794299364089966,
				0.22999799251556396,
				0.11161141842603683,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 468575133,
			"isDeleted": false,
			"id": "Y37UudVuuBAdw-qcDoWe1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 432.1394394155077,
			"y": 50.68251555976252,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.9713282105803387,
			"height": 25.254533475088692,
			"seed": 1168388617,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4856641052901409,
					0.48566410529016935
				],
				[
					-0.9713282105803387,
					2.913984631741016
				],
				[
					0,
					12.141602632254177
				],
				[
					0,
					21.369220632767366
				],
				[
					-0.4856641052901409,
					24.768869369798523
				],
				[
					-0.4856641052901409,
					25.254533475088692
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.21774201095104218,
				0.16733340919017792,
				0.12002117931842804,
				0.015555267222225666,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1292464307,
			"isDeleted": false,
			"id": "KS0SDYwWNGv4JGXeeV0jt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 425.3401419414454,
			"y": 64.76677461317738,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.198946211093471,
			"height": 3.399648737031157,
			"seed": 1899682057,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4856641052901409,
					0.9713282105803387
				],
				[
					4.370976947611496,
					2.9139846317409877
				],
				[
					9.71328210580333,
					3.399648737031157
				],
				[
					10.198946211093471,
					3.399648737031157
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08825399726629257,
				0.1854800134897232,
				0.07166086137294769,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1997105149,
			"isDeleted": false,
			"id": "_-1wguXLjHsz8XQ9Z7uV5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 439.91006510015035,
			"y": 67.68075924491836,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.913984631741016,
			"height": 8.25628978993285,
			"seed": 310427209,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.48566410529016935
				],
				[
					0,
					0.9713282105803387
				],
				[
					-0.4856641052901409,
					2.913984631741016
				],
				[
					1.9426564211606774,
					7.770625684642681
				],
				[
					2.428320526450875,
					8.25628978993285
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09576397389173508,
				0.12060672044754028,
				0.019124817103147507,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1721688659,
			"isDeleted": false,
			"id": "Pj3hpx2iicejqbIDCnMEb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 440.8813933107307,
			"y": 63.79544640259704,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.4283205264508183,
			"height": 0.9713282105803387,
			"seed": 761027177,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4856641052901409,
					0
				],
				[
					-1.9426564211606774,
					0.9713282105803387
				],
				[
					-2.4283205264508183,
					0.9713282105803387
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16718900203704834,
				0.08112490922212601,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 16080989,
			"isDeleted": false,
			"id": "qMDvYDx4ZOpw_Dc5ezUqy",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 445.7380343636324,
			"y": 68.16642335020853,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.8853128423213548,
			"height": 6.799297474062342,
			"seed": 1355209353,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.48566410529019777,
					1.9426564211606774
				],
				[
					-0.9713282105803387,
					3.3996487370311854
				],
				[
					-1.4569923158705365,
					5.342305158191834
				],
				[
					-0.48566410529019777,
					6.799297474062342
				],
				[
					0.9713282105803387,
					6.799297474062342
				],
				[
					0.9713282105803387,
					6.313633368772173
				],
				[
					-0.48566410529019777,
					2.4283205264508467
				],
				[
					-2.913984631741016,
					0.48566410529016935
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1309206485748291,
				0.17475000023841858,
				0.18410605192184448,
				0.23115909099578857,
				0.41010400652885437,
				0.2293006330728531,
				0.03988247737288475,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 86,
			"versionNonce": 1003823091,
			"isDeleted": false,
			"id": "CxA8mSkKRrtwby6B20kaE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 441.852721521311,
			"y": 72.53740029782006,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.799297474062314,
			"height": 12.627266737544346,
			"seed": 372208905,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4856641052901409
				],
				[
					-0.4856641052901409,
					1.4569923158704796
				],
				[
					0,
					2.9139846317409877
				],
				[
					1.9426564211606774,
					4.856641052901665
				],
				[
					3.399648737031157,
					4.856641052901665
				],
				[
					4.370976947611496,
					2.9139846317409877
				],
				[
					4.8566410529016935,
					0.9713282105803103
				],
				[
					5.342305158191834,
					-0.48566410529016935
				],
				[
					5.827969263482032,
					-0.48566410529016935
				],
				[
					5.827969263482032,
					0.4856641052901409
				],
				[
					6.313633368772173,
					0
				],
				[
					6.313633368772173,
					-1.9426564211606774
				],
				[
					5.342305158191834,
					-5.342305158191863
				],
				[
					4.370976947611496,
					-7.770625684642681
				],
				[
					2.913984631741016,
					-6.799297474062342
				],
				[
					2.4283205264508183,
					-1.9426564211606774
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06557385623455048,
				0.07229382544755936,
				0.14749634265899658,
				0.1608574241399765,
				0.11264343559741974,
				0.11649966239929199,
				0.05581814423203468,
				0,
				0,
				0.010829712264239788,
				0.07175042480230331,
				0.1572965383529663,
				0.12733468413352966,
				0.08930359035730362,
				0.017802825197577477,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 81,
			"versionNonce": 1870875837,
			"isDeleted": false,
			"id": "1_0TeH8dzdqoMAv6OuC1W",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 448.1663548900832,
			"y": 69.62341566607904,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.170274421673867,
			"height": 12.627266737544375,
			"seed": 164984457,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4856641052901409,
					0.48566410529016935
				],
				[
					-0.9713282105803387,
					0.48566410529016935
				],
				[
					-0.9713282105803387,
					-1.456992315870508
				],
				[
					-0.4856641052901409,
					-2.4283205264508467
				],
				[
					0.48566410529019777,
					-0.9713282105803387
				],
				[
					2.4283205264508183,
					3.399648737031157
				],
				[
					4.8566410529016935,
					6.313633368772173
				],
				[
					5.342305158191834,
					3.8853128423213263
				],
				[
					5.827969263482032,
					-0.48566410529016935
				],
				[
					7.284961579352512,
					-1.456992315870508
				],
				[
					9.22761800051319,
					3.8853128423213263
				],
				[
					10.198946211093528,
					10.198946211093528
				],
				[
					9.71328210580333,
					10.198946211093528
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.03313519433140755,
				0.06146084517240524,
				0.13774359226226807,
				0.20331603288650513,
				0.15817944705486298,
				0.06073553487658501,
				0.049996186047792435,
				0.09587051719427109,
				0.16935190558433533,
				0.21665652096271515,
				0.07636132836341858,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 82,
			"versionNonce": 917678483,
			"isDeleted": false,
			"id": "NLUlE9PHjC0Yidn_e3EGG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 499.56574292120484,
			"y": 15.148047133177897,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.377433292871387,
			"height": 19.201411028260395,
			"seed": 1944773033,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.446544442517677
				],
				[
					0,
					1.339633327553031
				],
				[
					0,
					3.572355540141473
				],
				[
					0.446544442517677,
					11.610155505459772
				],
				[
					0.8930888850354108,
					12.949788833012832
				],
				[
					0.446544442517677,
					12.05669994797745
				],
				[
					-1.339633327553031,
					9.377433292871359
				],
				[
					-4.01889998265915,
					9.377433292871359
				],
				[
					-7.144711080282889,
					13.842877718048186
				],
				[
					-8.484344407835977,
					18.30832214322504
				],
				[
					-6.698166637765269,
					19.201411028260395
				],
				[
					-3.125811097623739,
					19.201411028260395
				],
				[
					0.446544442517677,
					17.41523325818966
				],
				[
					0.8930888850354108,
					17.41523325818966
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09300500154495239,
				0.12275400012731552,
				0.14875400066375732,
				0.21202600002288818,
				0.19792425632476807,
				0.1420474499464035,
				0.11033215373754501,
				0.12064437568187714,
				0.1736750453710556,
				0.2306741327047348,
				0.24755023419857025,
				0.21258041262626648,
				0.02940475381910801,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1112845597,
			"isDeleted": false,
			"id": "gy-QYqOVpOyzHdr7qwKMo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 505.37082067393476,
			"y": 26.311658196119993,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7861777700707648,
			"height": 7.144711080282946,
			"seed": 1906175913,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.44654444251773384,
					0.446544442517677
				],
				[
					-0.44654444251773384,
					1.3396333275530594
				],
				[
					0,
					4.911988867694504
				],
				[
					1.339633327553031,
					7.144711080282946
				],
				[
					1.339633327553031,
					7.144711080282946
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1355028748512268,
				0.19342944025993347,
				0.21053537726402283,
				0.04543936252593994,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 1013841715,
			"isDeleted": false,
			"id": "1yAhl63ZDVrXu5PTj7myM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 507.6035428865232,
			"y": 22.73930265597852,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8930888850354108,
			"height": 0.446544442517677,
			"seed": 1474353097,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8930888850354108,
					-0.446544442517677
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09644400328397751,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 148570493,
			"isDeleted": false,
			"id": "Zv2jLDewkMF_uCYMWbchV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 510.72935398414694,
			"y": 24.972024868566933,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.698166637765269,
			"height": 8.484344407835977,
			"seed": 1293146665,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.446544442517677,
					0
				],
				[
					-0.446544442517677,
					0.446544442517677
				],
				[
					-0.446544442517677,
					1.7861777700707364
				],
				[
					0.446544442517677,
					5.805077752729886
				],
				[
					0.8930888850354108,
					7.591255522800623
				],
				[
					2.232722212588442,
					4.911988867694532
				],
				[
					5.805077752729915,
					-0.893088885035354
				],
				[
					6.251622195247592,
					-0.893088885035354
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09318182617425919,
				0.13666638731956482,
				0.16663900017738342,
				0.15384560823440552,
				0.13671648502349854,
				0.11712570488452911,
				0.07388976961374283,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1198366931,
			"isDeleted": false,
			"id": "q9EDAD-O8m4nHe0ApRson",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 520.553331719536,
			"y": 26.75820263863767,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.484344407835977,
			"height": 10.717066620424418,
			"seed": 188672745,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.446544442517677,
					0
				],
				[
					1.339633327553031,
					0
				],
				[
					2.679266655106119,
					0
				],
				[
					4.465444425176827,
					-1.7861777700707364
				],
				[
					3.125811097623796,
					-3.125811097623796
				],
				[
					-0.446544442517677,
					-0.446544442517677
				],
				[
					-1.339633327553031,
					4.465444425176827
				],
				[
					1.786177770070708,
					7.591255522800623
				],
				[
					6.698166637765269,
					5.805077752729886
				],
				[
					7.144711080282946,
					5.358533310212209
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15293563902378082,
				0.2007099986076355,
				0.22796276211738586,
				0.17574001848697662,
				0.1428450047969818,
				0.21178027987480164,
				0.26981407403945923,
				0.08329889178276062,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1750583773,
			"isDeleted": false,
			"id": "vN_DB58ZlNiajWe-WNffB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 534.3962094375843,
			"y": 24.972024868566933,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.484344407835977,
			"height": 7.144711080282946,
			"seed": 2050880873,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.446544442517677,
					0
				],
				[
					-2.232722212588442,
					0.446544442517677
				],
				[
					-3.125811097623796,
					1.3396333275530594
				],
				[
					-4.01889998265915,
					3.125811097623796
				],
				[
					-3.125811097623796,
					6.251622195247563
				],
				[
					0.446544442517677,
					7.144711080282946
				],
				[
					4.01889998265915,
					3.125811097623796
				],
				[
					4.465444425176827,
					2.679266655106119
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12014321982860565,
				0.17718200385570526,
				0.21863998472690582,
				0.2781539857387543,
				0.23472082614898682,
				0.032984618097543716,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1095241331,
			"isDeleted": false,
			"id": "8FWKT2xQh6rqGGEahqEWX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 542.4340094029026,
			"y": 12.468780478071778,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.893088885035354,
			"height": 19.201411028260395,
			"seed": 1092351529,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.446544442517677
				],
				[
					0,
					2.679266655106119
				],
				[
					0,
					12.503244390495155
				],
				[
					0,
					17.861777700707364
				],
				[
					-0.446544442517677,
					18.754866585742718
				],
				[
					-0.893088885035354,
					18.30832214322504
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08159799128770828,
				0.2577199935913086,
				0.293503999710083,
				0.22714495658874512,
				0.017817290499806404,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1641842237,
			"isDeleted": false,
			"id": "umUzPdDKFnhs8AJc87MEu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 537.0754760926903,
			"y": 23.185847098496197,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.37743329287133,
			"height": 1.3396333275530594,
			"seed": 60063017,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.446544442517677,
					0.8930888850353824
				],
				[
					4.01889998265915,
					1.3396333275530594
				],
				[
					8.930888850353654,
					1.3396333275530594
				],
				[
					9.37743329287133,
					1.3396333275530594
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.33577999472618103,
				0.12516647577285767,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 80,
			"versionNonce": 482592787,
			"isDeleted": false,
			"id": "HiB-LpAlSN2b-gFECsyb_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 556.7234315634685,
			"y": 24.972024868566933,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.484344407836033,
			"height": 16.522144373154305,
			"seed": 462998121,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.893088885035354
				],
				[
					0,
					-0.446544442517677
				],
				[
					0.446544442517677,
					6.251622195247563
				],
				[
					0,
					13.842877718048214
				],
				[
					-1.339633327553031,
					15.62905548811895
				],
				[
					-2.232722212588442,
					10.717066620424418
				],
				[
					-0.893088885035354,
					3.572355540141473
				],
				[
					4.01889998265915,
					-0.446544442517677
				],
				[
					6.251622195247592,
					1.3396333275530594
				],
				[
					5.358533310212181,
					5.805077752729886
				],
				[
					2.232722212588442,
					9.823977735389036
				],
				[
					2.232722212588442,
					9.377433292871359
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09380798041820526,
				0.15233200788497925,
				0.1924576461315155,
				0.21252907812595367,
				0.18655605614185333,
				0.11230899393558502,
				0.10797369480133057,
				0.17284323275089264,
				0.22186905145645142,
				0.22652490437030792,
				0.033021941781044006,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1481291421,
			"isDeleted": false,
			"id": "m13ca6W6lqH_zYh4lQMIc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 565.654320413822,
			"y": 29.43746929374379,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.358533310212238,
			"height": 8.0377999653183,
			"seed": 1877028521,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.446544442517677,
					0.893088885035354
				],
				[
					-0.446544442517677,
					2.2327222125884134
				],
				[
					0.446544442517677,
					3.1258110976237674
				],
				[
					3.125811097623796,
					2.6792666551060904
				],
				[
					4.911988867694561,
					0
				],
				[
					4.911988867694561,
					-3.125811097623796
				],
				[
					2.679266655106119,
					-4.911988867694532
				],
				[
					0.446544442517677,
					-4.018899982659178
				],
				[
					0,
					-4.018899982659178
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08787854015827179,
				0.14117003977298737,
				0.2107459157705307,
				0.2726920545101166,
				0.287564754486084,
				0.1678106039762497,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 802639283,
			"isDeleted": false,
			"id": "7Zv6MF_8kETHtB9aEykWZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 568.7801315114459,
			"y": 28.09783596619073,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.358533310212238,
			"height": 2.2327222125884134,
			"seed": 388942409,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.446544442517677,
					0.893088885035354
				],
				[
					1.7861777700707648,
					2.2327222125884134
				],
				[
					4.465444425176827,
					1.7861777700707364
				],
				[
					5.358533310212238,
					1.3396333275530594
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07513998448848724,
				0.18738800287246704,
				0.06008187681436539,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1448336125,
			"isDeleted": false,
			"id": "NlMS1jQHjYET1QZqzrdw8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 577.7110203617996,
			"y": 12.468780478071778,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3396333275530878,
			"height": 21.880677683366514,
			"seed": 564051849,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.446544442517677
				],
				[
					0.446544442517677,
					-0.446544442517677
				],
				[
					0.446544442517677,
					6.251622195247592
				],
				[
					0,
					16.96868881567201
				],
				[
					-0.446544442517677,
					21.434133240848837
				],
				[
					-0.8930888850354108,
					20.98758879833116
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13961774110794067,
				0.25632601976394653,
				0.3124540150165558,
				0.024577118456363678,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1302929235,
			"isDeleted": false,
			"id": "gUtfWiSCSvIyipWjW5B6R",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 571.0128537240344,
			"y": 24.07893598353158,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.717066620424418,
			"height": 1.7861777700707364,
			"seed": 1739581065,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.446544442517677,
					0
				],
				[
					1.786177770070708,
					0
				],
				[
					6.251622195247592,
					0.893088885035354
				],
				[
					9.823977735389064,
					1.7861777700707364
				],
				[
					10.717066620424418,
					1.7861777700707364
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16769097745418549,
				0.2270199954509735,
				0.20314465463161469,
				0.005267150700092316,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 343503709,
			"isDeleted": false,
			"id": "_hDKUtd8UsVth3R4t0YiN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 584.4091869995648,
			"y": 14.254958248142515,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.805077752729858,
			"height": 19.201411028260424,
			"seed": 385305257,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8930888850353824
				],
				[
					0.446544442517677,
					8.930888850353682
				],
				[
					0.446544442517677,
					16.075599930636628
				],
				[
					0,
					16.96868881567198
				],
				[
					0.446544442517677,
					14.289422160565891
				],
				[
					2.232722212588385,
					10.270522177906741
				],
				[
					4.465444425176827,
					9.823977735389064
				],
				[
					5.805077752729858,
					13.842877718048214
				],
				[
					5.358533310212181,
					18.754866585742718
				],
				[
					4.465444425176827,
					19.201411028260424
				],
				[
					4.465444425176827,
					18.30832214322504
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13603836297988892,
				0.21256399154663086,
				0.26093789935112,
				0.2295737862586975,
				0.15214568376541138,
				0.10799502581357956,
				0.11093679815530777,
				0.25394245982170105,
				0.33195650577545166,
				0.12977856397628784,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 546290931,
			"isDeleted": false,
			"id": "jTsVUp8rMzUChpU6e1jaR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 595.572798062507,
			"y": 27.651291523673052,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.144711080282946,
			"height": 1.339633327553031,
			"seed": 914237449,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.446544442517677
				],
				[
					0.446544442517677,
					0.446544442517677
				],
				[
					2.679266655106062,
					1.339633327553031
				],
				[
					5.805077752729858,
					1.339633327553031
				],
				[
					6.698166637765212,
					0.446544442517677
				],
				[
					7.144711080282946,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11515597254037857,
				0.16342401504516602,
				0.30137398838996887,
				0.3133179843425751,
				0.07930582016706467,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1057816509,
			"isDeleted": false,
			"id": "g4NdFG1O1Npi6zQbRYCzg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 609.8622202230728,
			"y": 22.73930265597852,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.698166637765212,
			"height": 7.591255522800623,
			"seed": 272551689,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.446544442517677
				],
				[
					4.0188999826592635,
					2.2327222125884134
				],
				[
					6.698166637765212,
					3.125811097623796
				],
				[
					6.251622195247592,
					4.01889998265915
				],
				[
					3.5723555401415297,
					5.358533310212209
				],
				[
					1.3396333275530878,
					6.698166637765269
				],
				[
					1.7861777700708217,
					7.591255522800623
				],
				[
					2.232722212588442,
					7.591255522800623
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.20757000148296356,
				0.29810598492622375,
				0.31984639167785645,
				0.3093488812446594,
				0.33884260058403015,
				0.36331138014793396,
				0.10918011516332626,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 1142007443,
			"isDeleted": false,
			"id": "VEVanVbyDJ-LI6H840rhe",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 622.6026717579196,
			"y": 20.048287060446484,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.272382432934933,
			"height": 10.013936629342368,
			"seed": 627525577,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.43538854910184455
				],
				[
					0.8707770982035754,
					2.1769427455091943
				],
				[
					1.7415541964072645,
					7.4016053347313004
				],
				[
					1.7415541964072645,
					9.578548080240523
				],
				[
					1.30616564730542,
					7.4016053347313004
				],
				[
					2.6123312946109536,
					3.9184969419165725
				],
				[
					5.660051138323865,
					0.8707770982036607
				],
				[
					7.836993883833088,
					0
				],
				[
					8.272382432934933,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10563400387763977,
				0.18145853281021118,
				0.14002572000026703,
				0.10576293617486954,
				0.08456479012966156,
				0.1439492553472519,
				0.18335933983325958,
				0.06559201329946518,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 2083520541,
			"isDeleted": false,
			"id": "z4ZsB6QSYF_aDWRCiUycM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 633.4873854854656,
			"y": 22.660618355057522,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.836993883833088,
			"height": 9.143159531138679,
			"seed": 328914793,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.43538854910184455,
					0
				],
				[
					1.3061656473055336,
					-0.43538854910184455
				],
				[
					2.176942745509109,
					-0.8707770982036891
				],
				[
					2.6123312946109536,
					-2.612331294611039
				],
				[
					0.43538854910184455,
					-3.483108392814728
				],
				[
					-2.1769427455092227,
					0
				],
				[
					-1.7415541964073782,
					4.353885491018417
				],
				[
					1.3061656473055336,
					5.660051138323951
				],
				[
					5.224662589222021,
					3.4831083928147564
				],
				[
					5.660051138323865,
					2.6123312946110673
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12590600550174713,
				0.165024995803833,
				0.16544228792190552,
				0.1178056001663208,
				0.13639898598194122,
				0.22708863019943237,
				0.23576165735721588,
				0.018479401245713234,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 81,
			"versionNonce": 518347827,
			"isDeleted": false,
			"id": "czX6VE7rMwGt46IK9EvPH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 645.2428763112152,
			"y": 22.225229805955678,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.836993883833202,
			"height": 25.687924397008715,
			"seed": 1682569159,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.43538854910184455,
					0
				],
				[
					1.7415541964073782,
					-0.8707770982036891
				],
				[
					3.047719843712912,
					-3.0477198437128834
				],
				[
					5.224662589222135,
					-9.143159531138679
				],
				[
					4.3538854910184455,
					-13.497045022157124
				],
				[
					2.6123312946110673,
					-13.497045022157124
				],
				[
					1.3061656473055336,
					-9.143159531138679
				],
				[
					2.1769427455092227,
					-2.612331294611039
				],
				[
					3.918496941916601,
					5.224662589222106
				],
				[
					4.3538854910184455,
					10.013936629342368
				],
				[
					2.1769427455092227,
					11.755490825749746
				],
				[
					-0.8707770982036891,
					12.19087937485159
				],
				[
					-2.6123312946110673,
					11.320102276647901
				],
				[
					-2.1769427455092227,
					9.143159531138707
				],
				[
					-1.7415541964073782,
					8.707770982036863
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.18005026876926422,
				0.21675997972488403,
				0.2301872819662094,
				0.15846145153045654,
				0.13076293468475342,
				0.1681363880634308,
				0.1981978416442871,
				0.19670850038528442,
				0.20022979378700256,
				0.2101556360721588,
				0.208343043923378,
				0.18758535385131836,
				0.038565490394830704,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 835974269,
			"isDeleted": false,
			"id": "fZuWKtMmJfExv0BCF6i1y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 655.6922014896595,
			"y": 8.728184783798554,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3061656473055336,
			"height": 17.85093051317554,
			"seed": 138885351,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.43538854910184455,
					0
				],
				[
					-0.8707770982036891,
					0.8707770982036891
				],
				[
					-0.43538854910184455,
					7.836993883833173
				],
				[
					-0.43538854910184455,
					15.673987767666347
				],
				[
					-1.3061656473055336,
					17.85093051317554
				],
				[
					-1.3061656473055336,
					16.10937631676819
				],
				[
					-0.8707770982036891,
					15.673987767666347
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16730007529258728,
				0.2708439826965332,
				0.32043200731277466,
				0.23565106093883514,
				0.024848967790603638,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 2096192979,
			"isDeleted": false,
			"id": "FmEvSJmIT0mHECoQDKfgu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 660.046086980678,
			"y": 20.4836756095483,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.401605334731357,
			"height": 8.272382432935018,
			"seed": 1520684295,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.43538854910184455,
					0
				],
				[
					0.43538854910184455,
					0.43538854910184455
				],
				[
					3.047719843712912,
					0.8707770982036891
				],
				[
					4.78927404012029,
					-1.3061656473055052
				],
				[
					3.918496941916601,
					-3.0477198437128834
				],
				[
					0,
					-0.8707770982036607
				],
				[
					-0.43538854910184455,
					3.4831083928147564
				],
				[
					2.6123312946110673,
					5.224662589222135
				],
				[
					6.530828236527668,
					4.3538854910184455
				],
				[
					6.966216785629513,
					3.918496941916601
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09731799364089966,
				0.1323930025100708,
				0.22528798878192902,
				0.24724237620830536,
				0.16351929306983948,
				0.14338375627994537,
				0.2534327507019043,
				0.24993304908275604,
				0.08066311478614807,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 196762845,
			"isDeleted": false,
			"id": "h_Pixadgn1zgdKISvT4H-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 671.8015778064276,
			"y": 17.87134431493726,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.401605334731244,
			"height": 6.966216785629484,
			"seed": 85875335,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.43538854910184455,
					0
				],
				[
					-1.30616564730542,
					-0.43538854910184455
				],
				[
					-2.6123312946109536,
					1.7415541964073782
				],
				[
					-2.176942745509109,
					5.224662589222106
				],
				[
					0.43538854910184455,
					6.53082823652764
				],
				[
					4.78927404012029,
					3.483108392814728
				],
				[
					4.78927404012029,
					3.0477198437128834
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06445300579071045,
				0.08643771708011627,
				0.18453000485897064,
				0.24273599684238434,
				0.18809165060520172,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1766599539,
			"isDeleted": false,
			"id": "48jzzcU7QDXRWoe0nipwe",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 679.6385716902608,
			"y": 8.728184783798554,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8707770982036891,
			"height": 19.59248470958289,
			"seed": 308681383,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.8707770982036607
				],
				[
					-0.43538854910184455,
					-0.8707770982036607
				],
				[
					-0.43538854910184455,
					3.047719843712912
				],
				[
					0,
					11.32010227664793
				],
				[
					0.43538854910184455,
					17.415541964073725
				],
				[
					0,
					18.72170761137923
				],
				[
					-0.43538854910184455,
					18.72170761137923
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09880398213863373,
				0.1356080025434494,
				0.22497400641441345,
				0.24862323701381683,
				0.2220233827829361,
				0.0511011965572834,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 1098168637,
			"isDeleted": false,
			"id": "NzTxUVXf_V9NllFcEa_an",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 673.9785205519369,
			"y": 17.87134431493726,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.01393662934231,
			"height": 0,
			"seed": 124434119,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.43538854910184455,
					0
				],
				[
					1.7415541964073782,
					0
				],
				[
					9.578548080240466,
					0
				],
				[
					10.01393662934231,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15358999371528625,
				0.2513920068740845,
				0.036051515489816666,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1211909395,
			"isDeleted": false,
			"id": "Xc3tntu9CuitsH3VFSWKp",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 689.2171197705013,
			"y": 19.61289851134464,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.401605334731357,
			"height": 8.272382432935018,
			"seed": 550155655,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.43538854910184455,
					0
				],
				[
					0.8707770982036891,
					-0.8707770982036891
				],
				[
					0.43538854910184455,
					-1.7415541964073782
				],
				[
					-1.7415541964073782,
					-1.3061656473055336
				],
				[
					-2.6123312946110673,
					2.612331294611039
				],
				[
					-0.43538854910184455,
					6.53082823652764
				],
				[
					3.918496941916601,
					5.660051138323951
				],
				[
					4.78927404012029,
					5.224662589222106
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0906359851360321,
				0.18708200752735138,
				0.15576116740703583,
				0.09438369423151016,
				0.16356506943702698,
				0.18449954688549042,
				0.01908322051167488,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 79,
			"versionNonce": 476350877,
			"isDeleted": false,
			"id": "Fq1mlYVH6KcDPftah6SEU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 701.8433876944548,
			"y": 8.292796234696738,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.57854808024058,
			"height": 18.286319062277357,
			"seed": 1463863495,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.43538854910184455,
					1.3061656473055052
				],
				[
					-0.8707770982036891,
					3.9184969419165725
				],
				[
					-0.8707770982036891,
					7.4016053347313004
				],
				[
					-0.43538854910184455,
					12.626267923953407
				],
				[
					0.43538854910184455,
					13.497045022157096
				],
				[
					0,
					13.061656473055251
				],
				[
					-2.6123312946110673,
					11.320102276647901
				],
				[
					-4.78927404012029,
					11.320102276647901
				],
				[
					-5.660051138323979,
					13.93243357125894
				],
				[
					-4.3538854910184455,
					17.415541964073697
				],
				[
					-1.7415541964073782,
					18.286319062277357
				],
				[
					3.047719843712912,
					17.415541964073697
				],
				[
					3.918496941916601,
					16.980153414971852
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09926998615264893,
				0.12596578896045685,
				0.17717880010604858,
				0.24285848438739777,
				0.22065463662147522,
				0.15587085485458374,
				0.10728298872709274,
				0.10738995671272278,
				0.18093854188919067,
				0.29390326142311096,
				0.2658591866493225,
				0.08311425894498825,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 825764531,
			"isDeleted": false,
			"id": "gmZ3SSXtOlWNwWm0kvH8X",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 723.6128151495469,
			"y": 18.306732864039105,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.578548080240466,
			"height": 17.85093051317554,
			"seed": 1521510311,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					4.353885491018417
				],
				[
					0.43538854910184455,
					14.80321066946263
				],
				[
					0,
					17.85093051317554
				],
				[
					-0.8707770982036891,
					14.80321066946263
				],
				[
					-1.7415541964073782,
					6.095439687425795
				],
				[
					1.3061656473055336,
					0
				],
				[
					6.095439687425824,
					0
				],
				[
					7.836993883833088,
					4.353885491018417
				],
				[
					6.5308282365275545,
					8.27238243293499
				],
				[
					3.918496941916601,
					9.578548080240523
				],
				[
					3.918496941916601,
					9.143159531138679
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17464275658130646,
				0.209056556224823,
				0.2115134596824646,
				0.1264883428812027,
				0.039388276636600494,
				0.061676301062107086,
				0.16269800066947937,
				0.23124194145202637,
				0.23726651072502136,
				0.016604889184236526,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1035685373,
			"isDeleted": false,
			"id": "v7aB5X4XTGCRSC42bymxT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 734.4975288770929,
			"y": 20.919064158650144,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.966216785629513,
			"height": 6.53082823652764,
			"seed": 1258211399,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8707770982036891,
					1.7415541964073782
				],
				[
					-0.8707770982036891,
					3.047719843712912
				],
				[
					0.8707770982036891,
					4.3538854910184455
				],
				[
					2.6123312946110673,
					4.3538854910184455
				],
				[
					5.660051138323979,
					1.7415541964073782
				],
				[
					6.095439687425824,
					-0.8707770982036607
				],
				[
					2.1769427455092227,
					-2.1769427455091943
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10779427736997604,
				0.11083575338125229,
				0.18033984303474426,
				0.1988648921251297,
				0.22158394753932953,
				0.2124517560005188,
				0.018201477825641632,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 149314643,
			"isDeleted": false,
			"id": "tVeAwZUCPyIqb56GsqUxb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 739.2868029172132,
			"y": 22.660618355057522,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.966216785629513,
			"height": 4.353885491018417,
			"seed": 228024999,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8707770982036891,
					0.43538854910184455
				],
				[
					2.1769427455092227,
					0.8707770982036891
				],
				[
					3.4831083928147564,
					0.8707770982036891
				],
				[
					6.530828236527668,
					-2.612331294611039
				],
				[
					6.966216785629513,
					-3.483108392814728
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14727047085762024,
				0.17429599165916443,
				0.019306641072034836,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 612009565,
			"isDeleted": false,
			"id": "C0HruHgMLGmxOPmYNAZNs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 750.6069051938612,
			"y": 6.5512420382893595,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.1769427455092227,
			"height": 20.027873258684735,
			"seed": 205993095,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.43538854910184455
				],
				[
					-0.8707770982036891,
					6.966216785629484
				],
				[
					-0.8707770982036891,
					15.673987767666318
				],
				[
					-1.3061656473055336,
					20.027873258684735
				],
				[
					-1.7415541964073782,
					19.59248470958292
				],
				[
					-2.1769427455092227,
					19.157096160481075
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14456945657730103,
				0.23072198033332825,
				0.284496009349823,
				0.21667221188545227,
				0.017914123833179474,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 1528650227,
			"isDeleted": false,
			"id": "NAvIuH68QGp1A6LfzBeO1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 742.769911310028,
			"y": 18.306732864039105,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.143159531138735,
			"height": 2.1769427455091943,
			"seed": 1492450695,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.43538854910184455,
					0.43538854910184455
				],
				[
					2.1769427455092227,
					0.8707770982036891
				],
				[
					8.707770982036891,
					1.7415541964073782
				],
				[
					9.143159531138735,
					2.1769427455091943
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14394348859786987,
				0.21952398121356964,
				0.12058380246162415,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1936962237,
			"isDeleted": false,
			"id": "roj9jS7A1TZVjG2voBu8e",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 756.702344881287,
			"y": 7.422019136493049,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.966216785629513,
			"height": 19.59248470958289,
			"seed": 320924743,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.43538854910184455
				],
				[
					0.8707770982036891,
					8.27238243293499
				],
				[
					1.3061656473055336,
					15.238599218564474
				],
				[
					1.3061656473055336,
					16.109376316768163
				],
				[
					1.3061656473055336,
					13.93243357125894
				],
				[
					2.6123312946110673,
					10.884713727546057
				],
				[
					5.224662589222135,
					10.449325178444212
				],
				[
					6.966216785629513,
					13.93243357125894
				],
				[
					6.966216785629513,
					19.59248470958289
				],
				[
					6.530828236527668,
					19.59248470958289
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11733505129814148,
				0.17421434819698334,
				0.1794196516275406,
				0.13755163550376892,
				0.05325353890657425,
				0.005235717631876469,
				0.019404876977205276,
				0.1224621906876564,
				0.16391098499298096,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1961075603,
			"isDeleted": false,
			"id": "LLWqsFa1II6Jtgya08O0Y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 642.6305450166042,
			"y": 43.99465726104782,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.401605334731357,
			"height": 24.817147298804997,
			"seed": 411998663,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8707770982036891,
					0.4353885491018161
				],
				[
					-1.7415541964073782,
					1.7415541964073498
				],
				[
					-2.1769427455092227,
					3.9184969419165725
				],
				[
					-3.047719843712912,
					14.80321066946263
				],
				[
					-1.3061656473055336,
					23.075593102397647
				],
				[
					2.1769427455092227,
					24.817147298804997
				],
				[
					3.918496941916601,
					24.381758749703152
				],
				[
					4.3538854910184455,
					23.946370200601308
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07342098653316498,
				0.06931393593549728,
				0.07030130177736282,
				0.22215917706489563,
				0.3247160017490387,
				0.32595041394233704,
				0.04217568784952164,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 2001228573,
			"isDeleted": false,
			"id": "jf3cMPiyNyBOYo7XSypbn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 652.6444816459466,
			"y": 60.97481067601967,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.143159531138735,
			"height": 10.013936629342368,
			"seed": 1170234631,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.43538854910184455,
					0
				],
				[
					3.047719843712912,
					1.7415541964073498
				],
				[
					7.401605334731357,
					5.660051138323951
				],
				[
					9.143159531138735,
					7.836993883833145
				],
				[
					8.272382432935046,
					9.143159531138679
				],
				[
					4.78927404012029,
					9.578548080240523
				],
				[
					1.7415541964073782,
					10.013936629342368
				],
				[
					0.8707770982036891,
					9.578548080240523
				],
				[
					2.1769427455092227,
					9.143159531138679
				],
				[
					2.6123312946110673,
					8.707770982036834
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1491359919309616,
				0.22831198573112488,
				0.22726787626743317,
				0.18931451439857483,
				0.16494262218475342,
				0.18527404963970184,
				0.25337862968444824,
				0.29054054617881775,
				0.05591979995369911,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 1047509299,
			"isDeleted": false,
			"id": "Txv0mkJcH_5MOFRc8eTrC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 671.0482989339795,
			"y": 62.041242070404536,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.400538546002963,
			"height": 2.2286868312863533,
			"seed": 1810033287,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7428956104287181,
					0
				],
				[
					4.45737366257265,
					1.1143434156431624
				],
				[
					10.029090740788547,
					1.8572390260719658
				],
				[
					10.400538546002963,
					2.2286868312863533
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19527648389339447,
				0.289000004529953,
				0.09260519593954086,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 1818879869,
			"isDeleted": false,
			"id": "TEAxPwR-cX_77Trs88PTb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 673.2769857652659,
			"y": 69.4701981746924,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.428956104287863,
			"height": 0.37144780521438747,
			"seed": 2012813639,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.37144780521438747
				],
				[
					3.3430302469295157,
					-0.37144780521438747
				],
				[
					7.057508299073447,
					0
				],
				[
					7.428956104287863,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12855148315429688,
				0.23304198682308197,
				0.09735574573278427,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1428691667,
			"isDeleted": false,
			"id": "H9vG96nGdli3pL9q6NI4T",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 684.0489721164832,
			"y": 59.44110743390377,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.372120987718176,
			"height": 17.458046845076495,
			"seed": 1422735367,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7428956104288318,
					-0.37144780521438747
				],
				[
					-1.1143434156432477,
					-0.37144780521438747
				],
				[
					-2.6001346365007976,
					0.7428956104288034
				],
				[
					-8.171851714716695,
					7.800403909502279
				],
				[
					-13.372120987718176,
					15.972255624218946
				],
				[
					-12.629225377289345,
					17.086599039862108
				],
				[
					-12.257777572075042,
					16.71515123464772
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11592648178339005,
				0.135320246219635,
				0.2112545222043991,
				0.25000399351119995,
				0.24418343603610992,
				0.071772001683712,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 85585885,
			"isDeleted": false,
			"id": "knDyNhlnwPnl0Cfi_Mjc6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 696.3067496885583,
			"y": 50.15491230354394,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.6001346365007976,
			"height": 22.286868312863618,
			"seed": 1865926695,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.3714478052143022,
					4.828821467787122
				],
				[
					-0.7428956104288318,
					17.458046845076495
				],
				[
					-2.2286868312864954,
					22.286868312863618
				],
				[
					-1.4857912208576636,
					21.172524897220427
				],
				[
					-1.1143434156432477,
					20.429629286791652
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19407400488853455,
				0.2794699966907501,
				0.26194217801094055,
				0.02042999304831028,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1705199731,
			"isDeleted": false,
			"id": "5hoLW2HZV0jXUdl24D7Q-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 699.6497799354878,
			"y": 66.87006353819166,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.571717078215897,
			"height": 4.828821467787122,
			"seed": 1859701255,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.3714478052144159,
					0
				],
				[
					1.8572390260719658,
					-0.7428956104288034
				],
				[
					2.9715824417150998,
					-1.8572390260719942
				],
				[
					2.2286868312863817,
					-2.600134636500769
				],
				[
					0.3714478052144159,
					-1.8572390260719942
				],
				[
					-0.3714478052144159,
					0
				],
				[
					-0.3714478052144159,
					1.4857912208575499
				],
				[
					1.8572390260719658,
					1.8572390260719658
				],
				[
					4.828821467787066,
					2.2286868312863533
				],
				[
					5.2002692730014815,
					2.2286868312863533
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17051199078559875,
				0.25228798389434814,
				0.2509361207485199,
				0.11589895933866501,
				0.06946847587823868,
				0.14115145802497864,
				0.2398776262998581,
				0.2723597586154938,
				0.09273193031549454,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 795470909,
			"isDeleted": false,
			"id": "bz2ZLCmqq44l8OFKc6Jyl",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 708.5645272606332,
			"y": 65.38427231733408,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.943164883430313,
			"height": 8.914747325145441,
			"seed": 945805191,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.37144780521438747
				],
				[
					0.3714478052144159,
					1.4857912208575783
				],
				[
					1.4857912208575499,
					2.6001346365007407
				],
				[
					2.6001346365007976,
					0.37144780521438747
				],
				[
					4.457373662572763,
					-2.600134636500769
				],
				[
					5.571717078215897,
					-2.9715824417151566
				],
				[
					5.943164883430313,
					1.1143434156431624
				],
				[
					5.2002692730014815,
					5.571717078215897
				],
				[
					5.2002692730014815,
					5.943164883430285
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10309924185276031,
				0.1248888224363327,
				0.08416427671909332,
				0.05655413866043091,
				0.15800000727176666,
				0.20163674652576447,
				0.05909646674990654,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1168622099,
			"isDeleted": false,
			"id": "z0OIfz0imBvLt0FaKpEtN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 718.5936180014219,
			"y": 65.01282451211966,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.571717078215897,
			"height": 6.686060493859088,
			"seed": 2032695783,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7428956104288318,
					0.7428956104288034
				],
				[
					-1.4857912208576636,
					2.2286868312863817
				],
				[
					-0.3714478052144159,
					5.571717078215926
				],
				[
					1.8572390260719658,
					5.571717078215926
				],
				[
					4.085925857358234,
					2.2286868312863817
				],
				[
					4.085925857358234,
					-1.1143434156431624
				],
				[
					1.114343415643134,
					-0.37144780521438747
				],
				[
					-0.3714478052144159,
					2.9715824417151566
				],
				[
					-0.3714478052144159,
					3.71447805214396
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09787100553512573,
				0.1693039834499359,
				0.1882798820734024,
				0.1286018341779709,
				0.09279192984104156,
				0.07806256413459778,
				0.028794463723897934,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 456875165,
			"isDeleted": false,
			"id": "BJofgFr6loCMj13U0xb9s",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 722.6795438587801,
			"y": 64.26992890169089,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.514881961646097,
			"height": 17.458046845076495,
			"seed": 170350663,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7428956104287181,
					0
				],
				[
					-0.7428956104287181,
					0.37144780521438747
				],
				[
					-0.7428956104287181,
					1.4857912208575783
				],
				[
					-0.3714478052143022,
					5.943164883430313
				],
				[
					-0.3714478052143022,
					11.51488196164621
				],
				[
					-2.9715824417150998,
					15.972255624218917
				],
				[
					-7.428956104287863,
					17.458046845076495
				],
				[
					-11.514881961646097,
					13.743568792932564
				],
				[
					-11.143434156431795,
					13.372120987718176
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07654086500406265,
				0.13416776061058044,
				0.14722326397895813,
				0.21082571148872375,
				0.2945308983325958,
				0.2665885090827942,
				0.021584991365671158,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 1311508403,
			"isDeleted": false,
			"id": "TWEMSbxEUfEvuF29iL2ze",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 730.8513955734968,
			"y": 53.126494745259066,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.8572390260719658,
			"height": 16.71515123464772,
			"seed": 154792615,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.37144780521438747
				],
				[
					0.3714478052144159,
					1.4857912208575783
				],
				[
					0.3714478052144159,
					10.400538546003048
				],
				[
					-1.114343415643134,
					16.343703429433333
				],
				[
					-1.4857912208575499,
					16.343703429433333
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0957377627491951,
				0.1470600962638855,
				0.2351589947938919,
				0.0812317505478859,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 4178173,
			"isDeleted": false,
			"id": "MST9tDpg3GcDVC4Ok-MS0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 724.5367828848521,
			"y": 61.29834645997573,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.400538546003077,
			"height": 3.343030246929544,
			"seed": 57394311,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.3714478052144159
				],
				[
					2.2286868312864954,
					0.7428956104288034
				],
				[
					10.02909074078866,
					2.9715824417151566
				],
				[
					10.400538546003077,
					3.343030246929544
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16996200382709503,
				0.15074364840984344,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 94,
			"versionNonce": 1968609619,
			"isDeleted": false,
			"id": "H6JSDRdj9p1CWTdsuhN4v",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 756.8527419385043,
			"y": 66.12716792776286,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.257777572074929,
			"height": 18.943838065934074,
			"seed": 1301705543,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.3714478052143022,
					0
				],
				[
					-0.7428956104287181,
					-0.37144780521438747
				],
				[
					-1.114343415643134,
					-0.7428956104287749
				],
				[
					-1.8572390260719658,
					-1.1143434156431908
				],
				[
					-3.7144780521439316,
					-1.8572390260719658
				],
				[
					-8.543299519930997,
					-9.286195130359829
				],
				[
					-8.543299519930997,
					-10.40053854600302
				],
				[
					-8.171851714716581,
					-11.886329766860598
				],
				[
					-6.3146126886446154,
					-15.229360013790142
				],
				[
					-3.343030246929402,
					-16.71515123464772
				],
				[
					-1.114343415643134,
					-17.458046845076495
				],
				[
					2.2286868312864954,
					-16.71515123464772
				],
				[
					3.7144780521439316,
					-14.115016598146951
				],
				[
					3.7144780521439316,
					-12.257777572074986
				],
				[
					2.2286868312864954,
					-11.51488196164621
				],
				[
					0,
					-9.657642935574245
				],
				[
					-2.228686831286268,
					-8.171851714716666
				],
				[
					-4.45737366257265,
					-7.428956104287863
				],
				[
					-6.3146126886446154,
					-6.314612688644701
				],
				[
					-7.800403909502165,
					-4.828821467787122
				],
				[
					-8.543299519930997,
					-2.9715824417151566
				],
				[
					-8.543299519930997,
					-0.37144780521438747
				],
				[
					-8.543299519930997,
					1.4857912208575783
				],
				[
					-8.171851714716581,
					1.1143434156431908
				],
				[
					-4.45737366257265,
					-0.7428956104287749
				],
				[
					-0.3714478052143022,
					-3.343030246929544
				],
				[
					2.6001346365007976,
					-5.571717078215897
				],
				[
					2.9715824417152135,
					-5.943164883430285
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07964498549699783,
				0.17958199977874756,
				0.22079525887966156,
				0.23691150546073914,
				0.20144592225551605,
				0.17418140172958374,
				0.16788968443870544,
				0.16332806646823883,
				0.17111383378505707,
				0.16846807301044464,
				0.17343853414058685,
				0.17121581733226776,
				0.13681484758853912,
				0.1363850086927414,
				0.1445021629333496,
				0.1272931843996048,
				0.13020144402980804,
				0.15980948507785797,
				0.151325523853302,
				0.15649008750915527,
				0.14027486741542816,
				0.13962584733963013,
				0.15432751178741455,
				0.1809747964143753,
				0.1756911277770996,
				0.19482462108135223,
				0.12005709856748581,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 603494749,
			"isDeleted": false,
			"id": "6vNZWP8sQM8vMPcCgC_MI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 778.0252668357248,
			"y": 56.46952499218861,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.428956104287863,
			"height": 9.657642935574245,
			"seed": 400354567,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.3714478052144159
				],
				[
					0.3714478052144159,
					0.3714478052144159
				],
				[
					0.7428956104288318,
					0.3714478052144159
				],
				[
					4.828821467787179,
					2.2286868312863817
				],
				[
					7.057508299073561,
					3.343030246929544
				],
				[
					7.057508299073561,
					3.71447805214396
				],
				[
					4.457373662572763,
					4.828821467787122
				],
				[
					1.1143434156432477,
					6.686060493859088
				],
				[
					-0.3714478052143022,
					8.91474732514547
				],
				[
					1.1143434156432477,
					9.657642935574245
				],
				[
					1.4857912208576636,
					9.286195130359857
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08356893807649612,
				0.092247374355793,
				0.13205768167972565,
				0.2157514989376068,
				0.1763964593410492,
				0.1013503149151802,
				0.09081823378801346,
				0.18093426525592804,
				0.26714226603507996,
				0.0866282656788826,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 69,
			"versionNonce": 679343859,
			"isDeleted": false,
			"id": "IpWb034p3esC9UC7JWVo2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 798.3177442309191,
			"y": 57.926448125707395,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 0.38127422156446755,
			"seed": 134517159,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.38127422156446755
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.037591706961393356,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 80,
			"versionNonce": 532112829,
			"isDeleted": false,
			"id": "r62pNp8GBqLesXyI-BjLB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 801.3679380034348,
			"y": 45.72567303564446,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.388032874418172,
			"height": 19.44498529978779,
			"seed": 1829873991,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.38127422156446755,
					0.38127422156446755
				],
				[
					-0.7625484431289351,
					1.9063711078223378
				],
				[
					-0.7625484431289351,
					8.769307095982725
				],
				[
					-0.7625484431289351,
					14.869694641014206
				],
				[
					-0.7625484431289351,
					16.01351730570761
				],
				[
					-0.7625484431289351,
					14.107146197885271
				],
				[
					-2.2876453293868053,
					9.913129760676128
				],
				[
					-4.575290658773611,
					8.769307095982725
				],
				[
					-6.481661766595948,
					11.819500868498466
				],
				[
					-7.24421020972477,
					16.776065748836515
				],
				[
					-4.575290658773611,
					19.44498529978779
				],
				[
					-1.5250968862578702,
					19.44498529978779
				],
				[
					0.7625484431289351,
					17.53861419196545
				],
				[
					1.1438226646934027,
					17.157339970400983
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07391226291656494,
				0.12359905987977982,
				0.2379699945449829,
				0.26835551857948303,
				0.2771802842617035,
				0.21890346705913544,
				0.19836224615573883,
				0.213457390666008,
				0.23834805190563202,
				0.2639336884021759,
				0.24026885628700256,
				0.21629610657691956,
				0.11519332975149155,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1713938579,
			"isDeleted": false,
			"id": "P8iMyDoR8le7LzWc6lNTJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 807.8495997700307,
			"y": 60.2140934550942,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.150581317547221,
			"height": 8.388032874418258,
			"seed": 1467136839,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.38127422156446755,
					-0.7625484431289351
				],
				[
					0.38127422156446755,
					-3.0501937725157404
				],
				[
					-1.5250968862578702,
					-4.956564880338078
				],
				[
					-3.8127422156446755,
					-2.2876453293868053
				],
				[
					-3.8127422156446755,
					2.287645329386777
				],
				[
					-1.5250968862578702,
					3.4314679940801796
				],
				[
					4.575290658773611,
					-1.1438226646934027
				],
				[
					5.337839101902546,
					-1.9063711078223378
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.21705199778079987,
				0.18710443377494812,
				0.1471477597951889,
				0.20260553061962128,
				0.3103373944759369,
				0.2897075116634369,
				0.06976135075092316,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1721607709,
			"isDeleted": false,
			"id": "OEgLJZRJfBDdpMt2u1gXS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 819.2878264169647,
			"y": 41.91293081999979,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.143822664693289,
			"height": 22.876453293867996,
			"seed": 691052167,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.38127422156435387,
					0
				],
				[
					-0.7625484431289351,
					0
				],
				[
					-1.143822664693289,
					1.1438226646934027
				],
				[
					-1.143822664693289,
					9.53185553911166
				],
				[
					-1.143822664693289,
					17.919888413529947
				],
				[
					-1.143822664693289,
					22.876453293867996
				],
				[
					-0.7625484431289351,
					22.876453293867996
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16318850219249725,
				0.20095598697662354,
				0.24500799179077148,
				0.19786444306373596,
				0.014958374202251434,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 403510835,
			"isDeleted": false,
			"id": "FabgPMoVO8xA5XQwQxHlb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 821.5754717463515,
			"y": 56.78262546101399,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.7191133234669,
			"height": 8.00675865285379,
			"seed": 713809575,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7625484431289351,
					0.38127422156446755
				],
				[
					-1.143822664693289,
					1.1438226646934027
				],
				[
					-0.7625484431289351,
					2.2876453293868053
				],
				[
					1.5250968862578702,
					4.956564880338078
				],
				[
					3.8127422156446755,
					6.100387545031452
				],
				[
					4.575290658773611,
					3.8127422156446755
				],
				[
					4.575290658773611,
					0.38127422156446755
				],
				[
					2.2876453293868053,
					-1.9063711078223378
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08277798444032669,
				0.06936825811862946,
				0.03522900491952896,
				0.12802423536777496,
				0.15651679039001465,
				0.16625891625881195,
				0.057403046637773514,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 194828925,
			"isDeleted": false,
			"id": "Id_e6bU3auvAv80TYOPLU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 824.6256655188672,
			"y": 59.0702707904008,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.0501937725157404,
			"height": 2.668919550951273,
			"seed": 1720515623,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.38127422156458124,
					0.38127422156446755
				],
				[
					0.7625484431289351,
					1.1438226646934027
				],
				[
					2.6689195509513866,
					2.668919550951273
				],
				[
					3.0501937725157404,
					2.668919550951273
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.1600322276353836,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 756144083,
			"isDeleted": false,
			"id": "O5OKi9XfwZt_NwZZB-bMP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 831.4886015070276,
			"y": 57.16389968257846,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.194016437209257,
			"height": 5.337839101902517,
			"seed": 1150382823,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.38127422156458124,
					2.2876453293868053
				],
				[
					1.1438226646935163,
					3.8127422156446755
				],
				[
					3.8127422156446755,
					5.337839101902517
				],
				[
					4.194016437209257,
					5.337839101902517
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08931197971105576,
				0.08931197971105576,
				0.07206564396619797,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 1198949085,
			"isDeleted": false,
			"id": "eqPRKAtyPr4GLVBVSKR1M",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 838.351537495188,
			"y": 56.401351239449525,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.575290658773611,
			"height": 18.682436856658853,
			"seed": 234740135,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.143822664693289,
					1.5250968862578702
				],
				[
					-1.906371107822224,
					3.431467994080208
				],
				[
					-2.668919550951159,
					6.48166176659592
				],
				[
					-4.194016437209029,
					17.919888413529918
				],
				[
					-4.575290658773611,
					18.682436856658853
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14191198348999023,
				0.2647404968738556,
				0.32944878935813904,
				0.17800527811050415,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 1934452083,
			"isDeleted": false,
			"id": "SmG3RDYXePTybJ0GXvV_8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 725.5633930862665,
			"y": 84.80338985269663,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.03380311732974,
			"height": 3.6956467298167013,
			"seed": 233409415,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8212548288481685,
					0
				],
				[
					4.927528973088897,
					1.6425096576963085
				],
				[
					9.03380311732974,
					2.8743919009685612
				],
				[
					8.212548288481571,
					3.6956467298167013
				],
				[
					7.801920874057487,
					3.6956467298167013
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08018799126148224,
				0.21404598653316498,
				0.23136794567108154,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 1052516157,
			"isDeleted": false,
			"id": "lK8yI_n0j2-eVqWzt5KJA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 727.2059027439628,
			"y": 91.78405589790594,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.391293459633403,
			"height": 2.0531370721203928,
			"seed": 1529485671,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.41062741442408424,
					-0.82125482884814
				],
				[
					3.6956467298166444,
					-2.0531370721203928
				],
				[
					6.980666045209205,
					-1.2318822432722243
				],
				[
					7.391293459633403,
					-0.41062741442408424
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15536199510097504,
				0.3185639977455139,
				0.13001684844493866,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 839270163,
			"isDeleted": false,
			"id": "SstjLDNROZUWHX327wWDW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 693.1238273467644,
			"y": 105.3347605739005,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2318822432722527,
			"height": 9.033803117329683,
			"seed": 344432679,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4106274144240558
				],
				[
					0,
					4.106274144240757
				],
				[
					0.8212548288481685,
					9.033803117329683
				],
				[
					1.2318822432722527,
					8.623175702905598
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10633200407028198,
				0.17316198348999023,
				0.05248638987541199,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 131018653,
			"isDeleted": false,
			"id": "ePhgaStlhU4Jup4SbFVis",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 694.3557095900367,
			"y": 100.40723160081157,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.642509657696337,
			"height": 1.6425096576963085,
			"seed": 1195448039,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8212548288481685,
					-0.41062741442408424
				],
				[
					-1.642509657696337,
					-0.41062741442408424
				],
				[
					-1.642509657696337,
					1.2318822432722243
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0780239850282669,
				0.09157614409923553,
				0.0823977068066597,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 62055603,
			"isDeleted": false,
			"id": "YkrEQPiiEMmXWfvddDmiV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 701.7470030496701,
			"y": 103.2816235017801,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.623175702905542,
			"height": 9.444430531753767,
			"seed": 871510215,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.41062741442408424,
					0.82125482884814
				],
				[
					1.2318822432722527,
					6.98066604520929
				],
				[
					1.6425096576962233,
					8.623175702905598
				],
				[
					3.28501931539256,
					8.212548288481543
				],
				[
					6.15941121636115,
					4.106274144240757
				],
				[
					8.212548288481571,
					2.0531370721203928
				],
				[
					8.623175702905542,
					4.106274144240757
				],
				[
					8.623175702905542,
					7.801920874057458
				],
				[
					8.623175702905542,
					9.444430531753767
				],
				[
					8.623175702905542,
					9.033803117329683
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1457033008337021,
				0.1728437840938568,
				0.19521771371364594,
				0.1645570695400238,
				0.08149844408035278,
				0.07881448417901993,
				0.13165006041526794,
				0.15569674968719482,
				0.04082653671503067,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1893807101,
			"isDeleted": false,
			"id": "d9LTxFRGjUI4ys286JOt0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 716.1189625545128,
			"y": 95.8903300421467,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.231882243272139,
			"height": 17.65697882023531,
			"seed": 2007834183,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.41062741442408424,
					-0.4106274144240558
				],
				[
					-0.8212548288481685,
					-0.4106274144240558
				],
				[
					-0.8212548288481685,
					-1.6425096576963085
				],
				[
					-0.41062741442408424,
					-2.0531370721203643
				],
				[
					0.41062741442397055,
					2.0531370721203928
				],
				[
					0.41062741442397055,
					9.855057946177851
				],
				[
					0.41062741442397055,
					15.603841748114945
				],
				[
					0.41062741442397055,
					15.603841748114945
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.05054742470383644,
				0.01477368175983429,
				0.05432351678609848,
				0.13418051600456238,
				0.22283399105072021,
				0.08490853756666183,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 69,
			"versionNonce": 1878644307,
			"isDeleted": false,
			"id": "exhvFTrH0wrbStN-so9gN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 711.1914335814238,
			"y": 102.46036867293193,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.623175702905655,
			"height": 1.2318822432722527,
			"seed": 1348157831,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8212548288481685,
					0
				],
				[
					7.801920874057487,
					1.2318822432722527
				],
				[
					8.623175702905655,
					1.2318822432722527
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19067688286304474,
				0.10736807435750961,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 99855453,
			"isDeleted": false,
			"id": "qZiq3eYhvVo8e_FOaou5-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 722.6890011852979,
			"y": 103.69225091620419,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.338156387513095,
			"height": 9.444430531753767,
			"seed": 1709075751,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4106274144241979,
					0
				],
				[
					0.8212548288481685,
					-0.41062741442408424
				],
				[
					2.4637644865445054,
					-0.8212548288481685
				],
				[
					4.927528973089011,
					-1.2318822432722527
				],
				[
					4.106274144240842,
					-2.463764486544477
				],
				[
					2.053137072120421,
					-2.8743919009685612
				],
				[
					0.4106274144241979,
					1.2318822432722243
				],
				[
					0.4106274144241979,
					5.748783801937066
				],
				[
					4.516901558664927,
					6.570038630785206
				],
				[
					5.338156387513095,
					6.570038630785206
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06886333972215652,
				0.07585742324590683,
				0.17916598916053772,
				0.22913198173046112,
				0.2316831648349762,
				0.17691870033740997,
				0.11378946155309677,
				0.1606135219335556,
				0.08720453083515167,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1169265651,
			"isDeleted": false,
			"id": "rILIQuSU9VLcMzh3EYrrJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 730.4909220593554,
			"y": 103.69225091620419,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.516901558664813,
			"height": 8.212548288481543,
			"seed": 265144999,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4106274144240558
				],
				[
					0.41062741442408424,
					3.695646729816673
				],
				[
					1.2318822432722527,
					6.15941121636115
				],
				[
					2.053137072120421,
					5.748783801937066
				],
				[
					2.8743919009685897,
					2.0531370721203643
				],
				[
					4.106274144240842,
					-1.6425096576963085
				],
				[
					4.516901558664813,
					-2.0531370721203928
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13516293466091156,
				0.14050829410552979,
				0.15089450776576996,
				0.16539041697978973,
				0.08391732722520828,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 81,
			"versionNonce": 1457002685,
			"isDeleted": false,
			"id": "qbo2suIpiH3cXvlGZWIjG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 736.6503332757165,
			"y": 104.92413315947641,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.391293459633289,
			"height": 29.97580125295761,
			"seed": 195847879,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.8743919009685897,
					-2.0531370721203928
				],
				[
					6.980666045209318,
					-5.748783801937094
				],
				[
					6.980666045209318,
					-9.855057946177851
				],
				[
					6.570038630785348,
					-11.908195018298244
				],
				[
					5.748783801937179,
					-11.908195018298244
				],
				[
					4.106274144240842,
					-9.855057946177851
				],
				[
					2.8743919009685897,
					-6.570038630785234
				],
				[
					2.8743919009685897,
					-0.41062741442408424
				],
				[
					3.285019315392674,
					6.15941121636115
				],
				[
					3.285019315392674,
					12.3188224327223
				],
				[
					3.695646729816758,
					16.83572399138714
				],
				[
					2.4637644865445054,
					18.067606234659365
				],
				[
					0,
					16.014469162539
				],
				[
					-0.41062741442397055,
					10.676312775025991
				],
				[
					0,
					9.855057946177851
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.24514199793338776,
				0.27009302377700806,
				0.21858340501785278,
				0.15841901302337646,
				0.1274547427892685,
				0.16405880451202393,
				0.18170058727264404,
				0.1534338742494583,
				0.11748935282230377,
				0.20700915157794952,
				0.18999764323234558,
				0.05324682593345642,
				0.019589293748140335,
				0.08632464706897736,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 887135635,
			"isDeleted": false,
			"id": "ioNdiyQDRvROC0azZufhP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 746.9160186363185,
			"y": 104.51350574505233,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.748783801937066,
			"height": 9.444430531753767,
			"seed": 1158006759,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.41062741442397055,
					0.41062741442408424
				],
				[
					3.28501931539256,
					0.8212548288481685
				],
				[
					4.927528973088897,
					0.41062741442408424
				],
				[
					3.6956467298166444,
					-2.0531370721203928
				],
				[
					1.231882243272139,
					-2.0531370721203928
				],
				[
					-0.8212548288481685,
					0.41062741442408424
				],
				[
					-0.8212548288481685,
					4.927528973088926
				],
				[
					2.874391900968476,
					7.391293459633374
				],
				[
					3.28501931539256,
					6.980666045209318
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09995291382074356,
				0.20526522397994995,
				0.16342929005622864,
				0.050733186304569244,
				0.0910021960735321,
				0.22833377122879028,
				0.11632232367992401,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 2100295965,
			"isDeleted": false,
			"id": "nZDs_VM4pDVbc5DrnEDt0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 754.717939510376,
			"y": 102.46036867293193,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.801920874057487,
			"height": 9.855057946177823,
			"seed": 682714695,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.6425096576963085
				],
				[
					0.41062741442397055,
					6.15941121636115
				],
				[
					0.8212548288481685,
					7.801920874057458
				],
				[
					1.231882243272139,
					4.516901558664841
				],
				[
					4.106274144240729,
					-0.82125482884814
				],
				[
					7.801920874057487,
					-2.0531370721203643
				],
				[
					7.801920874057487,
					-1.6425096576963085
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.20328198373317719,
				0.24758899211883545,
				0.19947785139083862,
				0.17496082186698914,
				0.2205149531364441,
				0.05975521728396416,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 683504435,
			"isDeleted": false,
			"id": "FrBlCvgsUyeoJNPCMa9A3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 764.1623700421297,
			"y": 103.69225091620419,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.927528973089011,
			"height": 8.623175702905627,
			"seed": 260173415,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.41062741442408424,
					0
				],
				[
					0.8212548288481685,
					0
				],
				[
					2.053137072120421,
					-0.8212548288481685
				],
				[
					2.4637644865443917,
					-2.8743919009685612
				],
				[
					0,
					-2.463764486544477
				],
				[
					-1.2318822432722527,
					0.4106274144240558
				],
				[
					-0.41062741442408424,
					4.927528973088897
				],
				[
					3.28501931539256,
					5.748783801937066
				],
				[
					3.695646729816758,
					4.927528973088897
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16020825505256653,
				0.21351198852062225,
				0.13376067578792572,
				0.0551614984869957,
				0.08117758482694626,
				0.21111667156219482,
				0.11266235262155533,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1651297661,
			"isDeleted": false,
			"id": "dkBvVxZ36azzP5y2AibN0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 773.1961731594595,
			"y": 101.22848642965971,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.801920874057487,
			"height": 6.980666045209318,
			"seed": 1759681735,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.2318822432722243
				],
				[
					0.41062741442397055,
					2.874391900968533
				],
				[
					0.8212548288481685,
					4.927528973088926
				],
				[
					1.642509657696337,
					5.748783801937066
				],
				[
					3.6956467298166444,
					2.874391900968533
				],
				[
					6.57003863078512,
					1.2318822432722243
				],
				[
					7.801920874057487,
					3.285019315392617
				],
				[
					7.391293459633289,
					6.980666045209318
				],
				[
					7.391293459633289,
					6.980666045209318
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14102798700332642,
				0.19404400885105133,
				0.22210800647735596,
				0.12205658107995987,
				0.12682776153087616,
				0.2059115320444107,
				0.13246002793312073,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1638831315,
			"isDeleted": false,
			"id": "AOa6c2LjsiHDgxP1Z4hm-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 788.8000149075743,
			"y": 100.81785901523563,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.516901558664813,
			"height": 8.212548288481543,
			"seed": 1259931431,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.41062741442408424,
					0.41062741442408424
				],
				[
					-1.2318822432722527,
					2.8743919009685612
				],
				[
					-1.6425096576962233,
					6.980666045209318
				],
				[
					0.41062741442408424,
					8.212548288481543
				],
				[
					2.4637644865445054,
					7.391293459633403
				],
				[
					2.8743919009685897,
					7.391293459633403
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11336600035429001,
				0.1933940052986145,
				0.19182266294956207,
				0.01685061678290367,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1171264989,
			"isDeleted": false,
			"id": "BOx-hE1VmG2JZ6QIEIVF5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 794.1381712950874,
			"y": 106.97727023159678,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.15941121636115,
			"height": 8.623175702905598,
			"seed": 1087516711,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8212548288480548,
					0
				],
				[
					1.6425096576962233,
					0
				],
				[
					3.28501931539256,
					-1.2318822432722243
				],
				[
					3.6956467298166444,
					-3.2850193153925886
				],
				[
					2.0531370721203075,
					-3.2850193153925886
				],
				[
					0.41062741442397055,
					-0.4106274144240558
				],
				[
					1.6425096576962233,
					3.6956467298167013
				],
				[
					5.748783801936952,
					5.33815638751301
				],
				[
					6.15941121636115,
					5.33815638751301
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06109900027513504,
				0.07357077300548553,
				0.17520199716091156,
				0.22443200647830963,
				0.17880339920520782,
				0.2526343762874603,
				0.33397600054740906,
				0.12838704884052277,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1330283123,
			"isDeleted": false,
			"id": "oF8Zzy6-GGUIXg7n4P4Ra",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 497.46350717509705,
			"y": 147.53775749384715,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.071908171577832,
			"height": 12.400537152167146,
			"seed": 1704425095,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.3286289805893716,
					0.442876326863086
				],
				[
					-1.7715053074524576,
					1.7715053074524008
				],
				[
					-1.7715053074524576,
					3.1001342880417724
				],
				[
					-0.8857526537262288,
					7.5288975566728595
				],
				[
					3.1001342880417724,
					10.186155517851546
				],
				[
					7.528897556672916,
					7.971773883536002
				],
				[
					9.300402864125374,
					3.1001342880417724
				],
				[
					8.414650210399088,
					-1.3286289805893716
				],
				[
					4.87163959549423,
					-2.2143816343156004
				],
				[
					-1.3286289805893716,
					1.7715053074524008
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.041301973164081573,
				0.04627841338515282,
				0.09841696172952652,
				0.1559007316827774,
				0.22151827812194824,
				0.23640960454940796,
				0.18024557828903198,
				0.12295456230640411,
				0.13849645853042603,
				0.0833420380949974,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 40587837,
			"isDeleted": false,
			"id": "Y7MqOwm1WNXz4UkPKHqXo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 496.1348781945077,
			"y": 156.39528403110938,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.2143816343156004,
			"height": 12.40053715216709,
			"seed": 1131785799,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.442876326863086,
					0
				],
				[
					-0.885752653726172,
					0
				],
				[
					-1.3286289805893148,
					0.442876326863086
				],
				[
					-1.7715053074524576,
					2.6572579611786296
				],
				[
					-1.7715053074524576,
					7.5288975566728595
				],
				[
					0,
					12.40053715216709
				],
				[
					0.4428763268631428,
					12.40053715216709
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13527999818325043,
				0.1824219971895218,
				0.22826796770095825,
				0.24037069082260132,
				0.07547116279602051,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 710392851,
			"isDeleted": false,
			"id": "cHJw9dn23zTlOMHVLKSE6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 503.6637757511806,
			"y": 155.06665505052,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.543010614904915,
			"height": 14.61491878648269,
			"seed": 884291175,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.442876326863086,
					-0.8857526537262288
				],
				[
					0.8857526537262288,
					-1.3286289805893148
				],
				[
					1.3286289805893716,
					-1.7715053074524576
				],
				[
					3.1001342880418292,
					2.2143816343156004
				],
				[
					3.543010614904915,
					7.971773883536002
				],
				[
					2.6572579611786864,
					12.400537152167146
				],
				[
					2.6572579611786864,
					12.843413479030232
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.18209600448608398,
				0.2916542589664459,
				0.38661399483680725,
				0.3196862041950226,
				0.06175534054636955,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 354419357,
			"isDeleted": false,
			"id": "ja5SgKTymUHz1iE42-I7Z",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 497.02063084823396,
			"y": 168.79582118327647,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.74327919098846,
			"height": 1.3286289805893716,
			"seed": 170957447,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4428763268631428
				],
				[
					0.885752653726172,
					1.3286289805893716
				],
				[
					6.200268576083545,
					0.8857526537262288
				],
				[
					9.74327919098846,
					0
				],
				[
					9.74327919098846,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.2385679930448532,
				0.40816864371299744,
				0.21874557435512543,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1322041779,
			"isDeleted": false,
			"id": "XM2ZvO4IMPdkSgUYbuW5G",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 600.210815007339,
			"y": 142.22324157148978,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.971773883536002,
			"height": 9.74327919098846,
			"seed": 801638503,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.442876326863086,
					-0.442876326863086
				],
				[
					-0.885752653726172,
					-0.442876326863086
				],
				[
					-1.3286289805893148,
					0.4428763268631428
				],
				[
					-2.6572579611786296,
					3.985886941768001
				],
				[
					-1.3286289805893148,
					7.971773883536002
				],
				[
					2.2143816343156004,
					8.414650210399145
				],
				[
					5.314515922357373,
					4.87163959549423
				],
				[
					4.87163959549423,
					0.8857526537262288
				],
				[
					2.2143816343156004,
					-1.3286289805893148
				],
				[
					-1.3286289805893148,
					1.3286289805893148
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1265459954738617,
				0.16121600568294525,
				0.22284600138664246,
				0.2419164776802063,
				0.22436849772930145,
				0.18994973599910736,
				0.12348129600286484,
				0.12355493009090424,
				0.042003996670246124,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1654630141,
			"isDeleted": false,
			"id": "gxJNtAUebJzbzClJxH7zj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 597.9964333730234,
			"y": 148.42351014757332,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7715053074524576,
			"height": 10.186155517851603,
			"seed": 697792551,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.442876326863086,
					0.4428763268631428
				],
				[
					-1.3286289805893148,
					0.8857526537262288
				],
				[
					-1.3286289805893148,
					2.2143816343156004
				],
				[
					-1.3286289805893148,
					6.643144902946688
				],
				[
					-0.8857526537262288,
					9.300402864125374
				],
				[
					0.4428763268631428,
					10.186155517851603
				],
				[
					0.4428763268631428,
					10.186155517851603
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10647088289260864,
				0.16534799337387085,
				0.20678848028182983,
				0.1392958015203476,
				0.019622741267085075,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1439699795,
			"isDeleted": false,
			"id": "Y29Xg4fUsxB3uuwx5FSm0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 604.196701949107,
			"y": 147.53775749384715,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7715053074524576,
			"height": 11.957660825304004,
			"seed": 1559159879,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.442876326863086
				],
				[
					0,
					0.885752653726172
				],
				[
					0.442876326863086,
					1.7715053074524008
				],
				[
					1.7715053074524576,
					6.643144902946631
				],
				[
					0.885752653726172,
					11.51478449844086
				],
				[
					0.885752653726172,
					11.957660825304004
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08262231200933456,
				0.14638742804527283,
				0.1913318783044815,
				0.08246862888336182,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 1030471517,
			"isDeleted": false,
			"id": "ueWDtfV6vUVUuVJUBr-DA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 597.1106807192972,
			"y": 162.15267628032984,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.971773883536002,
			"height": 1.7715053074524576,
			"seed": 119598407,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4428763268631428,
					0
				],
				[
					1.3286289805893716,
					-0.4428763268631428
				],
				[
					4.428763268631144,
					-0.4428763268631428
				],
				[
					7.971773883536002,
					0.885752653726172
				],
				[
					7.971773883536002,
					1.3286289805893148
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11493151634931564,
				0.16092818975448608,
				0.25970038771629333,
				0.23866170644760132,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 1874342131,
			"isDeleted": false,
			"id": "_fGvJGyeTvSZRGc8O640L",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 519.1644471913895,
			"y": 148.42351014757332,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.87163959549423,
			"height": 13.729166132756518,
			"seed": 2023027495,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8857526537262288,
					0.4428763268631428
				],
				[
					2.6572579611786864,
					2.6572579611786864
				],
				[
					4.87163959549423,
					9.300402864125374
				],
				[
					4.428763268631087,
					13.729166132756518
				],
				[
					3.985886941768001,
					13.729166132756518
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1639920026063919,
				0.2290239930152893,
				0.26480796933174133,
				0.07716970890760422,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 735431613,
			"isDeleted": false,
			"id": "l0Bb2lKinmfedlDmmaN8z",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 530.6792316898304,
			"y": 148.86638647443647,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7715053074524576,
			"height": 11.514784498440918,
			"seed": 667178247,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8857526537262288,
					0.442876326863086
				],
				[
					1.3286289805893148,
					1.7715053074524576
				],
				[
					1.7715053074524576,
					11.514784498440918
				],
				[
					1.7715053074524576,
					11.514784498440918
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17235958576202393,
				0.233615443110466,
				0.187862366437912,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 2114689683,
			"isDeleted": false,
			"id": "UEGVQlVUTZjjkNHjA8U9n",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 548.3942847643549,
			"y": 148.86638647443647,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7715053074524576,
			"height": 14.172042459619547,
			"seed": 1869128647,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8857526537262288,
					1.3286289805893148
				],
				[
					1.7715053074524576,
					6.643144902946688
				],
				[
					0.4428763268631428,
					13.729166132756461
				],
				[
					0.4428763268631428,
					14.172042459619547
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17458777129650116,
				0.33297398686408997,
				0.26942017674446106,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 1845447709,
			"isDeleted": false,
			"id": "SjEftwvzS-kwki0YtlbL4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 559.9090692627958,
			"y": 147.98063382071024,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.6572579611786296,
			"height": 13.729166132756461,
			"seed": 1320346247,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.442876326863086
				],
				[
					0.4428763268631428,
					0
				],
				[
					2.6572579611786296,
					5.314515922357316
				],
				[
					1.7715053074524576,
					12.400537152167146
				],
				[
					1.3286289805893148,
					13.286289805893375
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06299197673797607,
				0.14752602577209473,
				0.19976675510406494,
				0.11702597141265869,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 1837158451,
			"isDeleted": false,
			"id": "JssJ6YNy_RZWLzSNXf7zj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 578.0669986641834,
			"y": 149.7521391281627,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8857526537262856,
			"height": 14.172042459619547,
			"seed": 1395347559,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4428763268631428,
					0.442876326863086
				],
				[
					-0.4428763268631428,
					4.428763268631087
				],
				[
					-0.4428763268631428,
					13.729166132756461
				],
				[
					-0.8857526537262856,
					14.172042459619547
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.24354547262191772,
				0.14136292040348053,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 1138344061,
			"isDeleted": false,
			"id": "Mgf7Sb1SeQXz4-Qv339v7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 583.8243909134038,
			"y": 147.98063382071024,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.1001342880418292,
			"height": 13.729166132756461,
			"seed": 1844680487,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4428763268631428,
					0.442876326863086
				],
				[
					1.3286289805893716,
					1.7715053074524576
				],
				[
					3.1001342880418292,
					8.414650210399145
				],
				[
					2.2143816343156004,
					13.286289805893375
				],
				[
					1.7715053074524576,
					13.729166132756461
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19664400815963745,
				0.251691997051239,
				0.3904860317707062,
				0.2952883243560791,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 1342067155,
			"isDeleted": false,
			"id": "cvmiE5xkZa_co-LABLg5e",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 546.1799031300393,
			"y": 175.8818424130863,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3286289805893716,
			"height": 5.314515922357316,
			"seed": 1019443463,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					2.6572579611786296
				],
				[
					0.442876326863086,
					4.428763268631087
				],
				[
					0.8857526537262288,
					5.314515922357316
				],
				[
					1.3286289805893716,
					4.428763268631087
				],
				[
					1.3286289805893716,
					3.1001342880417724
				],
				[
					1.3286289805893716,
					2.2143816343155436
				],
				[
					0.8857526537262288,
					1.3286289805893148
				],
				[
					0,
					2.2143816343155436
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10015838593244553,
				0.12411682307720184,
				0.11858376860618591,
				0.0397191159427166,
				0.0011702575720846653,
				0.0013676452217623591,
				0,
				0.0016682434361428022,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 80,
			"versionNonce": 1931913437,
			"isDeleted": false,
			"id": "ZQfRUVeEBXIO5qv881FP7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 545.7370268031763,
			"y": 169.6815738370027,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.971773883536059,
			"height": 13.729166132756461,
			"seed": 1855719047,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4428763268631428
				],
				[
					0,
					1.7715053074524576
				],
				[
					0.885752653726172,
					6.200268576083602
				],
				[
					1.3286289805893148,
					9.74327919098846
				],
				[
					1.7715053074524576,
					10.629031844714689
				],
				[
					1.3286289805893148,
					10.186155517851603
				],
				[
					0.885752653726172,
					8.414650210399145
				],
				[
					-0.8857526537262856,
					6.200268576083602
				],
				[
					-3.985886941768058,
					6.200268576083602
				],
				[
					-6.200268576083602,
					9.300402864125374
				],
				[
					-4.87163959549423,
					12.843413479030232
				],
				[
					-2.2143816343156004,
					13.729166132756461
				],
				[
					0,
					13.286289805893375
				],
				[
					0.442876326863086,
					12.843413479030232
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12029492110013962,
				0.2320220023393631,
				0.2954169809818268,
				0.3070164918899536,
				0.1976420283317566,
				0.1552686095237732,
				0.10690435767173767,
				0.11476001143455505,
				0.17958295345306396,
				0.21499194204807281,
				0.240071102976799,
				0.2411736100912094,
				0.159818634390831,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 916103027,
			"isDeleted": false,
			"id": "bkVGg6J-xRMWGgyIzufJG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 551.9372953792598,
			"y": 176.3247187399494,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4428763268631428,
			"height": 4.87163959549423,
			"seed": 1778030727,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4428763268631428
				],
				[
					0,
					2.6572579611786864
				],
				[
					0.4428763268631428,
					4.87163959549423
				],
				[
					0.4428763268631428,
					3.985886941768001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12437399476766586,
				0.23910997807979584,
				0.1915300041437149,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 225936701,
			"isDeleted": false,
			"id": "uESiPudRiJpXT7guNLXdz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 553.7088006867123,
			"y": 173.22458445190762,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3286289805893148,
			"height": 0.442876326863086,
			"seed": 2012628807,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4428763268631428,
					0
				],
				[
					-0.8857526537262856,
					0.442876326863086
				],
				[
					-1.3286289805893148,
					0.442876326863086
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11232846230268478,
				0.083436980843544,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1268529427,
			"isDeleted": false,
			"id": "gwW2c_kPGcgBPJU6lcPE_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 556.808934974754,
			"y": 174.11033710563385,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.200268576083545,
			"height": 6.200268576083602,
			"seed": 1238600999,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4428763268631428,
					0
				],
				[
					-0.4428763268631428,
					-0.4428763268631428
				],
				[
					0,
					1.7715053074524576
				],
				[
					0.4428763268631428,
					4.428763268631087
				],
				[
					0.4428763268631428,
					5.757392249220459
				],
				[
					1.7715053074524576,
					3.985886941768001
				],
				[
					5.757392249220402,
					0.442876326863086
				],
				[
					5.757392249220402,
					0.442876326863086
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1022220179438591,
				0.18984204530715942,
				0.18613657355308533,
				0.20154953002929688,
				0.2206605225801468,
				0.22256560623645782,
				0.13546743988990784,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1982715293,
			"isDeleted": false,
			"id": "rL_xtiYoqPNPj__pWvojH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 537.3223765927771,
			"y": 98.8213615389048,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.442876326863086,
			"height": 13.729166132756518,
			"seed": 1749981287,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4428763268631428
				],
				[
					0,
					1.3286289805893716
				],
				[
					0.442876326863086,
					2.6572579611786864
				],
				[
					0.442876326863086,
					5.757392249220459
				],
				[
					0.442876326863086,
					13.286289805893375
				],
				[
					0.442876326863086,
					13.729166132756518
				],
				[
					0.442876326863086,
					13.286289805893375
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06736666709184647,
				0.09084927290678024,
				0.11206734925508499,
				0.12902282178401947,
				0.041596680879592896,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 746167987,
			"isDeleted": false,
			"id": "4osRb-OSNJxfhCzIAU8OF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 536.4366239390508,
			"y": 95.72122725086302,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.500671440208862,
			"height": 1.7715053074524576,
			"seed": 529251463,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.442876326863086
				],
				[
					-0.442876326863086,
					-0.442876326863086
				],
				[
					0,
					-0.442876326863086
				],
				[
					3.5430106149048584,
					0.4428763268631428
				],
				[
					9.300402864125374,
					0.8857526537262288
				],
				[
					14.172042459619604,
					-0.8857526537262288
				],
				[
					15.057795113345776,
					-0.8857526537262288
				],
				[
					14.61491878648269,
					-0.442876326863086
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06018298491835594,
				0.10593456774950027,
				0.15480399131774902,
				0.2299719899892807,
				0.26554790139198303,
				0.22528766095638275,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 679156221,
			"isDeleted": false,
			"id": "O4dJCe17AoRz4i_f6hiuK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 551.0515427255336,
			"y": 97.0498562314524,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8857526537262288,
			"height": 13.286289805893318,
			"seed": 1538592711,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.442876326863086,
					1.7715053074524008
				],
				[
					-0.8857526537262288,
					6.643144902946631
				],
				[
					-0.442876326863086,
					10.629031844714689
				],
				[
					0,
					13.286289805893318
				],
				[
					-0.442876326863086,
					13.286289805893318
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14919210970401764,
				0.22672997415065765,
				0.21339523792266846,
				0.02685580402612686,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 69,
			"versionNonce": 64573523,
			"isDeleted": false,
			"id": "5sxIwaRcUGHnMkCElUQFO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 538.6510055733664,
			"y": 112.9934039985244,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.971773883536002,
			"height": 0.8857526537262288,
			"seed": 908125607,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					3.1001342880417724,
					-0.442876326863086
				],
				[
					7.971773883536002,
					-0.8857526537262288
				],
				[
					7.971773883536002,
					-0.8857526537262288
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.29734402894973755,
				0.08254831284284592,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 87,
			"versionNonce": 1029755485,
			"isDeleted": false,
			"id": "75crFXS8GyQa9eegJTcGT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 539.5367582270926,
			"y": 97.93560888517862,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.314515922357373,
			"height": 6.200268576083545,
			"seed": 452558151,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.442876326863086,
					0
				],
				[
					-0.8857526537262288,
					0.442876326863086
				],
				[
					-0.8857526537262288,
					3.1001342880417724
				],
				[
					-0.442876326863086,
					5.314515922357316
				],
				[
					0,
					5.314515922357316
				],
				[
					0,
					2.2143816343155436
				],
				[
					0.442876326863086,
					-0.4428763268631428
				],
				[
					0.442876326863086,
					-0.8857526537262288
				],
				[
					0.8857526537262288,
					-0.4428763268631428
				],
				[
					2.2143816343155436,
					0.442876326863086
				],
				[
					3.1001342880418292,
					0.885752653726172
				],
				[
					3.985886941768001,
					1.3286289805893148
				],
				[
					4.428763268631144,
					1.3286289805893148
				],
				[
					3.985886941768001,
					2.2143816343155436
				],
				[
					3.5430106149048584,
					3.5430106149048584
				],
				[
					3.5430106149048584,
					4.87163959549423
				],
				[
					2.6572579611786864,
					5.314515922357316
				],
				[
					1.3286289805893716,
					4.87163959549423
				],
				[
					0,
					3.5430106149048584
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1394362449645996,
				0.17534445226192474,
				0.14429357647895813,
				0.09533767402172089,
				0.080672487616539,
				0.0899900496006012,
				0.0889214500784874,
				0.1079399436712265,
				0.09731805324554443,
				0.09326834231615067,
				0.08126397430896759,
				0.04843981936573982,
				0.035159699618816376,
				0.037959106266498566,
				0.07833480834960938,
				0.09777712821960449,
				0.14722873270511627,
				0.16984042525291443,
				0.06812689453363419,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 88,
			"versionNonce": 1670499827,
			"isDeleted": false,
			"id": "UoNPYCZmGJJEsN--k266i",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 544.408397822587,
			"y": 98.8213615389048,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.314515922357316,
			"height": 7.5288975566728595,
			"seed": 1999688999,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.442876326863086,
					0.4428763268631428
				],
				[
					-0.8857526537262288,
					0.8857526537262288
				],
				[
					-0.8857526537262288,
					1.7715053074524576
				],
				[
					-1.3286289805893716,
					3.985886941768058
				],
				[
					-1.3286289805893716,
					4.87163959549423
				],
				[
					-0.8857526537262288,
					3.543010614904915
				],
				[
					-0.442876326863086,
					0.4428763268631428
				],
				[
					0,
					-1.7715053074524008
				],
				[
					0,
					-2.2143816343155436
				],
				[
					-0.442876326863086,
					-1.7715053074524008
				],
				[
					0,
					-2.2143816343155436
				],
				[
					0.8857526537262288,
					-2.6572579611786296
				],
				[
					1.7715053074524576,
					-2.2143816343155436
				],
				[
					2.2143816343155436,
					-1.7715053074524008
				],
				[
					2.2143816343155436,
					-0.885752653726172
				],
				[
					1.3286289805893716,
					0.4428763268631428
				],
				[
					0.442876326863086,
					1.3286289805893716
				],
				[
					0,
					1.7715053074524576
				],
				[
					-1.3286289805893716,
					2.6572579611786864
				],
				[
					-2.2143816343155436,
					3.1001342880418292
				],
				[
					-2.6572579611786864,
					3.1001342880418292
				],
				[
					-3.1001342880417724,
					3.1001342880418292
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10746398568153381,
				0.13701999187469482,
				0.17956705391407013,
				0.20404428243637085,
				0.1767379492521286,
				0.09654544293880463,
				0.0739329531788826,
				0.190532386302948,
				0.2585895359516144,
				0.21755966544151306,
				0.2068561464548111,
				0.21313653886318207,
				0.2359151989221573,
				0.24258527159690857,
				0.25679370760917664,
				0.2365226447582245,
				0.20767025649547577,
				0.18162231147289276,
				0.13576769828796387,
				0.06214776635169983,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 84,
			"versionNonce": 833650365,
			"isDeleted": false,
			"id": "rfraXRPU_TggkrmtUDO1n",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 539.0938819002296,
			"y": 105.90738276871463,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.757392249220459,
			"height": 7.086021229809774,
			"seed": 778522663,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4428763268631428,
					0.442876326863086
				],
				[
					-0.4428763268631428,
					1.3286289805893148
				],
				[
					-0.4428763268631428,
					2.6572579611786296
				],
				[
					0,
					4.87163959549423
				],
				[
					0.442876326863086,
					5.314515922357316
				],
				[
					1.3286289805893148,
					2.6572579611786296
				],
				[
					1.7715053074524576,
					-0.4428763268631428
				],
				[
					1.7715053074524576,
					-1.7715053074524576
				],
				[
					2.2143816343155436,
					-0.8857526537262288
				],
				[
					3.1001342880417724,
					0.442876326863086
				],
				[
					4.428763268631087,
					1.7715053074524576
				],
				[
					4.87163959549423,
					2.6572579611786296
				],
				[
					5.314515922357316,
					2.6572579611786296
				],
				[
					4.87163959549423,
					2.6572579611786296
				],
				[
					3.9858869417679443,
					3.1001342880417724
				],
				[
					2.2143816343155436,
					3.5430106149048584
				],
				[
					0.442876326863086,
					3.985886941768001
				],
				[
					0.885752653726172,
					3.985886941768001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0765344575047493,
				0.11899811029434204,
				0.15755361318588257,
				0.18968728184700012,
				0.16718032956123352,
				0.09765798598527908,
				0.09515991061925888,
				0.17684753239154816,
				0.21661563217639923,
				0.22908233106136322,
				0.22938692569732666,
				0.22163519263267517,
				0.21353335678577423,
				0.22221408784389496,
				0.23423394560813904,
				0.2205173671245575,
				0.03390621766448021,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 1588172691,
			"isDeleted": false,
			"id": "Q6AHIkwQWBUT_1v5WxKU7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 545.7370268031763,
			"y": 106.35025909557771,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3286289805893716,
			"height": 4.428763268631144,
			"seed": 616879783,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4428763268631428
				],
				[
					0,
					0.8857526537262288
				],
				[
					0,
					1.3286289805893716
				],
				[
					0,
					2.2143816343155436
				],
				[
					0.442876326863086,
					3.1001342880417724
				],
				[
					-0.8857526537262856,
					4.428763268631144
				],
				[
					-0.8857526537262856,
					4.428763268631144
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06442700326442719,
				0.05923599377274513,
				0.13082171976566315,
				0.14879681169986725,
				0.126353457570076,
				0.05388357490301132,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 69,
			"versionNonce": 1812700957,
			"isDeleted": false,
			"id": "vThvWjbOFk5sN-Cd319-a",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 508.09253901981174,
			"y": 133.36571503422755,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.314515922357316,
			"height": 9.300402864125374,
			"seed": 244708039,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.885752653726172,
					2.2143816343155436
				],
				[
					4.87163959549423,
					8.857526537262231
				],
				[
					5.314515922357316,
					9.300402864125374
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15387897193431854,
				0.06283892691135406,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 1666657587,
			"isDeleted": false,
			"id": "6ybZq8K___sS4c-BorfBN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 514.7356839227584,
			"y": 128.9369517655964,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.6572579611786296,
			"height": 9.300402864125374,
			"seed": 990008935,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4428763268631428
				],
				[
					0,
					1.3286289805893716
				],
				[
					0.442876326863086,
					2.2143816343156004
				],
				[
					1.3286289805893148,
					5.314515922357373
				],
				[
					2.2143816343155436,
					9.300402864125374
				],
				[
					2.6572579611786296,
					9.300402864125374
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11936544626951218,
				0.19310399889945984,
				0.21134299039840698,
				0.04673486202955246,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 48477053,
			"isDeleted": false,
			"id": "6aXZcaq3hRUZki9NG1-S7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 518.2786945376633,
			"y": 125.83681747755463,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.985886941768001,
			"height": 10.629031844714689,
			"seed": 50872167,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.442876326863086,
					-0.442876326863086
				],
				[
					-0.442876326863086,
					-1.3286289805893148
				],
				[
					-0.442876326863086,
					-2.2143816343155436
				],
				[
					0,
					-2.2143816343155436
				],
				[
					0.8857526537262288,
					-1.3286289805893148
				],
				[
					2.6572579611786864,
					2.2143816343156004
				],
				[
					3.543010614904915,
					7.971773883536002
				],
				[
					3.543010614904915,
					8.414650210399145
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.053168028593063354,
				0.02796218916773796,
				0.02105725184082985,
				0.07214263826608658,
				0.19336822628974915,
				0.24373699724674225,
				0.025248778983950615,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 1426132691,
			"isDeleted": false,
			"id": "cA48c4wKplL0WoCBANv4q",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 524.92183944061,
			"y": 121.40805420892355,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7715053074524576,
			"height": 7.086021229809774,
			"seed": 1278573223,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.3286289805893148
				],
				[
					0,
					2.6572579611786296
				],
				[
					0.8857526537262288,
					4.87163959549423
				],
				[
					1.7715053074524576,
					7.086021229809774
				],
				[
					1.7715053074524576,
					7.086021229809774
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13098599016666412,
				0.1598159819841385,
				0.05901474133133888,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 1115306973,
			"isDeleted": false,
			"id": "Ue-XkBSXWeIWl9sWa-ydF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 528.907726382378,
			"y": 116.09353828656617,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7715053074524576,
			"height": 7.971773883536002,
			"seed": 640699527,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4428763268631428,
					0.8857526537262288
				],
				[
					0.4428763268631428,
					2.2143816343155436
				],
				[
					0.8857526537262288,
					3.985886941768001
				],
				[
					1.7715053074524576,
					7.528897556672916
				],
				[
					1.7715053074524576,
					7.971773883536002
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1042463406920433,
				0.13370339572429657,
				0.23033998906612396,
				0.13720501959323883,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 1715321971,
			"isDeleted": false,
			"id": "3RjXse6lBkeZFtPnNRP5T",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 557.6946876284802,
			"y": 109.0075170567564,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.2143816343154867,
			"height": 10.186155517851546,
			"seed": 734263911,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.44287632686302913,
					0.8857526537262288
				],
				[
					-0.885752653726172,
					1.7715053074524576
				],
				[
					-1.3286289805893148,
					4.428763268631087
				],
				[
					-2.2143816343154867,
					9.300402864125317
				],
				[
					-2.2143816343154867,
					10.186155517851546
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07275399565696716,
				0.0769747942686081,
				0.15452167391777039,
				0.08712872117757797,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 1927329853,
			"isDeleted": false,
			"id": "UqvV6ghuISvfoZ8iWdXeM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 568.323719473195,
			"y": 116.9792909402924,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7715053074524576,
			"height": 8.857526537262231,
			"seed": 1723860039,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4428763268631428,
					0.4428763268631428
				],
				[
					-1.7715053074524576,
					4.428763268631144
				],
				[
					-1.7715053074524576,
					8.414650210399145
				],
				[
					-1.7715053074524576,
					8.857526537262231
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13542801141738892,
				0.08333761245012283,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 852735507,
			"isDeleted": false,
			"id": "673bnSXrx1Wh0YAFxpQAG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 586.9245252014457,
			"y": 122.73668318951286,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.543010614904915,
			"height": 11.957660825304004,
			"seed": 1244128007,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-2.2143816343155436,
					2.6572579611786864
				],
				[
					-3.543010614904915,
					6.643144902946688
				],
				[
					-3.543010614904915,
					11.514784498440918
				],
				[
					-3.543010614904915,
					11.957660825304004
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0997861921787262,
				0.11081405729055405,
				0.050710633397102356,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 70,
			"versionNonce": 1576577181,
			"isDeleted": false,
			"id": "GP1Tk-DXc3m6czTx7zSKB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 594.0105464312554,
			"y": 130.26558074618578,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.1001342880417724,
			"height": 8.414650210399088,
			"seed": 558477767,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.3286289805893148,
					2.6572579611786864
				],
				[
					-2.6572579611786864,
					5.314515922357316
				],
				[
					-3.1001342880417724,
					7.971773883536002
				],
				[
					-3.1001342880417724,
					8.414650210399088
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10816006362438202,
				0.08974078297615051,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 431586227,
			"isDeleted": false,
			"id": "WwNBM5wvCdhE5-goaCkTD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 574.5239880492785,
			"y": 104.13587746126217,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.857526537262231,
			"height": 8.857526537262231,
			"seed": 871460999,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4428763268631428,
					0
				],
				[
					-0.4428763268631428,
					0.442876326863086
				],
				[
					-0.8857526537262288,
					1.3286289805893148
				],
				[
					0.4428763268631428,
					5.314515922357316
				],
				[
					0.8857526537262288,
					7.971773883536002
				],
				[
					0.8857526537262288,
					7.528897556672916
				],
				[
					1.7715053074524576,
					4.428763268631087
				],
				[
					4.428763268631087,
					0.8857526537262288
				],
				[
					7.528897556672916,
					-0.4428763268631428
				],
				[
					7.971773883536002,
					-0.8857526537262288
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06919623166322708,
				0.12493044883012772,
				0.14433206617832184,
				0.12483429163694382,
				0.11945538222789764,
				0.12582287192344666,
				0.16942889988422394,
				0.08112832903862,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 76,
			"versionNonce": 359894269,
			"isDeleted": false,
			"id": "83r_cA4XkJqxoVrqrH_Zt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 585.1530198939931,
			"y": 108.12176440303017,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.857526537262174,
			"height": 11.514784498440918,
			"seed": 2114108935,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.442876326863086,
					0
				],
				[
					1.3286289805893716,
					-0.442876326863086
				],
				[
					2.2143816343155436,
					-1.3286289805893148
				],
				[
					1.3286289805893716,
					-2.2143816343155436
				],
				[
					-0.442876326863086,
					-2.2143816343155436
				],
				[
					-2.6572579611786864,
					0.442876326863086
				],
				[
					-3.5430106149048584,
					5.757392249220459
				],
				[
					-1.3286289805893716,
					9.300402864125374
				],
				[
					4.428763268631087,
					8.414650210399145
				],
				[
					5.314515922357316,
					7.971773883536002
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.042258940637111664,
				0.09740445017814636,
				0.08743002265691757,
				0.08750378340482712,
				0.17723529040813446,
				0.24422632157802582,
				0.2726231813430786,
				0.08614465594291687,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 83,
			"versionNonce": 1461030227,
			"isDeleted": false,
			"id": "Y2-jabLteQfsirhmabGSh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 594.0105464312554,
			"y": 114.76490930597686,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.414650210399088,
			"height": 23.029568996881835,
			"seed": 851168135,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.442876326863086,
					-0.8857526537262288
				],
				[
					1.3286289805893148,
					-1.7715053074524576
				],
				[
					2.6572579611786864,
					-3.985886941768001
				],
				[
					5.757392249220459,
					-7.528897556672916
				],
				[
					7.971773883536002,
					-11.957660825304004
				],
				[
					7.971773883536002,
					-14.61491878648269
				],
				[
					7.086021229809774,
					-14.61491878648269
				],
				[
					5.757392249220459,
					-12.400537152167146
				],
				[
					3.985886941768001,
					-7.971773883536002
				],
				[
					2.6572579611786864,
					-1.7715053074524576
				],
				[
					1.3286289805893148,
					4.428763268631087
				],
				[
					0.442876326863086,
					8.414650210399145
				],
				[
					-0.442876326863086,
					8.414650210399145
				],
				[
					-0.442876326863086,
					5.757392249220459
				],
				[
					1.7715053074524576,
					0.8857526537262288
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12285199016332626,
				0.12055401504039764,
				0.08303619176149368,
				0.06672961264848709,
				0.055849213153123856,
				0.0705128163099289,
				0.08755841106176376,
				0.11070477217435837,
				0.14704947173595428,
				0.1651604026556015,
				0.17727698385715485,
				0.16197469830513,
				0.14477618038654327,
				0.12890642881393433,
				0.06482250988483429,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 73,
			"versionNonce": 2027087197,
			"isDeleted": false,
			"id": "dEBSgkSCAEHlHGEJWQGck",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 473.20704283280054,
			"y": 68.89725513216848,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.936956431007559,
			"height": 14.551134132659058,
			"seed": 1304123111,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6929111491742219,
					-0.6929111491742219
				],
				[
					-0.6929111491742219,
					-1.3858222983484723
				],
				[
					2.0787334475227226,
					-6.236200342568168
				],
				[
					11.086578386787892,
					-13.165311834310558
				],
				[
					15.244045281833337,
					-14.551134132659058
				],
				[
					15.244045281833337,
					-13.165311834310558
				],
				[
					15.244045281833337,
					-13.165311834310558
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07148224115371704,
				0.09013229608535767,
				0.17406198382377625,
				0.23247000575065613,
				0.24519720673561096,
				0.04042959585785866,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 1581148915,
			"isDeleted": false,
			"id": "0b7wZ7CnCHMu3QOpQORbM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 491.2227327113308,
			"y": 47.417009507767006,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.165311834310558,
			"height": 12.472400685136336,
			"seed": 1797663495,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6929111491742219,
					-0.6929111491742219
				],
				[
					3.4645557458712233,
					-1.3858222983484723
				],
				[
					10.393667237613613,
					-2.7716445966969445
				],
				[
					13.165311834310558,
					-2.0787334475227226
				],
				[
					11.086578386787835,
					3.4645557458712233
				],
				[
					9.007844939265112,
					9.00784493926514
				],
				[
					9.007844939265112,
					9.700756088439391
				],
				[
					9.700756088439391,
					9.700756088439391
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13770300149917603,
				0.21216198801994324,
				0.24369436502456665,
				0.22725598514080048,
				0.27272510528564453,
				0.293550968170166,
				0.11726907640695572,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 2070426045,
			"isDeleted": false,
			"id": "VJ57F3UNyqcCfgMoUYYiD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 471.1283093852778,
			"y": 90.37750075656996,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.31493379009089,
			"height": 23.558979071924227,
			"seed": 282025543,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6929111491742219,
					0
				],
				[
					0,
					2.0787334475227226
				],
				[
					4.157466895045445,
					11.086578386787863
				],
				[
					6.236200342568168,
					20.094423326053004
				],
				[
					7.6220226409166685,
					23.558979071924227
				],
				[
					7.6220226409166685,
					23.558979071924227
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.2213365137577057,
				0.3127780258655548,
				0.31874585151672363,
				0.11858493089675903,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1941607571,
			"isDeleted": false,
			"id": "EzNSdkuKXGuV-M2UyU4vm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 488.4510881146339,
			"y": 108.39319063510024,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.779489535962114,
			"height": 15.936956431007559,
			"seed": 1466394439,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6929111491742219
				],
				[
					-0.6929111491742788,
					-1.3858222983485007
				],
				[
					0,
					0
				],
				[
					2.7716445966969445,
					5.543289193393946
				],
				[
					5.543289193393889,
					9.700756088439391
				],
				[
					6.92911149174239,
					11.086578386787835
				],
				[
					6.236200342568168,
					11.779489535962114
				],
				[
					3.4645557458711664,
					12.472400685136336
				],
				[
					0.6929111491742219,
					13.858222983484836
				],
				[
					-2.0787334475227226,
					14.551134132659058
				],
				[
					-4.157466895045445,
					12.472400685136336
				],
				[
					-4.850378044219724,
					11.779489535962114
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.21298599243164062,
				0.29329001903533936,
				0.30935120582580566,
				0.2743047773838043,
				0.2506326735019684,
				0.25852686166763306,
				0.29925087094306946,
				0.26461634039878845,
				0.07833651453256607,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 710210077,
			"isDeleted": false,
			"id": "os7zNniLiMIUWHV58QjFh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 29.977482732815645,
			"y": 142.62959010893917,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.12995388768718,
			"height": 16.642067101200325,
			"seed": 1862197287,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7235681348348066
				],
				[
					1.4471362696696133,
					-1.4471362696696133
				],
				[
					7.959249483182759,
					-5.06497694384359
				],
				[
					10.12995388768718,
					-7.959249483182759
				],
				[
					7.959249483182759,
					-9.406385752852373
				],
				[
					4.341408809008783,
					-7.959249483182759
				],
				[
					0.7235681348348066,
					-2.8942725393391697
				],
				[
					0,
					2.8942725393391697
				],
				[
					3.6178406741739764,
					6.512113213513146
				],
				[
					9.406385752852373,
					7.235681348347953
				],
				[
					9.406385752852373,
					6.512113213513146
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1378760039806366,
				0.17421600222587585,
				0.20093874633312225,
				0.1805136650800705,
				0.14043645560741425,
				0.11374355852603912,
				0.10826373100280762,
				0.14267492294311523,
				0.16660916805267334,
				0.02719290181994438,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 121670195,
			"isDeleted": false,
			"id": "EtOUuQCNVVFEeo5AoQPkn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 44.44884542951155,
			"y": 137.56461316509558,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.12995388768718,
			"height": 11.577090157356736,
			"seed": 144797895,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7235681348348066,
					2.17070440450442
				],
				[
					2.17070440450442,
					7.235681348347953
				],
				[
					2.8942725393392266,
					9.406385752852373
				],
				[
					4.341408809008783,
					5.06497694384359
				],
				[
					6.512113213513203,
					0
				],
				[
					9.406385752852373,
					-2.170704404504363
				],
				[
					10.12995388768718,
					-2.170704404504363
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09768234193325043,
				0.10165642946958542,
				0.11168255656957626,
				0.12234454602003098,
				0.1312381625175476,
				0.023911163210868835,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1921689213,
			"isDeleted": false,
			"id": "qjlqegvYL8HQpDSQNuOWA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 56.74950372170309,
			"y": 135.39390876059122,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.406385752852373,
			"height": 9.406385752852316,
			"seed": 1338648807,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7235681348348066
				],
				[
					-0.7235681348348066,
					2.170704404504363
				],
				[
					-0.7235681348348066,
					6.512113213513146
				],
				[
					0.7235681348348066,
					9.406385752852316
				],
				[
					2.170704404504363,
					8.68281761801751
				],
				[
					4.341408809008783,
					3.6178406741739764
				],
				[
					8.682817618017566,
					0.7235681348348066
				],
				[
					8.682817618017566,
					0.7235681348348066
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08873251080513,
				0.10658105462789536,
				0.09515029937028885,
				0.10670916736125946,
				0.12112899869680405,
				0.02490939386188984,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1303825363,
			"isDeleted": false,
			"id": "oW_hZ9N_Y9uf8-nGWboB7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 68.32659387905983,
			"y": 139.0117494347652,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.68281761801751,
			"height": 9.406385752852373,
			"seed": 141132839,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.4471362696696133,
					0.7235681348348066
				],
				[
					-2.17070440450442,
					2.8942725393391697
				],
				[
					-2.8942725393391697,
					4.341408809008783
				],
				[
					-0.7235681348348066,
					7.235681348347953
				],
				[
					3.6178406741739764,
					6.512113213513146
				],
				[
					5.7885450786783395,
					2.170704404504363
				],
				[
					5.064976943843533,
					-2.17070440450442
				],
				[
					0.7235681348348066,
					-2.17070440450442
				],
				[
					-1.4471362696696133,
					1.4471362696695564
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.052423980087041855,
				0.060160063207149506,
				0.08953250199556351,
				0.12025631964206696,
				0.1417795717716217,
				0.14138421416282654,
				0.12706540524959564,
				0.08668704330921173,
				0.023872222751379013,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 650825437,
			"isDeleted": false,
			"id": "mbCslzuxardgKQOQZaOP4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 75.56227522740778,
			"y": 139.0117494347652,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.577090157356736,
			"height": 11.577090157356736,
			"seed": 1434555591,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7235681348348066,
					0
				],
				[
					-0.7235681348348066,
					-0.7235681348348066
				],
				[
					0,
					1.4471362696695564
				],
				[
					1.4471362696696133,
					5.064976943843533
				],
				[
					2.8942725393391697,
					6.512113213513146
				],
				[
					5.7885450786783395,
					1.4471362696695564
				],
				[
					9.406385752852316,
					-5.06497694384359
				],
				[
					10.129953887687122,
					-5.06497694384359
				],
				[
					10.853522022521929,
					-5.06497694384359
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06592004746198654,
				0.06184976175427437,
				0.12385864555835724,
				0.14078818261623383,
				0.12151681631803513,
				0.1052933931350708,
				0.0910935029387474,
				0.016330383718013763,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 456382835,
			"isDeleted": false,
			"id": "DI-HacY4xUxJmF-iYBRrT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 63.26161693521624,
			"y": 157.10095280563507,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 20.98347591020911,
			"height": 15.194930831530712,
			"seed": 1208155943,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7235681348348066
				],
				[
					0,
					-1.4471362696696133
				],
				[
					-1.4471362696695564,
					-1.4471362696696133
				],
				[
					-4.341408809008783,
					1.4471362696696133
				],
				[
					-7.959249483182759,
					9.406385752852316
				],
				[
					-5.7885450786783395,
					13.024226427026292
				],
				[
					-0.7235681348348066,
					11.577090157356736
				],
				[
					2.8942725393391697,
					8.682817618017566
				],
				[
					3.6178406741739764,
					8.682817618017566
				],
				[
					5.06497694384359,
					13.024226427026292
				],
				[
					9.406385752852373,
					13.747794561861099
				],
				[
					13.024226427026349,
					10.853522022521929
				],
				[
					13.024226427026349,
					6.512113213513146
				],
				[
					8.682817618017566,
					2.8942725393391697
				],
				[
					4.341408809008783,
					4.341408809008783
				],
				[
					4.341408809008783,
					7.959249483182759
				],
				[
					5.06497694384359,
					7.959249483182759
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.073766328394413,
				0.11584307998418808,
				0.15673743188381195,
				0.17709670960903168,
				0.18012842535972595,
				0.15330788493156433,
				0.10970403999090195,
				0.104804627597332,
				0.14435037970542908,
				0.16947945952415466,
				0.20242227613925934,
				0.20515576004981995,
				0.18344980478286743,
				0.14851056039333344,
				0.030623504891991615,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1168567101,
			"isDeleted": false,
			"id": "-jq-cIzr1AjRmWlUt-r6I",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 79.18011590158176,
			"y": 161.44236161464386,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.853522022521929,
			"height": 9.406385752852316,
			"seed": 2033479303,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7235681348348066,
					-0.7235681348348066
				],
				[
					-0.7235681348348066,
					0
				],
				[
					0,
					3.6178406741739764
				],
				[
					1.4471362696696133,
					6.512113213513146
				],
				[
					2.8942725393391697,
					5.7885450786783395
				],
				[
					6.512113213513146,
					0
				],
				[
					9.406385752852316,
					-2.8942725393391697
				],
				[
					10.129953887687122,
					-2.8942725393391697
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07811099290847778,
				0.10450875759124756,
				0.1186407133936882,
				0.1307171881198883,
				0.12708498537540436,
				0.12928506731987,
				0.0046981810592114925,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 2097034003,
			"isDeleted": false,
			"id": "lN1hUQjgjjLmmFm7XXs0A",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 90.03363792410369,
			"y": 157.82452094046988,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.682817618017566,
			"height": 9.406385752852316,
			"seed": 931611079,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7235681348348066,
					1.4471362696695564
				],
				[
					-0.7235681348348066,
					2.8942725393391697
				],
				[
					-0.7235681348348066,
					5.064976943843533
				],
				[
					0,
					8.68281761801751
				],
				[
					0.7235681348348066,
					9.406385752852316
				],
				[
					2.8942725393391697,
					6.512113213513146
				],
				[
					5.06497694384359,
					2.170704404504363
				],
				[
					7.959249483182759,
					0.7235681348348066
				],
				[
					7.959249483182759,
					0.7235681348348066
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.061697814613580704,
				0.07793691754341125,
				0.09027963131666183,
				0.09710025042295456,
				0.12731295824050903,
				0.12527771294116974,
				0.029392821714282036,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 2139126685,
			"isDeleted": false,
			"id": "UNFxt4L2ii4v0O_iVRnFu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 102.33429621629523,
			"y": 161.44236161464386,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.577090157356736,
			"height": 8.682817618017566,
			"seed": 1150209063,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7235681348347498,
					0
				],
				[
					2.170704404504363,
					0
				],
				[
					2.8942725393391697,
					0
				],
				[
					3.6178406741739764,
					-0.7235681348348066
				],
				[
					2.170704404504363,
					-1.4471362696696133
				],
				[
					-2.8942725393392266,
					0
				],
				[
					-4.341408809008783,
					4.341408809008783
				],
				[
					-0.7235681348348066,
					7.235681348347953
				],
				[
					6.512113213513146,
					5.7885450786783395
				],
				[
					7.235681348347953,
					5.064976943843533
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09064263850450516,
				0.13084600865840912,
				0.146769717335701,
				0.1260763257741928,
				0.08781982213258743,
				0.14128048717975616,
				0.18837863206863403,
				0.016498351469635963,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 327964851,
			"isDeleted": false,
			"id": "tQN5N4Ql0hjXo2vHNT51O",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 115.35852264332152,
			"y": 159.99522534497424,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.406385752852373,
			"height": 7.959249483182759,
			"seed": 566733223,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7235681348348066,
					0
				],
				[
					-2.170704404504363,
					-0.7235681348348066
				],
				[
					-3.6178406741739764,
					0.7235681348348066
				],
				[
					-5.06497694384359,
					2.17070440450442
				],
				[
					-5.06497694384359,
					7.235681348347953
				],
				[
					2.8942725393391697,
					7.235681348347953
				],
				[
					4.341408809008783,
					6.512113213513146
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09120199829339981,
				0.14151199162006378,
				0.1784220039844513,
				0.22148816287517548,
				0.06630831956863403,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 2089353213,
			"isDeleted": false,
			"id": "SRzGpaXyqaUdOgfPGNblc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 126.93561280067826,
			"y": 144.07672637860873,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.170704404504363,
			"height": 27.495589123722254,
			"seed": 1810064839,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7235681348348066,
					0
				],
				[
					-1.4471362696696133,
					3.6178406741739764
				],
				[
					-0.7235681348348066,
					15.918498966365519
				],
				[
					-1.4471362696696133,
					27.495589123722254
				],
				[
					-2.170704404504363,
					27.495589123722254
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11144598573446274,
				0.14877310395240784,
				0.16334204375743866,
				0.006910156458616257,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 746900051,
			"isDeleted": false,
			"id": "tjVhht1izLfZEpuJd1OZM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 117.52922704782594,
			"y": 157.10095280563507,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.642067101200325,
			"height": 3.6178406741739764,
			"seed": 267123623,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7235681348347498,
					0
				],
				[
					2.170704404504363,
					-0.7235681348348066
				],
				[
					5.064976943843533,
					-0.7235681348348066
				],
				[
					15.918498966365462,
					2.8942725393391697
				],
				[
					16.642067101200325,
					2.8942725393391697
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1056239902973175,
				0.1667499989271164,
				0.05568484589457512,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 1656879197,
			"isDeleted": false,
			"id": "onkyiKrR8bzTheLOEIJjv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 137.78913482320024,
			"y": 162.8894978843134,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.170704404504363,
			"height": 10.12995388768718,
			"seed": 292679047,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7235681348348635,
					2.17070440450442
				],
				[
					-0.7235681348348635,
					4.341408809008783
				],
				[
					-0.7235681348348635,
					7.235681348347953
				],
				[
					0.7235681348347498,
					10.12995388768718
				],
				[
					1.4471362696694996,
					9.406385752852373
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10793499648571014,
				0.12779198586940765,
				0.05222659185528755,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 482215923,
			"isDeleted": false,
			"id": "u2CPJ4N3virHTNrtUmwJK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 142.13054363220897,
			"y": 154.9302484011307,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4471362696696133,
			"height": 2.170704404504363,
			"seed": 1616165735,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7235681348347498,
					0
				],
				[
					-1.4471362696696133,
					0
				],
				[
					-1.4471362696696133,
					2.170704404504363
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.058677978813648224,
				0.028960388153791428,
				0.010192596353590488,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 469558461,
			"isDeleted": false,
			"id": "D1etOp_q_2VXoK9x890so",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 145.0248161715482,
			"y": 162.8894978843134,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.12995388768718,
			"height": 10.129953887687122,
			"seed": 1793320263,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7235681348348635,
					0.7235681348348066
				],
				[
					-2.1707044045044768,
					2.17070440450442
				],
				[
					-2.1707044045044768,
					4.341408809008783
				],
				[
					0.7235681348347498,
					7.959249483182759
				],
				[
					5.064976943843476,
					8.682817618017566
				],
				[
					7.9592494831827025,
					5.06497694384359
				],
				[
					5.7885450786783395,
					0
				],
				[
					0,
					-1.4471362696695564
				],
				[
					-0.7235681348348635,
					2.17070440450442
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.06799722462892532,
				0.12443792819976807,
				0.14541567862033844,
				0.15297582745552063,
				0.15457583963871002,
				0.13073879480361938,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1514049939,
			"isDeleted": false,
			"id": "z8Bb5gpl8f01o3Rd92xwV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 153.70763378956565,
			"y": 163.61306601914822,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.12995388768718,
			"height": 12.300658292191542,
			"seed": 627319271,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7235681348348066
				],
				[
					0.7235681348348635,
					4.341408809008783
				],
				[
					1.4471362696696133,
					5.788545078678396
				],
				[
					4.34140880900884,
					5.788545078678396
				],
				[
					7.235681348347953,
					1.4471362696696133
				],
				[
					7.959249483182816,
					1.4471362696696133
				],
				[
					7.959249483182816,
					8.682817618017566
				],
				[
					9.40638575285243,
					12.300658292191542
				],
				[
					10.12995388768718,
					12.300658292191542
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11595199257135391,
				0.15179400146007538,
				0.15322107076644897,
				0.11954651027917862,
				0.16376657783985138,
				0.2689709961414337,
				0.1791774034500122,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1541096733,
			"isDeleted": false,
			"id": "7Tx8qvtXmsxliS5MT8J16",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 192.34107115862173,
			"y": 213.99686142892295,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.126913224343639,
			"height": 17.099988862301473,
			"seed": 2013003847,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6576918793193158,
					-0.657691879319259
				],
				[
					-1.3153837586385748,
					-0.657691879319259
				],
				[
					-1.9730756379578906,
					-1.3153837586385748
				],
				[
					-1.3153837586385748,
					-1.3153837586385748
				],
				[
					4.603843155234983,
					0.6576918793193158
				],
				[
					11.180761948427858,
					5.261535034554299
				],
				[
					13.153837586385748,
					7.23461067251219
				],
				[
					12.496145707066432,
					7.23461067251219
				],
				[
					9.207686310470024,
					7.892302551831449
				],
				[
					5.261535034554299,
					9.86537818978934
				],
				[
					2.6307675172771496,
					13.811529465705064
				],
				[
					3.2884593965964086,
					15.784605103662898
				],
				[
					3.9461512759157245,
					15.784605103662898
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0508887954056263,
				0.09200436621904373,
				0.15464797616004944,
				0.22501800954341888,
				0.288100004196167,
				0.24247348308563232,
				0.18882006406784058,
				0.17177627980709076,
				0.1882251650094986,
				0.22342638671398163,
				0.2742704153060913,
				0.10726315528154373,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 61,
			"versionNonce": 1446831923,
			"isDeleted": false,
			"id": "qCDUiDeXlQQJ6YdJ8SDj8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 222.59489760730895,
			"y": 200.1853319632179,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.415372620940047,
			"height": 27.623058931410128,
			"seed": 1935511335,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6576918793193158,
					0.6576918793193158
				],
				[
					-0.6576918793193158,
					2.6307675172772065
				],
				[
					0,
					11.83845382774723
				],
				[
					1.3153837586385748,
					19.73075637957868
				],
				[
					1.3153837586385748,
					21.703832017536513
				],
				[
					0.657691879319259,
					17.75768074162079
				],
				[
					-2.6307675172771496,
					14.46922134502438
				],
				[
					-6.576918793192874,
					15.126913224343639
				],
				[
					-9.207686310470024,
					22.36152389685583
				],
				[
					-6.576918793192874,
					27.623058931410128
				],
				[
					-2.6307675172771496,
					27.623058931410128
				],
				[
					0.657691879319259,
					24.334599534813663
				],
				[
					1.3153837586385748,
					23.019215776175088
				],
				[
					1.3153837586385748,
					24.99229141413298
				],
				[
					3.2884593965964086,
					26.965367052090812
				],
				[
					7.234610672512133,
					26.965367052090812
				],
				[
					9.207686310470024,
					23.019215776175088
				],
				[
					7.892302551831449,
					19.73075637957868
				],
				[
					2.6307675172771496,
					21.046140138217254
				],
				[
					0.657691879319259,
					24.334599534813663
				],
				[
					0,
					24.99229141413298
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07133398205041885,
				0.07904507219791412,
				0.19432801008224487,
				0.25434398651123047,
				0.1907648891210556,
				0.15026319026947021,
				0.09736587852239609,
				0.10641998052597046,
				0.1486651599407196,
				0.19106890261173248,
				0.18963201344013214,
				0.16935479640960693,
				0.14799371361732483,
				0.1844012439250946,
				0.22258464992046356,
				0.25098085403442383,
				0.3023691773414612,
				0.3122027814388275,
				0.17509230971336365,
				0.011673248372972012,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1708038525,
			"isDeleted": false,
			"id": "_7iGaxxYLX5FcNrdF-wIs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 229.82950827982108,
			"y": 222.54685586007372,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.892302551831449,
			"height": 1.9730756379578338,
			"seed": 1536033543,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.9730756379578906,
					0.657691879319259
				],
				[
					7.892302551831449,
					1.9730756379578338
				],
				[
					7.892302551831449,
					1.9730756379578338
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13246600329875946,
				0.18909670412540436,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 387942611,
			"isDeleted": false,
			"id": "tyanbxbuRumQ-0WvppRfo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 245.61411338348398,
			"y": 198.86994820457932,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3153837586385748,
			"height": 31.569210207325796,
			"seed": 1101545127,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.657691879319259,
					0
				],
				[
					-0.657691879319259,
					3.2884593965964655
				],
				[
					0,
					17.09998886230153
				],
				[
					-0.657691879319259,
					29.596134569367962
				],
				[
					-1.3153837586385748,
					31.569210207325796
				],
				[
					-1.3153837586385748,
					30.911518328006537
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.22485800087451935,
				0.2483557164669037,
				0.15890344977378845,
				0.011863769963383675,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 320365021,
			"isDeleted": false,
			"id": "HMNgHF5gFvaxAwu9HXMcY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 237.72181083165253,
			"y": 216.6276289462001,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.49614570706649,
			"height": 1.3153837586385748,
			"seed": 1393682343,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6576918793193158,
					0.6576918793193158
				],
				[
					11.180761948427914,
					1.3153837586385748
				],
				[
					12.49614570706649,
					1.3153837586385748
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13457998633384705,
				0.1420825868844986,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 310179443,
			"isDeleted": false,
			"id": "ZrebTV9yg7XsUUIV7sFCO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 254.16410781463475,
			"y": 223.8622396187123,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.180761948427858,
			"height": 9.207686310469967,
			"seed": 923352903,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.3153837586385748,
					1.3153837586385748
				],
				[
					-1.3153837586385748,
					6.576918793192817
				],
				[
					0.657691879319259,
					7.892302551831392
				],
				[
					5.919226913873558,
					7.892302551831392
				],
				[
					9.865378189789283,
					2.6307675172771496
				],
				[
					9.207686310470024,
					-1.3153837586385748
				],
				[
					1.9730756379578338,
					-1.3153837586385748
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14489199221134186,
				0.1724960058927536,
				0.22238199412822723,
				0.26352131366729736,
				0.27445632219314575,
				0.028667176142334938,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 415899197,
			"isDeleted": false,
			"id": "B_HRwQc9HBsvkIFFxoWUG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 261.3987184871469,
			"y": 228.46608277394728,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.576918793192874,
			"height": 5.261535034554299,
			"seed": 1174026663,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.9730756379578906,
					1.3153837586385748
				],
				[
					3.2884593965964655,
					1.9730756379578338
				],
				[
					6.576918793192874,
					4.603843155234983
				],
				[
					6.576918793192874,
					5.261535034554299
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10181500017642975,
				0.12362997233867645,
				0.09371664375066757,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1192996883,
			"isDeleted": false,
			"id": "jCY2WFoNglK4rXvFP5Fng",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 172.6103147790431,
			"y": 260.69298486059233,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.784605103662898,
			"height": 15.126913224343639,
			"seed": 1465028711,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.657691879319259,
					0
				],
				[
					8.549994431150708,
					2.6307675172771496
				],
				[
					15.126913224343582,
					6.576918793192874
				],
				[
					15.784605103662898,
					8.549994431150765
				],
				[
					13.811529465705007,
					8.549994431150765
				],
				[
					9.207686310470024,
					9.207686310470024
				],
				[
					5.919226913873558,
					12.49614570706649
				],
				[
					3.9461512759157245,
					15.126913224343639
				],
				[
					5.919226913873558,
					14.469221345024323
				],
				[
					6.576918793192874,
					13.811529465705064
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17665600776672363,
				0.2579760253429413,
				0.22076770663261414,
				0.17497588694095612,
				0.16941748559474945,
				0.1848996877670288,
				0.24817697703838348,
				0.2932202219963074,
				0.0830235630273819,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 231034525,
			"isDeleted": false,
			"id": "vn1TxNNyTVdcs7vNkVeIC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 198.9179899518146,
			"y": 264.63913613650806,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.549994431150708,
			"height": 27.62305893141007,
			"seed": 1313803751,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.9730756379578906
				],
				[
					1.3153837586385748,
					14.469221345024323
				],
				[
					0,
					24.334599534813663
				],
				[
					-1.3153837586385748,
					23.676907655494347
				],
				[
					-2.6307675172771496,
					15.126913224343639
				],
				[
					-2.6307675172771496,
					4.60384315523504
				],
				[
					2.6307675172771496,
					-3.2884593965964086
				],
				[
					5.919226913873558,
					-2.6307675172771496
				],
				[
					5.919226913873558,
					3.2884593965964655
				],
				[
					4.603843155234983,
					9.86537818978934
				],
				[
					3.9461512759157245,
					11.180761948427914
				],
				[
					3.9461512759157245,
					9.86537818978934
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14032800495624542,
				0.1800462007522583,
				0.16730917990207672,
				0.15606145560741425,
				0.13086849451065063,
				0.12498477101325989,
				0.15560199320316315,
				0.22271227836608887,
				0.2503087520599365,
				0.1745787411928177,
				0.0387754812836647,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 384972211,
			"isDeleted": false,
			"id": "oC9t7GRsZoaXMCOjnV_YE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 210.75644377956178,
			"y": 261.35067673991165,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.892302551831449,
			"height": 13.153837586385748,
			"seed": 1746853287,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.657691879319259
				],
				[
					0,
					4.603843155234983
				],
				[
					0,
					7.892302551831449
				],
				[
					0,
					5.919226913873558
				],
				[
					3.2884593965964086,
					-1.9730756379578906
				],
				[
					7.892302551831449,
					-5.261535034554299
				],
				[
					7.892302551831449,
					-5.261535034554299
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08911297470331192,
				0.16707415878772736,
				0.22542700171470642,
				0.27079179883003235,
				0.2400890737771988,
				0.03801995888352394,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 817591037,
			"isDeleted": false,
			"id": "fa0PwYO90YCrf7jG3fo8I",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 221.93720572798964,
			"y": 266.61221177446595,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.865378189789283,
			"height": 11.180761948427858,
			"seed": 641735111,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.657691879319259,
					0.657691879319259
				],
				[
					-1.3153837586385748,
					3.9461512759157245
				],
				[
					-0.657691879319259,
					5.261535034554299
				],
				[
					1.3153837586385748,
					5.919226913873558
				],
				[
					5.919226913873615,
					4.603843155234983
				],
				[
					7.892302551831449,
					-1.3153837586385748
				],
				[
					5.919226913873615,
					-5.261535034554299
				],
				[
					1.3153837586385748,
					-4.60384315523504
				],
				[
					-1.9730756379578338,
					4.603843155234983
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11044726520776749,
				0.14657211303710938,
				0.1485191285610199,
				0.1421079784631729,
				0.12992969155311584,
				0.1378869265317917,
				0.16297903656959534,
				0.024981629103422165,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1629947731,
			"isDeleted": false,
			"id": "3NuJ169z_5Fz-WkvjPvOB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 234.43335143505612,
			"y": 260.69298486059233,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.892302551831449,
			"height": 11.180761948427914,
			"seed": 1426261607,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6576918793193158,
					0
				],
				[
					-2.6307675172771496,
					0.6576918793193158
				],
				[
					-3.2884593965964655,
					1.9730756379578906
				],
				[
					-3.9461512759157245,
					7.23461067251219
				],
				[
					-1.3153837586385748,
					11.180761948427914
				],
				[
					3.2884593965964086,
					10.523070069108599
				],
				[
					3.9461512759157245,
					9.86537818978934
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06394919008016586,
				0.11934750527143478,
				0.20149600505828857,
				0.23275268077850342,
				0.06372103840112686,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1848511325,
			"isDeleted": false,
			"id": "Dyv1yM38cJyi3VpPfiFxk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 246.92949714212256,
			"y": 265.2968280158274,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.86537818978934,
			"height": 11.180761948427914,
			"seed": 1400138375,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6576918793193158,
					-0.6576918793193158
				],
				[
					1.3153837586385748,
					-1.3153837586385748
				],
				[
					0.6576918793193158,
					-1.9730756379578906
				],
				[
					-1.9730756379578338,
					-3.2884593965964655
				],
				[
					-5.261535034554299,
					0
				],
				[
					-6.576918793192874,
					5.261535034554299
				],
				[
					-3.9461512759157245,
					7.892302551831449
				],
				[
					2.6307675172771496,
					7.234610672512133
				],
				[
					3.2884593965964655,
					6.576918793192874
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11820199340581894,
				0.1733194887638092,
				0.17683151364326477,
				0.16803008317947388,
				0.22277075052261353,
				0.22477319836616516,
				0.05112976208329201,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1544594675,
			"isDeleted": false,
			"id": "Qy00p1n6He-jicyFOeOM6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 260.0833347285083,
			"y": 263.3237523778695,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.892302551831449,
			"height": 15.126913224343639,
			"seed": 647949543,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.9730756379578338,
					0
				],
				[
					-3.2884593965964086,
					0
				],
				[
					-5.261535034554299,
					0
				],
				[
					-3.2884593965964086,
					0.6576918793193158
				],
				[
					1.3153837586385748,
					5.261535034554299
				],
				[
					2.6307675172771496,
					11.180761948427914
				],
				[
					-0.657691879319259,
					15.126913224343639
				],
				[
					-4.603843155234983,
					14.469221345024323
				],
				[
					-4.603843155234983,
					13.811529465705064
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1043739914894104,
				0.15681399405002594,
				0.14107979834079742,
				0.1356654316186905,
				0.16128796339035034,
				0.20154403150081635,
				0.049518097192049026,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 644782013,
			"isDeleted": false,
			"id": "8y3DcR4z4ImMwh8s5pRtM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 267.97563728033975,
			"y": 267.2699036537852,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.892302551831449,
			"height": 18.415372620940047,
			"seed": 116108103,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6576918793193158
				],
				[
					0.6576918793193158,
					1.9730756379578906
				],
				[
					0.6576918793193158,
					2.6307675172771496
				],
				[
					1.3153837586385748,
					5.261535034554299
				],
				[
					3.2884593965964655,
					11.838453827747173
				],
				[
					3.9461512759157245,
					17.099988862301473
				],
				[
					2.6307675172771496,
					18.415372620940047
				],
				[
					0,
					17.75768074162079
				],
				[
					-3.2884593965964086,
					13.811529465705064
				],
				[
					-3.9461512759157245,
					13.153837586385748
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.01778222620487213,
				0.02580908127129078,
				0.05468878149986267,
				0.10028909146785736,
				0.15581224858760834,
				0.17793017625808716,
				0.2225033938884735,
				0.20406058430671692,
				0.07386481016874313,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 792039059,
			"isDeleted": false,
			"id": "W2zp8cFuZZzNkCzyD8p4y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 279.98843552886774,
			"y": 267.97601271566674,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6572037157195041,
			"height": 9.200852020072773,
			"seed": 1460852935,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6572037157194472
				],
				[
					0,
					5.914833441475309
				],
				[
					0,
					9.200852020072773
				],
				[
					-0.6572037157195041,
					9.200852020072773
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1992499977350235,
				0.23403400182724,
				0.10554836690425873,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 866031645,
			"isDeleted": false,
			"id": "wV0lQQ5gxibyvMS5Tg02j",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 279.98843552886774,
			"y": 260.7467718427524,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.9716111471584554,
			"height": 2.6288148628779027,
			"seed": 812734343,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.3144074314390082,
					1.3144074314389513
				],
				[
					-1.9716111471584554,
					2.6288148628779027
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14180828630924225,
				0.10580401867628098,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1296843827,
			"isDeleted": false,
			"id": "ebeQxCI4vI9Ml5TltO1nH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 286.56047268606255,
			"y": 266.66160528422773,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.858055735792277,
			"height": 13.801278030109131,
			"seed": 2081539655,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6572037157195041
				],
				[
					0,
					2.6288148628779595
				],
				[
					0.6572037157194472,
					6.57203715719487
				],
				[
					2.6288148628779027,
					8.543648304353326
				],
				[
					4.600426010036358,
					3.943222294316911
				],
				[
					8.543648304353269,
					-0.6572037157194472
				],
				[
					9.858055735792277,
					1.9716111471584554
				],
				[
					8.543648304353269,
					8.543648304353326
				],
				[
					7.229240872914261,
					12.48687059867018
				],
				[
					7.229240872914261,
					13.144074314389684
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08360446244478226,
				0.13747021555900574,
				0.12346944957971573,
				0.05993408337235451,
				0.10187744349241257,
				0.15726247429847717,
				0.14799529314041138,
				0.05080447345972061,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 800033917,
			"isDeleted": false,
			"id": "xsOvg727gk3VHGOI_majt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 302.4945395072822,
			"y": 271.43078133544304,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.110154970247322,
			"height": 13.251134502177877,
			"seed": 974646249,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8281959063862132,
					0.8281959063861564
				],
				[
					-0.8281959063862132,
					1.656391812772256
				],
				[
					-1.6563918127723127,
					4.140979531930611
				],
				[
					0,
					8.281959063861166
				],
				[
					3.312783625544398,
					10.766546783019521
				],
				[
					6.62556725108891,
					7.453763157475066
				],
				[
					6.62556725108891,
					0.8281959063861564
				],
				[
					2.4845877191582986,
					-2.4845877191583554
				],
				[
					-1.6563918127723127,
					0.8281959063861564
				],
				[
					-2.4845877191584123,
					5.79737134470281
				],
				[
					-2.4845877191584123,
					6.625567251088967
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0475044846534729,
				0.09997811913490295,
				0.14221610128879547,
				0.1694377064704895,
				0.2034565806388855,
				0.19706429541110992,
				0.18827907741069794,
				0.09883541613817215,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 238765523,
			"isDeleted": false,
			"id": "5IsX927AzyYsd3zqvXZXO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 309.9483026647572,
			"y": 276.39995677375975,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.907526314950132,
			"height": 26.50226900435581,
			"seed": 712294729,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8281959063860995
				],
				[
					0.8281959063860995,
					2.4845877191583554
				],
				[
					2.4845877191584123,
					5.79737134470281
				],
				[
					3.312783625544512,
					9.938350876633422
				],
				[
					3.312783625544512,
					14.907526314950132
				],
				[
					-3.312783625544512,
					21.5330935660391
				],
				[
					-10.766546783019521,
					25.674073097969654
				],
				[
					-11.59474268940562,
					26.50226900435581
				],
				[
					-11.59474268940562,
					25.674073097969654
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06717553734779358,
				0.1054108589887619,
				0.15848425030708313,
				0.16712945699691772,
				0.2526100277900696,
				0.2954557538032532,
				0.05386706441640854,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 2053305565,
			"isDeleted": false,
			"id": "GQmIMlSIfcJoqdSNoIQaz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 324.326536717791,
			"y": 279.16976949496524,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.202114192201464,
			"height": 6.339957727383137,
			"seed": 1614233833,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7044397474870152,
					0
				],
				[
					-1.4088794949740304,
					0
				],
				[
					-1.4088794949740304,
					-0.7044397474870152
				],
				[
					0.7044397474870152,
					-1.4088794949740304
				],
				[
					7.044397474870209,
					-1.4088794949740304
				],
				[
					14.793234697227433,
					4.9310782324091065
				],
				[
					14.793234697227433,
					4.9310782324091065
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06181298941373825,
				0.0964069813489914,
				0.1615903675556183,
				0.2816839814186096,
				0.3246840238571167,
				0.04451379552483559,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 152638323,
			"isDeleted": false,
			"id": "VdEXDKlcFA0frncGwVFJN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 348.2774881323497,
			"y": 274.2386912625561,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.86215646481827,
			"height": 14.088794949740418,
			"seed": 1240605385,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7044397474870152,
					0
				],
				[
					-0.7044397474870152,
					0.7044397474870152
				],
				[
					1.4088794949740304,
					0.7044397474870152
				],
				[
					4.9310782324091065,
					1.4088794949740304
				],
				[
					8.45327696984424,
					2.8177589899481177
				],
				[
					9.157716717331255,
					3.522198737435133
				],
				[
					6.339957727383137,
					4.931078232409163
				],
				[
					2.817758989948061,
					10.566596212305285
				],
				[
					0.7044397474870152,
					14.088794949740418
				],
				[
					0.7044397474870152,
					12.679915454766387
				],
				[
					1.4088794949740304,
					11.975475707279372
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06997878849506378,
				0.09139663726091385,
				0.2229672223329544,
				0.2526971697807312,
				0.25201672315597534,
				0.23108114302158356,
				0.1785825490951538,
				0.1800910383462906,
				0.2046860307455063,
				0.04725857451558113,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 2135576893,
			"isDeleted": false,
			"id": "lgM5sHTd-VJVMEVcThWmo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 374.34175878936935,
			"y": 265.78541429271183,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7044397474870152,
			"height": 0.7044397474870152,
			"seed": 1274006569,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7044397474870152,
					0.7044397474870152
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.016070708632469177,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 774647059,
			"isDeleted": false,
			"id": "7VcJTcfB0TtHFGjZwwWce",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 374.34175878936935,
			"y": 259.4454565653287,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.384355202253403,
			"height": 26.76871040450675,
			"seed": 257823369,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7044397474870152,
					2.817758989948061
				],
				[
					1.4088794949740873,
					7.044397474870152
				],
				[
					1.4088794949740873,
					22.5420719195846
				],
				[
					0.7044397474870152,
					19.72431292963654
				],
				[
					0,
					14.088794949740361
				],
				[
					2.8177589899481177,
					9.86215646481827
				],
				[
					9.86215646481827,
					11.2710359597923
				],
				[
					13.384355202253403,
					17.610993687175494
				],
				[
					12.679915454766387,
					23.95095141455863
				],
				[
					9.157716717331255,
					26.064270657019676
				],
				[
					4.931078232409163,
					26.76871040450675
				],
				[
					2.1133192424611025,
					24.655391162045646
				],
				[
					2.1133192424611025,
					23.95095141455863
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04708721861243248,
				0.06215270981192589,
				0.13152246177196503,
				0.0845920741558075,
				0.07222915440797806,
				0.0592338852584362,
				0.08434039354324341,
				0.08895422518253326,
				0.11590121686458588,
				0.12428576499223709,
				0.12206863611936569,
				0.03915005549788475,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1002906013,
			"isDeleted": false,
			"id": "hXBGEzxIiIC14R2n_sPu0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 390.5438729815708,
			"y": 277.0564502525042,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.157716717331255,
			"height": 10.566596212305285,
			"seed": 1537146281,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7044397474870152,
					1.4088794949740304
				],
				[
					-1.4088794949740304,
					2.817758989948061
				],
				[
					0,
					6.339957727383137
				],
				[
					3.522198737435076,
					7.044397474870152
				],
				[
					7.044397474870209,
					6.339957727383137
				],
				[
					7.748837222357224,
					1.4088794949740304
				],
				[
					5.6355179798961785,
					-2.8177589899481177
				],
				[
					2.817758989948061,
					-3.522198737435133
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09422171115875244,
				0.12221847474575043,
				0.13608978688716888,
				0.1781775802373886,
				0.2108200341463089,
				0.20095275342464447,
				0.03192459046840668,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 552276659,
			"isDeleted": false,
			"id": "hWypYhEpIgJK37G474kZN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 397.588270456441,
			"y": 280.57864898993927,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.339957727383194,
			"height": 2.1133192424610456,
			"seed": 699394089,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4088794949740304,
					0.7044397474870152
				],
				[
					5.635517979896122,
					-0.7044397474870152
				],
				[
					6.339957727383194,
					-1.4088794949740304
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11685870587825775,
				0.08552383631467819,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 84600317,
			"isDeleted": false,
			"id": "vmo0g4d3dHUcfuX-vHPU_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 410.97262565869437,
			"y": 256.6276975753806,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.1133192424610456,
			"height": 27.473150151993764,
			"seed": 1166847625,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.4088794949740304,
					4.931078232409163
				],
				[
					-1.4088794949740304,
					9.86215646481827
				],
				[
					-0.7044397474870152,
					19.724312929636596
				],
				[
					0,
					27.473150151993764
				],
				[
					0.7044397474870152,
					27.473150151993764
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.17941519618034363,
				0.22701434791088104,
				0.04506368935108185,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 1375487059,
			"isDeleted": false,
			"id": "OJSaFEef8zDKd552XRG-3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 416.60814363859055,
			"y": 255.21881808040655,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4088794949740304,
			"height": 29.58646939445481,
			"seed": 1518670505,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.4088794949740304
				],
				[
					0,
					4.931078232409163
				],
				[
					0.7044397474870152,
					11.2710359597923
				],
				[
					1.4088794949740304,
					24.655391162045703
				],
				[
					0.7044397474870152,
					29.58646939445481
				],
				[
					0,
					29.58646939445481
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15754801034927368,
				0.2139360010623932,
				0.20595934987068176,
				0.0477830208837986,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 236396125,
			"isDeleted": false,
			"id": "8isnhJZ3owD92Iq6LXBRO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 401.8149089413631,
			"y": 274.2386912625561,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.202114192201464,
			"height": 0.7044397474870152,
			"seed": 79239593,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.4088794949740304,
					0.7044397474870152
				],
				[
					-2.1133192424610456,
					0.7044397474870152
				],
				[
					0.7044397474870152,
					0.7044397474870152
				],
				[
					12.679915454766387,
					0
				],
				[
					14.088794949740418,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09870999306440353,
				0.2980639934539795,
				0.08667736500501633,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1496728051,
			"isDeleted": false,
			"id": "5N1LMGpn0Vxe_zXlxIKKv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 427.17473985089583,
			"y": 275.6475707575301,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.86215646481827,
			"height": 11.2710359597923,
			"seed": 2064597449,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7044397474870152,
					0
				],
				[
					1.4088794949740304,
					0
				],
				[
					3.522198737435076,
					-1.4088794949740304
				],
				[
					2.817758989948061,
					-2.817758989948061
				],
				[
					-2.1133192424610456,
					-4.226638484922091
				],
				[
					-6.339957727383194,
					-1.4088794949740304
				],
				[
					-6.339957727383194,
					3.522198737435133
				],
				[
					1.4088794949740304,
					7.044397474870209
				],
				[
					2.1133192424610456,
					7.044397474870209
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08800598233938217,
				0.13458599150180817,
				0.20500998198986053,
				0.19674795866012573,
				0.11388171464204788,
				0.09558901935815811,
				0.18210577964782715,
				0.09073547273874283,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 767380157,
			"isDeleted": false,
			"id": "mVfmcX5VyOiz_KEeqOS1m",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 434.92357707325306,
			"y": 274.2386912625561,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.339957727383137,
			"height": 14.793234697227376,
			"seed": 762515817,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7044397474870152,
					0
				],
				[
					-0.7044397474870152,
					3.522198737435133
				],
				[
					0,
					8.45327696984424
				],
				[
					1.4088794949740304,
					9.86215646481827
				],
				[
					2.817758989948061,
					3.522198737435133
				],
				[
					5.635517979896122,
					-4.9310782324091065
				],
				[
					5.635517979896122,
					-4.9310782324091065
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12062997370958328,
				0.12840469181537628,
				0.125628262758255,
				0.1947091668844223,
				0.11071637272834778,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 262114195,
			"isDeleted": false,
			"id": "vNLVs_VO54IPGx-CLyER6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 444.7857335380713,
			"y": 274.9431310100431,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.339957727383137,
			"height": 6.339957727383194,
			"seed": 1849123657,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.4088794949740873
				],
				[
					1.4088794949740304,
					2.8177589899481177
				],
				[
					5.635517979896122,
					5.6355179798961785
				],
				[
					6.339957727383137,
					6.339957727383194
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1229807436466217,
				0.061796508729457855,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1688136477,
			"isDeleted": false,
			"id": "C1Qj93M6OWKpZtJ6O96NI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 455.3523297503766,
			"y": 274.9431310100431,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.044397474870209,
			"height": 26.064270657019733,
			"seed": 1503697033,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.4088794949740304,
					2.1133192424611025
				],
				[
					-4.226638484922148,
					9.157716717331255
				],
				[
					-6.339957727383194,
					25.359830909532718
				],
				[
					-7.044397474870209,
					26.064270657019733
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15080301463603973,
				0.3542659878730774,
				0.18237723410129547,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1768857907,
			"isDeleted": false,
			"id": "3JdV6j0w_JpSqJiMieqFq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 482.8254799023704,
			"y": 260.8543360603027,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.793234697227376,
			"height": 25.359830909532718,
			"seed": 242277833,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7044397474870152
				],
				[
					-0.704439747487072,
					5.635517979896122
				],
				[
					0,
					14.793234697227376
				],
				[
					0.7044397474869584,
					18.31543343466251
				],
				[
					0,
					16.90655393968848
				],
				[
					-4.226638484922091,
					14.088794949740361
				],
				[
					-9.157716717331255,
					14.793234697227376
				],
				[
					-11.975475707279315,
					20.428752677123555
				],
				[
					-9.862156464818327,
					24.655391162045646
				],
				[
					-4.931078232409163,
					25.359830909532718
				],
				[
					2.113319242460989,
					21.13319242461057
				],
				[
					2.817758989948061,
					21.13319242461057
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15356998145580292,
				0.20063000917434692,
				0.17636001110076904,
				0.1359265148639679,
				0.1416352242231369,
				0.20099890232086182,
				0.22268201410770416,
				0.2263936698436737,
				0.21138396859169006,
				0.03687442094087601,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 590184317,
			"isDeleted": false,
			"id": "BHBOfGkHgQDUcG6CvzSIk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 489.8698773772405,
			"y": 274.2386912625561,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.453276969844183,
			"height": 14.793234697227376,
			"seed": 1524750857,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7044397474870152
				],
				[
					-0.7044397474869584,
					2.1133192424611025
				],
				[
					0,
					6.339957727383194
				],
				[
					1.4088794949740304,
					10.566596212305285
				],
				[
					2.1133192424611025,
					11.2710359597923
				],
				[
					3.522198737435133,
					4.931078232409163
				],
				[
					4.931078232409163,
					0
				],
				[
					7.044397474870266,
					-3.522198737435076
				],
				[
					7.748837222357224,
					-3.522198737435076
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15951482951641083,
				0.1343316286802292,
				0.10751006752252579,
				0.12532702088356018,
				0.18249554932117462,
				0.22112411260604858,
				0.05949551239609718,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 269091539,
			"isDeleted": false,
			"id": "g3CTQgy9v09nbs0aelgKt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 501.84535308451984,
			"y": 275.6475707575301,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.044397474870152,
			"height": 9.86215646481827,
			"seed": 1151160745,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7044397474869584,
					0
				],
				[
					-0.7044397474869584,
					2.8177589899481177
				],
				[
					1.4088794949740304,
					4.931078232409163
				],
				[
					4.931078232409163,
					4.931078232409163
				],
				[
					6.339957727383194,
					1.4088794949740873
				],
				[
					6.339957727383194,
					-4.226638484922091
				],
				[
					2.1133192424611025,
					-4.9310782324091065
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15976598858833313,
				0.1380908489227295,
				0.17726193368434906,
				0.28779399394989014,
				0.3071945607662201,
				0.30799978971481323,
				0.05748001113533974,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1336575965,
			"isDeleted": false,
			"id": "tbuL0Z2iYEJLfJS6TqnKz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 506.07199156944205,
			"y": 276.3520105050172,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.635517979896122,
			"height": 4.9310782324091065,
			"seed": 673631561,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7044397474869584,
					1.4088794949740304
				],
				[
					1.4088794949740304,
					2.1133192424610456
				],
				[
					4.93107823240905,
					4.9310782324091065
				],
				[
					5.635517979896122,
					4.226638484922091
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.19136667251586914,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1007169651,
			"isDeleted": false,
			"id": "vurhMQUni6lSPxVWsEDxY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 521.5696660141564,
			"y": 270.716492525121,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4088794949740304,
			"height": 10.566596212305285,
			"seed": 393773705,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7044397474870152
				],
				[
					-0.7044397474869584,
					3.522198737435076
				],
				[
					0.704439747487072,
					10.566596212305285
				],
				[
					0.704439747487072,
					10.566596212305285
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.15399694442749023,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 203916349,
			"isDeleted": false,
			"id": "KnhrMleFKZNY-AmnrVU8L",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 521.5696660141564,
			"y": 265.0809745452248,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.113319242460989,
			"height": 1.4088794949740304,
			"seed": 1741768649,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7044397474869584,
					0.7044397474870152
				],
				[
					-2.113319242460989,
					1.4088794949740304
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13799630105495453,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1328523795,
			"isDeleted": false,
			"id": "20AfQUBcOIPZMg1A-odao",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 528.6140634890266,
			"y": 270.012052777634,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.044397474870152,
			"height": 12.67991545476633,
			"seed": 212147465,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7044397474869584,
					4.9310782324091065
				],
				[
					2.113319242460989,
					9.86215646481827
				],
				[
					3.522198737435019,
					7.748837222357224
				],
				[
					5.635517979896122,
					2.1133192424610456
				],
				[
					5.635517979896122,
					0.7044397474870152
				],
				[
					6.339957727383194,
					6.339957727383194
				],
				[
					7.044397474870152,
					12.67991545476633
				],
				[
					7.044397474870152,
					12.67991545476633
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.22085198760032654,
				0.23106186091899872,
				0.11734902858734131,
				0.09747771918773651,
				0.2837308645248413,
				0.37617599964141846,
				0.16409531235694885,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1015411869,
			"isDeleted": false,
			"id": "LKtBEnY9pgPRfHmi6cUsW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 563.4721599364146,
			"y": 260.0691288721827,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6717519266620684,
			"height": 22.167813579849508,
			"seed": 686036425,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1.3435038533241936
				],
				[
					0,
					-2.015255779986319
				],
				[
					-0.6717519266620684,
					-2.6870077066483873
				],
				[
					0,
					3.3587596333105694
				],
				[
					0,
					14.106790459904289
				],
				[
					0,
					19.48080587320112
				],
				[
					0,
					16.12204623989055
				],
				[
					0,
					14.778542386566357
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05022198334336281,
				0.039958372712135315,
				0.08467547595500946,
				0.15151290595531464,
				0.1321691870689392,
				0.09907931834459305,
				0.003281066892668605,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 779546547,
			"isDeleted": false,
			"id": "EQnUOe1uR1cOVsp4h9eCZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 560.1134003031041,
			"y": 256.7103692388722,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 20.15255779986319,
			"height": 26.87007706648427,
			"seed": 401022601,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6717519266621252
				],
				[
					3.3587596333105694,
					-1.3435038533242505
				],
				[
					12.763286606580095,
					-0.6717519266621252
				],
				[
					17.4655500932148,
					0.6717519266621252
				],
				[
					18.13730201987687,
					0.6717519266621252
				],
				[
					17.4655500932148,
					0
				],
				[
					16.793798166552733,
					0
				],
				[
					16.793798166552733,
					0.6717519266621252
				],
				[
					17.4655500932148,
					6.717519266621082
				],
				[
					18.809053946539052,
					16.12204623989055
				],
				[
					19.48080587320112,
					21.496061653187382
				],
				[
					19.48080587320112,
					24.183069359835827
				],
				[
					20.15255779986319,
					24.854821286497952
				],
				[
					19.48080587320112,
					24.183069359835827
				],
				[
					17.4655500932148,
					22.839565506511633
				],
				[
					13.435038533242164,
					22.167813579849508
				],
				[
					8.732775046607458,
					22.167813579849508
				],
				[
					2.687007706648501,
					24.183069359835827
				],
				[
					0.6717519266621821,
					25.52657321316002
				],
				[
					2.015255779986319,
					24.854821286497952
				],
				[
					2.687007706648501,
					24.854821286497952
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07699398696422577,
				0.11992224305868149,
				0.14935480058193207,
				0.13772793114185333,
				0.13044269382953644,
				0.12941879034042358,
				0.12328241020441055,
				0.11178594827651978,
				0.12384100258350372,
				0.1333378553390503,
				0.13021047413349152,
				0.1280355602502823,
				0.12731768190860748,
				0.12450481951236725,
				0.10128146409988403,
				0.098160520195961,
				0.11824462562799454,
				0.141496941447258,
				0.14532950520515442,
				0.04744940251111984,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 66,
			"versionNonce": 1282889981,
			"isDeleted": false,
			"id": "v9LjshigrNPWIgU8e0ED2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 566.8309195697252,
			"y": 249.321098045589,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.717519266621025,
			"height": 8.732775046607372,
			"seed": 1942917289,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6717519266620968
				],
				[
					0,
					-1.3435038533241936
				],
				[
					-0.6717519266621821,
					-0.6717519266620968
				],
				[
					-0.6717519266621821,
					2.015255779986319
				],
				[
					-0.6717519266621821,
					5.37401541329686
				],
				[
					-0.6717519266621821,
					6.045767339958957
				],
				[
					-0.6717519266621821,
					5.37401541329686
				],
				[
					-0.6717519266621821,
					3.358759633310541
				],
				[
					-0.6717519266621821,
					0.6717519266621252
				],
				[
					-0.6717519266621821,
					-1.3435038533241936
				],
				[
					-0.6717519266621821,
					-2.6870077066484157
				],
				[
					-1.3435038533242505,
					-2.6870077066484157
				],
				[
					0,
					-2.015255779986319
				],
				[
					2.015255779986319,
					-1.3435038533241936
				],
				[
					4.030511559972638,
					-1.3435038533241936
				],
				[
					4.702263486634706,
					-1.3435038533241936
				],
				[
					4.702263486634706,
					-2.015255779986319
				],
				[
					4.702263486634706,
					-1.3435038533241936
				],
				[
					4.702263486634706,
					0.6717519266621252
				],
				[
					4.702263486634706,
					2.687007706648444
				],
				[
					5.374015413296775,
					4.702263486634763
				],
				[
					5.374015413296775,
					6.045767339958957
				],
				[
					4.702263486634706,
					6.045767339958957
				],
				[
					3.3587596333104557,
					6.045767339958957
				],
				[
					2.015255779986319,
					5.37401541329686
				],
				[
					0.6717519266620684,
					5.37401541329686
				],
				[
					1.3435038533241368,
					5.37401541329686
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.031502410769462585,
				0.10221490263938904,
				0.1539149135351181,
				0.16935110092163086,
				0.17555591464042664,
				0.16267040371894836,
				0.08626754581928253,
				0.05256088078022003,
				0.04101904481649399,
				0.07193893194198608,
				0.09182263165712357,
				0.12313369661569595,
				0.15621960163116455,
				0.1571628749370575,
				0.14199349284172058,
				0.13265350461006165,
				0.13364681601524353,
				0.1283918172121048,
				0.13004614412784576,
				0.14733487367630005,
				0.15030960738658905,
				0.15375329554080963,
				0.18866494297981262,
				0.22627228498458862,
				0.24169494211673737,
				0.23615814745426178,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1543799123,
			"isDeleted": false,
			"id": "NUFAWteZWWGxl6452pgAe",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 567.5026714963873,
			"y": 259.39737694552065,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6717519266620684,
			"height": 6.717519266621025,
			"seed": 2046950409,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6717519266620684
				],
				[
					0,
					3.3587596333105125
				],
				[
					0,
					6.045767339958957
				],
				[
					0.6717519266620684,
					6.717519266621025
				],
				[
					0.6717519266620684,
					6.717519266621025
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1506199985742569,
				0.12523816525936127,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 897397085,
			"isDeleted": false,
			"id": "TEbPYs6xLzmdzlrhu_jxD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 564.8156637897389,
			"y": 262.08438465216904,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.045767339958957,
			"height": 0.6717519266621252,
			"seed": 1677758505,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6717519266621252
				],
				[
					2.015255779986319,
					0.6717519266621252
				],
				[
					4.702263486634706,
					0
				],
				[
					6.045767339958957,
					0
				],
				[
					6.045767339958957,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07765597850084305,
				0.21351999044418335,
				0.22870586812496185,
				0.07684347778558731,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1362026227,
			"isDeleted": false,
			"id": "-xLqmvq66uI9mYcJQVVI-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 567.5026714963873,
			"y": 272.83241547876275,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.045767339958957,
			"height": 1.3435038533242505,
			"seed": 1108674633,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6717519266620684,
					0.6717519266621252
				],
				[
					0.6717519266620684,
					0.6717519266621252
				],
				[
					3.3587596333105694,
					0.6717519266621252
				],
				[
					4.702263486634706,
					1.3435038533242505
				],
				[
					5.374015413296888,
					1.3435038533242505
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04201797395944595,
				0.21080200374126434,
				0.26301097869873047,
				0.151166632771492,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1156119997,
			"isDeleted": false,
			"id": "lYD4A1-zMPjqfz-cMW11y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 592.9452039455467,
			"y": 256.31173116197897,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.495769716660675,
			"height": 17.45064669437471,
			"seed": 109569129,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.49858990555358673
				],
				[
					0,
					-1.99435962221429
				],
				[
					0,
					-2.9915394333214067
				],
				[
					0.4985899055535583,
					-0.9971798111071735
				],
				[
					1.495769716660675,
					7.4788485833034315
				],
				[
					0.9971798111072303,
					13.960517355499746
				],
				[
					0.9971798111072303,
					14.459107261053305
				],
				[
					1.495769716660675,
					13.960517355499746
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.032791320234537125,
				0.08924520760774612,
				0.12170547246932983,
				0.1451171636581421,
				0.1197572648525238,
				0.023845581337809563,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 410814611,
			"isDeleted": false,
			"id": "XNYqwXqWS1iUYJ8siO1HP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 589.9536645122254,
			"y": 276.75391728967503,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.476028394410605,
			"height": 7.97743848885699,
			"seed": 1486300457,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.4985899055535583
				],
				[
					-0.4985899055535583,
					-0.9971798111071166
				],
				[
					-0.4985899055535583,
					-1.495769716660675
				],
				[
					0,
					0.49858990555361515
				],
				[
					2.4929495277677916,
					5.484488961089198
				],
				[
					4.487309149982025,
					6.481668772196315
				],
				[
					6.481668772196258,
					1.4957697166607318
				],
				[
					7.977438488857047,
					-1.495769716660675
				],
				[
					7.977438488857047,
					-0.9971798111071166
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.04828488081693649,
				0.10601837188005447,
				0.13207589089870453,
				0.14312200248241425,
				0.1339227855205536,
				0.15981942415237427,
				0.15913580358028412,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 568081949,
			"isDeleted": false,
			"id": "fXadRA6LrMq88VI0WV1OG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -11.000864841887193,
			"y": 215.0091311285289,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.640445901182659,
			"height": 12.960668851774017,
			"seed": 1734070473,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.43202229505914147
				],
				[
					0,
					2.160111475295679
				],
				[
					-0.43202229505914147,
					9.0724681962418
				],
				[
					-0.8640445901182829,
					12.528646556714875
				],
				[
					-1.296066885177396,
					12.096624261655734
				],
				[
					-0.43202229505914147,
					7.776401311064404
				],
				[
					3.4561783604730465,
					1.7280891802365375
				],
				[
					6.912356720946121,
					-0.43202229505914147
				],
				[
					7.344379016005263,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10949786007404327,
				0.1413879096508026,
				0.15989795327186584,
				0.15773004293441772,
				0.14845605194568634,
				0.17817464470863342,
				0.24813391268253326,
				0.07767300307750702,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 665058867,
			"isDeleted": false,
			"id": "UAlhLZSzdgkIIbtmWSh4X",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2.360418940704534,
			"y": 218.8973317840611,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.480334425887008,
			"height": 8.208423606123517,
			"seed": 647430249,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8640445901182545,
					0.8640445901182829
				],
				[
					-1.296066885177396,
					2.160111475295679
				],
				[
					-1.7280891802365375,
					3.456178360473075
				],
				[
					-0.8640445901182545,
					6.048312130827867
				],
				[
					2.160111475295679,
					5.616289835768754
				],
				[
					4.320222950591329,
					3.0241560654139334
				],
				[
					4.752245245650471,
					0
				],
				[
					3.0241560654139334,
					-2.1601114752956505
				],
				[
					0,
					-1.728089180236509
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09566199034452438,
				0.12418799102306366,
				0.18112100660800934,
				0.20472894608974457,
				0.20726147294044495,
				0.26963311433792114,
				0.19774039089679718,
				0.023101380094885826,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 323515005,
			"isDeleted": false,
			"id": "yB8bcTEOJ-_CJGf2BQZjH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1.064352055527138,
			"y": 221.05744325935677,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.184267540709612,
			"height": 1.7280891802365375,
			"seed": 747275721,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.43202229505914147
				],
				[
					0.8640445901182829,
					0.8640445901182545
				],
				[
					1.7280891802365375,
					1.296066885177396
				],
				[
					4.752245245650471,
					1.7280891802365375
				],
				[
					5.184267540709612,
					1.7280891802365375
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10629598796367645,
				0.16600900888442993,
				0.10322457551956177,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 2039201747,
			"isDeleted": false,
			"id": "8kqDHOKkXga01XVZItDDK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 6.280026960478125,
			"y": 218.03328719394284,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.91235672094615,
			"height": 9.0724681962418,
			"seed": 1092194793,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.296066885177396
				],
				[
					0,
					3.0241560654139334
				],
				[
					0.43202229505914147,
					4.752245245650471
				],
				[
					1.296066885177396,
					6.480334425887008
				],
				[
					2.592133770354792,
					4.320222950591329
				],
				[
					5.184267540709612,
					0
				],
				[
					6.91235672094615,
					-1.296066885177396
				],
				[
					6.91235672094615,
					2.160111475295679
				],
				[
					5.616289835768725,
					7.776401311064404
				],
				[
					5.616289835768725,
					7.344379016005263
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0718199759721756,
				0.1498793065547943,
				0.17214557528495789,
				0.11158819496631622,
				0.09761746227741241,
				0.16466626524925232,
				0.217496857047081,
				0.04792352393269539,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 99556061,
			"isDeleted": false,
			"id": "PSavJlFzxksWT1XE4CXhd",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 16.64856204189732,
			"y": 218.8973317840611,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.048312130827867,
			"height": 6.912356720946121,
			"seed": 389422185,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.296066885177396,
					1.7280891802365375
				],
				[
					-1.296066885177396,
					4.320222950591358
				],
				[
					0.8640445901182829,
					5.184267540709612
				],
				[
					3.8882006555322164,
					3.8882006555322164
				],
				[
					4.752245245650471,
					0
				],
				[
					2.592133770354792,
					-1.728089180236509
				],
				[
					-0.43202229505911305,
					3.0241560654139334
				],
				[
					-0.43202229505911305,
					3.456178360473075
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06316549330949783,
				0.1583620011806488,
				0.17972220480442047,
				0.19678308069705963,
				0.2347613275051117,
				0.22508594393730164,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1749699955,
			"isDeleted": false,
			"id": "u-p9GQFMRjnpCuz92JCS0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 20.536762697429538,
			"y": 217.6012648988837,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.800557376478338,
			"height": 19.008980982601884,
			"seed": 526343465,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8640445901182829
				],
				[
					-0.43202229505914147,
					3.456178360473075
				],
				[
					0.8640445901182545,
					6.91235672094615
				],
				[
					2.592133770354792,
					10.800557376478338
				],
				[
					2.1601114752956505,
					15.552802622128809
				],
				[
					-2.160111475295679,
					19.008980982601884
				],
				[
					-6.91235672094615,
					18.1449363924836
				],
				[
					-8.208423606123546,
					15.120780327069667
				],
				[
					-7.776401311064404,
					14.688758032010526
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10191067308187485,
				0.18425235152244568,
				0.20821963250637054,
				0.26085153222084045,
				0.2996271550655365,
				0.21188604831695557,
				0.018065979704260826,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1382135613,
			"isDeleted": false,
			"id": "99I3vZAXrnCtIGbyYAV50",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 30.473275483789592,
			"y": 220.62542096429763,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.0724681962418,
			"height": 10.368535081419225,
			"seed": 313985225,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.43202229505914147,
					0
				],
				[
					3.0241560654139334,
					-1.7280891802365375
				],
				[
					3.456178360473075,
					-4.320222950591329
				],
				[
					0.8640445901182545,
					-4.752245245650471
				],
				[
					-1.296066885177396,
					-0.8640445901182545
				],
				[
					-0.43202229505914147,
					3.8882006555322164
				],
				[
					3.456178360473075,
					5.616289835768754
				],
				[
					7.344379016005263,
					4.320222950591329
				],
				[
					7.776401311064404,
					3.8882006555322164
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1292179822921753,
				0.2023800015449524,
				0.19310876727104187,
				0.13637347519397736,
				0.1880628913640976,
				0.2821890115737915,
				0.3091566264629364,
				0.11145810037851334,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1193682707,
			"isDeleted": false,
			"id": "kp5KsFUiRx2RaazAqYrki",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -14.457043202360268,
			"y": 238.3383350617221,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.640445901182659,
			"height": 15.120780327069667,
			"seed": 409286761,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.43202229505914147
				],
				[
					0,
					1.7280891802365375
				],
				[
					0.43202229505914147,
					4.752245245650471
				],
				[
					1.7280891802365375,
					12.096624261655734
				],
				[
					1.296066885177396,
					15.120780327069667
				],
				[
					0.43202229505914147,
					14.256735736951413
				],
				[
					-2.1601114752956505,
					7.776401311064404
				],
				[
					-0.8640445901182545,
					2.5921337703548204
				],
				[
					3.456178360473075,
					0
				],
				[
					6.480334425887008,
					2.160111475295679
				],
				[
					6.048312130827867,
					5.616289835768754
				],
				[
					3.0241560654139334,
					7.344379016005263
				],
				[
					3.0241560654139334,
					6.91235672094615
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.052581787109375,
				0.07484295964241028,
				0.11376076936721802,
				0.13185781240463257,
				0.12955637276172638,
				0.07341970503330231,
				0.08482439815998077,
				0.1449432075023651,
				0.16436199843883514,
				0.15789709985256195,
				0.025406768545508385,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1124190109,
			"isDeleted": false,
			"id": "YfBO6JNcdNQZMwN5vVF1b",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -5.384575006118467,
			"y": 236.17822358642644,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.752245245650471,
			"height": 8.640445901182659,
			"seed": 253599625,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.296066885177396
				],
				[
					0,
					2.592133770354792
				],
				[
					0.43202229505914147,
					4.320222950591329
				],
				[
					0.8640445901182545,
					7.776401311064404
				],
				[
					0.8640445901182545,
					8.640445901182659
				],
				[
					1.296066885177396,
					6.048312130827867
				],
				[
					4.320222950591329,
					2.592133770354792
				],
				[
					4.752245245650471,
					2.592133770354792
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.060033995658159256,
				0.06568444520235062,
				0.11379537731409073,
				0.14756061136722565,
				0.13157513737678528,
				0.13040155172348022,
				0.045938752591609955,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1016450227,
			"isDeleted": false,
			"id": "ou5CoiQAKwZXPoXbA7s5A",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2.391826304945937,
			"y": 239.20237965184037,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.616289835768725,
			"height": 6.912356720946121,
			"seed": 303265865,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.43202229505914147,
					0.8640445901182545
				],
				[
					-1.296066885177396,
					2.1601114752956505
				],
				[
					-1.7280891802365375,
					4.320222950591329
				],
				[
					0.8640445901182545,
					5.616289835768725
				],
				[
					3.4561783604730465,
					4.320222950591329
				],
				[
					3.888200655532188,
					0.8640445901182545
				],
				[
					1.7280891802365375,
					-1.296066885177396
				],
				[
					-0.8640445901182829,
					1.296066885177396
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09312597662210464,
				0.1337839961051941,
				0.14882785081863403,
				0.15614053606987,
				0.1632160097360611,
				0.1121731549501419,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1510001661,
			"isDeleted": false,
			"id": "x2c9hnbgczxFbJG0YUyHv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 8.440138435773804,
			"y": 238.3383350617221,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.208423606123517,
			"height": 13.39269114683313,
			"seed": 980775625,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.43202229505914147
				],
				[
					0,
					1.2960668851774244
				],
				[
					0.43202229505911305,
					4.752245245650471
				],
				[
					0.8640445901182545,
					11.66460196659662
				],
				[
					0.8640445901182545,
					13.39269114683313
				],
				[
					0.43202229505911305,
					9.936512786360083
				],
				[
					1.296066885177396,
					3.0241560654139334
				],
				[
					5.616289835768725,
					0
				],
				[
					8.208423606123517,
					1.2960668851774244
				],
				[
					7.344379016005263,
					4.752245245650471
				],
				[
					4.320222950591329,
					7.776401311064404
				],
				[
					4.320222950591329,
					7.776401311064404
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0926479771733284,
				0.10524484515190125,
				0.13579416275024414,
				0.12545791268348694,
				0.09623022377490997,
				0.0701211541891098,
				0.14464539289474487,
				0.20166592299938202,
				0.20503494143486023,
				0.08020123094320297,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 1547681363,
			"isDeleted": false,
			"id": "WCZg7tL_GS8EgryVWkBt6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1.095759419768541,
			"y": 252.16304850361436,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7280891802365375,
			"height": 13.824713441892271,
			"seed": 63811337,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.43202229505914147
				],
				[
					0,
					0
				],
				[
					0.43202229505911305,
					5.184267540709612
				],
				[
					0.8640445901182545,
					12.096624261655762
				],
				[
					-0.43202229505914147,
					13.39269114683313
				],
				[
					-0.8640445901182829,
					12.960668851773988
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1222979724407196,
				0.15900400280952454,
				0.17732541263103485,
				0.12946802377700806,
				0.028766723349690437,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1465926749,
			"isDeleted": false,
			"id": "S04kJ0z1X4HfLB-f-V_vI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -4.088508120941071,
			"y": 258.21136063444226,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.800557376478338,
			"height": 0.43202229505914147,
			"seed": 5723657,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8640445901182829,
					0
				],
				[
					2.160111475295679,
					0
				],
				[
					4.752245245650471,
					0
				],
				[
					10.368535081419196,
					-0.43202229505914147
				],
				[
					10.800557376478338,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13282501697540283,
				0.1953199803829193,
				0.23079998791217804,
				0.09620800614356995,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 16415731,
			"isDeleted": false,
			"id": "drOt7oxpUY5TZ37kmig-6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 12.328339091305992,
			"y": 256.4832714542057,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.048312130827867,
			"height": 9.072468196241829,
			"seed": 2059348521,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.43202229505914147,
					0
				],
				[
					-1.296066885177396,
					0
				],
				[
					-2.592133770354792,
					1.2960668851774244
				],
				[
					-2.592133770354792,
					4.7522452456504425
				],
				[
					0.8640445901182829,
					7.344379016005291
				],
				[
					3.456178360473075,
					5.616289835768725
				],
				[
					3.0241560654139334,
					1.7280891802365659
				],
				[
					0,
					-1.7280891802365375
				],
				[
					-1.7280891802365375,
					0
				],
				[
					-1.7280891802365375,
					3.456178360473075
				],
				[
					-1.296066885177396,
					3.456178360473075
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10444198548793793,
				0.11797378212213516,
				0.1269632875919342,
				0.14670483767986298,
				0.1642736792564392,
				0.17486345767974854,
				0.12850341200828552,
				0.07061053812503815,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 2129768637,
			"isDeleted": false,
			"id": "hnLNnEMjs3t34MTRwJUF5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 25.28900794307998,
			"y": 255.61922686408744,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.480334425887008,
			"height": 9.072468196241772,
			"seed": 1227020169,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8640445901182829,
					0
				],
				[
					3.0241560654139334,
					0
				],
				[
					4.320222950591358,
					-0.8640445901182829
				],
				[
					4.752245245650471,
					-2.592133770354792
				],
				[
					2.160111475295679,
					-3.456178360473075
				],
				[
					-0.43202229505911305,
					-0.8640445901182829
				],
				[
					-0.8640445901182545,
					3.4561783604730465
				],
				[
					1.2960668851774244,
					5.616289835768697
				],
				[
					5.616289835768754,
					4.320222950591329
				],
				[
					5.616289835768754,
					3.888200655532188
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.18417000770568848,
				0.23642200231552124,
				0.24085400998592377,
				0.17155441641807556,
				0.12217767536640167,
				0.18390780687332153,
				0.20268283784389496,
				0.02219216898083687,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1724679571,
			"isDeleted": false,
			"id": "L03UohmRXWyEtv1ahUljt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 33.497431549203526,
			"y": 254.32315997891004,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.616289835768725,
			"height": 7.776401311064376,
			"seed": 186118665,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.43202229505911305
				],
				[
					0,
					0.8640445901182545
				],
				[
					0,
					2.1601114752956505
				],
				[
					0.43202229505914147,
					5.616289835768725
				],
				[
					0.43202229505914147,
					6.912356720946093
				],
				[
					1.296066885177396,
					5.184267540709584
				],
				[
					3.0241560654139334,
					1.296066885177396
				],
				[
					5.184267540709584,
					-0.8640445901182829
				],
				[
					5.616289835768725,
					-0.8640445901182829
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07384054362773895,
				0.09784246981143951,
				0.12012646347284317,
				0.14172668755054474,
				0.13450418412685394,
				0.12697015702724457,
				0.04536929354071617,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 508989725,
			"isDeleted": false,
			"id": "iMcvHmOLxF1V-sZPBj--3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 40.84181056520879,
			"y": 253.02709309373265,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.0483121308278385,
			"height": 6.0483121308278385,
			"seed": 366111145,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.43202229505914147,
					0.43202229505911305
				],
				[
					-0.8640445901182545,
					0.8640445901182545
				],
				[
					-0.8640445901182545,
					2.1601114752956505
				],
				[
					-0.8640445901182545,
					4.752245245650471
				],
				[
					-0.43202229505914147,
					6.0483121308278385
				],
				[
					1.296066885177396,
					5.184267540709612
				],
				[
					2.592133770354792,
					2.592133770354792
				],
				[
					4.752245245650471,
					0.8640445901182545
				],
				[
					5.184267540709584,
					0.8640445901182545
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.055865541100502014,
				0.08535345643758774,
				0.10080154240131378,
				0.12691046297550201,
				0.14758923649787903,
				0.1423272341489792,
				0.03217300400137901,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 82598707,
			"isDeleted": false,
			"id": "B4AQQjpjGm06c9ulR8bdq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 46.890122696036656,
			"y": 255.61922686408744,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.480334425887008,
			"height": 6.912356720946121,
			"seed": 398124361,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.43202229505914147,
					0.8640445901182545
				],
				[
					-0.8640445901182829,
					3.024156065413962
				],
				[
					0.43202229505914147,
					3.888200655532188
				],
				[
					1.7280891802365375,
					4.320222950591329
				],
				[
					4.752245245650471,
					3.024156065413962
				],
				[
					5.616289835768725,
					-0.43202229505914147
				],
				[
					3.888200655532188,
					-2.592133770354792
				],
				[
					0.8640445901182545,
					-2.592133770354792
				],
				[
					-0.43202229505914147,
					0
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10784997791051865,
				0.13984601199626923,
				0.16260400414466858,
				0.2073354870080948,
				0.22024618089199066,
				0.188736230134964,
				0.11310458183288574,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1392534909,
			"isDeleted": false,
			"id": "2emS4NrCA7n5TLkV0lAWK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 52.93843482686452,
			"y": 252.5950707986735,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.344379016005263,
			"height": 8.208423606123489,
			"seed": 657751721,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.43202229505914147,
					0.8640445901182545
				],
				[
					-0.43202229505914147,
					1.7280891802365375
				],
				[
					-0.43202229505914147,
					3.4561783604730465
				],
				[
					0.43202229505914147,
					7.344379016005263
				],
				[
					1.296066885177396,
					8.208423606123489
				],
				[
					3.456178360473075,
					4.320222950591329
				],
				[
					6.48033442588698,
					0
				],
				[
					6.912356720946121,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04827798530459404,
				0.08965282887220383,
				0.11374789476394653,
				0.13667480647563934,
				0.14199016988277435,
				0.17722134292125702,
				0.07353872805833817,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 666926291,
			"isDeleted": false,
			"id": "IMckk7AAPhwVkq32Wx6FN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 41.27383286026793,
			"y": 208.96081899770104,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.43202229505911305,
			"height": 15.120780327069667,
			"seed": 1521741673,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.43202229505914147
				],
				[
					0,
					1.296066885177396
				],
				[
					0,
					4.320222950591329
				],
				[
					0,
					11.23257967153748
				],
				[
					0.43202229505911305,
					15.120780327069667
				],
				[
					0.43202229505911305,
					14.688758032010526
				],
				[
					0,
					14.256735736951413
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09941872954368591,
				0.12245077639818192,
				0.18604391813278198,
				0.23335061967372894,
				0.20366068184375763,
				0.009157989174127579,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 271625693,
			"isDeleted": false,
			"id": "A8YO0RMNk95y357Kpwohq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 35.65754302449918,
			"y": 206.36868522734625,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.208423606123546,
			"height": 11.23257967153745,
			"seed": 1043235145,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.43202229505914147
				],
				[
					2.160111475295679,
					-3.0241560654139334
				],
				[
					4.752245245650471,
					-6.912356720946121
				],
				[
					6.048312130827867,
					-6.048312130827867
				],
				[
					6.91235672094615,
					-0.43202229505914147
				],
				[
					7.776401311064404,
					3.888200655532188
				],
				[
					8.208423606123546,
					4.320222950591329
				],
				[
					8.208423606123546,
					3.888200655532188
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07407897710800171,
				0.2333959937095642,
				0.24769815802574158,
				0.27318331599235535,
				0.3205908238887787,
				0.33560851216316223,
				0.07723721116781235,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1256155763,
			"isDeleted": false,
			"id": "QnPpZBYosZ88Y-rSmm2OD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 44.297988925681864,
			"y": 230.56193375065772,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.7522452456504425,
			"height": 1.728089180236509,
			"seed": 1615407625,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.43202229505911305
				],
				[
					0.43202229505911305,
					0.8640445901182545
				],
				[
					3.0241560654139334,
					1.296066885177396
				],
				[
					4.7522452456504425,
					1.728089180236509
				],
				[
					4.7522452456504425,
					1.728089180236509
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07039199769496918,
				0.17397649586200714,
				0.19751302897930145,
				0.03564636409282684,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1694034493,
			"isDeleted": false,
			"id": "kNP5eexzPwTXvW6PDcB4O",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 43.43394433556358,
			"y": 235.31417899630816,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.616289835768725,
			"height": 1.7280891802365375,
			"seed": 1757904425,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.43202229505914147
				],
				[
					0.43202229505914147,
					1.2960668851774244
				],
				[
					1.296066885177396,
					1.7280891802365375
				],
				[
					4.752245245650471,
					1.7280891802365375
				],
				[
					5.616289835768725,
					1.7280891802365375
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.17563602328300476,
				0.21060198545455933,
				0.14069899916648865,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 856663059,
			"isDeleted": false,
			"id": "IRrPoXITVdC0-PYBQ1oRF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 64.60303679346111,
			"y": 249.13889243820043,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8640445901182545,
			"height": 12.096624261655705,
			"seed": 1720956489,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.43202229505914147,
					-0.43202229505914147
				],
				[
					0.43202229505914147,
					0.43202229505914147
				],
				[
					0.8640445901182545,
					5.616289835768725
				],
				[
					0.8640445901182545,
					11.23257967153748
				],
				[
					0.8640445901182545,
					11.664601966596564
				],
				[
					0.8640445901182545,
					11.23257967153748
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12475650012493134,
				0.22360599040985107,
				0.24286599457263947,
				0.1738927960395813,
				0.020101197063922882,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 37395101,
			"isDeleted": false,
			"id": "K3kFIWCbEnUCjThgtr3TW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 60.71483613792893,
			"y": 246.1147363727865,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.072468196241772,
			"height": 8.640445901182659,
			"seed": 53615945,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.1601114752956505,
					-1.296066885177396
				],
				[
					5.616289835768725,
					-4.752245245650471
				],
				[
					6.912356720946121,
					-5.184267540709584
				],
				[
					7.776401311064376,
					-1.7280891802365375
				],
				[
					8.640445901182659,
					2.592133770354792
				],
				[
					9.072468196241772,
					3.456178360473075
				],
				[
					9.072468196241772,
					3.0241560654139334
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.24824798107147217,
				0.2567402720451355,
				0.2161256968975067,
				0.27138566970825195,
				0.3135077953338623,
				0.14953701198101044,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1212656051,
			"isDeleted": false,
			"id": "OMIis_9HgdUXTfkUzLwmI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 47.24724616119653,
			"y": 164.65413356916076,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.32171170677509,
			"height": 20.973851340243954,
			"seed": 242488105,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5826069816734503,
					-0.5826069816734503
				],
				[
					-2.9130349083671945,
					0
				],
				[
					-4.660855853387545,
					1.7478209450203224
				],
				[
					-7.57389076175474,
					7.573890761754768
				],
				[
					-9.32171170677509,
					14.565174541836086
				],
				[
					-9.32171170677509,
					20.391244358570503
				],
				[
					-9.32171170677509,
					20.391244358570503
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12732800841331482,
				0.1589439958333969,
				0.2172819823026657,
				0.25297972559928894,
				0.11851473897695541,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 10960637,
			"isDeleted": false,
			"id": "xI-FCiZEpQVdrRpV6xc0g",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 27.438608784299504,
			"y": 187.9584128360985,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.982567560162579,
			"height": 11.069532651795413,
			"seed": 2021420297,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5826069816734503
				],
				[
					0,
					-1.1652139633469005
				],
				[
					0.5826069816733934,
					3.4956418900406447
				],
				[
					2.330427926693744,
					8.15649774342819
				],
				[
					5.826069816734389,
					7.57389076175474
				],
				[
					10.486925670121934,
					0.5826069816734218
				],
				[
					12.817353596815735,
					-2.913034908367223
				],
				[
					13.399960578489186,
					-2.913034908367223
				],
				[
					13.982567560162579,
					-2.3304279266937726
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06790795922279358,
				0.15135458111763,
				0.17057879269123077,
				0.18352587521076202,
				0.23445852100849152,
				0.23448599874973297,
				0.10386587679386139,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 799931219,
			"isDeleted": false,
			"id": "7he90rvSPgVyPGvftW_jc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 16.519008016265786,
			"y": 270.0019078599159,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8123794163810487,
			"height": 8.529983872001026,
			"seed": 1415169193,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.40618970819051015,
					0
				],
				[
					-0.40618970819051015,
					0.4061897081904817
				],
				[
					0,
					3.249517665524195
				],
				[
					0.40618970819053857,
					7.31141474742941
				],
				[
					0,
					8.529983872001026
				],
				[
					0,
					8.529983872001026
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0899219959974289,
				0.14091843366622925,
				0.21953198313713074,
				0.22325439751148224,
				0.08130255341529846,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1723881309,
			"isDeleted": false,
			"id": "E6miIRgzrNWATvgs-8F35",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 12.050921226170004,
			"y": 279.34427114829793,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.936173580191536,
			"height": 7.717604455620005,
			"seed": 960220073,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.40618970819051015,
					0
				],
				[
					-0.40618970819051015,
					1.6247588327620974
				],
				[
					1.6247588327620974,
					6.092845622857908
				],
				[
					4.061897081905272,
					7.717604455620005
				],
				[
					6.499035331048418,
					4.874276498286292
				],
				[
					8.529983872001026,
					1.2185691245716157
				],
				[
					8.529983872001026,
					0.8123794163810771
				],
				[
					8.529983872001026,
					0.8123794163810771
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11490099877119064,
				0.16630463302135468,
				0.18949420750141144,
				0.20947860181331635,
				0.20029571652412415,
				0.08397021144628525,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 630790387,
			"isDeleted": false,
			"id": "hICS311QQgay7EwIXBWxj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -28.974239301073027,
			"y": 302.9032742233484,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.591880953906298,
			"height": 8.529983872001026,
			"seed": 1886321769,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.4061897081904817
				],
				[
					0.40618970819053857,
					0
				],
				[
					1.6247588327620974,
					3.6557073737147334
				],
				[
					2.437138249143146,
					6.4990353310484466
				],
				[
					2.8433279573336847,
					2.843327957333713
				],
				[
					4.874276498286321,
					-0.8123794163810203
				],
				[
					7.311414747429467,
					-0.4061897081904817
				],
				[
					8.529983872001026,
					3.6557073737147334
				],
				[
					9.342363288382074,
					2.4371382491431746
				],
				[
					9.748552996572613,
					0.8123794163810771
				],
				[
					12.18569124571576,
					-0.8123794163810203
				],
				[
					12.591880953906298,
					6.4990353310484466
				],
				[
					12.18569124571576,
					7.717604455620005
				],
				[
					12.18569124571576,
					7.717604455620005
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11608059704303741,
				0.14282284677028656,
				0.1435713768005371,
				0.10657128691673279,
				0.12916652858257294,
				0.1705654263496399,
				0.18090014159679413,
				0.07447879016399384,
				0.07683346420526505,
				0.1591385453939438,
				0.1204092726111412,
				0.05181014910340309,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1859609533,
			"isDeleted": false,
			"id": "ocBa1FLLMg6ZkUlRIltVH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -13.539030389833073,
			"y": 305.34041247249155,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.280466206476831,
			"height": 8.123794163810487,
			"seed": 892635753,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8123794163810771
				],
				[
					0.8123794163810487,
					2.8433279573336563
				],
				[
					3.249517665524195,
					3.6557073737147334
				],
				[
					4.468086790095782,
					2.4371382491431746
				],
				[
					5.280466206476831,
					-1.2185691245715589
				],
				[
					4.061897081905244,
					-4.468086790095754
				],
				[
					0.8123794163810487,
					-2.8433279573336563
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.05654235929250717,
				0.12304358184337616,
				0.1728438436985016,
				0.18559372425079346,
				0.16720205545425415,
				0.005385376047343016,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 395281043,
			"isDeleted": false,
			"id": "JAb-dcyLd6Fo_r2ESQ-dB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -9.88332301611834,
			"y": 306.1527918888726,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.686655914667341,
			"height": 0.8123794163810203,
			"seed": 1061879305,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8123794163810487,
					0
				],
				[
					2.030948540952636,
					0.4061897081904817
				],
				[
					5.280466206476831,
					0.8123794163810203
				],
				[
					5.686655914667341,
					0.8123794163810203
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07647198438644409,
				0.07287853956222534,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 219014173,
			"isDeleted": false,
			"id": "chJ7Hvxl6i03dQkMvL_qB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -0.9471494359267751,
			"y": 302.9032742233484,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.655707373714705,
			"height": 5.686655914667369,
			"seed": 829498185,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.40618970819051015,
					0.40618970819053857
				],
				[
					1.6247588327620974,
					2.030948540952636
				],
				[
					3.655707373714705,
					5.280466206476831
				],
				[
					3.655707373714705,
					5.686655914667369
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07065197825431824,
				0.017618529498577118,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 2118629427,
			"isDeleted": false,
			"id": "z52gbYekrwcvBFbPZ-j3W",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3.927127062359517,
			"y": 301.6847050987768,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.311414747429467,
			"height": 8.529983872001026,
			"seed": 1451907209,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.2185691245715873,
					0
				],
				[
					-2.437138249143146,
					1.6247588327620974
				],
				[
					-6.09284562285788,
					6.905225039238928
				],
				[
					-7.311414747429467,
					8.529983872001026
				],
				[
					-7.311414747429467,
					8.529983872001026
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10218799114227295,
				0.20349200069904327,
				0.24424301087856293,
				0.11289428919553757,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 894785661,
			"isDeleted": false,
			"id": "8oOt_I_3tBpkFKwJSoLMM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 13.269490350741592,
			"y": 301.2785153905863,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.09284562285788,
			"height": 11.77950153752522,
			"seed": 1801845929,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.4061897081904817
				],
				[
					0,
					-0.8123794163810203
				],
				[
					0.8123794163810487,
					1.2185691245716157
				],
				[
					1.2185691245715873,
					6.092845622857908
				],
				[
					0.8123794163810487,
					9.342363288382103
				],
				[
					0.8123794163810487,
					6.4990353310484466
				],
				[
					2.8433279573336847,
					1.2185691245716157
				],
				[
					5.686655914667341,
					-2.4371382491431177
				],
				[
					6.09284562285788,
					-2.4371382491431177
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07727999985218048,
				0.09692998975515366,
				0.15217366814613342,
				0.14524325728416443,
				0.16265839338302612,
				0.13958758115768433,
				0.14749212563037872,
				0.04307513311505318,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 2007513555,
			"isDeleted": false,
			"id": "4ClfCHs-SvoS6iyDinS9v",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 20.17471538998052,
			"y": 304.934222764301,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.468086790095782,
			"height": 6.905225039238928,
			"seed": 1829787721,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.40618970819053857
				],
				[
					0,
					1.2185691245716157
				],
				[
					0.40618970819051015,
					2.4371382491431746
				],
				[
					2.437138249143146,
					2.4371382491431746
				],
				[
					4.468086790095782,
					0.8123794163810771
				],
				[
					4.468086790095782,
					-2.4371382491431177
				],
				[
					2.8433279573336847,
					-4.468086790095754
				],
				[
					0.8123794163810487,
					-4.061897081905215
				],
				[
					0.40618970819051015,
					-3.6557073737147334
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0741080641746521,
				0.16253399848937988,
				0.21414126455783844,
				0.2665703296661377,
				0.24968847632408142,
				0.14597029983997345,
				0.009534912183880806,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1634681053,
			"isDeleted": false,
			"id": "bbDJ2VGES8Vw-RVVagbyn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 21.799474222742617,
			"y": 304.934222764301,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.874276498286292,
			"height": 0.40618970819053857,
			"seed": 270481385,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.2185691245715873,
					0
				],
				[
					2.437138249143146,
					0
				],
				[
					4.468086790095782,
					0.40618970819053857
				],
				[
					4.874276498286292,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09894436597824097,
				0.16813510656356812,
				0.22397997975349426,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 549947251,
			"isDeleted": false,
			"id": "2KkQWkkILumNWDzhTjWZX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 27.892319845600497,
			"y": 299.2475668496337,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.905225039238928,
			"height": 8.123794163810487,
			"seed": 856192297,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.40618970819053857
				],
				[
					0.40618970819051015,
					-0.40618970819053857
				],
				[
					1.6247588327620974,
					1.2185691245715589
				],
				[
					2.437138249143146,
					3.6557073737146766
				],
				[
					2.8433279573336847,
					1.6247588327620974
				],
				[
					4.468086790095782,
					-0.40618970819053857
				],
				[
					6.09284562285788,
					-0.40618970819053857
				],
				[
					6.905225039238928,
					3.249517665524195
				],
				[
					6.49903533104839,
					7.31141474742941
				],
				[
					6.49903533104839,
					7.717604455619949
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10160897672176361,
				0.18324600160121918,
				0.20278997719287872,
				0.13189545273780823,
				0.039766814559698105,
				0.11079748719930649,
				0.1984338015317917,
				0.19547387957572937,
				0.05438946560025215,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1458380093,
			"isDeleted": false,
			"id": "4sUN0SKnssg5PIbTrMVBX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 37.23468313398257,
			"y": 300.46613597420526,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.09284562285788,
			"height": 6.092845622857851,
			"seed": 202514345,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.40618970819053857,
					0.8123794163810203
				],
				[
					-0.8123794163810487,
					2.030948540952636
				],
				[
					-0.8123794163810487,
					3.6557073737147334
				],
				[
					1.2185691245715873,
					6.092845622857851
				],
				[
					4.061897081905244,
					6.092845622857851
				],
				[
					5.280466206476831,
					3.6557073737147334
				],
				[
					3.6557073737147334,
					0.8123794163810203
				],
				[
					-0.40618970819053857,
					0.8123794163810203
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.10320309549570084,
				0.14700759947299957,
				0.15050466358661652,
				0.17700012028217316,
				0.1572445034980774,
				0.027096832171082497,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 804004115,
			"isDeleted": false,
			"id": "ERPHve2eMYdhYXFfyjl-O",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 39.26563167493521,
			"y": 300.0599462660147,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.123794163810516,
			"height": 18.68472657676415,
			"seed": 1891633705,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.40618970819053857
				],
				[
					0,
					0.8123794163810771
				],
				[
					1.2185691245715589,
					3.6557073737147334
				],
				[
					2.437138249143146,
					9.748552996572585
				],
				[
					2.0309485409526076,
					15.841398619430493
				],
				[
					-0.8123794163810487,
					18.68472657676415
				],
				[
					-5.686655914667369,
					12.18569124571576
				],
				[
					-5.686655914667369,
					11.373311829334739
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11175598204135895,
				0.22109685838222504,
				0.2149432748556137,
				0.20943869650363922,
				0.19302362203598022,
				0.01556396484375,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 758148509,
			"isDeleted": false,
			"id": "Dw_CM1ufeO0Tsib87uTB_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 46.577046422364646,
			"y": 302.9032742233484,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.09284562285788,
			"height": 7.311414747429467,
			"seed": 1852775145,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.40618970819053857,
					0
				],
				[
					2.030948540952636,
					-0.8123794163810203
				],
				[
					1.6247588327620974,
					-1.6247588327620974
				],
				[
					-1.2185691245715589,
					-1.6247588327620974
				],
				[
					-2.8433279573336847,
					2.030948540952636
				],
				[
					-1.2185691245715589,
					5.686655914667369
				],
				[
					3.249517665524195,
					3.6557073737147334
				],
				[
					3.249517665524195,
					2.843327957333713
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.156126007437706,
				0.24158401787281036,
				0.19951559603214264,
				0.20571285486221313,
				0.3599476218223572,
				0.1540675312280655,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1317832371,
			"isDeleted": false,
			"id": "Xyvl-tLdcI7cr1KDy2518",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 55.51322000255621,
			"y": 300.8723256823958,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.49903533104839,
			"height": 0.8123794163810203,
			"seed": 103037865,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8123794163810487,
					0.4061897081904817
				],
				[
					2.8433279573336563,
					0.4061897081904817
				],
				[
					6.49903533104839,
					0.4061897081904817
				],
				[
					6.49903533104839,
					0.8123794163810203
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15113800764083862,
				0.20487500727176666,
				0.22998949885368347,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 325759485,
			"isDeleted": false,
			"id": "hBb5sqCpccc3y4z6Hq4CW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 55.10703029436567,
			"y": 306.1527918888726,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.09284562285788,
			"height": 1.2185691245715589,
			"seed": 1609017577,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.40618970819053857,
					0.8123794163810203
				],
				[
					2.030948540952636,
					1.2185691245715589
				],
				[
					6.09284562285788,
					0.8123794163810203
				],
				[
					6.09284562285788,
					0.8123794163810203
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1542360782623291,
				0.176421657204628,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 860829779,
			"isDeleted": false,
			"id": "LJCvCdGETZwdTyW633LAH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 66.88653183189089,
			"y": 299.2475668496337,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.59188095390627,
			"height": 9.748552996572585,
			"seed": 940058153,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.40618970819053857
				],
				[
					0.40618970819053857,
					-0.8123794163810771
				],
				[
					1.6247588327621258,
					1.6247588327620974
				],
				[
					2.4371382491431746,
					5.280466206476831
				],
				[
					2.8433279573336847,
					6.092845622857851
				],
				[
					3.2495176655242233,
					2.8433279573336563
				],
				[
					4.874276498286321,
					0.4061897081904817
				],
				[
					6.905225039238957,
					2.4371382491431177
				],
				[
					7.717604455619977,
					6.49903533104839
				],
				[
					7.717604455619977,
					6.092845622857851
				],
				[
					9.748552996572613,
					1.2185691245715589
				],
				[
					11.779501537525249,
					-1.6247588327620974
				],
				[
					12.59188095390627,
					0.4061897081904817
				],
				[
					11.779501537525249,
					5.280466206476831
				],
				[
					10.967122121144172,
					8.123794163810487
				],
				[
					11.37331182933471,
					7.717604455619949
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08879999071359634,
				0.1646520048379898,
				0.22329699993133545,
				0.2207963913679123,
				0.1496315598487854,
				0.1076076328754425,
				0.14431451261043549,
				0.20097580552101135,
				0.2108861654996872,
				0.18770873546600342,
				0.1369919776916504,
				0.20545755326747894,
				0.26762592792510986,
				0.2579043209552765,
				0.0323830246925354,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1453156957,
			"isDeleted": false,
			"id": "6gbvsDr3AJd_IL_LN3spo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 82.72793045132136,
			"y": 300.0599462660147,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.468086790095811,
			"height": 7.311414747429467,
			"seed": 1629486569,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.40618970819053857
				],
				[
					-1.2185691245715589,
					2.4371382491431746
				],
				[
					-0.8123794163810203,
					6.092845622857908
				],
				[
					2.030948540952636,
					6.905225039238928
				],
				[
					3.2495176655242517,
					5.686655914667369
				],
				[
					2.843327957333713,
					2.4371382491431746
				],
				[
					-0.8123794163810203,
					-0.40618970819053857
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.20401516556739807,
				0.20834822952747345,
				0.21252942085266113,
				0.2562441825866699,
				0.29533568024635315,
				0.0781862810254097,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 2081076723,
			"isDeleted": false,
			"id": "00JRbqEKOGGfdhhN0YFmv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 84.75887899227399,
			"y": 301.2785153905863,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.061897081905272,
			"height": 2.843327957333713,
			"seed": 1689624969,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.6247588327620974,
					0.8123794163810771
				],
				[
					4.061897081905272,
					2.4371382491431746
				],
				[
					4.061897081905272,
					2.843327957333713
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12381799519062042,
				0.20506198704242706,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 664409789,
			"isDeleted": false,
			"id": "YqByn2r5JVWgFHeJ7_5ZI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 89.63315549056028,
			"y": 299.2475668496337,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.686655914667369,
			"height": 6.092845622857851,
			"seed": 1660062697,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.2185691245716157,
					1.2185691245715589
				],
				[
					4.061897081905272,
					4.468086790095754
				],
				[
					5.280466206476831,
					6.092845622857851
				],
				[
					5.686655914667369,
					6.092845622857851
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.18774953484535217,
				0.03881988674402237,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1204125587,
			"isDeleted": false,
			"id": "rDImjeNRSOkCx_fOWwnak",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 97.35075994618029,
			"y": 297.21661830868106,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.748552996572585,
			"height": 8.936173580191564,
			"seed": 1816971561,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8123794163810771,
					0
				],
				[
					-1.6247588327620974,
					0.40618970819053857
				],
				[
					-6.905225039238928,
					4.468086790095754
				],
				[
					-9.748552996572585,
					8.936173580191564
				],
				[
					-9.748552996572585,
					8.936173580191564
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1405789852142334,
				0.21058563888072968,
				0.3158339858055115,
				0.19784015417099,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 553793309,
			"isDeleted": false,
			"id": "g4g8FViUwbWXuIbvmYSj7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 102.88648261919306,
			"y": 301.1383189389608,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.317692803318664,
			"height": 9.871395005185434,
			"seed": 1040933193,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7897116004148188,
					0
				],
				[
					-1.1845674006222282,
					0
				],
				[
					0.3948558002074378,
					-0.3948558002074378
				],
				[
					3.158846401659332,
					-1.5794232008296945
				],
				[
					4.343413802281589,
					-3.158846401659332
				],
				[
					2.3691348012445133,
					-3.55370220186677
				],
				[
					0,
					-0.7897116004148756
				],
				[
					-0.7897116004148188,
					3.553702201866713
				],
				[
					0.3948558002074378,
					6.317692803318664
				],
				[
					4.738269602488998,
					4.73826960248897
				],
				[
					5.133125402696436,
					4.343413802281532
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1244179978966713,
				0.20759600400924683,
				0.24271725118160248,
				0.17389117181301117,
				0.09238684177398682,
				0.11002463102340698,
				0.1527102291584015,
				0.1724800169467926,
				0.01205145288258791,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 280368435,
			"isDeleted": false,
			"id": "7aJlSVCqHIkbIlcWhXI9E",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 110.38874282313398,
			"y": 299.1640399379237,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.922837003111226,
			"height": 7.897116004148302,
			"seed": 805010089,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.3948558002074094,
					0
				],
				[
					-0.7897116004148188,
					0.3948558002074378
				],
				[
					-0.7897116004148188,
					0.7897116004148756
				],
				[
					0,
					4.343413802281589
				],
				[
					0.3948558002074094,
					7.502260203940921
				],
				[
					0.7897116004148472,
					7.10740440373354
				],
				[
					2.3691348012445133,
					3.158846401659332
				],
				[
					4.738269602488998,
					-0.394855800207381
				],
				[
					5.1331254026964075,
					-0.394855800207381
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06170797720551491,
				0.07794830203056335,
				0.14965398609638214,
				0.18429617583751678,
				0.1872325986623764,
				0.15976376831531525,
				0.1693342924118042,
				0.02530389465391636,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 222776189,
			"isDeleted": false,
			"id": "XGGNDirokUn9zcWXLPs-W",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 116.31157982624524,
			"y": 298.7691841377163,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.1331254026964075,
			"height": 7.502260203940921,
			"seed": 231773769,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.394855800207381
				],
				[
					0,
					1.5794232008296376
				],
				[
					0.3948558002074094,
					3.553702201866713
				],
				[
					1.1845674006222566,
					7.502260203940921
				],
				[
					1.579423200829666,
					7.502260203940921
				],
				[
					2.369134801244485,
					3.158846401659332
				],
				[
					5.1331254026964075,
					0
				],
				[
					5.1331254026964075,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04807998612523079,
				0.0947345569729805,
				0.12923789024353027,
				0.12959878146648407,
				0.13318660855293274,
				0.15164624154567719,
				0.010113891214132309,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1178793683,
			"isDeleted": false,
			"id": "3URC2QSW8Ak_hmHfZE-lg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 124.20869583039357,
			"y": 301.1383189389608,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.1331254026964075,
			"height": 7.897116004148359,
			"seed": 1715797769,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.1845674006222566,
					1.1845674006221998
				],
				[
					-1.9742790010370754,
					2.7639906014518942
				],
				[
					-0.7897116004148472,
					4.73826960248897
				],
				[
					1.579423200829666,
					5.1331254026964075
				],
				[
					3.158846401659332,
					1.9742790010370754
				],
				[
					2.7639906014519227,
					-1.5794232008296945
				],
				[
					0.3948558002074094,
					-2.763990601451951
				],
				[
					-0.7897116004148472,
					1.1845674006221998
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1267046183347702,
				0.20018599927425385,
				0.1959342062473297,
				0.2128756046295166,
				0.22657006978988647,
				0.17206265032291412,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1823134685,
			"isDeleted": false,
			"id": "a0WWkebkKg7IVGROMxUY0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 128.94696543288254,
			"y": 299.1640399379237,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.1331254026964075,
			"height": 7.107404403733483,
			"seed": 162191753,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.394855800207381,
					1.1845674006222566
				],
				[
					-0.394855800207381,
					2.3691348012445133
				],
				[
					0,
					5.133125402696464
				],
				[
					0.7897116004148756,
					5.527981202903845
				],
				[
					1.5794232008296945,
					2.763990601451951
				],
				[
					2.763990601451951,
					-0.394855800207381
				],
				[
					4.343413802281589,
					-1.5794232008296376
				],
				[
					4.7382696024890265,
					-1.5794232008296376
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09069400280714035,
				0.11250597983598709,
				0.14961539208889008,
				0.13190576434135437,
				0.14111654460430145,
				0.1730412244796753,
				0.07193191349506378,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 654484595,
			"isDeleted": false,
			"id": "aj6HSKfSJHFeEhKuxjbyh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 140.79263943910505,
			"y": 303.9023095404127,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.897116004148302,
			"height": 26.85019441410435,
			"seed": 71316041,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.3948558002074378,
					-0.3948558002074378
				],
				[
					0.7897116004148188,
					-1.1845674006222566
				],
				[
					2.3691348012445133,
					-3.55370220186677
				],
				[
					4.343413802281589,
					-8.29197180435574
				],
				[
					3.55370220186677,
					-12.24052980642989
				],
				[
					1.5794232008296945,
					-13.819953007259585
				],
				[
					0.7897116004148188,
					-12.24052980642989
				],
				[
					0.7897116004148188,
					-7.107404403733483
				],
				[
					1.9742790010370754,
					0
				],
				[
					1.9742790010370754,
					7.897116004148302
				],
				[
					0.3948558002074378,
					12.24052980642989
				],
				[
					-2.3691348012445133,
					13.030241406844766
				],
				[
					-3.553702201866713,
					7.897116004148302
				],
				[
					-3.553702201866713,
					7.502260203940921
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06990399211645126,
				0.10597921907901764,
				0.24025799334049225,
				0.2499978393316269,
				0.1918097287416458,
				0.14207959175109863,
				0.13124719262123108,
				0.12510885298252106,
				0.14565597474575043,
				0.17444118857383728,
				0.20578017830848694,
				0.20056164264678955,
				0.029505645856261253,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 993939517,
			"isDeleted": false,
			"id": "JZHmCnC-h5E5yjXINsFh9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 147.1103322424237,
			"y": 301.5331747391682,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7897116004148188,
			"height": 5.1331254026964075,
			"seed": 1424883785,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7897116004148188
				],
				[
					-0.394855800207381,
					1.5794232008296945
				],
				[
					-0.394855800207381,
					3.158846401659332
				],
				[
					0.3948558002074378,
					5.1331254026964075
				],
				[
					0.3948558002074378,
					5.1331254026964075
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12259100377559662,
				0.2075280398130417,
				0.24033401906490326,
				0.08437075465917587,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1522245139,
			"isDeleted": false,
			"id": "ZMgoPIdXXSyQO08TNsows",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 148.6897554432534,
			"y": 298.7691841377163,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.3948558002074378,
			"height": 0.394855800207381,
			"seed": 1839717481,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.3948558002074378,
					0
				],
				[
					-0.3948558002074378,
					0.394855800207381
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15988250076770782,
				0.07839138805866241,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1994604701,
			"isDeleted": false,
			"id": "xbZ92djMqFsyLoxDnf8hJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 152.63831344532755,
			"y": 299.5588957381311,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.948558002074151,
			"height": 6.317692803318664,
			"seed": 938195369,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.3948558002074378
				],
				[
					0,
					1.1845674006222566
				],
				[
					0.7897116004148188,
					2.3691348012445133
				],
				[
					3.948558002074151,
					6.317692803318664
				],
				[
					3.948558002074151,
					6.317692803318664
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11089498549699783,
				0.16793599724769592,
				0.03622106835246086,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1281647539,
			"isDeleted": false,
			"id": "MQ__tHZ1Xc0_IjqBkARER",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 157.77143884802396,
			"y": 299.95375153833857,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.107404403733483,
			"height": 10.661106605600253,
			"seed": 1601561033,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.3948558002074378
				],
				[
					-0.3948558002074378,
					-0.3948558002074378
				],
				[
					-2.3691348012445133,
					1.5794232008296376
				],
				[
					-7.107404403733483,
					10.266250805392815
				],
				[
					-7.107404403733483,
					10.266250805392815
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12984000146389008,
				0.24442797899246216,
				0.13821829855442047,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1699423485,
			"isDeleted": false,
			"id": "i0RqQXLCZYXTJbhILXs30",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 103.84113083371795,
			"y": 318.2208270775757,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.280054228473091,
			"height": 27.602678606274026,
			"seed": 1805938153,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.492904975112026
				],
				[
					0,
					-0.985809950224052
				],
				[
					-0.492904975112026,
					-0.985809950224052
				],
				[
					-0.985809950224052,
					0
				],
				[
					-3.450334825784239,
					4.929049751120374
				],
				[
					-6.407764676456452,
					12.81552935291296
				],
				[
					-6.900669651568478,
					18.730389054257387
				],
				[
					-3.943239800896265,
					22.673628855153652
				],
				[
					0.492904975112026,
					25.631058705825865
				],
				[
					4.436144776008348,
					26.616868656049974
				],
				[
					7.886479601792587,
					26.616868656049974
				],
				[
					8.379384576904613,
					26.616868656049974
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14654400944709778,
				0.1775979846715927,
				0.2158840000629425,
				0.25604668259620667,
				0.26436513662338257,
				0.28477728366851807,
				0.3086576461791992,
				0.3366164565086365,
				0.3263780176639557,
				0.0759899914264679,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1143174483,
			"isDeleted": false,
			"id": "Vtu3r7O8PfC-oleM39525",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 116.16375521151889,
			"y": 340.4015509576173,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.351004477352774,
			"height": 10.8439094524648,
			"seed": 954249769,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9858099502241089,
					-0.492904975112026
				],
				[
					-1.478714925336135,
					-0.492904975112026
				],
				[
					-1.478714925336135,
					-0.985809950224052
				],
				[
					2.957429850672213,
					0
				],
				[
					7.393574626680504,
					2.464524875560187
				],
				[
					8.872289552016639,
					4.929049751120374
				],
				[
					7.393574626680504,
					6.407764676456452
				],
				[
					3.450334825784239,
					7.886479601792587
				],
				[
					0,
					9.365194527128665
				],
				[
					-0.49290497511208287,
					9.858099502240748
				],
				[
					0.492904975112026,
					9.858099502240748
				],
				[
					1.478714925336078,
					9.858099502240748
				],
				[
					1.971619900448104,
					9.365194527128665
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1044948399066925,
				0.2528960108757019,
				0.34414198994636536,
				0.3482966423034668,
				0.2962972819805145,
				0.29340672492980957,
				0.37342044711112976,
				0.43436312675476074,
				0.42769524455070496,
				0.3261892795562744,
				0.08428344875574112,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 435649885,
			"isDeleted": false,
			"id": "3Qrcvu7ZTbvJ5ZZrpLL4f",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 131.76633701007066,
			"y": 339.39190033449046,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.0088766523207084,
			"height": 10.6824473819035,
			"seed": 1534710089,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6676529613689866,
					0
				],
				[
					-2.3367853647914103,
					0.33382648068447907
				],
				[
					-3.0044383261603684,
					1.001479442053494
				],
				[
					-3.3382648068448475,
					1.335305922737973
				],
				[
					-2.3367853647914103,
					3.0044383261603684
				],
				[
					1.0014794420534372,
					5.341223690951722
				],
				[
					2.670611845475861,
					7.678009055743132
				],
				[
					1.6691324034224237,
					9.680967939850063
				],
				[
					-1.6691324034224237,
					10.6824473819035
				],
				[
					-2.6706118454758894,
					9.013314978481105
				],
				[
					-2.3367853647914103,
					8.679488497796626
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10157598555088043,
				0.13144400715827942,
				0.14594866335391998,
				0.14979229867458344,
				0.13320507109165192,
				0.13026681542396545,
				0.17850174009799957,
				0.2263825684785843,
				0.02884262055158615,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1095717619,
			"isDeleted": false,
			"id": "Jp3nnovLSm3JUAWq61MJJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 140.44582550786723,
			"y": 329.3771059139559,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3353059227379163,
			"height": 18.69428291833117,
			"seed": 653519529,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.33382648068447907,
					0
				],
				[
					-0.6676529613689581,
					-0.33382648068447907
				],
				[
					-1.0014794420534372,
					0
				],
				[
					-0.6676529613689581,
					5.341223690951779
				],
				[
					0,
					14.020712188748348
				],
				[
					0.33382648068447907,
					18.36045643764669
				],
				[
					0.33382648068447907,
					18.026629956962154
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09689999371767044,
				0.1276720017194748,
				0.15167199075222015,
				0.21489401161670685,
				0.21462173759937286,
				0.018829436972737312,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1010420157,
			"isDeleted": false,
			"id": "JsB1t2G_E_3sJRuwpEgOI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 142.7826108726586,
			"y": 343.73164458338874,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.007397210267243,
			"height": 7.344182575058653,
			"seed": 1695929481,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.33382648068447907,
					2.0029588841069312
				],
				[
					-0.33382648068447907,
					3.0044383261603684
				],
				[
					0.6676529613689866,
					4.3397442488983415
				],
				[
					2.6706118454758894,
					4.673570729582821
				],
				[
					4.005917768213806,
					1.6691324034223953
				],
				[
					3.3382648068448475,
					-1.3353059227379163
				],
				[
					1.0014794420534656,
					-2.6706118454758325
				],
				[
					-1.0014794420534372,
					0.33382648068447907
				],
				[
					-0.6676529613689581,
					2.6706118454758894
				],
				[
					-0.33382648068447907,
					3.0044383261603684
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07930908352136612,
				0.09093350172042847,
				0.13780002295970917,
				0.1749219298362732,
				0.16711081564426422,
				0.18099850416183472,
				0.17536328732967377,
				0.12192700058221817,
				0.009816131554543972,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 342785171,
			"isDeleted": false,
			"id": "g5fttQ1sa9QLZPII3afBx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 149.4591404863483,
			"y": 342.06251217996635,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.011835536427611,
			"height": 6.008876652320737,
			"seed": 1494707977,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.33382648068447907
				],
				[
					0.6676529613689581,
					0.33382648068447907
				],
				[
					1.6691324034224237,
					4.005917768213806
				],
				[
					2.002958884106903,
					5.007397210267243
				],
				[
					2.670611845475861,
					3.0044383261603116
				],
				[
					3.00443832616034,
					0.33382648068447907
				],
				[
					4.005917768213806,
					0.33382648068447907
				],
				[
					4.673570729582764,
					2.3367853647913535
				],
				[
					5.675050171636229,
					2.3367853647913535
				],
				[
					6.676529613689667,
					0
				],
				[
					7.344182575058653,
					0.6676529613689581
				],
				[
					7.344182575058653,
					4.005917768213806
				],
				[
					8.011835536427611,
					5.675050171636258
				],
				[
					8.011835536427611,
					5.341223690951722
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0756479799747467,
				0.17625197768211365,
				0.21528439223766327,
				0.1268499791622162,
				0.05265029892325401,
				0.04865814372897148,
				0.12475176900625229,
				0.15484823286533356,
				0.11432943493127823,
				0.08190716803073883,
				0.15320998430252075,
				0.20660822093486786,
				0.10644851624965668,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 221481501,
			"isDeleted": false,
			"id": "4i7D46i8fOQXhdN3uaP30",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 170.15638228878632,
			"y": 331.38006479806285,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.682447381903472,
			"height": 16.691324034224237,
			"seed": 1431551241,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.33382648068447907
				],
				[
					-0.3338264806845075,
					4.005917768213806
				],
				[
					0,
					7.344182575058653
				],
				[
					0,
					10.348620901219022
				],
				[
					0.33382648068447907,
					12.685406266010375
				],
				[
					-0.3338264806845075,
					12.685406266010375
				],
				[
					-3.0044383261603684,
					11.350100343272459
				],
				[
					-5.007397210267271,
					11.683926823956938
				],
				[
					-5.675050171636229,
					14.354538669432827
				],
				[
					-4.339744248898313,
					16.023671072855223
				],
				[
					-2.002958884106903,
					15.356018111486264
				],
				[
					0.33382648068447907,
					13.686885708063812
				],
				[
					1.3353059227379163,
					14.354538669432827
				],
				[
					2.336785364791382,
					16.691324034224237
				],
				[
					4.005917768213806,
					16.35749755353976
				],
				[
					5.007397210267243,
					14.354538669432827
				],
				[
					4.339744248898285,
					12.017753304641417
				],
				[
					2.336785364791382,
					11.01627386258798
				],
				[
					2.002958884106903,
					10.6824473819035
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12410998344421387,
				0.1592240035533905,
				0.19084399938583374,
				0.17622046172618866,
				0.1363532990217209,
				0.04438794031739235,
				0.04646340757608414,
				0.08256619423627853,
				0.07230349630117416,
				0.04951233044266701,
				0.04772622510790825,
				0.09999386966228485,
				0.18425363302230835,
				0.22539229691028595,
				0.23132836818695068,
				0.21173031628131866,
				0.01971481367945671,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 959935027,
			"isDeleted": false,
			"id": "ZxTmqhfyIN6xWVKY770pa",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 175.49760597973804,
			"y": 344.7331240254422,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.005917768213806,
			"height": 1.335305922737973,
			"seed": 180290921,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.3353059227379447,
					1.335305922737973
				],
				[
					3.6720912875293266,
					1.335305922737973
				],
				[
					4.005917768213806,
					1.001479442053494
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10452398657798767,
				0.0689881294965744,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 769015421,
			"isDeleted": false,
			"id": "hrZSit50O9mfrEgf9O0dQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 185.84622688095706,
			"y": 329.3771059139559,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3353059227379447,
			"height": 18.36045643764669,
			"seed": 1329693641,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.33382648068447907,
					0.6676529613689581
				],
				[
					-1.0014794420534656,
					2.0029588841069312
				],
				[
					-1.0014794420534656,
					9.013314978481105
				],
				[
					-1.0014794420534656,
					15.356018111486264
				],
				[
					-1.0014794420534656,
					18.36045643764669
				],
				[
					-1.3353059227379447,
					18.36045643764669
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08817499130964279,
				0.12591034173965454,
				0.22832797467708588,
				0.26305916905403137,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1888531411,
			"isDeleted": false,
			"id": "gQLiLm9DkcASm7enkNbJ8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 180.17117670932083,
			"y": 341.72868569928187,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.680967939850035,
			"height": 2.6706118454758325,
			"seed": 790260425,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.33382648068447907
				],
				[
					0.33382648068447907,
					0.6676529613689581
				],
				[
					2.002958884106903,
					1.0014794420534372
				],
				[
					9.013314978481048,
					2.6706118454758325
				],
				[
					9.680967939850035,
					2.6706118454758325
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1649785190820694,
				0.2334039956331253,
				0.11213967949151993,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 618882781,
			"isDeleted": false,
			"id": "xlKBCPIWqjYj5hKgLIT9I",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 192.39789130628367,
			"y": 346.3071222172826,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.03153564273137,
			"height": 7.103344436797215,
			"seed": 1147999977,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.29597268486654116,
					0.8879180545996519
				],
				[
					0.8879180545996519,
					2.367781478932386
				],
				[
					1.7758361091993038,
					3.5516722183986644
				],
				[
					3.5516722183986076,
					4.735562957864829
				],
				[
					5.03153564273137,
					2.367781478932386
				],
				[
					5.03153564273137,
					-0.8879180545996519
				],
				[
					3.5516722183986076,
					-2.367781478932386
				],
				[
					2.6637541637989557,
					-2.0718087940658165
				],
				[
					1.183890739466193,
					-1.1838907394662215
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11309997737407684,
				0.1500440090894699,
				0.20977599918842316,
				0.20658472180366516,
				0.09893222153186798,
				0.09303362667560577,
				0.09674648940563202,
				0.021576354280114174,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 445694323,
			"isDeleted": false,
			"id": "CiL9f6kBkLpiC9oul_2XA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 194.17372741548297,
			"y": 346.8990675870157,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.735562957864829,
			"height": 1.1838907394662783,
			"seed": 1542720585,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.2959726848665696
				],
				[
					0.8879180545996519,
					1.1838907394662783
				],
				[
					4.735562957864829,
					1.1838907394662783
				],
				[
					4.735562957864829,
					0.8879180545997087
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1201929897069931,
				0.16818717122077942,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 619479869,
			"isDeleted": false,
			"id": "LbqZRj-j28SWXArlbRCl8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 204.82874407067885,
			"y": 343.64336805348364,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.32750832759794,
			"height": 5.623481012464538,
			"seed": 906658185,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.2959726848665696
				],
				[
					-0.2959726848665696,
					-0.8879180545996519
				],
				[
					0,
					-0.5919453697331392
				],
				[
					0.8879180545996519,
					2.0718087940658734
				],
				[
					1.183890739466193,
					4.439590272998316
				],
				[
					1.4798634243327626,
					3.5516722183986076
				],
				[
					2.6637541637989557,
					0.2959726848665696
				],
				[
					5.03153564273137,
					-1.1838907394662215
				],
				[
					5.03153564273137,
					-0.8879180545996519
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1380094289779663,
				0.1877860426902771,
				0.17977505922317505,
				0.16324719786643982,
				0.15316420793533325,
				0.14126741886138916,
				0.07955596596002579,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1350441747,
			"isDeleted": false,
			"id": "yVGl_I84V_aZi_DMicChM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 209.86027971341022,
			"y": 344.8272587929498,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.143617588131718,
			"height": 4.439590272998316,
			"seed": 409839913,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8879180545997087
				],
				[
					0,
					1.479863424332791
				],
				[
					0.5919453697331107,
					2.6637541637990125
				],
				[
					2.6637541637989557,
					2.367781478932443
				],
				[
					4.143617588131718,
					0.5919453697331392
				],
				[
					1.7758361091993038,
					-1.7758361091993038
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08471600711345673,
				0.12401599436998367,
				0.19978198409080505,
				0.2562659978866577,
				0.22282686829566956,
				0.012882019393146038,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 307434397,
			"isDeleted": false,
			"id": "F5Xchnv4Y8D667GngiJ5Q",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 212.52403387720918,
			"y": 345.41920416268295,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.663754163798984,
			"height": 0.8879180545996519,
			"seed": 158464489,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8879180545996803,
					0.5919453697331392
				],
				[
					2.3677814789324145,
					0.8879180545996519
				],
				[
					2.663754163798984,
					0.5919453697331392
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09957067668437958,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 1053769907,
			"isDeleted": false,
			"id": "ZnRl6-oh62CYMRWKX5bDK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 220.5152963686061,
			"y": 334.76418750748707,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.5919453697331107,
			"height": 13.022798134128323,
			"seed": 1225500745,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.2959726848665696,
					0
				],
				[
					-0.2959726848665696,
					0.2959726848665696
				],
				[
					-0.5919453697331107,
					1.7758361091993606
				],
				[
					-0.2959726848665696,
					7.695289806530354
				],
				[
					-0.2959726848665696,
					12.726825449261753
				],
				[
					-0.5919453697331107,
					13.022798134128323
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0902559831738472,
				0.08034375309944153,
				0.15114660561084747,
				0.2331327199935913,
				0.07631023973226547,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1229494269,
			"isDeleted": false,
			"id": "0x_fodi2-ETJNs1VhVrUu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 216.96362415020747,
			"y": 340.9796138896847,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.03153564273137,
			"height": 0.8879180545996519,
			"seed": 1494749001,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5919453697331107,
					-0.5919453697330823
				],
				[
					4.735562957864829,
					-0.8879180545996519
				],
				[
					5.03153564273137,
					-0.8879180545996519
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13689014315605164,
				0.16499541699886322,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1059762771,
			"isDeleted": false,
			"id": "qWyYaB0Xre7V4tDvcmpIK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 227.61864080540334,
			"y": 343.0514226837505,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.03153564273137,
			"height": 8.287235176263437,
			"seed": 1062756777,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5919453697330823,
					-1.1838907394661646
				],
				[
					0.5919453697330823,
					-2.0718087940658165
				],
				[
					-1.1838907394662215,
					-2.9597268486654684
				],
				[
					-3.551672218398636,
					-0.887918054599595
				],
				[
					-3.847644903265177,
					2.959726848665582
				],
				[
					-1.7758361091993322,
					5.327508327597968
				],
				[
					0.8879180545996519,
					4.735562957864886
				],
				[
					1.183890739466193,
					4.439590272998316
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14552047848701477,
				0.17910800874233246,
				0.16929195821285248,
				0.11790557950735092,
				0.1874273717403412,
				0.2691708207130432,
				0.02944113127887249,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 600739933,
			"isDeleted": false,
			"id": "kkSDWLdR3lj-FOtnl9a2U",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 234.42601255733402,
			"y": 340.6836412048181,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7758361091993038,
			"height": 3.255699533532038,
			"seed": 1810371177,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.29597268486654116,
					0
				],
				[
					-0.8879180545996519,
					-0.29597268486651274
				],
				[
					-1.4798634243327626,
					0.5919453697330823
				],
				[
					-1.7758361091993038,
					1.1838907394662215
				],
				[
					-1.4798634243327626,
					2.367781478932386
				],
				[
					-0.5919453697331107,
					2.9597268486655253
				],
				[
					-1.183890739466193,
					2.6637541637989557
				],
				[
					-1.4798634243327626,
					2.367781478932386
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07246200740337372,
				0.055241331458091736,
				0.15087811648845673,
				0.1681331843137741,
				0.13946005702018738,
				0.06994228810071945,
				0.02123214676976204,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 845606899,
			"isDeleted": false,
			"id": "JWEbjO500dCZGQIcO8fiL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 234.7219852422006,
			"y": 340.6836412048181,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.807371751930702,
			"height": 9.76709860059617,
			"seed": 1882575657,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.2959726848665696,
					0
				],
				[
					-0.5919453697331107,
					-0.29597268486651274
				],
				[
					-1.4798634243327626,
					-0.29597268486651274
				],
				[
					-3.551672218398636,
					1.1838907394662215
				],
				[
					-3.847644903265177,
					2.9597268486655253
				],
				[
					-0.8879180545996803,
					5.031535642731399
				],
				[
					1.183890739466193,
					6.511399067064133
				],
				[
					0.5919453697330823,
					8.287235176263437
				],
				[
					-2.3677814789324145,
					9.471125915729658
				],
				[
					-5.32750832759794,
					9.471125915729658
				],
				[
					-5.623481012464509,
					9.471125915729658
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16382598876953125,
				0.18982598185539246,
				0.24966800212860107,
				0.2378152757883072,
				0.2442208230495453,
				0.3148575723171234,
				0.2626538872718811,
				0.23334451019763947,
				0.29862019419670105,
				0.17853452265262604,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1068924093,
			"isDeleted": false,
			"id": "wtKJlbDNOXO3EgdPUlguY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 182.926765390554,
			"y": 356.0742208178788,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.9912624913968955,
			"height": 15.686552297927278,
			"seed": 2113331337,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1.1838907394662215
				],
				[
					0,
					-1.7758361091993606
				],
				[
					0.29597268486654116,
					-0.2959726848665696
				],
				[
					1.183890739466193,
					6.511399067064133
				],
				[
					0.8879180545996519,
					11.542934709795475
				],
				[
					0.8879180545996519,
					9.471125915729658
				],
				[
					2.6637541637989557,
					7.991262491396867
				],
				[
					5.623481012464481,
					8.583207861130006
				],
				[
					7.695289806530354,
					10.35904397032931
				],
				[
					7.9912624913968955,
					11.838907394662044
				],
				[
					7.103344436797244,
					12.726825449261753
				],
				[
					4.735562957864829,
					13.614743503861348
				],
				[
					1.7758361091993038,
					13.910716188727918
				],
				[
					0,
					13.318770818994835
				],
				[
					0.29597268486654116,
					13.318770818994835
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12715399265289307,
				0.1901319921016693,
				0.15837600827217102,
				0.19119302928447723,
				0.1066201776266098,
				0.08594827353954315,
				0.1765236258506775,
				0.21727868914604187,
				0.19519290328025818,
				0.25982579588890076,
				0.2939908802509308,
				0.247832790017128,
				0.03885052353143692,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 445282707,
			"isDeleted": false,
			"id": "kdXX8hHLfal9ytoVBzUNk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 195.3576181549492,
			"y": 364.36145599414226,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.511399067064161,
			"height": 14.502661558461057,
			"seed": 1196127593,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692885,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5919453697330823
				],
				[
					-0.2959726848665696,
					-0.8879180545996519
				],
				[
					-0.2959726848665696,
					-0.5919453697330823
				],
				[
					1.183890739466193,
					2.6637541637990125
				],
				[
					2.071808794065845,
					9.175153230863089
				],
				[
					0.8879180545996519,
					13.614743503861405
				],
				[
					0.29597268486654116,
					12.430852764395183
				],
				[
					-0.8879180545996803,
					6.51139906706419
				],
				[
					2.071808794065845,
					1.4798634243327342
				],
				[
					5.03153564273137,
					0.2959726848665696
				],
				[
					5.623481012464481,
					2.367781478932443
				],
				[
					4.4395902729982595,
					5.327508327597911
				],
				[
					2.3677814789324145,
					6.51139906706419
				],
				[
					2.071808794065845,
					6.21542638219762
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11360998451709747,
				0.16281597316265106,
				0.22106601297855377,
				0.19933532178401947,
				0.18107043206691742,
				0.16450005769729614,
				0.11945794522762299,
				0.11224301159381866,
				0.17316821217536926,
				0.21180684864521027,
				0.21071383357048035,
				0.10485272109508514,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 77716765,
			"isDeleted": false,
			"id": "lxEx6MX7Fr56xg0hxGMEO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 206.30860749501161,
			"y": 362.8815925698095,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.9597268486655253,
			"height": 2.0718087940658165,
			"seed": 125764457,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.2959726848665696,
					-0.2959726848665696
				],
				[
					-0.8879180545996803,
					-1.1838907394662215
				],
				[
					-1.1838907394662215,
					-1.4798634243327342
				],
				[
					-2.0718087940658734,
					-0.5919453697331392
				],
				[
					-2.9597268486655253,
					0.5919453697330823
				],
				[
					-2.663754163798984,
					0.2959726848665696
				],
				[
					-1.7758361091993322,
					0
				],
				[
					-1.4798634243327626,
					0
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12781798839569092,
				0.07824130356311798,
				0.07520077377557755,
				0.1600099503993988,
				0.10948958992958069,
				0.007383148185908794,
				0.0000036315918805485126,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 1959513907,
			"isDeleted": false,
			"id": "nDWXri06jocznktxshRrS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 206.01263481014504,
			"y": 361.6977018303433,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.3677814789324145,
			"height": 0.29597268486651274,
			"seed": 464342505,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5919453697331107,
					0
				],
				[
					0.8879180545996519,
					0
				],
				[
					1.4798634243327626,
					0
				],
				[
					1.7758361091993038,
					0
				],
				[
					2.0718087940658734,
					0
				],
				[
					2.3677814789324145,
					0.29597268486651274
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.01132647693157196,
				0.028155913576483727,
				0.004565887618809938,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1778528637,
			"isDeleted": false,
			"id": "FxeZgTbPPLd39eEHTaEEG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 208.67638897394403,
			"y": 360.2178384060105,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.103344436797244,
			"height": 9.175153230863145,
			"seed": 2038568169,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.2959726848665696,
					0
				],
				[
					-0.5919453697331107,
					0
				],
				[
					-0.8879180545996803,
					0
				],
				[
					-2.3677814789324145,
					1.1838907394662783
				],
				[
					-3.847644903265177,
					2.959726848665582
				],
				[
					-3.551672218398636,
					3.847644903265177
				],
				[
					-1.1838907394662215,
					4.439590272998316
				],
				[
					1.183890739466193,
					5.327508327597968
				],
				[
					2.3677814789324145,
					6.807371751930759
				],
				[
					2.071808794065845,
					8.287235176263493
				],
				[
					0.5919453697330823,
					9.175153230863145
				],
				[
					-2.0718087940658734,
					9.175153230863145
				],
				[
					-4.439590272998288,
					8.287235176263493
				],
				[
					-4.735562957864829,
					7.991262491396924
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05556198209524155,
				0.15044137835502625,
				0.14436441659927368,
				0.18794238567352295,
				0.29511338472366333,
				0.3018362522125244,
				0.2064787596464157,
				0.20572280883789062,
				0.21720795333385468,
				0.2568523585796356,
				0.31251227855682373,
				0.28891414403915405,
				0.11138729751110077,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 1402040531,
			"isDeleted": false,
			"id": "BEmPbCUTP_i4OHnCzFxDf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 250.1851793308349,
			"y": 340.854616628264,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.473086209703297,
			"height": 0.7702805645184867,
			"seed": 1757848297,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.1554208467777016,
					0
				],
				[
					-1.5405611290369734,
					0
				],
				[
					-0.7702805645184867,
					0.38514028225927177
				],
				[
					1.9257014112961883,
					-0.38514028225921493
				],
				[
					6.9325250806663234,
					-0.38514028225921493
				],
				[
					6.9325250806663234,
					-0.38514028225921493
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0729459822177887,
				0.1401481330394745,
				0.3163430094718933,
				0.40199199318885803,
				0.07517559826374054,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 2098788829,
			"isDeleted": false,
			"id": "n8y4RkvZ9oBKtXstn4ZnB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 250.5703196130941,
			"y": 348.9425625557081,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.70280564518481,
			"height": 1.1554208467777585,
			"seed": 1211525609,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7702805645184867
				],
				[
					3.081122258073947,
					0.7702805645184867
				],
				[
					7.317665362925595,
					0
				],
				[
					7.70280564518481,
					-0.38514028225927177
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.3703380227088928,
				0.16917996108531952,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 946986611,
			"isDeleted": false,
			"id": "rdjZAG-pNACYML_wf0c7q",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 279.8409810647964,
			"y": 338.5437749347086,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.09476959681416,
			"height": 12.324489032295673,
			"seed": 1888626473,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.38514028225921493,
					0.7702805645184299
				],
				[
					-3.081122258073947,
					3.8514028225923767
				],
				[
					-7.70280564518481,
					7.702805645184753
				],
				[
					-10.7839279032587,
					9.628507056480998
				],
				[
					-8.087945927444025,
					9.628507056480998
				],
				[
					-4.621683387110863,
					10.013647338740213
				],
				[
					-1.1554208467777016,
					10.7839279032587
				],
				[
					1.1554208467777016,
					11.554208467777187
				],
				[
					1.9257014112961883,
					11.939348750036402
				],
				[
					2.31084169355546,
					12.324489032295673
				],
				[
					2.31084169355546,
					12.324489032295673
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.20636801421642303,
				0.2613140046596527,
				0.2681235373020172,
				0.2990940809249878,
				0.40145713090896606,
				0.445306658744812,
				0.46866747736930847,
				0.4841367304325104,
				0.46153345704078674,
				0.0906239002943039,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 653768253,
			"isDeleted": false,
			"id": "IwGrrPYMOMelLKv6XqaG2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 294.4763117906475,
			"y": 342.78031803956026,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.013647338740213,
			"height": 10.7839279032587,
			"seed": 1376433289,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.38514028225921493,
					0
				],
				[
					1.5405611290369734,
					0.38514028225921493
				],
				[
					3.4662625403331617,
					0.38514028225921493
				],
				[
					7.317665362925538,
					0
				],
				[
					8.473086209703297,
					-2.31084169355546
				],
				[
					6.9325250806663234,
					-3.081122258073947
				],
				[
					3.8514028225923767,
					-1.5405611290369734
				],
				[
					2.3108416935554033,
					1.9257014112961883
				],
				[
					3.4662625403331617,
					6.547384798407052
				],
				[
					6.547384798407052,
					7.702805645184753
				],
				[
					9.628507056480998,
					5.777104233888565
				],
				[
					10.013647338740213,
					5.39196395162935
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06355999410152435,
				0.11832159757614136,
				0.18241198360919952,
				0.25154998898506165,
				0.18950332701206207,
				0.09990197420120239,
				0.06409893929958344,
				0.11249084770679474,
				0.19406698644161224,
				0.18968896567821503,
				0.05809878557920456,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 775133203,
			"isDeleted": false,
			"id": "T_iI789sglPNmCIcewU2X",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 308.34136195198016,
			"y": 342.01003747504177,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.473086209703297,
			"height": 8.858226491962512,
			"seed": 1528357065,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.38514028225927177,
					0
				],
				[
					-0.7702805645184867,
					0.7702805645184867
				],
				[
					-0.7702805645184867,
					1.9257014112961883
				],
				[
					0,
					5.39196395162935
				],
				[
					0.7702805645184867,
					7.317665362925538
				],
				[
					1.5405611290369166,
					6.547384798407052
				],
				[
					3.4662625403331617,
					2.695981975814675
				],
				[
					7.317665362925538,
					-1.1554208467777585
				],
				[
					7.70280564518481,
					-1.5405611290369734
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10210800170898438,
				0.1438339799642563,
				0.18973401188850403,
				0.17221170663833618,
				0.16241542994976044,
				0.18825872242450714,
				0.04827038571238518,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 847242909,
			"isDeleted": false,
			"id": "-uotGB0wSnq1Fu_8mJWhL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 316.4293078794242,
			"y": 341.2397569105233,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.70280564518481,
			"height": 9.243366774221784,
			"seed": 1822298217,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7702805645184867
				],
				[
					-0.38514028225921493,
					2.3108416935554033
				],
				[
					-0.7702805645184867,
					6.547384798407052
				],
				[
					-0.38514028225921493,
					7.70280564518481
				],
				[
					1.5405611290369734,
					4.621683387110863
				],
				[
					3.8514028225923767,
					0.38514028225921493
				],
				[
					6.5473847984071085,
					-1.5405611290369734
				],
				[
					6.9325250806663234,
					-1.5405611290369734
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07886099070310593,
				0.09027398377656937,
				0.13607937097549438,
				0.12407940626144409,
				0.15615850687026978,
				0.18480877578258514,
				0.03647943213582039,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 583867827,
			"isDeleted": false,
			"id": "zbAbkCaT9pYCR9-jJCvjZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 326.8280955004237,
			"y": 343.93573888633796,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.317665362925595,
			"height": 8.473086209703297,
			"seed": 1764118825,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7702805645184867,
					0.7702805645184867
				],
				[
					-1.1554208467777016,
					2.3108416935554033
				],
				[
					-1.5405611290369734,
					3.4662625403331617
				],
				[
					0.38514028225921493,
					4.236543104851648
				],
				[
					2.695981975814675,
					2.695981975814675
				],
				[
					4.236543104851648,
					-1.5405611290369734
				],
				[
					1.9257014112961883,
					-4.236543104851648
				],
				[
					-1.9257014112961883,
					-1.9257014112961883
				],
				[
					-3.081122258073947,
					3.4662625403331617
				],
				[
					-2.695981975814675,
					3.8514028225923767
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0930589884519577,
				0.13958300650119781,
				0.1961980015039444,
				0.21805444359779358,
				0.223083034157753,
				0.23485608398914337,
				0.1729583740234375,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 308480765,
			"isDeleted": false,
			"id": "PISIVkV8vB8LZOYuJSuVB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 331.0646386052753,
			"y": 340.4694763460048,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.858226491962512,
			"height": 8.858226491962569,
			"seed": 331742121,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.1554208467777016
				],
				[
					0,
					5.006823669370135
				],
				[
					1.5405611290369734,
					6.5473847984071085
				],
				[
					4.236543104851648,
					3.08112225807389
				],
				[
					6.9325250806663234,
					0
				],
				[
					8.473086209703297,
					-1.9257014112961883
				],
				[
					8.858226491962512,
					-2.31084169355546
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2136159986257553,
				0.255002498626709,
				0.23084867000579834,
				0.21731671690940857,
				0.25366413593292236,
				0.09822820872068405,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 23392083,
			"isDeleted": false,
			"id": "t_zces1VP8sPnsF-Sveiu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 172.58258640181606,
			"y": 171.1166323746409,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 30.25185014979985,
			"height": 15.125925074899897,
			"seed": 62702985,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.0431672465447832,
					-0.5215836232723916
				],
				[
					-2.0863344930896233,
					-0.5215836232723916
				],
				[
					1.04316724654484,
					-1.0431672465448116
				],
				[
					6.780587102541347,
					-0.5215836232723916
				],
				[
					13.561174205082693,
					1.5647508698172317
				],
				[
					21.38492855416888,
					5.215836232724115
				],
				[
					26.079181163620547,
					10.431672465448202
				],
				[
					27.643932033437807,
					13.561174205082665
				],
				[
					28.165515656710227,
					14.082757828355085
				],
				[
					28.165515656710227,
					13.561174205082665
				],
				[
					28.165515656710227,
					13.561174205082665
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07622800022363663,
				0.07661101967096329,
				0.25045397877693176,
				0.2666241228580475,
				0.2535559833049774,
				0.2430802583694458,
				0.2719751000404358,
				0.3246544301509857,
				0.3357812464237213,
				0.1681186556816101,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1730323293,
			"isDeleted": false,
			"id": "eupOUlOPGhtVjGcVjmkkD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 207.52868916106758,
			"y": 184.67780657972355,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.474839711993013,
			"height": 14.082757828355113,
			"seed": 626390761,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5215836232723632,
					0.52158362327242
				],
				[
					1.56475086981726,
					3.1295017396344633
				],
				[
					4.694252609451723,
					7.823754349086187
				],
				[
					6.259003479268927,
					11.474839711993042
				],
				[
					6.259003479268927,
					13.039590581810273
				],
				[
					3.6510853629068833,
					13.039590581810273
				],
				[
					0,
					13.561174205082693
				],
				[
					-3.6510853629068265,
					14.082757828355113
				],
				[
					-5.215836232724087,
					14.082757828355113
				],
				[
					-4.694252609451667,
					13.561174205082693
				],
				[
					-4.1726689861792465,
					13.039590581810273
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06878634542226791,
				0.19127599895000458,
				0.20247259736061096,
				0.19273483753204346,
				0.2354399412870407,
				0.2874671220779419,
				0.34273046255111694,
				0.3974206745624542,
				0.3961222469806671,
				0.1291225254535675,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 206671091,
			"isDeleted": false,
			"id": "k8If5jTbZIiOnq8xRNByd",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 164.75883205272993,
			"y": 186.2425574495408,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.518006958537853,
			"height": 41.726689861792806,
			"seed": 1550904393,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5215836232723916
				],
				[
					1.04316724654484,
					1.5647508698172032
				],
				[
					2.6079181163620433,
					8.86692159563097
				],
				[
					3.6510853629068833,
					17.73384319126194
				],
				[
					5.737419855996507,
					26.60076478689291
				],
				[
					8.34533797235855,
					32.859768266161836
				],
				[
					10.43167246544823,
					38.07560449888595
				],
				[
					11.474839711993013,
					41.205106238520386
				],
				[
					12.518006958537853,
					41.726689861792806
				],
				[
					12.518006958537853,
					41.726689861792806
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17048199474811554,
				0.1957390159368515,
				0.2367950677871704,
				0.30107152462005615,
				0.34087371826171875,
				0.34618204832077026,
				0.3683454394340515,
				0.3612401485443115,
				0.1406886875629425,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1158688701,
			"isDeleted": false,
			"id": "jhccQXv1MGpQn7kU0nwjj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 173.6257536483609,
			"y": 233.18508354405776,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.518006958537853,
			"height": 10.43167246544823,
			"seed": 784656073,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.52158362327242,
					0.5215836232723632
				],
				[
					3.6510853629068833,
					3.6510853629068265
				],
				[
					6.259003479268927,
					7.82375434908613
				],
				[
					7.302170725813767,
					9.38850521890339
				],
				[
					7.823754349086187,
					7.82375434908613
				],
				[
					8.86692159563097,
					3.6510853629068265
				],
				[
					11.474839711993013,
					0
				],
				[
					11.996423335265433,
					-1.04316724654484
				],
				[
					12.518006958537853,
					-0.52158362327242
				],
				[
					12.518006958537853,
					-0.52158362327242
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14483898878097534,
				0.23411999642848969,
				0.26113200187683105,
				0.24851638078689575,
				0.3395983874797821,
				0.33590781688690186,
				0.36121800541877747,
				0.36176425218582153,
				0.13838233053684235,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 84,
			"versionNonce": 1998157459,
			"isDeleted": false,
			"id": "6mWq3ybrXBvpeeqD2jGq7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 70.56015364732372,
			"y": 323.1477306329777,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 103.36809811774975,
			"height": 77.93196926154957,
			"seed": 700784969,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-2.70597115491492,
					0.5411942309829669
				],
				[
					-5.953136540812807,
					1.6235826929489576
				],
				[
					-9.200301926710722,
					3.2471653858979153
				],
				[
					-8.659107695727727,
					4.329553847863906
				],
				[
					-7.576719233761764,
					4.870748078846816
				],
				[
					-12.447467312608609,
					13.529855774574628
				],
				[
					-15.694632698506496,
					26.518517318166175
				],
				[
					-11.365078850642647,
					29.224488473081067
				],
				[
					-7.576719233761764,
					29.76568270406409
				],
				[
					-8.11791346474476,
					36.80120770684283
				],
				[
					-3.247165385897887,
					38.42479039979179
				],
				[
					2.70597115491492,
					37.88359616880882
				],
				[
					7.035525002778769,
					41.671955785689704
				],
				[
					15.153438467523529,
					42.21315001667273
				],
				[
					24.894934625217218,
					38.96598463077481
				],
				[
					30.306876935047057,
					38.42479039979179
				],
				[
					31.38926539701302,
					38.96598463077481
				],
				[
					34.09523655192794,
					36.260013475859864
				],
				[
					35.1776250138939,
					36.260013475859864
				],
				[
					34.09523655192794,
					40.048373092740746
				],
				[
					31.930459627996015,
					46.54270386453658
				],
				[
					31.38926539701302,
					50.872257712400426
				],
				[
					31.38926539701302,
					54.11942309829834
				],
				[
					30.848071166030024,
					56.82539425321323
				],
				[
					30.306876935047057,
					58.44897694616219
				],
				[
					30.848071166030024,
					60.07255963911115
				],
				[
					31.38926539701302,
					60.613753870094115
				],
				[
					33.01284808996198,
					58.99017117714516
				],
				[
					35.1776250138939,
					56.82539425321323
				],
				[
					38.42479039979179,
					54.11942309829834
				],
				[
					40.048373092740746,
					53.57822886731532
				],
				[
					41.13076155470671,
					55.201811560264275
				],
				[
					42.21315001667267,
					58.44897694616219
				],
				[
					43.29553847863866,
					63.31972502500906
				],
				[
					46.00150963355355,
					68.19047310385588
				],
				[
					49.789869250434435,
					73.0612211827027
				],
				[
					55.74300579124727,
					75.76719233761764
				],
				[
					62.77853079402604,
					77.3907750305666
				],
				[
					69.81405579680481,
					77.93196926154957
				],
				[
					75.76719233761764,
					77.93196926154957
				],
				[
					79.55555195449853,
					77.3907750305666
				],
				[
					82.80271734039641,
					76.30838656860061
				],
				[
					86.5910769572773,
					74.14360964466869
				],
				[
					87.67346541924326,
					73.0612211827027
				],
				[
					87.13227118826029,
					72.52002695171979
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14656174182891846,
				0.2324339896440506,
				0.26949700713157654,
				0.2353438436985016,
				0.30406373739242554,
				0.41079986095428467,
				0.3877975046634674,
				0.31105297803878784,
				0.4273792803287506,
				0.4781217873096466,
				0.39569762349128723,
				0.37918639183044434,
				0.4197005033493042,
				0.3682006001472473,
				0.3732922375202179,
				0.4506910741329193,
				0.4799564480781555,
				0.45320412516593933,
				0.5231621265411377,
				0.6233420372009277,
				0.566067636013031,
				0.5241860151290894,
				0.5392208099365234,
				0.5714746117591858,
				0.5202251076698303,
				0.502325713634491,
				0.4911857843399048,
				0.49338942766189575,
				0.49490150809288025,
				0.47723057866096497,
				0.45274677872657776,
				0.4891347885131836,
				0.4805273711681366,
				0.4859980344772339,
				0.526638925075531,
				0.5344992876052856,
				0.5455260276794434,
				0.5306569933891296,
				0.5156509876251221,
				0.5227301716804504,
				0.5005070567131042,
				0.3680787980556488,
				0.14723199605941772,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 978137117,
			"isDeleted": false,
			"id": "FykIJX4zbAOMnzVNCjGNE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 29.50021092766535,
			"y": 393.55470582232465,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.35525017907690426,
			"height": 0,
			"seed": 1366982761,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.35525017907690426,
					0
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1081289779,
			"isDeleted": false,
			"id": "aFZ-1qAiPlBLzHD8IJczv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 29.144960748588446,
			"y": 391.7784549269402,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7105003581537801,
			"height": 0.3552501790768474,
			"seed": 1785732809,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7105003581537801,
					0.3552501790768474
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.00909945648163557,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 348857469,
			"isDeleted": false,
			"id": "dXFmkYQS966rBqk-hY4Az",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 29.144960748588446,
			"y": 389.29170367340186,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.144256625845173,
			"height": 11.012755551383748,
			"seed": 1513537833,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.35525017907687584,
					-0.35525017907690426
				],
				[
					-0.35525017907687584,
					-0.7105003581537517
				],
				[
					0.35525017907690426,
					0
				],
				[
					1.0657505372307128,
					5.32875268615345
				],
				[
					2.131501074461397,
					10.302255193229996
				],
				[
					2.8420014326151772,
					9.947005014153149
				],
				[
					2.8420014326151772,
					6.394503223384163
				],
				[
					4.263002148922766,
					1.7762508953845213
				],
				[
					6.039253044307259,
					0.7105003581538085
				],
				[
					7.460253760614847,
					4.618252327999642
				],
				[
					7.460253760614847,
					7.815503939691723
				],
				[
					7.105003581537943,
					7.105003581537915
				],
				[
					8.881254476922436,
					2.48675125353833
				],
				[
					10.6575053723069,
					1.0657505372307128
				],
				[
					12.789006446768298,
					2.8420014326151772
				],
				[
					12.789006446768298,
					7.460253760614876
				],
				[
					12.433756267691393,
					9.947005014153149
				],
				[
					12.789006446768298,
					9.591754835076188
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09711999446153641,
				0.16212573647499084,
				0.2041056752204895,
				0.23179122805595398,
				0.13011011481285095,
				0.11957165598869324,
				0.12623843550682068,
				0.14354047179222107,
				0.16989126801490784,
				0.18450278043746948,
				0.21749670803546906,
				0.16205236315727234,
				0.14202994108200073,
				0.19675034284591675,
				0.23227429389953613,
				0.12439007312059402,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1279602131,
			"isDeleted": false,
			"id": "b642rIl0jeqxF86h8hanK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 46.552219523356385,
			"y": 392.84420546417084,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.618252327999642,
			"height": 7.460253760614876,
			"seed": 641299113,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.35525017907690426,
					0.7105003581538085
				],
				[
					-0.7105003581537801,
					3.90775196984589
				],
				[
					-0.7105003581537801,
					5.32875268615345
				],
				[
					1.4210007163075886,
					5.32875268615345
				],
				[
					3.5525017907689573,
					2.8420014326151772
				],
				[
					3.9077519698458616,
					-0.35525017907690426
				],
				[
					2.486751253538273,
					-2.1315010744614256
				],
				[
					0,
					-0.7105003581538085
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08180822432041168,
				0.12230554223060608,
				0.1484837681055069,
				0.15554498136043549,
				0.19189248979091644,
				0.21401043236255646,
				0.011668975464999676,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1749781725,
			"isDeleted": false,
			"id": "Bq_21yuJjn71SdZMojIR3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 46.90746970243329,
			"y": 394.6204563595553,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.973502507076546,
			"height": 1.7762508953844645,
			"seed": 1038277929,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.35525017907687584,
					0.7105003581538085
				],
				[
					1.0657505372306844,
					1.7762508953844645
				],
				[
					4.618252327999642,
					1.0657505372307128
				],
				[
					4.973502507076546,
					0.7105003581538085
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.19821248948574066,
				0.14410021901130676,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 1034287987,
			"isDeleted": false,
			"id": "AFWqN4tHwUOZQ8x4h4AVb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 56.1439743584326,
			"y": 390.7127043897094,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.263002148922737,
			"height": 6.749753402461067,
			"seed": 530524777,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.3552501790769611
				],
				[
					0,
					0.7105003581538085
				],
				[
					0.7105003581537801,
					1.421000716307617
				],
				[
					2.486751253538273,
					4.263002148922794
				],
				[
					4.263002148922737,
					6.749753402461067
				],
				[
					4.263002148922737,
					6.749753402461067
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1472029983997345,
				0.2136009782552719,
				0.25436636805534363,
				0.06062045320868492,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 1415571773,
			"isDeleted": false,
			"id": "QjsYyFgxfldJcL4Uehx12",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 61.11747686550915,
			"y": 392.13370510601703,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.394503223384135,
			"height": 7.105003581537858,
			"seed": 1081045353,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7105003581538085,
					0
				],
				[
					-1.4210007163075886,
					-0.3552501790768474
				],
				[
					-1.7762508953844929,
					-0.3552501790768474
				],
				[
					-2.8420014326151772,
					1.421000716307617
				],
				[
					-6.394503223384135,
					6.74975340246101
				],
				[
					-6.394503223384135,
					6.74975340246101
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.17633074522018433,
				0.25136029720306396,
				0.2755259871482849,
				0.12625116109848022,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 282858771,
			"isDeleted": false,
			"id": "kCHTOC158RNlohfnbtvoB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 33.05271271843431,
			"y": 407.05421262724667,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.591754835076216,
			"height": 9.591754835076188,
			"seed": 1732819049,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7105003581538085
				],
				[
					0,
					-1.065750537230656
				],
				[
					0,
					-1.4210007163075602
				],
				[
					0.35525017907690426,
					0
				],
				[
					0.7105003581538085,
					3.90775196984589
				],
				[
					1.0657505372307128,
					8.170754118768627
				],
				[
					1.4210007163075886,
					7.460253760614819
				],
				[
					2.8420014326151772,
					3.5525017907689858
				],
				[
					6.394503223384135,
					0.3552501790769611
				],
				[
					9.236504655999312,
					0.7105003581538085
				],
				[
					9.591754835076216,
					0.7105003581538085
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.047343019396066666,
				0.07079211622476578,
				0.09233389049768448,
				0.1227836012840271,
				0.13366280496120453,
				0.1302727311849594,
				0.15334457159042358,
				0.15611477196216583,
				0.1208028569817543,
				0.0389031358063221,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 174700957,
			"isDeleted": false,
			"id": "vnIHEHc_N4h7k5K0hqv2k",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 43.3549679116643,
			"y": 411.67246495524637,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.394503223384135,
			"height": 7.460253760614819,
			"seed": 452017609,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7105003581537801,
					1.4210007163075602
				],
				[
					-0.7105003581537801,
					2.1315010744613687
				],
				[
					-0.7105003581537801,
					2.486751253538273
				],
				[
					2.4867512535383014,
					2.486751253538273
				],
				[
					4.973502507076574,
					1.065750537230656
				],
				[
					5.6840028652303545,
					-0.7105003581538085
				],
				[
					5.32875268615345,
					-3.1972516116920815
				],
				[
					2.131501074461397,
					-4.973502507076546
				],
				[
					2.131501074461397,
					-4.6182523279996985
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06302600353956223,
				0.06302600353956223,
				0.131789430975914,
				0.15447939932346344,
				0.16479244828224182,
				0.21420297026634216,
				0.209654301404953,
				0.06427545100450516,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1969093299,
			"isDeleted": false,
			"id": "uQ7KxROY5csTXMMUa1Dow",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 46.90746970243329,
			"y": 412.0277151343232,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.197251611692053,
			"height": 0.7105003581538085,
			"seed": 101354857,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.35525017907687584,
					0.3552501790769611
				],
				[
					1.0657505372306844,
					0.7105003581538085
				],
				[
					2.8420014326151772,
					0.7105003581538085
				],
				[
					3.197251611692053,
					0.7105003581538085
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07513650506734848,
				0.10006722807884216,
				0.06888747960329056,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 328891901,
			"isDeleted": false,
			"id": "EoWzmZuGcyG88uRpFMEvK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 51.880972209509835,
			"y": 408.4752133435543,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.749753402461039,
			"height": 5.6840028652303545,
			"seed": 1557506729,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.35525017907690426,
					0.3552501790768474
				],
				[
					-0.35525017907690426,
					1.065750537230656
				],
				[
					0.7105003581537801,
					3.552501790768929
				],
				[
					1.4210007163075886,
					5.32875268615345
				],
				[
					2.8420014326151772,
					3.552501790768929
				],
				[
					4.618252327999642,
					0
				],
				[
					5.684002865230326,
					-0.35525017907690426
				],
				[
					6.03925304430723,
					1.421000716307617
				],
				[
					6.03925304430723,
					4.263002148922737
				],
				[
					6.394503223384135,
					4.618252327999642
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.049575988203287125,
				0.112342469394207,
				0.1789991706609726,
				0.20953287184238434,
				0.15234902501106262,
				0.11742596328258514,
				0.16622231900691986,
				0.19629666209220886,
				0.0563475638628006,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1741827155,
			"isDeleted": false,
			"id": "n0r3HPrOjBmJNYy9JGKtZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 61.47272704458602,
			"y": 408.83046352263113,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.394503223384135,
			"height": 7.105003581537915,
			"seed": 451613993,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7105003581537801,
					0.3552501790769611
				],
				[
					-1.0657505372306844,
					0.7105003581538085
				],
				[
					-1.4210007163075602,
					1.7762508953845213
				],
				[
					-0.7105003581537801,
					4.263002148922794
				],
				[
					2.131501074461397,
					4.973502507076603
				],
				[
					4.263002148922766,
					3.1972516116920815
				],
				[
					4.973502507076574,
					0.3552501790769611
				],
				[
					3.1972516116920815,
					-2.131501074461312
				],
				[
					1.4210007163075886,
					-0.7105003581537517
				],
				[
					0.7105003581538085,
					2.842001432615234
				],
				[
					1.0657505372307128,
					3.1972516116920815
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10745199769735336,
				0.14538998901844025,
				0.18333135545253754,
				0.1684991419315338,
				0.18113425374031067,
				0.19210174679756165,
				0.17162247002124786,
				0.07863662391901016,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1458812509,
			"isDeleted": false,
			"id": "QI2YULnS4bT83KDhV43q_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 66.09097937258569,
			"y": 407.05421262724667,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.170754118768627,
			"height": 15.275757700306599,
			"seed": 931193481,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7105003581538085,
					0
				],
				[
					-0.7105003581538085,
					0.3552501790769611
				],
				[
					-1.0657505372306844,
					1.0657505372307128
				],
				[
					-0.35525017907690426,
					3.90775196984589
				],
				[
					0.35525017907690426,
					9.947005014153092
				],
				[
					0.35525017907690426,
					13.854756983998982
				],
				[
					-1.7762508953844929,
					15.275757700306599
				],
				[
					-6.03925304430723,
					14.56525734215279
				],
				[
					-7.815503939691723,
					11.368005730460709
				],
				[
					-7.815503939691723,
					11.012755551383805
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09580999612808228,
				0.12319198250770569,
				0.1408388912677765,
				0.1923919916152954,
				0.21556033194065094,
				0.18693161010742188,
				0.09735830873250961,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 202320371,
			"isDeleted": false,
			"id": "pBYD2C9EAWoBg3RpGXOnq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 72.13023241689292,
			"y": 408.83046352263113,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4210007163075886,
			"height": 1.065750537230656,
			"seed": 253590793,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.35525017907690426,
					0
				],
				[
					0.35525017907690426,
					-0.3552501790768474
				],
				[
					1.4210007163075886,
					-1.065750537230656
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06523797661066055,
				0,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1598481085,
			"isDeleted": false,
			"id": "zh_TFvyB3YvN6DEfRNtKN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 71.41973205873914,
			"y": 410.25146423893875,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.815503939691723,
			"height": 4.263002148922794,
			"seed": 340209961,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.35525017907690426
				],
				[
					-0.35525017907690426,
					0.35525017907690426
				],
				[
					0.35525017907690426,
					0.35525017907690426
				],
				[
					3.197251611692053,
					0
				],
				[
					4.973502507076546,
					-0.7105003581538085
				],
				[
					4.618252327999642,
					-0.7105003581538085
				],
				[
					2.8420014326151772,
					-1.421000716307617
				],
				[
					1.4210007163075886,
					-1.421000716307617
				],
				[
					1.0657505372306844,
					-1.065750537230656
				],
				[
					1.4210007163075886,
					1.0657505372307128
				],
				[
					3.197251611692053,
					2.8420014326151772
				],
				[
					7.105003581537915,
					2.8420014326151772
				],
				[
					7.460253760614819,
					2.8420014326151772
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12061700224876404,
				0.16098269820213318,
				0.24940697848796844,
				0.30254700779914856,
				0.22499407827854156,
				0.10334756225347519,
				0.08220803737640381,
				0.16495294868946075,
				0.24285873770713806,
				0.22607940435409546,
				0.15564404428005219,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1192981395,
			"isDeleted": false,
			"id": "a6_jrZrIPbLUSFNvikIaF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 51.59715803718343,
			"y": 427.32287306608686,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.525742848414552,
			"height": 0.5816571419383649,
			"seed": 2036740169,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.0357999967843057,
					-0.5816571419383649
				],
				[
					3.199114280661064,
					-0.5816571419383649
				],
				[
					5.23491427744537,
					-0.5816571419383649
				],
				[
					5.525742848414552,
					-0.2908285709692109
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1639387458562851,
				0.17190274596214294,
				0.04469546675682068,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1630896925,
			"isDeleted": false,
			"id": "Y6KsSQL-8LKBT5VSK30Id",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 54.505443746875315,
			"y": 431.10364448868626,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.4899428516302464,
			"height": 1.4541428548459407,
			"seed": 143762825,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5816571419383649,
					0.5816571419383649
				],
				[
					0.8724857129075474,
					1.1633142838767867
				],
				[
					2.0357999967843057,
					1.4541428548459407
				],
				[
					3.1991142806610355,
					1.4541428548459407
				],
				[
					3.4899428516302464,
					1.4541428548459407
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06333459168672562,
				0.09603207558393478,
				0.13377465307712555,
				0.06911034882068634,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 422414643,
			"isDeleted": false,
			"id": "Ozh8TZUE2S6C5iVa-1Ktj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 47.33151584806782,
			"y": 445.1841181127583,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2010959616589219,
			"height": 9.608767693271488,
			"seed": 2048256425,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4003653205530213
				],
				[
					-0.4003653205529645,
					4.003653205529815
				],
				[
					0,
					8.007306411059574
				],
				[
					0.8007306411059574,
					9.608767693271488
				],
				[
					0.8007306411059574,
					9.208402372718467
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.21503201127052307,
				0.26757997274398804,
				0.06467577815055847,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 19994493,
			"isDeleted": false,
			"id": "nWZwe5evqAgbxby2wQg0V",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 42.126766680879115,
			"y": 443.18229150999343,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.407671731612538,
			"height": 7.606941090506609,
			"seed": 1341526473,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4003653205529645,
					0
				],
				[
					-0.4003653205529645,
					-0.4003653205529645
				],
				[
					0,
					-1.2010959616589503
				],
				[
					1.6014612822119147,
					-3.2029225644238295
				],
				[
					4.003653205529787,
					-6.0054798082946945
				],
				[
					5.204749167188709,
					-6.0054798082946945
				],
				[
					6.405845128847659,
					-2.4021919233179005
				],
				[
					7.206575769953616,
					0.800730641105929
				],
				[
					7.606941090506581,
					1.6014612822119147
				],
				[
					8.007306411059574,
					1.2010959616588934
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15526199340820312,
				0.21478399634361267,
				0.2535119950771332,
				0.26526710391044617,
				0.26098498702049255,
				0.32983654737472534,
				0.3657647669315338,
				0.1623190939426422,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 934013651,
			"isDeleted": false,
			"id": "Ecz_NVSK111XtwCUL79-V",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 52.13589969470357,
			"y": 449.5881366388411,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.804383846635744,
			"height": 8.007306411059517,
			"seed": 15584329,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8007306411059574,
					0
				],
				[
					-2.402191923317872,
					1.601461282211858
				],
				[
					-2.402191923317872,
					2.802557243870865
				],
				[
					-0.4003653205529645,
					4.404018526082723
				],
				[
					1.6014612822119147,
					6.405845128847659
				],
				[
					2.0018266027649076,
					7.606941090506552
				],
				[
					0.4003653205529929,
					8.007306411059517
				],
				[
					-2.402191923317872,
					7.606941090506552
				],
				[
					-2.8025572438708366,
					6.8062104494006235
				],
				[
					-2.8025572438708366,
					6.405845128847659
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04059097170829773,
				0.10871200263500214,
				0.16607998311519623,
				0.13179150223731995,
				0.12074831873178482,
				0.14688372611999512,
				0.1758747547864914,
				0.1378081738948822,
				0.03324926644563675,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1501241309,
			"isDeleted": false,
			"id": "yDXPxsjn89N4-7EoR5Vs0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 58.54174482355123,
			"y": 448.38704067718214,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8007306411059574,
			"height": 8.407671731612538,
			"seed": 988923593,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8007306411059858
				],
				[
					0,
					2.0018266027648792
				],
				[
					0.4003653205529929,
					6.005479808294638
				],
				[
					0.8007306411059574,
					8.407671731612538
				],
				[
					0.8007306411059574,
					8.407671731612538
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11702875047922134,
				0.17170800268650055,
				0.2024812549352646,
				0.029368743300437927,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1731008627,
			"isDeleted": false,
			"id": "V6hC0j9prGIEvCNH4RwvC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 56.139552900233355,
			"y": 452.7910592032649,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.0054798082946945,
			"height": 0.4003653205529645,
			"seed": 1231287017,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4003653205529645
				],
				[
					2.0018266027649076,
					0.4003653205529645
				],
				[
					5.605114487741702,
					0
				],
				[
					6.0054798082946945,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.30300647020339966,
				0.18091289699077606,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1076173885,
			"isDeleted": false,
			"id": "8rqWRWEmAI8rjG-VGwj2J",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 65.34795527295188,
			"y": 456.7947124087947,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4003653205529929,
			"height": 0.4003653205529645,
			"seed": 239398953,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4003653205529929,
					0
				],
				[
					-0.4003653205529929,
					0.4003653205529645
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.278903990983963,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 360157715,
			"isDeleted": false,
			"id": "NNtVQhmH-MxKAzm74QWe8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 77.35891488954121,
			"y": 450.7892326005,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.007306411059574,
			"height": 24.021919233178778,
			"seed": 1645673833,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					3.2029225644238295,
					-2.802557243870808
				],
				[
					6.405845128847659,
					-9.208402372718467
				],
				[
					6.405845128847659,
					-12.411324937142297
				],
				[
					4.003653205529787,
					-12.811690257695318
				],
				[
					1.6014612822119147,
					-10.409498334377417
				],
				[
					1.2010959616589503,
					-6.005479808294638
				],
				[
					2.802557243870865,
					-0.4003653205529645
				],
				[
					4.40401852608278,
					5.60511448774173
				],
				[
					4.804383846635744,
					9.208402372718524
				],
				[
					4.40401852608278,
					10.809863654930439
				],
				[
					2.0018266027649076,
					11.21022897548346
				],
				[
					-1.2010959616589219,
					10.009133013824453
				],
				[
					-1.6014612822119147,
					7.206575769953645
				],
				[
					-1.2010959616589219,
					6.8062104494006235
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.29041197896003723,
				0.2756381332874298,
				0.18096230924129486,
				0.13828693330287933,
				0.14343535900115967,
				0.15914928913116455,
				0.18167023360729218,
				0.18394991755485535,
				0.20398513972759247,
				0.23328912258148193,
				0.24371658265590668,
				0.18064053356647491,
				0.018394287675619125,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1292930205,
			"isDeleted": false,
			"id": "aoTlbculA1HCwO4w5w8a-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 86.16695194170677,
			"y": 450.388867279947,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2010959616589503,
			"height": 5.204749167188766,
			"seed": 1446677353,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4003653205529645
				],
				[
					-0.8007306411059858,
					2.001826602764936
				],
				[
					-0.8007306411059858,
					3.2029225644238295
				],
				[
					0,
					5.204749167188766
				],
				[
					0.4003653205529645,
					5.204749167188766
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.18436647951602936,
				0.22407998144626617,
				0.056035980582237244,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 864147379,
			"isDeleted": false,
			"id": "J9PUo6rekJNoQjHRDoAGu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 87.36804790336566,
			"y": 446.7855793949702,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.800730641105929,
			"height": 0.800730641105929,
			"seed": 464923529,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4003653205529645,
					0.4003653205529645
				],
				[
					-0.800730641105929,
					0.800730641105929
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.056111570447683334,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 535752957,
			"isDeleted": false,
			"id": "eHTQoSKipRtrcHAnHtM7x",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 92.17243175000141,
			"y": 448.78740599773516,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.40401852608278,
			"height": 5.605114487741616,
			"seed": 1174155465,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4003653205529645
				],
				[
					1.2010959616589503,
					2.402191923317787
				],
				[
					4.40401852608278,
					5.605114487741616
				],
				[
					4.40401852608278,
					5.605114487741616
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12359490990638733,
				0.20633286237716675,
				0.02472592145204544,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 1332898131,
			"isDeleted": false,
			"id": "Kw20UdDBzOwUYRpC9FHKP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 97.77754623774314,
			"y": 448.78740599773516,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.0054798082946945,
			"height": 6.405845128847659,
			"seed": 1103971849,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8007306411059858,
					0
				],
				[
					-1.6014612822119147,
					-0.4003653205530213
				],
				[
					-4.003653205529815,
					2.0018266027648224
				],
				[
					-5.204749167188709,
					4.0036532055297585
				],
				[
					-6.0054798082946945,
					6.005479808294638
				],
				[
					-6.0054798082946945,
					6.005479808294638
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10242999345064163,
				0.22992950677871704,
				0.30605000257492065,
				0.3168940246105194,
				0.12635263800621033,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1715587421,
			"isDeleted": false,
			"id": "RdHY2AtG8XebthHx5FhnG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 104.58375668714376,
			"y": 449.5881366388411,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.60511448774173,
			"height": 7.206575769953588,
			"seed": 605023497,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4003653205529645,
					0
				],
				[
					1.2010959616589503,
					-0.4003653205529645
				],
				[
					2.4021919233178437,
					-0.800730641105929
				],
				[
					4.0036532055297585,
					-1.6014612822119147
				],
				[
					4.0036532055297585,
					-2.001826602764936
				],
				[
					1.6014612822119147,
					-2.4021919233179005
				],
				[
					-0.8007306411059858,
					0
				],
				[
					-0.8007306411059858,
					2.802557243870865
				],
				[
					1.6014612822119147,
					4.804383846635687
				],
				[
					4.804383846635744,
					3.603287884976794
				],
				[
					4.804383846635744,
					3.2029225644238295
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13477398455142975,
				0.1937599778175354,
				0.2811959981918335,
				0.23060449957847595,
				0.13725857436656952,
				0.1908627599477768,
				0.27910321950912476,
				0.3106747567653656,
				0.0608336478471756,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1855964915,
			"isDeleted": false,
			"id": "8SUccFPgcaZbUEjNNXNyy",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 112.19069777765037,
			"y": 447.1859447155232,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.60511448774173,
			"height": 8.007306411059517,
			"seed": 867233385,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4003653205530213,
					0
				],
				[
					-0.8007306411059858,
					0.4003653205529645
				],
				[
					-0.8007306411059858,
					3.603287884976794
				],
				[
					-0.4003653205530213,
					6.8062104494006235
				],
				[
					0.800730641105929,
					7.206575769953588
				],
				[
					2.0018266027648792,
					4.0036532055297585
				],
				[
					4.404018526082723,
					-0.800730641105929
				],
				[
					4.804383846635744,
					-0.800730641105929
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13694241642951965,
				0.21369622647762299,
				0.2268640697002411,
				0.18223755061626434,
				0.19156302511692047,
				0.0829012468457222,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 559584701,
			"isDeleted": false,
			"id": "IxFLrXV5EfUVUF1rfUbnp",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 117.79581226539204,
			"y": 447.9866753566292,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.40401852608278,
			"height": 6.005479808294638,
			"seed": 64728873,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.2010959616589503
				],
				[
					0,
					4.40401852608278
				],
				[
					0.8007306411059858,
					6.005479808294638
				],
				[
					2.0018266027648792,
					4.0036532055297585
				],
				[
					4.40401852608278,
					0.4003653205529645
				],
				[
					4.40401852608278,
					0.4003653205529645
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15833798050880432,
				0.159287229180336,
				0.1319284737110138,
				0.132585808634758,
				0.056580230593681335,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 663777427,
			"isDeleted": false,
			"id": "MClWuuA4S6BPnNcm2kgQA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 124.60202271479267,
			"y": 449.98850195939406,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.605114487741673,
			"height": 6.005479808294638,
			"seed": 810235433,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4003653205529645,
					0.800730641105929
				],
				[
					-1.2010959616588934,
					3.2029225644238295
				],
				[
					1.2010959616589503,
					4.404018526082723
				],
				[
					4.003653205529815,
					2.802557243870865
				],
				[
					4.40401852608278,
					0.4003653205529645
				],
				[
					2.4021919233179005,
					-1.6014612822119147
				],
				[
					-0.800730641105929,
					0.4003653205529645
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09922000020742416,
				0.19498199224472046,
				0.2554694712162018,
				0.235001802444458,
				0.26124730706214905,
				0.23312008380889893,
				0.007507995702326298,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 744150557,
			"isDeleted": false,
			"id": "rqBSSfPzCfyJvrCF7KesK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 128.60567592032248,
			"y": 449.1877713182881,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.005479808294638,
			"height": 6.405845128847659,
			"seed": 131891657,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4003653205529645
				],
				[
					0,
					1.2010959616588934
				],
				[
					1.2010959616588934,
					4.804383846635687
				],
				[
					2.0018266027648792,
					6.405845128847659
				],
				[
					4.0036532055297585,
					3.603287884976794
				],
				[
					5.605114487741673,
					0.4003653205529645
				],
				[
					6.005479808294638,
					0
				],
				[
					6.005479808294638,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09224380552768707,
				0.10819259285926819,
				0.12679477035999298,
				0.11262799054384232,
				0.11975637823343277,
				0.08689428865909576,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 2080040499,
			"isDeleted": false,
			"id": "wX3vtHqdUglEfAI-5U6hU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 72.95489636345846,
			"y": 472.0085945898079,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.8062104494006235,
			"height": 6.0054798082946945,
			"seed": 1468566153,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4003653205529645,
					-0.4003653205529645
				],
				[
					-0.8007306411059574,
					-0.4003653205529645
				],
				[
					-0.8007306411059574,
					0
				],
				[
					0.4003653205529929,
					2.802557243870865
				],
				[
					2.8025572438708366,
					4.0036532055297585
				],
				[
					5.605114487741702,
					2.0018266027648792
				],
				[
					6.005479808294666,
					-0.8007306411059858
				],
				[
					4.003653205529787,
					-2.001826602764936
				],
				[
					1.6014612822119147,
					0
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.125575989484787,
				0.1894560009241104,
				0.23453247547149658,
				0.2565234899520874,
				0.2779347598552704,
				0.28719890117645264,
				0.22829724848270416,
				0.02429598942399025,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 36964989,
			"isDeleted": false,
			"id": "r0EvtRUxVkYLFCi_kj9yK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 77.35891488954121,
			"y": 472.8093252309138,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.0054798082946945,
			"height": 2.001826602764936,
			"seed": 1097964521,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8007306411059574,
					0.800730641105929
				],
				[
					2.802557243870865,
					2.001826602764936
				],
				[
					5.605114487741702,
					2.001826602764936
				],
				[
					6.0054798082946945,
					1.6014612822119147
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1581690013408661,
				0.2659519910812378,
				0.16514572501182556,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1925556179,
			"isDeleted": false,
			"id": "V6ZStBkhRjHj8pD5tCFvr",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 87.36804790336566,
			"y": 464.4016534993013,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8007306411059858,
			"height": 10.809863654930439,
			"seed": 1145035049,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.2010959616589503
				],
				[
					0.8007306411059858,
					6.8062104494006235
				],
				[
					0.4003653205530213,
					10.809863654930439
				],
				[
					0.4003653205530213,
					10.809863654930439
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.23852798342704773,
				0.2321549952030182,
				0.057986173778772354,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1135063773,
			"isDeleted": false,
			"id": "ttFttqYELMR7E_8hES6dm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 82.96402937728291,
			"y": 470.4071333075959,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.407671731612567,
			"height": 1.2010959616590071,
			"seed": 1393501801,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4003653205529929,
					0.8007306411059858
				],
				[
					1.6014612822119432,
					1.2010959616590071
				],
				[
					4.003653205529787,
					1.2010959616590071
				],
				[
					8.007306411059602,
					1.2010959616590071
				],
				[
					8.407671731612567,
					1.2010959616590071
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12157198786735535,
				0.19591598212718964,
				0.22991599142551422,
				0.14279669523239136,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1913075059,
			"isDeleted": false,
			"id": "W0hsAOhHgIKCFYZ00uUfd",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 48.13224648917378,
			"y": 482.01772760363235,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2010959616589219,
			"height": 16.815343463225133,
			"seed": 769074825,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.8007306411059858
				],
				[
					0,
					-1.2010959616589503
				],
				[
					0,
					1.601461282211858
				],
				[
					-0.4003653205529645,
					8.808037052165503
				],
				[
					-0.8007306411059574,
					14.813516860460197
				],
				[
					-0.8007306411059574,
					15.614247501566183
				],
				[
					-1.2010959616589219,
					15.614247501566183
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.18206699192523956,
				0.2736699879169464,
				0.32756802439689636,
				0.3304387927055359,
				0.048275481909513474,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 2101825341,
			"isDeleted": false,
			"id": "bKeCSJhmPpWuEURCNBJPd",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 43.327862642538065,
			"y": 498.43270574630446,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.606941090506581,
			"height": 7.206575769953645,
			"seed": 1027650665,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8007306411059574,
					-0.800730641105929
				],
				[
					-1.2010959616589503,
					-1.2010959616589503
				],
				[
					-1.2010959616589503,
					-1.6014612822119147
				],
				[
					-0.8007306411059574,
					-0.4003653205529645
				],
				[
					0.4003653205529645,
					3.603287884976794
				],
				[
					2.402191923317872,
					5.60511448774173
				],
				[
					4.0036532055297585,
					4.0036532055297585
				],
				[
					6.005479808294666,
					0
				],
				[
					6.405845128847631,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11019198596477509,
				0.1481200009584427,
				0.1766849309206009,
				0.1865537464618683,
				0.2305757999420166,
				0.28243744373321533,
				0.07807421684265137,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1493569299,
			"isDeleted": false,
			"id": "ZZpAnDoGaMrg2vrg0nPhS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 55.3388222591274,
			"y": 494.82941786132767,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.804383846635744,
			"height": 7.206575769953588,
			"seed": 2022008841,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4003653205529645,
					0.4003653205529645
				],
				[
					-1.2010959616589219,
					1.2010959616588934
				],
				[
					-1.2010959616589219,
					2.0018266027648792
				],
				[
					0,
					4.0036532055297585
				],
				[
					1.6014612822119147,
					5.204749167188709
				],
				[
					2.0018266027649076,
					5.605114487741673
				],
				[
					-0.4003653205529645,
					6.405845128847659
				],
				[
					-2.8025572438708366,
					7.206575769953588
				],
				[
					-2.402191923317872,
					6.8062104494006235
				],
				[
					-1.6014612822119147,
					6.405845128847659
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09828197956085205,
				0.13799600303173065,
				0.19610001146793365,
				0.19753719866275787,
				0.21694666147232056,
				0.25574377179145813,
				0.20257405936717987,
				0.046754393726587296,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 762601373,
			"isDeleted": false,
			"id": "TTqkCAQnI_uPwpghmD5pf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 60.543571426316134,
			"y": 493.6283218996687,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4003653205529645,
			"height": 8.007306411059574,
			"seed": 1991623305,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					2.0018266027648792
				],
				[
					0,
					3.603287884976794
				],
				[
					0,
					5.204749167188709
				],
				[
					0.4003653205529645,
					7.606941090506609
				],
				[
					0.4003653205529645,
					8.007306411059574
				],
				[
					0.4003653205529645,
					8.007306411059574
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07484399527311325,
				0.108101986348629,
				0.15152600407600403,
				0.18012595176696777,
				0.044572386890649796,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1513665715,
			"isDeleted": false,
			"id": "t9LRVV49Pehn00k70xNj6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 57.340648861892305,
			"y": 498.0323404257515,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.404018526082751,
			"height": 0.4003653205529645,
			"seed": 1129572745,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4003653205529645,
					0
				],
				[
					1.6014612822119147,
					0
				],
				[
					4.003653205529787,
					-0.4003653205529645
				],
				[
					4.404018526082751,
					-0.4003653205529645
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.22316598892211914,
				0.2741380035877228,
				0.10407998412847519,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 174089213,
			"isDeleted": false,
			"id": "dAHrCM4msnodNEG26SX2D",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 64.94758995239889,
			"y": 499.63380170796336,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4003653205529645,
			"height": 0,
			"seed": 934506185,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4003653205529645,
					0
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2454102486371994,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 356886099,
			"isDeleted": false,
			"id": "i0PwV5MCQhZAG1SyW6xPf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 83.76476001838887,
			"y": 486.4217461297151,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.606941090506581,
			"height": 12.010959616589389,
			"seed": 1667764521,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4003653205529645,
					0
				],
				[
					-1.2010959616589219,
					0.8007306411059858
				],
				[
					-1.2010959616589219,
					3.2029225644238295
				],
				[
					-1.2010959616589219,
					7.606941090506609
				],
				[
					-1.6014612822119147,
					8.00730641105963
				],
				[
					-0.4003653205529645,
					6.8062104494006235
				],
				[
					2.0018266027648792,
					6.405845128847659
				],
				[
					4.40401852608278,
					6.8062104494006235
				],
				[
					5.204749167188709,
					9.208402372718524
				],
				[
					4.003653205529815,
					11.21022897548346
				],
				[
					0.8007306411059858,
					12.010959616589389
				],
				[
					-2.402191923317872,
					12.010959616589389
				],
				[
					-2.402191923317872,
					10.809863654930439
				],
				[
					-2.0018266027648792,
					10.409498334377474
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10083413869142532,
				0.13152456283569336,
				0.13971561193466187,
				0.1452643722295761,
				0.1266145557165146,
				0.16382132470607758,
				0.20382821559906006,
				0.2336219847202301,
				0.2650653123855591,
				0.2600729465484619,
				0.22444359958171844,
				0.04401998966932297,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 135060573,
			"isDeleted": false,
			"id": "OaLiNCpUCs1O-f_wKO1WV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 92.17243175000141,
			"y": 490.82576465579785,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.804383846635744,
			"height": 14.813516860460197,
			"seed": 1762402089,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4003653205529645,
					-0.4003653205529645
				],
				[
					-0.4003653205529645,
					0.4003653205530213
				],
				[
					-0.4003653205529645,
					2.4021919233178437
				],
				[
					0.4003653205530213,
					9.608767693271488
				],
				[
					0,
					14.413151539907233
				],
				[
					-0.800730641105929,
					13.21205557824834
				],
				[
					-1.2010959616588934,
					8.407671731612538
				],
				[
					0.4003653205530213,
					3.603287884976851
				],
				[
					3.2029225644238295,
					1.6014612822119147
				],
				[
					3.603287884976851,
					2.0018266027648792
				],
				[
					2.001826602764936,
					5.204749167188709
				],
				[
					0.8007306411059858,
					8.007306411059574
				],
				[
					0.4003653205530213,
					8.407671731612538
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14288906753063202,
				0.14318832755088806,
				0.14065591990947723,
				0.1598699390888214,
				0.14617010951042175,
				0.09306411445140839,
				0.12614205479621887,
				0.14329107105731964,
				0.17065517604351044,
				0.2032267451286316,
				0.08580721914768219,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1896047603,
			"isDeleted": false,
			"id": "bX4vDFYePhnj1jY8DikrZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 102.18156476382586,
			"y": 489.22430337358594,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.605114487741673,
			"height": 7.206575769953588,
			"seed": 227860041,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.800730641105929,
					0
				],
				[
					-2.0018266027648792,
					0
				],
				[
					-2.802557243870808,
					0.800730641105929
				],
				[
					-3.2029225644237727,
					2.001826602764936
				],
				[
					-1.2010959616588934,
					3.2029225644238295
				],
				[
					0.8007306411059858,
					4.40401852608278
				],
				[
					1.2010959616589503,
					5.60511448774173
				],
				[
					-1.2010959616588934,
					6.8062104494006235
				],
				[
					-4.404018526082723,
					7.206575769953588
				],
				[
					-4.404018526082723,
					7.206575769953588
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11402798444032669,
				0.1736299693584442,
				0.21117599308490753,
				0.24802865087985992,
				0.19807122647762299,
				0.17653830349445343,
				0.23639585077762604,
				0.2879887819290161,
				0.1542692631483078,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 508250301,
			"isDeleted": false,
			"id": "zx2OUygCM7PmeSKOxrpo0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 142.02052322731208,
			"y": 63.14012911873289,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.177497372325888,
			"height": 18.242109522880895,
			"seed": 2110642377,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6290382594096968
				],
				[
					0,
					-1.2580765188193936
				],
				[
					0,
					-2.516153037638759
				],
				[
					-1.2580765188193368,
					-3.774229556458124
				],
				[
					-5.032306075277461,
					-1.887114778229062
				],
				[
					-4.403267815867764,
					3.1451912970484273
				],
				[
					-0.6290382594096968,
					8.806535631735585
				],
				[
					0.6290382594096968,
					12.580765188193709
				],
				[
					-1.2580765188193368,
					14.467879966422771
				],
				[
					-5.032306075277461,
					14.467879966422771
				],
				[
					-7.548459112916191,
					13.838841707013074
				],
				[
					-6.919420853506551,
					12.580765188193709
				],
				[
					-6.2903825940968545,
					11.951726928784012
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05628741532564163,
				0.07702996581792831,
				0.11039617657661438,
				0.1611577421426773,
				0.19804918766021729,
				0.21536053717136383,
				0.2205718755722046,
				0.21692246198654175,
				0.2517140507698059,
				0.25625765323638916,
				0.14626803994178772,
				0.024534331634640694,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 897084819,
			"isDeleted": false,
			"id": "cb-xVYDUp7Duhhd-AhczB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 145.7947527837702,
			"y": 70.05954997223941,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.548459112916248,
			"height": 14.467879966422771,
			"seed": 1008077801,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.2580765188193936,
					0.6290382594096968
				],
				[
					-1.2580765188193936,
					2.516153037638759
				],
				[
					-0.6290382594096968,
					6.2903825940968545
				],
				[
					2.5161530376387304,
					7.548459112916248
				],
				[
					5.032306075277461,
					4.4032678158677925
				],
				[
					6.2903825940968545,
					-1.887114778229062
				],
				[
					3.774229556458124,
					-6.919420853506523
				],
				[
					0.6290382594096968,
					-6.2903825940968545
				],
				[
					0,
					0
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08647830039262772,
				0.12190639972686768,
				0.15868555009365082,
				0.20112451910972595,
				0.20444796979427338,
				0.1800154745578766,
				0.12962545454502106,
				0.006751006934791803,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1321019677,
			"isDeleted": false,
			"id": "tv4-ZkLzzQok9oJT9T94c",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 159.0045562313736,
			"y": 49.93032567112948,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.8871147782290905,
			"height": 23.274415598158356,
			"seed": 629072201,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6290382594096968,
					0
				],
				[
					-0.6290382594096968,
					4.4032678158677925
				],
				[
					-1.2580765188193936,
					16.9840330040615
				],
				[
					-1.8871147782290905,
					23.274415598158356
				],
				[
					-1.8871147782290905,
					22.645377338748688
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1083262637257576,
				0.18011800944805145,
				0.21758468449115753,
				0.18993841111660004,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1708868403,
			"isDeleted": false,
			"id": "sPZokHvYd_3tSTkG3kEeb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 162.77878578783174,
			"y": 65.02724389696192,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.548459112916248,
			"height": 8.806535631735613,
			"seed": 892329321,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6290382594096968,
					0
				],
				[
					-1.8871147782290905,
					1.2580765188193936
				],
				[
					-1.8871147782290905,
					3.1451912970484273
				],
				[
					-1.2580765188193936,
					6.919420853506551
				],
				[
					1.2580765188193368,
					8.806535631735613
				],
				[
					4.403267815867764,
					7.548459112916248
				],
				[
					5.032306075277461,
					5.032306075277489
				],
				[
					5.661344334687158,
					2.516153037638759
				],
				[
					5.661344334687158,
					1.887114778229062
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.050230711698532104,
				0.07648574560880661,
				0.13075268268585205,
				0.2023286074399948,
				0.2559303641319275,
				0.2135552614927292,
				0.029816437512636185,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1792277885,
			"isDeleted": false,
			"id": "-xI41EHkbZgxmDYPESHkh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 175.35955097602545,
			"y": 54.33359348699727,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.8871147782290905,
			"height": 18.871147782290592,
			"seed": 123744521,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.2580765188193936,
					-0.6290382594096968
				],
				[
					-1.8871147782290905,
					1.887114778229062
				],
				[
					-1.2580765188193936,
					10.693650409964647
				],
				[
					-0.6290382594096968,
					18.242109522880895
				],
				[
					-0.6290382594096968,
					18.242109522880895
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10794498026371002,
				0.20713599026203156,
				0.24779999256134033,
				0.015857940539717674,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1519543507,
			"isDeleted": false,
			"id": "TILG6siao8Pbj1RPxYGP0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 170.32724490074793,
			"y": 64.39820563755225,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.951726928784069,
			"height": 0.6290382594096968,
			"seed": 677143849,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6290382594096968,
					-0.6290382594096968
				],
				[
					10.693650409964675,
					-0.6290382594096968
				],
				[
					11.951726928784069,
					-0.6290382594096968
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13729049265384674,
				0.05072280764579773,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 433145309,
			"isDeleted": false,
			"id": "Ay-YoaS7hPH2P_Q97dKi4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 183.53704834835133,
			"y": 65.65628215637162,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2580765188193368,
			"height": 6.919420853506551,
			"seed": 936053641,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.2580765188193368,
					3.1451912970484273
				],
				[
					-1.2580765188193368,
					5.032306075277489
				],
				[
					-0.6290382594096968,
					6.919420853506551
				],
				[
					0,
					6.2903825940968545
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1121232882142067,
				0.06654907017946243,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 456413811,
			"isDeleted": false,
			"id": "sCxJpSNdhbgxFL9X9Lq9I",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 184.79512486717073,
			"y": 59.36589956227476,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2580765188193936,
			"height": 2.5161530376387304,
			"seed": 1156124873,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.2580765188193936,
					0.6290382594096968
				],
				[
					-1.2580765188193936,
					2.5161530376387304
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09415298700332642,
				0.06777752935886383,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 516325949,
			"isDeleted": false,
			"id": "qOVeWHKVNEATk9peVSzY1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 187.31127790480946,
			"y": 67.54339693460068,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.661344334687158,
			"height": 10.06461215055495,
			"seed": 563226121,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6290382594096968,
					1.887114778229062
				],
				[
					-0.6290382594096968,
					3.7742295564580957
				],
				[
					1.8871147782290336,
					5.661344334687158
				],
				[
					4.403267815867821,
					4.4032678158677925
				],
				[
					5.032306075277461,
					0
				],
				[
					3.774229556458124,
					-4.4032678158677925
				],
				[
					1.8871147782290336,
					-3.774229556458124
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04490499943494797,
				0.04880300909280777,
				0.11536355316638947,
				0.16523346304893494,
				0.1689426600933075,
				0.13071030378341675,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 2022149139,
			"isDeleted": false,
			"id": "D1U2RBM2oVzb1snRVWpFr",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 195.48877527713535,
			"y": 64.39820563755225,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.919420853506551,
			"height": 10.064612150554979,
			"seed": 1268063657,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.62903825940964,
					0
				],
				[
					-1.2580765188193368,
					0
				],
				[
					-0.62903825940964,
					-0.6290382594096968
				],
				[
					0,
					0
				],
				[
					0.6290382594096968,
					3.1451912970484273
				],
				[
					0.6290382594096968,
					8.806535631735585
				],
				[
					0.6290382594096968,
					9.435573891145282
				],
				[
					1.8871147782290905,
					3.7742295564580957
				],
				[
					3.774229556458124,
					0
				],
				[
					5.6613443346872145,
					0
				],
				[
					5.6613443346872145,
					3.1451912970484273
				],
				[
					4.403267815867821,
					8.177497372325917
				],
				[
					4.403267815867821,
					7.54845911291622
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.03673715144395828,
				0.022459685802459717,
				0.12892258167266846,
				0.20139016211032867,
				0.21928539872169495,
				0.22838979959487915,
				0.19315789639949799,
				0.12479864805936813,
				0.10250994563102722,
				0.1722765564918518,
				0.23507343232631683,
				0.06819549202919006,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1586836125,
			"isDeleted": false,
			"id": "bottu8shrshJWiRl2Qjgs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 209.32761698414845,
			"y": 54.96263174640697,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.6613443346872145,
			"height": 17.6130712634712,
			"seed": 1783540937,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6290382594096968,
					-0.6290382594096968
				],
				[
					-0.6290382594096968,
					-1.2580765188193936
				],
				[
					2.5161530376387304,
					-2.516153037638759
				],
				[
					5.032306075277518,
					-1.2580765188193936
				],
				[
					4.403267815867821,
					2.5161530376387304
				],
				[
					1.8871147782290905,
					9.435573891145282
				],
				[
					1.2580765188193936,
					15.09691822583244
				],
				[
					1.8871147782290905,
					15.09691822583244
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15817199647426605,
				0.24252799153327942,
				0.2599261999130249,
				0.23666797578334808,
				0.20409363508224487,
				0.005771880969405174,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1719833011,
			"isDeleted": false,
			"id": "liZJuc_684aXrde23onzF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 211.21473176237754,
			"y": 73.20474126928784,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2580765188193368,
			"height": 2.516153037638759,
			"seed": 1129379209,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6290382594096968
				],
				[
					-0.6290382594096968,
					2.516153037638759
				],
				[
					0.62903825940964,
					2.516153037638759
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1611579954624176,
				0.1393725872039795,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 636409597,
			"isDeleted": false,
			"id": "yVVW2cxjcmI75rQNwE_Iu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 218.8415526714769,
			"y": -110.67978670644789,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 69.18479243020437,
			"height": 94.27378309170709,
			"seed": 1949252009,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7602724442879776
				],
				[
					0,
					-1.5205448885759267
				],
				[
					2.280817332863876,
					-5.321907110015729
				],
				[
					7.602724442879605,
					-17.486266218623086
				],
				[
					20.527355995774883,
					-41.05471199154988
				],
				[
					40.2944395472619,
					-66.90397509734052
				],
				[
					60.061523098748864,
					-85.91078620453953
				],
				[
					69.18479243020437,
					-94.27378309170709
				],
				[
					68.42451998591639,
					-93.51351064741914
				],
				[
					64.62315776447662,
					-88.19160353740341
				],
				[
					64.62315776447662,
					-88.19160353740341
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10795654356479645,
				0.15857531130313873,
				0.20543332397937775,
				0.24101857841014862,
				0.2473152130842209,
				0.25639238953590393,
				0.2679623067378998,
				0.2023082822561264,
				0.043064575642347336,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 374072147,
			"isDeleted": false,
			"id": "PtYalJJAXsdMAknGznFOV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 300.19070421028863,
			"y": -217.11792890676233,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.486266218623086,
			"height": 22.047900884350838,
			"seed": 555857673,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7602724442879776,
					0
				],
				[
					6.082179554303707,
					-1.5205448885759267
				],
				[
					12.924631552895335,
					-3.0410897771518535
				],
				[
					17.486266218623086,
					-2.2808173328639043
				],
				[
					15.965721330047188,
					4.561634665727752
				],
				[
					12.164359108607357,
					15.20544888575921
				],
				[
					12.924631552895335,
					19.006811107198985
				],
				[
					13.684903997183312,
					18.246538662911036
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0718216821551323,
				0.15249581634998322,
				0.18967600166797638,
				0.19258688390254974,
				0.21307477355003357,
				0.2590659260749817,
				0.1277966946363449,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 794095453,
			"isDeleted": false,
			"id": "5gbtKrbRVKz0O-gMcWpM9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 237.8483637786759,
			"y": -78.74834404635357,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 43.335529324413756,
			"height": 4.561634665727752,
			"seed": 860368841,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					3.801362221439831,
					-0.7602724442879776
				],
				[
					20.52735599577494,
					-2.280817332863876
				],
				[
					34.97253243724617,
					-2.280817332863876
				],
				[
					43.335529324413756,
					-0.7602724442879776
				],
				[
					41.8149844358378,
					2.280817332863876
				],
				[
					41.8149844358378,
					2.280817332863876
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1748879998922348,
				0.2956780195236206,
				0.323203980922699,
				0.3009811341762543,
				0.04669598489999771,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1345978611,
			"isDeleted": false,
			"id": "FHkXng6HP7oY2KQiaxlKQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 309.3139735417442,
			"y": -87.11134093352115,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.445176441471233,
			"height": 15.20544888575921,
			"seed": 1622480585,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7602724442879776,
					0
				],
				[
					-0.7602724442879776,
					-0.7602724442879207
				],
				[
					1.5205448885758983,
					-0.7602724442879207
				],
				[
					5.3219071100156725,
					0.7602724442879776
				],
				[
					11.40408666431938,
					7.602724442879605
				],
				[
					13.684903997183255,
					10.643814220031459
				],
				[
					9.123269331455504,
					12.924631552895335
				],
				[
					5.3219071100156725,
					14.44517644147129
				],
				[
					3.801362221439774,
					13.684903997183312
				],
				[
					4.561634665727752,
					13.684903997183312
				],
				[
					5.3219071100156725,
					13.684903997183312
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09620708972215652,
				0.11992138624191284,
				0.17613129317760468,
				0.2400442212820053,
				0.2404012382030487,
				0.2707880437374115,
				0.32618504762649536,
				0.2834320068359375,
				0.07096999883651733,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1763244989,
			"isDeleted": false,
			"id": "eB7ZpwF4gyPFpeazDI6fk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 237.8483637786759,
			"y": -65.82371249345823,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 53.21907110015724,
			"height": 95.03405553599504,
			"seed": 1571176489,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7602724442879776,
					0.7602724442879776
				],
				[
					4.561634665727752,
					10.643814220031459
				],
				[
					11.404086664319436,
					34.212259992958195
				],
				[
					19.767083551486962,
					58.54097821017291
				],
				[
					31.1711702158064,
					80.5888790945238
				],
				[
					44.856074212989654,
					90.47242087026729
				],
				[
					52.45879865586926,
					94.27378309170706
				],
				[
					53.21907110015724,
					95.03405553599504
				],
				[
					53.21907110015724,
					94.27378309170706
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1906948834657669,
				0.24259567260742188,
				0.28969240188598633,
				0.3448733985424042,
				0.3966273069381714,
				0.4168531596660614,
				0.4350563883781433,
				0.41829022765159607,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 231959187,
			"isDeleted": false,
			"id": "rxfF0UAcUBhf5X8HQQ5RC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 311.59479087460807,
			"y": 23.1281634882331,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.965721330047131,
			"height": 26.609535550078647,
			"seed": 1903283145,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7602724442879776
				],
				[
					1.5205448885758983,
					3.801362221439831
				],
				[
					8.362996887167526,
					14.44517644147129
				],
				[
					12.924631552895278,
					22.808173328638816
				],
				[
					13.684903997183255,
					25.84926310579067
				],
				[
					12.164359108607357,
					26.609535550078647
				],
				[
					6.08217955430365,
					25.08899066150269
				],
				[
					1.5205448885758983,
					24.32871821721477
				],
				[
					-1.5205448885759552,
					22.808173328638816
				],
				[
					-2.280817332863876,
					22.047900884350895
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17124399542808533,
				0.21280600130558014,
				0.2436482310295105,
				0.21324422955513,
				0.21154627203941345,
				0.27670058608055115,
				0.27078697085380554,
				0.2676406502723694,
				0.05668627843260765,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 2069658653,
			"isDeleted": false,
			"id": "y_Eb4p9TFLdNxmv7QgCRa",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 332.12214687038295,
			"y": -214.0768391296105,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.602724442879605,
			"height": 29.650625327230472,
			"seed": 1273136713,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.5205448885759267
				],
				[
					-0.7602724442879207,
					8.362996887167583
				],
				[
					-0.7602724442879207,
					12.924631552895335
				],
				[
					-1.5205448885758983,
					21.28762844006289
				],
				[
					-6.842451998591628,
					29.650625327230472
				],
				[
					-7.602724442879605,
					29.650625327230472
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09030557423830032,
				0.10429559648036957,
				0.1280006766319275,
				0.034689757972955704,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1406050355,
			"isDeleted": false,
			"id": "KHSM-aeMhHlm7rdyJBtd0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 316.1564255403358,
			"y": -169.22076491662085,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.12326933145556,
			"height": 13.684903997183284,
			"seed": 280030537,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7602724442879776,
					1.5205448885759267
				],
				[
					-3.0410897771518535,
					5.321907110015729
				],
				[
					-8.362996887167583,
					12.924631552895335
				],
				[
					-9.12326933145556,
					13.684903997183284
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08938522636890411,
				0.035700805485248566,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 235991165,
			"isDeleted": false,
			"id": "j5fTECmqYs9sNoyRkXq5m",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 294.108524655985,
			"y": -147.17286403226998,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.486266218623086,
			"height": 12.164359108607357,
			"seed": 1508549257,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7602724442879776,
					0.7602724442879492
				],
				[
					-4.561634665727809,
					3.041089777151825
				],
				[
					-9.883541775743481,
					6.842451998591628
				],
				[
					-16.725993774335166,
					11.404086664319408
				],
				[
					-17.486266218623086,
					12.164359108607357
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09694463759660721,
				0.10286203026771545,
				0.012703369371592999,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 1276256723,
			"isDeleted": false,
			"id": "s3wIt6Tf30zhoPjgQqLlA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 267.49898910590633,
			"y": -131.96741514651077,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 24.328718217214714,
			"height": 23.568445772926765,
			"seed": 366839465,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.5205448885758983,
					0.7602724442879492
				],
				[
					-2.280817332863876,
					1.5205448885758983
				],
				[
					-4.561634665727752,
					3.8013622214398026
				],
				[
					-12.164359108607357,
					9.883541775743481
				],
				[
					-23.568445772926736,
					22.808173328638787
				],
				[
					-24.328718217214714,
					23.568445772926765
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.03580697625875473,
				0.09088031202554703,
				0.0935826450586319,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1324865757,
			"isDeleted": false,
			"id": "JkxyOnqDo1kV8bEiT4Bsm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 241.64972600011572,
			"y": -95.4743378206887,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.883541775743481,
			"height": 12.924631552895363,
			"seed": 1230867881,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-3.0410897771518535,
					3.8013622214398026
				],
				[
					-7.602724442879605,
					9.123269331455532
				],
				[
					-9.883541775743481,
					12.164359108607385
				],
				[
					-9.883541775743481,
					12.924631552895363
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06647329777479172,
				0.021240264177322388,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 531918707,
			"isDeleted": false,
			"id": "oVxksIESZZCnJgB2Q-ZNs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 208.19773845144545,
			"y": -52.8990809405629,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.20544888575921,
			"height": 41.05471199154982,
			"seed": 813398761,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-3.801362221439831,
					5.321907110015729
				],
				[
					-9.123269331455504,
					16.72599377433511
				],
				[
					-13.684903997183312,
					31.17117021580634
				],
				[
					-15.20544888575921,
					39.534167102973925
				],
				[
					-15.20544888575921,
					41.05471199154982
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.042769044637680054,
				0.06258245557546616,
				0.0937185063958168,
				0.04302743449807167,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 933410109,
			"isDeleted": false,
			"id": "kukNovG3bWR3LETGQfusP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 328.3207846489432,
			"y": -65.82371249345823,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.0410897771518535,
			"height": 19.006811107198985,
			"seed": 1422363401,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7602724442879776,
					0
				],
				[
					-1.5205448885758983,
					0.7602724442879776
				],
				[
					-1.5205448885758983,
					4.561634665727752
				],
				[
					-1.5205448885758983,
					11.40408666431938
				],
				[
					-2.280817332863876,
					18.246538662911064
				],
				[
					-3.0410897771518535,
					19.006811107198985
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08722598105669022,
				0.10505600273609161,
				0.18055398762226105,
				0.16433560848236084,
				0.03030700609087944,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 284952851,
			"isDeleted": false,
			"id": "of1s2uCLpJB-h0ZmmDm0r",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 312.355063318896,
			"y": -38.453904499091664,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.643814220031402,
			"height": 12.164359108607357,
			"seed": 347419145,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-2.280817332863876,
					1.5205448885758983
				],
				[
					-3.0410897771517966,
					2.280817332863876
				],
				[
					-6.08217955430365,
					5.321907110015729
				],
				[
					-10.643814220031402,
					11.40408666431938
				],
				[
					-10.643814220031402,
					12.164359108607357
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07504797726869583,
				0.1260959804058075,
				0.1801680028438568,
				0.06228909268975258,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 326305181,
			"isDeleted": false,
			"id": "6EpDp14eKvRsn4NwpZDs8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 297.1496144331368,
			"y": -20.2073658361806,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.445176441471233,
			"height": 14.445176441471233,
			"seed": 411862569,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7602724442879207,
					0.7602724442879207
				],
				[
					-1.5205448885758983,
					1.5205448885758983
				],
				[
					-3.0410897771517966,
					3.0410897771517966
				],
				[
					-13.684903997183255,
					13.684903997183255
				],
				[
					-14.445176441471233,
					14.445176441471233
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10062798857688904,
				0.13378798961639404,
				0.010677002370357513,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1432317619,
			"isDeleted": false,
			"id": "Ds56k8CkoULIV-MLVSuNx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 263.69762688446656,
			"y": 5.641897269610013,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.8424519985916845,
			"height": 0.7602724442879776,
			"seed": 2144452169,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-3.0410897771518535,
					0.7602724442879776
				],
				[
					-4.561634665727752,
					0.7602724442879776
				],
				[
					-5.321907110015729,
					0
				],
				[
					-6.082179554303707,
					0
				],
				[
					-6.8424519985916845,
					0.7602724442879776
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09642098844051361,
				0.13751401007175446,
				0.1517167091369629,
				0.06268832087516785,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1167739389,
			"isDeleted": false,
			"id": "LyBBMsj9fEHKMGWuGC5tb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 228.72509444722039,
			"y": 21.6076185996572,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.12326933145556,
			"height": 11.40408666431938,
			"seed": 1875729001,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-6.8424519985916845,
					5.321907110015729
				],
				[
					-9.12326933145556,
					11.40408666431938
				],
				[
					-9.12326933145556,
					11.40408666431938
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.03733593598008156,
				0.0063232420943677425,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 797253715,
			"isDeleted": false,
			"id": "a7lSlHn1xwXBivW4MnND9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 324.51942242750334,
			"y": 63.422603035495,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.924631552895278,
			"height": 12.924631552895335,
			"seed": 934983881,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7602724442879207,
					-0.7602724442879207
				],
				[
					-0.7602724442879207,
					-1.5205448885758983
				],
				[
					-1.5205448885758983,
					-1.5205448885758983
				],
				[
					-2.280817332863876,
					-0.7602724442879207
				],
				[
					-6.08217955430365,
					3.801362221439831
				],
				[
					-11.40408666431938,
					10.643814220031459
				],
				[
					-12.924631552895278,
					11.404086664319436
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10929940640926361,
				0.16550198197364807,
				0.19675998389720917,
				0.16752807796001434,
				0.011805419810116291,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1327104605,
			"isDeleted": false,
			"id": "v6hLErz_vuZSTArx2qB9M",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 284.9852553245294,
			"y": 74.06641725552646,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.684903997183255,
			"height": 5.321907110015729,
			"seed": 1507442345,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7602724442879207,
					-0.7602724442879776
				],
				[
					-2.280817332863876,
					-3.0410897771518535
				],
				[
					-5.321907110015729,
					-4.561634665727752
				],
				[
					-12.164359108607357,
					-5.321907110015729
				],
				[
					-13.684903997183255,
					-5.321907110015729
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16199199855327606,
				0.1772085577249527,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1229168115,
			"isDeleted": false,
			"id": "I-Pl0nK7WgYSTmk26klUq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 265.21817177304246,
			"y": 69.50478258979871,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.561634665727752,
			"height": 0.7602724442879776,
			"seed": 1061914313,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.5205448885758983,
					0
				],
				[
					-2.280817332863876,
					0
				],
				[
					-4.561634665727752,
					-0.7602724442879776
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06041247397661209,
				0.04982971027493477,
				0.03680059686303139,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 348368573,
			"isDeleted": false,
			"id": "JIPpRPvvrjzOPyaCUxHSp",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 247.73190555441937,
			"y": 73.30614481123848,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.280817332863876,
			"height": 0.7602724442879776,
			"seed": 1211478761,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.5205448885758983,
					0.7602724442879776
				],
				[
					-2.280817332863876,
					0.7602724442879776
				],
				[
					0,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09256799519062042,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1302423443,
			"isDeleted": false,
			"id": "YKPL07E3j-aGpAsKsOj1-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 155.93490939328956,
			"y": 85.26073600189625,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.186423725764826,
			"height": 32.35368532880324,
			"seed": 885436457,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6602792924245477,
					0
				],
				[
					-2.641117169698248,
					1.3205585848490955
				],
				[
					-13.205585848491125,
					20.468658065161208
				],
				[
					-13.205585848491125,
					22.449495942434908
				],
				[
					-13.865865140915673,
					24.43033381970855
				],
				[
					-14.526144433340221,
					25.750892404557646
				],
				[
					-14.526144433340221,
					28.392009574255894
				],
				[
					-15.186423725764826,
					29.71256815910499
				],
				[
					-15.186423725764826,
					31.033126743954085
				],
				[
					-15.186423725764826,
					32.35368532880324
				],
				[
					-15.186423725764826,
					32.35368532880324
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1727210134267807,
				0.31394803524017334,
				0.5328179597854614,
				0.5514453053474426,
				0.5555030703544617,
				0.5530749559402466,
				0.5273321270942688,
				0.5109687447547913,
				0.5040608644485474,
				0.46394336223602295,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1698221853,
			"isDeleted": false,
			"id": "3-US4KtbPSjLZygCuqtZM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 132.8251341584301,
			"y": 121.57609708524683,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.205585848491125,
			"height": 11.224747971217425,
			"seed": 1796251017,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1708964692886,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6602792924246046,
					0
				],
				[
				],