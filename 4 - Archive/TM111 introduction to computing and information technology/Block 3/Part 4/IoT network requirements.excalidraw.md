---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
When discussing about iot devices we need to distinguish between tethered, therefore
using a cable and unthethered therefore using wireless communication. ^1tUUlMUf

Since most devices in iot require to use a wireless communication
we need to ask which type of network should be used.
While WiFi might seem like a good options connecting to a
customer router has many problems, first it the user change the password 
it needs to be updated in all the devices, second if the user turn off the WiFi
something like a smart meter would stop working, and last,y some
devices like again a smart meter might be located in hard to reach places
where signal is too weak. Last but not least the customer might not be happy to have
such responsibility in his pockets having to pay for the connection. Although at first glance
WiFi might seem like an unusable options, in IOT there are many applications and use cases
so it is worth noting that some IOT devices use WiFi to communicate ^ZYdBG4ok

The best candidate for IOT application in terms of network is the cellular network
since it has most of the previous problems fixed ( password, reach-ability, security) but it has 2
major problems. The first is that it is designed for long lived connection and moving users which
is the exact opposite of most IOT use cases ( although for some IOT application the cellular
network is a good fit and is used as is) and the second is that it is extremely expensive.
First mobile operators have to pay for the license spectrum, second they have to pay high
OPEX cost so the cost of electricity and running the infrastructure, plus they have to pay
also very high CAPEX costs. CAPEX are the one time costs of buying and installing the equipment,
in urban areas most of the cost is in installing all the cells that are required which are a lot, while
in more rural areas you need to install way less towers but you have to build the Back-haul infrastructure
to deliver communication and power. As we saw the wireless infrastructure very rarely lives for long,
it is almost always deployed only at the end of the network, the rest remain always threatened
for performance and security ^TnNeEfQu




As we saw in the previous parts iot present some new challenges that creates problems for the conventional 
networks we use today. First it the message size which is very small and very inefficient for networks made for 
cellular users. Additionally these type of networks use a process called dynamic allocation to try and give 
higher data rates only to the users that are using the network in the very moment, this is because usually 
users using the network continue doing so until they are finished and than stop. This is opposite to iot where 
it is very frequent to have short lived connections that continuously turn on and off so dynamic allocation is much more difficult.
The second problem is power in the sense of battery life, many iot devices operate on a battery and therefore it is crucial that
 they remain as efficient as possible to avoid draining the battery too fast ( a good life cycle for the battery of a iot devices is
 considered to be 10 years). The reason they use a battery is that they often are in hard to reach places, this introduces 
the next problem that is range, some iot applications need to cover vert wide ranges like a whole city or nation and some application 
are undergrad and require very high penetration. This very high range can be achieved by installing more towers but this come with its 
problem that is the next one. Iot devices need to be cheap, first because there is the need for so many of them and also because
 after they’d are very susceptible to natural disaster s and theft so it is important that they are not expensive to replace, a good 
target is to have devices costing 1 dollar but usually the range is more in the 10 to 15
 ^uv2InTYV


All the problems mentioned for iot networks lead to the development of a new type of 
network called Low Power Wide Area Network. This type of network exists in 2 forms, 
licensed and unlicensed. Unlicensed is very cheap and simple to operate, usually has very 
low data rates in the 100bps but also has a very good range and penetration 
thanks to this. The gateways usually have only an Ethernet port that is enough 
for both power and connection, they encrypt packets at source but have no other 
security measures and of course use the unlicensed spectrum. Licensed LPWANs use 
the cellular network to communicate and there fore comes with their benefits of 
performance and security but at the cost often of range and prices. They actually 
operate on very narrow band channels that remain unused by the regular cellular 
network, they exist in the form of LTE-M which uses small 4G channels and support 
idle mode and NB-IoT which uses 200KHz gaps between the 3G and 4G frequencies and on,y allow for up-link ^0pD6IT9O

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
			"version": 68,
			"versionNonce": 1171446030,
			"isDeleted": false,
			"id": "oATbz_d8m0n8C1pg3dM0C",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -155.10646027554196,
			"y": -14.178021722242136,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 28.858328936965393,
			"height": 45.565782532050605,
			"seed": 383063296,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.759429708867458,
					-0.7594297088675148
				],
				[
					4.556578253205032,
					-12.150875341880123
				],
				[
					9.113156506410121,
					-31.896047772435395
				],
				[
					9.872586215277636,
					-37.971485443375514
				],
				[
					9.872586215277636,
					-35.69319631677297
				],
				[
					9.872586215277636,
					-22.02346155715776
				],
				[
					14.429164468482668,
					-5.316007962072547
				],
				[
					19.74517243055527,
					0.7594297088675148
				],
				[
					23.54232097489279,
					-3.0377188354700024
				],
				[
					25.820610101495333,
					-15.188594177350183
				],
				[
					27.339469519230363,
					-30.377188354700422
				],
				[
					28.858328936965393,
					-42.528063696580574
				],
				[
					28.858328936965393,
					-44.80635282318309
				],
				[
					28.098899228097878,
					-41.009204278845544
				],
				[
					28.098899228097878,
					-40.24977456997803
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1505739986896515,
				0.1941295713186264,
				0.18422265350818634,
				0.15825891494750977,
				0.13970312476158142,
				0.1429663449525833,
				0.15815137326717377,
				0.1762249767780304,
				0.2145019769668579,
				0.22037853300571442,
				0.23563790321350098,
				0.20077770948410034,
				0.11611184477806091,
				0.0014579773414880037,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 62,
			"versionNonce": 1479378642,
			"isDeleted": false,
			"id": "kCO_ItGrcNAllB3qucQyT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -123.96984221197408,
			"y": -21.012889102049712,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.113156506410121,
			"height": 12.150875341880123,
			"seed": 660632832,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.2782891266025445,
					-1.5188594177350296
				],
				[
					4.556578253205089,
					-4.556578253205032
				],
				[
					4.556578253205089,
					-6.075437670940062
				],
				[
					1.5188594177350296,
					-5.316007962072547
				],
				[
					0,
					-0.7594297088675148
				],
				[
					0,
					3.797148544337574
				],
				[
					3.797148544337574,
					6.075437670940062
				],
				[
					8.353726797542663,
					1.5188594177350296
				],
				[
					9.113156506410121,
					0.7594297088675148
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15399767458438873,
				0.16054031252861023,
				0.12081866711378098,
				0.09523068368434906,
				0.1042800322175026,
				0.1536790430545807,
				0.14976879954338074,
				0.00913308747112751,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 812681038,
			"isDeleted": false,
			"id": "-M54QOs8v33gFtHp1R3HK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -111.05953716122639,
			"y": -41.5174912414725,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.2782891266025445,
			"height": 25.061180392627875,
			"seed": 422810880,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					3.0377188354700593
				],
				[
					1.5188594177350296,
					13.66973475961521
				],
				[
					2.2782891266025445,
					24.30175068376036
				],
				[
					0.7594297088675148,
					25.061180392627875
				],
				[
					0.7594297088675148,
					24.30175068376036
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14791201055049896,
				0.19701483845710754,
				0.21897387504577637,
				0.020893463864922523,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 842587282,
			"isDeleted": false,
			"id": "QA7pByEPSWiQzyNHzzK3Q",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -117.13497483216645,
			"y": -27.84775648185729,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.391445633012665,
			"height": 1.5188594177350296,
			"seed": 1476211968,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					3.0377188354700024,
					0.7594297088675148
				],
				[
					10.63201592414515,
					1.5188594177350296
				],
				[
					11.391445633012665,
					0.7594297088675148
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1911659836769104,
				0.10264434665441513,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 66,
			"versionNonce": 1337879950,
			"isDeleted": false,
			"id": "vJuXqCQyo0tUG-dGmeDl4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -102.70581036368378,
			"y": -24.05060793751977,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.63201592414515,
			"height": 9.872586215277636,
			"seed": 1243354368,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.5188594177350296
				],
				[
					0.7594297088675148,
					6.834867379807633
				],
				[
					3.0377188354700593,
					8.353726797542663
				],
				[
					5.316007962072604,
					4.556578253205089
				],
				[
					5.316007962072604,
					0
				],
				[
					5.316007962072604,
					0.7594297088675148
				],
				[
					4.556578253205089,
					5.316007962072604
				],
				[
					6.0754376709401186,
					8.353726797542663
				],
				[
					9.113156506410121,
					6.834867379807633
				],
				[
					10.63201592414515,
					1.5188594177350296
				],
				[
					10.63201592414515,
					-1.5188594177349728
				],
				[
					9.872586215277636,
					-0.7594297088675148
				],
				[
					9.872586215277636,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12690316140651703,
				0.17459967732429504,
				0.16599582135677338,
				0.12319927662611008,
				0.07795547693967819,
				0.07587393373250961,
				0.10073211789131165,
				0.13068881630897522,
				0.14064188301563263,
				0.1545458436012268,
				0.13617543876171112,
				0.010390838608145714,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 64,
			"versionNonce": 1674803794,
			"isDeleted": false,
			"id": "zlQZre2IpzQ9McAPu8Rxm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -89.03607560406857,
			"y": -23.291178228652257,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.594297088675091,
			"height": 9.872586215277636,
			"seed": 1387312384,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7594297088675148,
					0.7594297088675148
				],
				[
					-0.7594297088675148,
					1.5188594177350296
				],
				[
					-1.5188594177350296,
					4.556578253205089
				],
				[
					0.7594297088675148,
					6.0754376709401186
				],
				[
					4.556578253205032,
					3.797148544337574
				],
				[
					6.075437670940062,
					-0.7594297088675148
				],
				[
					3.0377188354700593,
					-3.7971485443375173
				],
				[
					-0.7594297088675148,
					-3.0377188354700024
				],
				[
					-1.5188594177350296,
					3.0377188354700593
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
				0.07172000408172607,
				0.08425500243902206,
				0.1475440114736557,
				0.15875858068466187,
				0.1553685963153839,
				0.14841485023498535,
				0.13151638209819794,
				0.11201059073209763,
				0.01671295240521431,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 284527566,
			"isDeleted": false,
			"id": "1-IPoEQ9a0NBf-Q0U2aW2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -83.72006764199602,
			"y": -25.569467355254744,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.0754376709401186,
			"height": 7.594297088675091,
			"seed": 200971520,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.759429708867458
				],
				[
					1.5188594177350296,
					3.7971485443375173
				],
				[
					2.2782891266025445,
					6.8348673798075765
				],
				[
					6.0754376709401186,
					-0.7594297088675148
				],
				[
					6.0754376709401186,
					-0.7594297088675148
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13586090505123138,
				0.1448391079902649,
				0.13958212733268738,
				0.0868784487247467,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 65,
			"versionNonce": 1272209426,
			"isDeleted": false,
			"id": "MTZ9J0JCF2fNCx2wDXbjt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -74.6069111355859,
			"y": -38.47977240600244,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.63201592414515,
			"height": 22.023461557157816,
			"seed": 10761472,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7594297088675148
				],
				[
					0.7594297088675148,
					3.7971485443375173
				],
				[
					1.5188594177350296,
					12.910305050747695
				],
				[
					2.2782891266025445,
					19.74517243055527
				],
				[
					2.2782891266025445,
					21.2640318482903
				],
				[
					2.2782891266025445,
					18.985742721687757
				],
				[
					5.316007962072604,
					13.669734759615153
				],
				[
					8.353726797542663,
					9.872586215277636
				],
				[
					9.872586215277636,
					10.63201592414515
				],
				[
					10.63201592414515,
					13.669734759615153
				],
				[
					9.872586215277636,
					15.188594177350183
				],
				[
					9.113156506410121,
					15.188594177350183
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.18239380419254303,
				0.18631750345230103,
				0.20270200073719025,
				0.177568718791008,
				0.14051461219787598,
				0.14580975472927094,
				0.15177154541015625,
				0.1259663701057434,
				0.07521432638168335,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1378804238,
			"isDeleted": false,
			"id": "77CRX6Kz8s8kQn2lDUWoT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -70.80976259124833,
			"y": -22.531748519784742,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.797148544337574,
			"height": 6.0754376709401186,
			"seed": 263419136,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7594297088675148
				],
				[
					0,
					2.2782891266025445
				],
				[
					0.7594297088675148,
					3.0377188354700593
				],
				[
					3.797148544337574,
					6.0754376709401186
				],
				[
					3.797148544337574,
					6.0754376709401186
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1366419941186905,
				0.1962980031967163,
				0.08809558302164078,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 62,
			"versionNonce": 1446153682,
			"isDeleted": false,
			"id": "DZjtsVRiAIPdN9NmZKcRC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -59.418316958235664,
			"y": -24.05060793751977,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.0754376709401186,
			"height": 9.113156506410178,
			"seed": 1998132480,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7594297088675148,
					-0.7594297088675148
				],
				[
					-1.5188594177350296,
					-0.7594297088675148
				],
				[
					-3.797148544337574,
					0.7594297088675148
				],
				[
					-3.0377188354700593,
					3.0377188354700593
				],
				[
					0.7594297088675148,
					5.316007962072604
				],
				[
					2.2782891266025445,
					7.594297088675148
				],
				[
					0.7594297088675148,
					8.353726797542663
				],
				[
					-3.797148544337574,
					8.353726797542663
				],
				[
					-3.797148544337574,
					8.353726797542663
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05061199888586998,
				0.09178683161735535,
				0.11519324034452438,
				0.1081208810210228,
				0.11941543221473694,
				0.16037127375602722,
				0.22972942888736725,
				0.07492285221815109,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1180921934,
			"isDeleted": false,
			"id": "rKPfhB1A-1hdVrAm6mZK-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -145.23387406026433,
			"y": 4.048291290578163,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.759429708867458,
			"height": 6.8348673798075765,
			"seed": 26227968,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.759429708867458
				],
				[
					0,
					2.2782891266024876
				],
				[
					0.759429708867458,
					6.075437670940062
				],
				[
					0.759429708867458,
					6.8348673798075765
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1269233375787735,
				0.17390377819538116,
				0.02013418637216091,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1476723602,
			"isDeleted": false,
			"id": "X4HsFQaGzlp2OCCSmew7Q",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -145.23387406026433,
			"y": -2.78657608922947,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7594297088675148,
			"height": 0.7594297088675148,
			"seed": 1462007040,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7594297088675148
				],
				[
					-0.7594297088675148,
					-0.7594297088675148
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
				0.022383209317922592,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 62,
			"versionNonce": 1500264078,
			"isDeleted": false,
			"id": "GlGWcKaibx58goVhEyw12",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -141.4367255159268,
			"y": 4.048291290578163,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.594297088675091,
			"height": 7.594297088675091,
			"seed": 8959232,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7594297088675148,
					0.759429708867458
				],
				[
					0.7594297088675148,
					3.0377188354700024
				],
				[
					1.5188594177350296,
					4.556578253205032
				],
				[
					2.2782891266025445,
					3.0377188354700024
				],
				[
					4.556578253205089,
					-0.7594297088675148
				],
				[
					6.0754376709401186,
					-1.5188594177350296
				],
				[
					7.594297088675091,
					2.2782891266024876
				],
				[
					7.594297088675091,
					5.316007962072547
				],
				[
					6.8348673798075765,
					6.075437670940062
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09308599680662155,
				0.12616953253746033,
				0.11680416762828827,
				0.06665048003196716,
				0.07551577687263489,
				0.14284011721611023,
				0.17240366339683533,
				0.0964900478720665,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 1803731282,
			"isDeleted": false,
			"id": "4E58Ts7feMIoMnD3OeTyo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -109.54067774349136,
			"y": -1.2677166714944406,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.5188594177350296,
			"height": 22.78289126602533,
			"seed": 67360000,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7594297088675148
				],
				[
					0,
					0
				],
				[
					0.7594297088675148,
					6.8348673798075765
				],
				[
					1.5188594177350296,
					19.74517243055527
				],
				[
					1.5188594177350296,
					22.023461557157816
				],
				[
					0,
					15.18859417735024
				],
				[
					0,
					14.429164468482725
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14961999654769897,
				0.20730999112129211,
				0.23554165661334991,
				0.1682656854391098,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 335688910,
			"isDeleted": false,
			"id": "SNEdMeY9qe9Fc9uDMZAps",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -117.89440454103396,
			"y": -4.3054355069645,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 20.504602139422786,
			"height": 3.797148544337574,
			"seed": 1383871744,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405043,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7594297088675148,
					0
				],
				[
					2.2782891266025445,
					0
				],
				[
					11.391445633012665,
					-0.7594297088675148
				],
				[
					18.226313012820242,
					-0.7594297088675148
				],
				[
					19.74517243055527,
					2.2782891266025445
				],
				[
					18.985742721687757,
					3.0377188354700593
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09421399235725403,
				0.19573599100112915,
				0.26220402121543884,
				0.21631503105163574,
				0.02845107950270176,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1275250450,
			"isDeleted": false,
			"id": "4OupEKifV4hhlMX12lkK7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -116.37554512329893,
			"y": 19.236885467928346,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.466883303952727,
			"height": 0.7594297088675148,
			"seed": 456602880,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7594297088675148,
					0
				],
				[
					3.0377188354700024,
					0
				],
				[
					9.872586215277636,
					-0.7594297088675148
				],
				[
					17.466883303952727,
					-0.7594297088675148
				],
				[
					17.466883303952727,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10343600809574127,
				0.2158059924840927,
				0.281358003616333,
				0.11369051784276962,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 64,
			"versionNonce": 2143185678,
			"isDeleted": false,
			"id": "ZnHVeXm69CnmJOxNWmc7j",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -89.03607560406857,
			"y": 13.920877505855799,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.353726797542606,
			"height": 9.113156506410121,
			"seed": 273995008,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7594297088675148,
					0
				],
				[
					-1.5188594177350296,
					2.2782891266024876
				],
				[
					-0.7594297088675148,
					6.075437670940062
				],
				[
					3.0377188354700593,
					6.8348673798075765
				],
				[
					6.075437670940062,
					3.7971485443375173
				],
				[
					5.316007962072547,
					-1.5188594177350296
				],
				[
					0.7594297088675148,
					-2.2782891266025445
				],
				[
					-2.2782891266025445,
					1.5188594177349728
				],
				[
					-2.2782891266025445,
					4.556578253205032
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
				0.08061499148607254,
				0.1292492002248764,
				0.152286097407341,
				0.1579892337322235,
				0.13025490939617157,
				0.10091308504343033,
				0.1264311820268631,
				0.1172313243150711,
				0.03865371644496918,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 838603986,
			"isDeleted": false,
			"id": "0exvIDJlGpOr3DCmFPC4x",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -76.88520026218839,
			"y": 4.048291290578163,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.0377188354700024,
			"height": 14.429164468482668,
			"seed": 1961538816,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.759429708867458
				],
				[
					0.7594297088675148,
					6.8348673798075765
				],
				[
					2.2782891266024876,
					14.429164468482668
				],
				[
					3.0377188354700024,
					12.910305050747638
				],
				[
					3.0377188354700024,
					12.150875341880123
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10215600579977036,
				0.1822117567062378,
				0.17016074061393738,
				0.015715239569544792,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 186243406,
			"isDeleted": false,
			"id": "ymxvBnaKk4jjaB_7eWVFV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -86.75778647746603,
			"y": 0.2511427462405891,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.985742721687757,
			"height": 0.7594297088675148,
			"seed": 2130203904,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					5.316007962072547,
					0
				],
				[
					14.429164468482668,
					0
				],
				[
					18.985742721687757,
					0
				],
				[
					18.985742721687757,
					0.7594297088675148
				],
				[
					17.466883303952727,
					0.7594297088675148
				],
				[
					17.466883303952727,
					0.7594297088675148
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.18524199724197388,
				0.24458050727844238,
				0.24488238990306854,
				0.2032810002565384,
				0.07903451472520828,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 66,
			"versionNonce": 788900498,
			"isDeleted": false,
			"id": "x-R8Q5l0x565X5HWZldQo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 49.38516574303935,
			"y": -180.40211858434887,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.106742750964258,
			"height": 21.116418876553524,
			"seed": 402430720,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7281523750535825,
					0.7281523750535825
				],
				[
					-0.7281523750535825,
					1.4563047501071367
				],
				[
					2.184457125160691,
					8.009676125589266
				],
				[
					5.097066625374964,
					16.747504626232086
				],
				[
					5.097066625374964,
					18.931961751392805
				],
				[
					3.640761875267856,
					18.931961751392805
				],
				[
					0.7281523750535825,
					16.747504626232086
				],
				[
					-0.7281523750535825,
					11.650438000857122
				],
				[
					-0.7281523750535825,
					5.0970666253749926
				],
				[
					2.9126095002142733,
					-0.7281523750535541
				],
				[
					6.553371375482129,
					-2.184457125160719
				],
				[
					9.465980875696403,
					-0.7281523750535541
				],
				[
					11.650438000857093,
					2.184457125160719
				],
				[
					12.378590375910676,
					5.825219000428547
				],
				[
					10.194133250749985,
					8.009676125589266
				],
				[
					6.553371375482129,
					8.009676125589266
				],
				[
					4.368914250321438,
					6.553371375482129
				],
				[
					4.368914250321438,
					5.825219000428547
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06213952600955963,
				0.13396911323070526,
				0.1751701682806015,
				0.20446841418743134,
				0.2068323940038681,
				0.18253003060817719,
				0.14591500163078308,
				0.13123752176761627,
				0.13647988438606262,
				0.16790692508220673,
				0.1954645961523056,
				0.23767437040805817,
				0.2661236524581909,
				0.28191110491752625,
				0.26211971044540405,
				0.21341943740844727,
				0.024844970554113388,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1835892622,
			"isDeleted": false,
			"id": "C4qBLZ_7pK1mKINqIh7ds",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 61.76375611895003,
			"y": -178.94581383424173,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.097066625375021,
			"height": 8.009676125589266,
			"seed": 1681988352,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7281523750535541
				],
				[
					0.7281523750535825,
					0.7281523750535825
				],
				[
					2.184457125160691,
					5.0970666253749926
				],
				[
					2.184457125160691,
					6.553371375482129
				],
				[
					2.184457125160691,
					3.640761875267856
				],
				[
					2.9126095002142733,
					0
				],
				[
					5.097066625375021,
					-1.4563047501071367
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
				0.08233200013637543,
				0.17017193138599396,
				0.1821066290140152,
				0.1572960764169693,
				0.10693737864494324,
				0.11135992407798767,
				0.051405854523181915,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 165054546,
			"isDeleted": false,
			"id": "Ur0TKuXILAOXHXx2FAp54",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 69.77343224453932,
			"y": -178.21766145918815,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.465980875696403,
			"height": 10.194133250749985,
			"seed": 210238208,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4563047501071082,
					0
				],
				[
					3.640761875267799,
					-0.7281523750535825
				],
				[
					5.097066625374964,
					-2.184457125160719
				],
				[
					4.368914250321382,
					-3.640761875267856
				],
				[
					1.4563047501071082,
					-2.9126095002142733
				],
				[
					-0.7281523750535825,
					0
				],
				[
					-1.456304750107165,
					4.36891425032141
				],
				[
					0.7281523750535257,
					6.553371375482129
				],
				[
					5.097066625374964,
					6.553371375482129
				],
				[
					7.281523750535655,
					4.36891425032141
				],
				[
					8.009676125589237,
					3.6407618752678275
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14781777560710907,
				0.18598541617393494,
				0.17153261601924896,
				0.16121618449687958,
				0.15972445905208588,
				0.191425621509552,
				0.2623235583305359,
				0.3139150142669678,
				0.26776123046875,
				0.06502395868301392,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 65,
			"versionNonce": 183655886,
			"isDeleted": false,
			"id": "ZzP57qae7AiEG3FTWw2LP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 77.78310837012856,
			"y": -179.6739662092953,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.106742750964258,
			"height": 11.650438000857122,
			"seed": 1344281344,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7281523750535825,
					-0.7281523750535825
				],
				[
					0.7281523750535825,
					1.4563047501071367
				],
				[
					2.184457125160691,
					6.553371375482101
				],
				[
					2.9126095002142733,
					8.009676125589266
				],
				[
					2.9126095002142733,
					4.36891425032141
				],
				[
					2.9126095002142733,
					0.7281523750535541
				],
				[
					4.368914250321438,
					0
				],
				[
					5.097066625374964,
					4.36891425032141
				],
				[
					5.097066625374964,
					6.553371375482101
				],
				[
					5.825219000428547,
					4.36891425032141
				],
				[
					8.009676125589294,
					0
				],
				[
					10.194133250749985,
					-2.184457125160719
				],
				[
					11.650438000857093,
					-1.4563047501071367
				],
				[
					12.378590375910676,
					4.36891425032141
				],
				[
					11.650438000857093,
					8.73782850064282
				],
				[
					10.922285625803568,
					9.465980875696403
				],
				[
					10.922285625803568,
					8.73782850064282
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06834619492292404,
				0.20750723779201508,
				0.2212095707654953,
				0.187120720744133,
				0.10393218696117401,
				0.07526224106550217,
				0.14344950020313263,
				0.2065921276807785,
				0.20180730521678925,
				0.12577225267887115,
				0.0955640897154808,
				0.13949666917324066,
				0.24014821648597717,
				0.31140637397766113,
				0.3116148114204407,
				0.06525304913520813,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 440774162,
			"isDeleted": false,
			"id": "mHkxftE7sEmqrnQ3ccUoG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 93.07430824625351,
			"y": -178.21766145918815,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.203809376339223,
			"height": 11.650438000857122,
			"seed": 1591474944,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7281523750535825,
					0
				],
				[
					2.1844571251607476,
					-1.4563047501071367
				],
				[
					4.368914250321438,
					-2.9126095002142733
				],
				[
					4.368914250321438,
					-3.640761875267856
				],
				[
					0.7281523750535825,
					-2.184457125160719
				],
				[
					-1.4563047501071082,
					1.4563047501071367
				],
				[
					-1.4563047501071082,
					4.36891425032141
				],
				[
					1.456304750107165,
					5.097066625374964
				],
				[
					5.825219000428547,
					3.6407618752678275
				],
				[
					8.009676125589294,
					0
				],
				[
					8.009676125589294,
					-3.640761875267856
				],
				[
					7.281523750535712,
					-4.368914250321438
				],
				[
					7.281523750535712,
					-2.184457125160719
				],
				[
					8.73782850064282,
					1.4563047501071367
				],
				[
					10.194133250749985,
					5.825219000428547
				],
				[
					10.922285625803568,
					7.281523750535683
				],
				[
					10.922285625803568,
					5.825219000428547
				],
				[
					11.65043800085715,
					1.4563047501071367
				],
				[
					13.834895126017841,
					-0.7281523750535825
				],
				[
					16.019352251178532,
					0
				],
				[
					16.747504626232114,
					3.6407618752678275
				],
				[
					16.747504626232114,
					5.825219000428547
				],
				[
					16.747504626232114,
					5.825219000428547
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1672540009021759,
				0.20142588019371033,
				0.19084051251411438,
				0.15440738201141357,
				0.15761636197566986,
				0.19548465311527252,
				0.21646243333816528,
				0.22553008794784546,
				0.18032650649547577,
				0.13747058808803558,
				0.1494843065738678,
				0.1748984307050705,
				0.19523093104362488,
				0.2543308436870575,
				0.2627410888671875,
				0.2021416872739792,
				0.1290648877620697,
				0.18195180594921112,
				0.2741132080554962,
				0.29737934470176697,
				0.07656265050172806,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1489073166,
			"isDeleted": false,
			"id": "3sLsjsv-E0JJJlE7M5wf8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 109.82181287248562,
			"y": -186.955489959831,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.456304750107165,
			"height": 0,
			"seed": 1896061696,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7281523750535825,
					0
				],
				[
					-1.456304750107165,
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
				0.1607470065355301,
				0.061307527124881744,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 625613778,
			"isDeleted": false,
			"id": "UMT455CFnNlEFIfg2hQrJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 114.91887949786064,
			"y": -180.40211858434887,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.737828500642877,
			"height": 10.194133250749985,
			"seed": 777214720,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7281523750535825,
					0
				],
				[
					-1.456304750107165,
					0
				],
				[
					-2.1844571251607476,
					1.4563047501071367
				],
				[
					1.4563047501070514,
					4.36891425032141
				],
				[
					5.825219000428547,
					7.281523750535683
				],
				[
					5.825219000428547,
					9.465980875696403
				],
				[
					1.4563047501070514,
					10.194133250749985
				],
				[
					-2.1844571251607476,
					8.009676125589266
				],
				[
					-2.91260950021433,
					7.281523750535683
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0634353905916214,
				0.1424766182899475,
				0.1369646042585373,
				0.14657443761825562,
				0.1822594255208969,
				0.2518576383590698,
				0.27303895354270935,
				0.04903173819184303,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 1087619662,
			"isDeleted": false,
			"id": "r9jxqi7mwwPGzkFIjYRvA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 147.28134212930513,
			"y": -222.9236429697991,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.560470296077483,
			"height": 23.760674772632882,
			"seed": 243415808,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7200204476555427,
					0
				],
				[
					-0.7200204476555427,
					0.7200204476555427
				],
				[
					-1.4400408953110855,
					7.200204476555399
				],
				[
					0,
					13.680388505455284
				],
				[
					3.6001022382777137,
					16.560470296077455
				],
				[
					6.480184028899885,
					14.400408953110826
				],
				[
					10.080286267177598,
					9.360265819522027
				],
				[
					13.680388505455312,
					2.160061342966628
				],
				[
					15.120429400766398,
					-5.040143133588799
				],
				[
					15.120429400766398,
					-7.200204476555427
				],
				[
					13.680388505455312,
					-5.760163581244342
				],
				[
					12.96036805779977,
					-5.040143133588799
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07071039080619812,
				0.157745823264122,
				0.19178909063339233,
				0.20690207183361053,
				0.20164550840854645,
				0.18876345455646515,
				0.19726452231407166,
				0.18779000639915466,
				0.16185128688812256,
				0.15869006514549255,
				0.05522000044584274,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 955961746,
			"isDeleted": false,
			"id": "UFUFmRMsNjIIBPXCwVZE0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 160.2417101871049,
			"y": -215.7234384932437,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.640245371866513,
			"height": 8.640245371866513,
			"seed": 1584331520,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7200204476555427,
					0.7200204476555427
				],
				[
					1.4400408953110855,
					3.6001022382777137
				],
				[
					2.160061342966628,
					5.040143133588799
				],
				[
					3.6001022382777137,
					1.4400408953110855
				],
				[
					6.480184028899885,
					-2.880081790622171
				],
				[
					7.92022492421097,
					-2.160061342966628
				],
				[
					7.92022492421097,
					3.6001022382777137
				],
				[
					7.92022492421097,
					5.760163581244342
				],
				[
					7.92022492421097,
					3.6001022382777137
				],
				[
					8.640245371866513,
					2.880081790622171
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1574459820985794,
				0.19590124487876892,
				0.1609547734260559,
				0.09073468297719955,
				0.07812076061964035,
				0.1622614711523056,
				0.23624557256698608,
				0.183991938829422,
				0.02330099418759346,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 100812942,
			"isDeleted": false,
			"id": "C-1pyvU0vZS_Cw5zDc5G-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 174.6421191402157,
			"y": -227.9637861033879,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7200204476555427,
			"height": 18.00051119138854,
			"seed": 1345223424,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.4400408953110855
				],
				[
					0,
					10.800306714833113
				],
				[
					-0.7200204476555427,
					18.00051119138854
				],
				[
					0,
					18.00051119138854
				],
				[
					0,
					17.280490743732997
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1866839975118637,
				0.23523397743701935,
				0.23824316263198853,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 143576914,
			"isDeleted": false,
			"id": "lhfv9Qj_hbSl-IiSpFSDQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 168.8819555589714,
			"y": -215.7234384932437,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.920224924210913,
			"height": 0.7200204476555427,
			"seed": 1733745408,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4400408953110855,
					0
				],
				[
					7.2002044765553705,
					0
				],
				[
					7.920224924210913,
					0.7200204476555427
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16095343232154846,
				0.0928715243935585,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 671483598,
			"isDeleted": false,
			"id": "1ezibC47SnAW0iZWyBGWa",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 179.6822622738045,
			"y": -227.9637861033879,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4400408953110855,
			"height": 7.92022492421097,
			"seed": 246283008,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7200204476555427
				],
				[
					0,
					0
				],
				[
					0.7200204476555427,
					2.880081790622171
				],
				[
					1.4400408953110855,
					6.480184028899885
				],
				[
					1.4400408953110855,
					7.200204476555427
				],
				[
					1.4400408953110855,
					6.480184028899885
				],
				[
					1.4400408953110855,
					5.760163581244342
				],
				[
					1.4400408953110855,
					5.760163581244342
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06804159283638,
				0.11429687589406967,
				0.1501573771238327,
				0.1691480129957199,
				0.16008788347244263,
				0.14865566790103912,
				0.1562446653842926,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1214059794,
			"isDeleted": false,
			"id": "k_eZapywozv3ryoCkkRjz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 180.40228272146004,
			"y": -212.84335670262152,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.92022492421097,
			"height": 7.92022492421097,
			"seed": 377502464,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4400408953110855,
					0
				],
				[
					5.040143133588799,
					-0.7200204476555427
				],
				[
					5.760163581244342,
					-2.880081790622171
				],
				[
					4.320122685933256,
					-4.320122685933256
				],
				[
					1.4400408953110855,
					-2.880081790622171
				],
				[
					0,
					1.4400408953110855
				],
				[
					2.160061342966628,
					3.6001022382777137
				],
				[
					7.92022492421097,
					2.880081790622171
				],
				[
					7.92022492421097,
					2.160061342966628
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1577019989490509,
				0.19263382256031036,
				0.16192694008350372,
				0.12636737525463104,
				0.14930573105812073,
				0.21756386756896973,
				0.25749364495277405,
				0.05387844890356064,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 1199045902,
			"isDeleted": false,
			"id": "wHKbK9nhFCuw7xAY85Jv5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 193.3626507792598,
			"y": -228.68380655104343,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4400408953110855,
			"height": 18.720531639044083,
			"seed": 1216027392,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7200204476555427,
					0
				],
				[
					-0.7200204476555427,
					1.4400408953110855
				],
				[
					0,
					8.640245371866513
				],
				[
					0.7200204476555427,
					16.560470296077455
				],
				[
					0.7200204476555427,
					18.720531639044083
				],
				[
					0,
					18.00051119138854
				],
				[
					0,
					17.280490743732997
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0864984467625618,
				0.17169803380966187,
				0.2435174286365509,
				0.2572268545627594,
				0.1611117571592331,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 165454546,
			"isDeleted": false,
			"id": "UvietRrXr3WTLrYz4JUot",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 187.60248719801547,
			"y": -216.44345894089923,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.080286267177598,
			"height": 0.7200204476555427,
			"seed": 146062080,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4400408953110855,
					0
				],
				[
					9.360265819522056,
					0
				],
				[
					10.080286267177598,
					0.7200204476555427
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16548199951648712,
				0.0653659999370575,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 164703054,
			"isDeleted": false,
			"id": "LZOxlqpkkpRH9GcW5jNu-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 200.56285525581524,
			"y": -230.12384744635452,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.480184028899828,
			"height": 19.440552086699626,
			"seed": 962583296,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.4400408953110855
				],
				[
					1.4400408953110855,
					8.640245371866513
				],
				[
					2.160061342966628,
					17.280490743732997
				],
				[
					2.160061342966628,
					19.440552086699626
				],
				[
					2.160061342966628,
					17.280490743732997
				],
				[
					2.880081790622171,
					12.96036805779974
				],
				[
					5.040143133588742,
					10.800306714833141
				],
				[
					6.480184028899828,
					12.96036805779974
				],
				[
					6.480184028899828,
					18.00051119138854
				],
				[
					5.760163581244285,
					19.440552086699626
				],
				[
					5.760163581244285,
					19.440552086699626
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1241929903626442,
				0.17021188139915466,
				0.20600619912147522,
				0.17644192278385162,
				0.097307950258255,
				0.037506867200136185,
				0.07770736515522003,
				0.18309003114700317,
				0.2220132201910019,
				0.07174123823642731,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 396654738,
			"isDeleted": false,
			"id": "cC_Hx468PIYZu9FZ-cMK6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 210.64314152299278,
			"y": -215.00341804558815,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.760163581244342,
			"height": 7.92022492421097,
			"seed": 137100032,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7200204476555427,
					0
				],
				[
					1.4400408953110855,
					0
				],
				[
					2.880081790622171,
					0
				],
				[
					2.880081790622171,
					-2.160061342966628
				],
				[
					0.7200204476555427,
					-2.880081790622171
				],
				[
					-2.160061342966628,
					-1.4400408953110855
				],
				[
					-2.880081790622171,
					2.160061342966628
				],
				[
					-0.7200204476555427,
					5.040143133588799
				],
				[
					2.880081790622171,
					4.320122685933256
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
				0.057549409568309784,
				0.13604125380516052,
				0.12900619208812714,
				0.08592700213193893,
				0.13398070633411407,
				0.21378754079341888,
				0.20305822789669037,
				0.034490205347537994,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 2104136078,
			"isDeleted": false,
			"id": "5-sil1iAxGZBo_pEDfLro",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 217.12332555189272,
			"y": -218.60352028386586,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.320122685933256,
			"height": 7.920224924210942,
			"seed": 558111488,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7200204476555427
				],
				[
					0,
					3.6001022382777137
				],
				[
					0,
					6.480184028899885
				],
				[
					0,
					7.200204476555427
				],
				[
					1.4400408953110855,
					3.6001022382777137
				],
				[
					2.880081790622171,
					0
				],
				[
					4.320122685933256,
					-0.7200204476555143
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
				0.09109198302030563,
				0.14342842996120453,
				0.13444018363952637,
				0.12968991696834564,
				0.1048995703458786,
				0.08326113969087601,
				0.011010284535586834,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 1366005330,
			"isDeleted": false,
			"id": "yPTQ3EDpDZR9m8z341dai",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 223.6035095807925,
			"y": -216.44345894089923,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.760163581244228,
			"height": 7.200204476555427,
			"seed": 1365965568,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7200204476555427,
					0
				],
				[
					1.4400408953110855,
					0.7200204476555427
				],
				[
					2.880081790622171,
					0.7200204476555427
				],
				[
					4.320122685933256,
					0
				],
				[
					3.6001022382777137,
					-1.4400408953110855
				],
				[
					0.7200204476555427,
					-1.4400408953110855
				],
				[
					-0.7200204476555427,
					0
				],
				[
					-1.4400408953109718,
					3.6001022382777137
				],
				[
					0.7200204476555427,
					5.760163581244342
				],
				[
					4.320122685933256,
					5.040143133588799
				],
				[
					4.320122685933256,
					5.040143133588799
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06628097593784332,
				0.070561982691288,
				0.09715262055397034,
				0.1545703411102295,
				0.13534528017044067,
				0.10769488662481308,
				0.16900207102298737,
				0.22625555098056793,
				0.21599698066711426,
				0.042504820972681046,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 2105356238,
			"isDeleted": false,
			"id": "vzqm0xcWOnaQG_dQ5yJVn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 235.84385719093672,
			"y": -226.5237452080768,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.080286267177598,
			"height": 17.280490743732997,
			"seed": 874715904,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7200204476555427
				],
				[
					0.7200204476555427,
					6.480184028899885
				],
				[
					1.4400408953110855,
					10.800306714833113
				],
				[
					2.160061342966628,
					10.800306714833113
				],
				[
					0,
					8.640245371866484
				],
				[
					-2.880081790622171,
					7.920224924210942
				],
				[
					-5.760163581244342,
					11.520327162488655
				],
				[
					-6.480184028899885,
					15.120429400766369
				],
				[
					-1.4400408953110855,
					17.280490743732997
				],
				[
					3.6001022382777137,
					17.280490743732997
				],
				[
					3.6001022382777137,
					17.280490743732997
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05193878337740898,
				0.18067800998687744,
				0.21773330867290497,
				0.1988419145345688,
				0.11938232183456421,
				0.09904098510742188,
				0.16100655496120453,
				0.25244736671447754,
				0.2888983190059662,
				0.0626421794295311,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 134806546,
			"isDeleted": false,
			"id": "xGnjr4H7PEplvzdrbM0lY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 146.5613216816496,
			"y": -176.1223138721889,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4400408953110855,
			"height": 20.88059298201071,
			"seed": 1101478656,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1.4400408953110855
				],
				[
					0,
					-2.160061342966628
				],
				[
					0,
					-2.880081790622171
				],
				[
					0.7200204476555427,
					2.880081790622171
				],
				[
					0.7200204476555427,
					11.520327162488655
				],
				[
					0,
					18.00051119138854
				],
				[
					0,
					16.560470296077455
				],
				[
					-0.7200204476555427,
					15.840449848421912
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06983499228954315,
				0.07858914136886597,
				0.10899020731449127,
				0.22556893527507782,
				0.18963439762592316,
				0.13181912899017334,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 371328526,
			"isDeleted": false,
			"id": "ggAxaSCskkfhABLOGXwpz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 140.0811376527497,
			"y": -167.48206850032238,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.120429400766398,
			"height": 1.440040895311057,
			"seed": 518617856,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.880081790622171,
					0
				],
				[
					10.080286267177598,
					0.7200204476555143
				],
				[
					14.400408953110855,
					1.440040895311057
				],
				[
					15.120429400766398,
					1.440040895311057
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.18926599621772766,
				0.25979799032211304,
				0.1843259036540985,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1500752338,
			"isDeleted": false,
			"id": "rUExivUJFIqZbygfyaisF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 159.52168973944936,
			"y": -163.8819662620447,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.080286267177598,
			"height": 7.200204476555427,
			"seed": 1850817280,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.160061342966628,
					0
				],
				[
					4.320122685933256,
					-1.4400408953110855
				],
				[
					4.320122685933256,
					-2.160061342966628
				],
				[
					1.4400408953110855,
					-2.160061342966628
				],
				[
					-0.7200204476555427,
					0
				],
				[
					-0.7200204476555427,
					3.6001022382777137
				],
				[
					2.880081790622171,
					5.040143133588799
				],
				[
					8.640245371866513,
					2.160061342966628
				],
				[
					9.360265819522056,
					0.7200204476555427
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1752919852733612,
				0.19152548909187317,
				0.1589556336402893,
				0.13112777471542358,
				0.16274484992027283,
				0.21253542602062225,
				0.20518261194229126,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1750209614,
			"isDeleted": false,
			"id": "BbsJjIXsdpCw7EmomKPel",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 173.2020782449046,
			"y": -177.56235476749998,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7200204476555427,
			"height": 18.720531639044083,
			"seed": 1156324096,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7200204476555427,
					0
				],
				[
					-0.7200204476555427,
					1.4400408953110855
				],
				[
					0,
					8.640245371866513
				],
				[
					0,
					17.280490743732997
				],
				[
					-0.7200204476555427,
					18.720531639044083
				],
				[
					-0.7200204476555427,
					18.00051119138854
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07292062044143677,
				0.1795099824666977,
				0.24291998147964478,
				0.25349777936935425,
				0.022948792204260826,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 214081426,
			"isDeleted": false,
			"id": "gMhymW_h1Dd6Mab76mWHJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 166.72189421600478,
			"y": -166.76204805266687,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.800306714833084,
			"height": 0.7200204476555427,
			"seed": 1390484224,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7200204476555427,
					0
				],
				[
					5.040143133588742,
					0
				],
				[
					10.080286267177542,
					0.7200204476555427
				],
				[
					10.800306714833084,
					0.7200204476555427
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05849798768758774,
				0.17235198616981506,
				0.05480486899614334,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 233200270,
			"isDeleted": false,
			"id": "1C_Ia3y0qv1eEBqY0B95B",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 182.56234406442667,
			"y": -179.00239566281107,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.92022492421097,
			"height": 20.16057253435517,
			"seed": 1813043968,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					2.160061342966628
				],
				[
					0.7200204476555427,
					10.080286267177598
				],
				[
					1.4400408953110855,
					18.720531639044083
				],
				[
					1.4400408953110855,
					19.440552086699626
				],
				[
					1.4400408953110855,
					15.120429400766369
				],
				[
					3.6001022382777137,
					11.520327162488684
				],
				[
					6.480184028899885,
					10.800306714833141
				],
				[
					7.92022492421097,
					15.840449848421912
				],
				[
					7.200204476555427,
					20.16057253435517
				],
				[
					6.480184028899885,
					20.16057253435517
				],
				[
					5.760163581244342,
					19.440552086699626
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17063799500465393,
				0.23123401403427124,
				0.2681535482406616,
				0.21483398973941803,
				0.10915057361125946,
				0.09211419522762299,
				0.18431982398033142,
				0.2866284251213074,
				0.29493448138237,
				0.06509020924568176,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1848434002,
			"isDeleted": false,
			"id": "fmNpGAlPF3_oTlbFtavgO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 196.24273256988198,
			"y": -164.60198670970024,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.360265819522056,
			"height": 7.200204476555399,
			"seed": 188545792,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7200204476555427,
					0
				],
				[
					2.160061342966628,
					0
				],
				[
					4.320122685933256,
					-0.7200204476555427
				],
				[
					5.760163581244342,
					-1.4400408953110855
				],
				[
					4.320122685933256,
					-2.8800817906221425
				],
				[
					0,
					-1.4400408953110855
				],
				[
					-2.160061342966628,
					1.4400408953110855
				],
				[
					0,
					4.320122685933256
				],
				[
					6.480184028899885,
					4.320122685933256
				],
				[
					7.200204476555427,
					4.320122685933256
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07812399417161942,
				0.16187399625778198,
				0.21150250732898712,
				0.1904754340648651,
				0.15530715882778168,
				0.217852383852005,
				0.30168572068214417,
				0.13475002348423004,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 2107103438,
			"isDeleted": false,
			"id": "dWX8HemaCdcH3lT-myM4g",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 207.04303928471506,
			"y": -168.92210939563347,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.360265819522112,
			"height": 6.480184028899856,
			"seed": 2013035264,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7200204476555427,
					0.7200204476555427
				],
				[
					1.4400408953110855,
					4.320122685933228
				],
				[
					2.160061342966628,
					6.480184028899856
				],
				[
					3.6001022382777137,
					4.320122685933228
				],
				[
					6.480184028899885,
					0
				],
				[
					9.360265819522112,
					0.7200204476555427
				],
				[
					9.360265819522112,
					0.7200204476555427
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16093066334724426,
				0.20426391065120697,
				0.19964325428009033,
				0.1583472341299057,
				0.14595550298690796,
				0.02106970176100731,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 722035474,
			"isDeleted": false,
			"id": "JovxVCF0bEJQlJJtABi_e",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 218.5633664472038,
			"y": -166.76204805266687,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.200204476555314,
			"height": 9.360265819522027,
			"seed": 1302993664,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7200204476555427,
					-0.7200204476555143
				],
				[
					1.4400408953110855,
					-0.7200204476555143
				],
				[
					2.880081790622171,
					-1.440040895311057
				],
				[
					3.6001022382777137,
					-2.8800817906221425
				],
				[
					1.4400408953110855,
					-3.6001022382776853
				],
				[
					-1.4400408953110855,
					-1.440040895311057
				],
				[
					-2.160061342966628,
					3.6001022382777137
				],
				[
					4.320122685933143,
					5.760163581244342
				],
				[
					5.0401431335886855,
					5.040143133588799
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06999798864126205,
				0.0758499726653099,
				0.11803500354290009,
				0.17583200335502625,
				0.13329394161701202,
				0.11244522035121918,
				0.18892407417297363,
				0.12066061049699783,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 1862242062,
			"isDeleted": false,
			"id": "nGUByS-_XlrgS4CHr84AQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 230.08369360969238,
			"y": -177.56235476749998,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.520327162488684,
			"height": 17.280490743732997,
			"seed": 1234238208,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7200204476555427
				],
				[
					0,
					2.880081790622171
				],
				[
					2.880081790622171,
					9.360265819522056
				],
				[
					4.320122685933256,
					11.520327162488655
				],
				[
					1.4400408953110855,
					10.080286267177598
				],
				[
					-2.880081790622171,
					9.360265819522056
				],
				[
					-5.760163581244342,
					11.520327162488655
				],
				[
					-5.760163581244342,
					15.120429400766369
				],
				[
					-2.160061342966628,
					17.280490743732997
				],
				[
					5.040143133588799,
					16.560470296077455
				],
				[
					5.760163581244342,
					15.840449848421912
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0843878760933876,
				0.1676662564277649,
				0.19002163410186768,
				0.16321709752082825,
				0.10510373115539551,
				0.05447421222925186,
				0.12690038979053497,
				0.21104736626148224,
				0.262411504983902,
				0.11702505499124527,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 768553170,
			"isDeleted": false,
			"id": "TSkLvw1cLzIuaoSjpUJXe",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 255.57964246349448,
			"y": -217.782463422846,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.612745691392462,
			"height": 0.70159321142404,
			"seed": 243866368,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.70159321142404,
					0
				],
				[
					1.4031864228481652,
					0
				],
				[
					3.507966057120342,
					-0.70159321142404
				],
				[
					4.911152479968422,
					-0.70159321142404
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
				0.09991998225450516,
				0.25356197357177734,
				0.28952398896217346,
				0.10469040274620056,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1050049870,
			"isDeleted": false,
			"id": "QgJwntMz2vt2hYdalFedF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 263.2971677891592,
			"y": -222.6936159028144,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.120711748512804,
			"height": 5.612745691392462,
			"seed": 1870535424,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7015932114240968,
					0
				],
				[
					1.40318642284808,
					0
				],
				[
					5.612745691392433,
					0.70159321142404
				],
				[
					8.419118537088707,
					2.1047796342721767
				],
				[
					8.419118537088707,
					4.2095592685443535
				],
				[
					5.612745691392433,
					5.612745691392462
				],
				[
					3.5079660571202567,
					5.612745691392462
				],
				[
					3.5079660571202567,
					4.911152479968393
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08217038214206696,
				0.31178000569343567,
				0.33077293634414673,
				0.2937459647655487,
				0.31247982382774353,
				0.38389530777931213,
				0.377258837223053,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 2048214674,
			"isDeleted": false,
			"id": "_hiuP68L6s3_O4leWpg3n",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 274.52265917194404,
			"y": -227.60476838278282,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.91115247996845,
			"height": 14.031864228481169,
			"seed": 2007522048,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7015932114240968,
					0
				],
				[
					3.5079660571203704,
					4.911152479968422
				],
				[
					4.91115247996845,
					11.927084594208992
				],
				[
					3.5079660571203704,
					14.031864228481169
				],
				[
					2.8063728456962735,
					12.62867780563306
				],
				[
					2.8063728456962735,
					11.927084594208992
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12993799149990082,
				0.21457397937774658,
				0.24658168852329254,
				0.22509613633155823,
				0.04737323150038719,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1370858382,
			"isDeleted": false,
			"id": "nSagP6D_5BMXRm4hX188x",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 282.94177770903275,
			"y": -229.00795480563096,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.1047796342721767,
			"height": 15.435050651329306,
			"seed": 1432181504,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4031864228481936,
					4.911152479968422
				],
				[
					2.1047796342721767,
					12.628677805633089
				],
				[
					2.1047796342721767,
					15.435050651329306
				],
				[
					1.4031864228481936,
					14.031864228481197
				],
				[
					1.4031864228481936,
					13.330271017057129
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.23285400867462158,
				0.28418999910354614,
				0.27014344930648804,
				0.03926864638924599,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 143828050,
			"isDeleted": false,
			"id": "XiURLl6MPrpLkFXsk_2Mc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 288.5545234004253,
			"y": -233.2175140741753,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.612745691392433,
			"height": 18.94301670844962,
			"seed": 1073855232,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.40318642284808,
					1.4031864228481368
				],
				[
					4.911152479968337,
					8.419118537088707
				],
				[
					5.612745691392433,
					16.838237074177442
				],
				[
					4.2095592685443535,
					18.94301670844962
				],
				[
					4.2095592685443535,
					18.24142349702555
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.18171799182891846,
				0.2943379878997803,
				0.37747201323509216,
				0.16409744322299957,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 2056651214,
			"isDeleted": false,
			"id": "2xuh_2XHoxDm1V4aqrdqG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 243.65255786928546,
			"y": -163.05819293176938,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.717525325664667,
			"height": 0.7015932114240684,
			"seed": 1095899904,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.70159321142404,
					0
				],
				[
					0.7015932114240968,
					0
				],
				[
					4.2095592685443535,
					0
				],
				[
					6.31433890281653,
					-0.7015932114240684
				],
				[
					7.015932114240627,
					-0.7015932114240684
				],
				[
					7.015932114240627,
					-0.7015932114240684
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.21872198581695557,
				0.32168999314308167,
				0.328865647315979,
				0.10540200769901276,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 589187602,
			"isDeleted": false,
			"id": "oQaXiVU6qg7vYD1juHnfz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 254.87804925207044,
			"y": -168.67093862316187,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.314338902816559,
			"height": 8.419118537088735,
			"seed": 155654912,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7015932114240968,
					0
				],
				[
					0.70159321142404,
					2.1047796342721767
				],
				[
					3.507966057120285,
					4.2095592685443535
				],
				[
					5.612745691392462,
					6.31433890281653
				],
				[
					4.911152479968365,
					6.31433890281653
				],
				[
					2.104779634272205,
					7.717525325664667
				],
				[
					0,
					8.419118537088735
				],
				[
					0,
					8.419118537088735
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.3243580162525177,
				0.33470961451530457,
				0.33457475900650024,
				0.37332379817962646,
				0.37761303782463074,
				0.08824694901704788,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1548785678,
			"isDeleted": false,
			"id": "IR4K5vRiA6Iinismyd9O5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 266.10354063485534,
			"y": -162.35659972034534,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.015932114240513,
			"height": 0.70159321142404,
			"seed": 439442176,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7015932114239831,
					0
				],
				[
					2.1047796342721767,
					-0.70159321142404
				],
				[
					4.91115247996845,
					-0.70159321142404
				],
				[
					6.31433890281653,
					-0.70159321142404
				],
				[
					5.612745691392547,
					-0.70159321142404
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10448797792196274,
				0.2558490037918091,
				0.3463999927043915,
				0.3776339888572693,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 63,
			"versionNonce": 1085224914,
			"isDeleted": false,
			"id": "rA9SFzBU3XUK3T1n_tta0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 273.11947274909596,
			"y": -167.26775220031374,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.40318642284808,
			"height": 9.822304959936844,
			"seed": 2069216000,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.70159321142404
				],
				[
					0,
					2.1047796342721767
				],
				[
					0,
					5.612745691392462
				],
				[
					0,
					8.419118537088707
				],
				[
					0,
					7.717525325664639
				],
				[
					0,
					5.612745691392462
				],
				[
					0,
					3.507966057120285
				],
				[
					0,
					1.4031864228481084
				],
				[
					-0.7015932114240968,
					-0.7015932114240684
				],
				[
					-0.7015932114240968,
					-1.4031864228481368
				],
				[
					-1.40318642284808,
					-1.4031864228481368
				],
				[
					-1.40318642284808,
					-0.7015932114240684
				],
				[
					-1.40318642284808,
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
				0.15625311434268951,
				0.1767394095659256,
				0.19986462593078613,
				0.19717709720134735,
				0.15346328914165497,
				0.12850011885166168,
				0.11385180801153183,
				0.10990039259195328,
				0.10823361575603485,
				0.12281966954469681,
				0.14813269674777985,
				0.15333233773708344,
				0.1805136352777481,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 66,
			"versionNonce": 1323198030,
			"isDeleted": false,
			"id": "kyxfwQWa1JvwFrYDhbWhp",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 277.3290320176403,
			"y": -167.9693454117378,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.419118537088707,
			"height": 8.419118537088707,
			"seed": 1498438400,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.40318642284808,
					0
				],
				[
					-2.8063728456962735,
					0
				],
				[
					-4.2095592685443535,
					0.7015932114240684
				],
				[
					-4.91115247996845,
					1.4031864228481084
				],
				[
					-5.612745691392433,
					2.1047796342721767
				],
				[
					-5.612745691392433,
					3.507966057120285
				],
				[
					-5.612745691392433,
					4.911152479968422
				],
				[
					-5.612745691392433,
					6.31433890281653
				],
				[
					-5.612745691392433,
					7.015932114240599
				],
				[
					-4.91115247996845,
					7.717525325664667
				],
				[
					-4.2095592685443535,
					7.717525325664667
				],
				[
					-3.5079660571202567,
					8.419118537088707
				],
				[
					-2.1047796342721767,
					8.419118537088707
				],
				[
					-0.7015932114240968,
					8.419118537088707
				],
				[
					0.7015932114240968,
					7.717525325664667
				],
				[
					2.1047796342721767,
					7.717525325664667
				],
				[
					2.8063728456962735,
					7.015932114240599
				],
				[
					2.8063728456962735,
					6.31433890281653
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1988164335489273,
				0.21398873627185822,
				0.21503497660160065,
				0.23601697385311127,
				0.23517832159996033,
				0.2460721731185913,
				0.26270249485969543,
				0.2689574360847473,
				0.2808091938495636,
				0.2939751446247101,
				0.3025657832622528,
				0.3121148347854614,
				0.3201506733894348,
				0.3277796804904938,
				0.3311007618904114,
				0.33154284954071045,
				0.3375079929828644,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1633447314,
			"isDeleted": false,
			"id": "NubaPkk4_lZlkp_uHv0fZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 277.3290320176403,
			"y": -168.67093862316187,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.40318642284808,
			"height": 8.419118537088735,
			"seed": 1043651328,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7015932114240684
				],
				[
					0.7015932114240968,
					4.2095592685443535
				],
				[
					0.7015932114240968,
					7.717525325664667
				],
				[
					0.7015932114240968,
					8.419118537088735
				],
				[
					1.40318642284808,
					8.419118537088735
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1825459897518158,
				0.24814800918102264,
				0.21709218621253967,
				0.11256103217601776,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1125674126,
			"isDeleted": false,
			"id": "wsctdZlSH-bCAJEYs5HRn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 278.0306252290644,
			"y": -167.26775220031374,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.91115247996845,
			"height": 0.70159321142404,
			"seed": 1850292992,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7015932114240968,
					0
				],
				[
					0.7015932114239831,
					0
				],
				[
					2.80637284569616,
					0.70159321142404
				],
				[
					4.2095592685443535,
					0.70159321142404
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
				0.09822350740432739,
				0.2249045968055725,
				0.21375173330307007,
				0.011896790005266666,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 1784474450,
			"isDeleted": false,
			"id": "I7Ch-lZ1KEdFB_0x-ExD1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 278.0306252290644,
			"y": -163.75978614319345,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.911152479968337,
			"height": 0,
			"seed": 1964915456,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7015932114239831,
					0
				],
				[
					2.1047796342721767,
					0
				],
				[
					3.5079660571202567,
					0
				],
				[
					4.2095592685443535,
					0
				],
				[
					4.911152479968337,
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
				0.23950186371803284,
				0.2795524299144745,
				0.2738894522190094,
				0.24091067910194397,
				0.07069989293813705,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 649571022,
			"isDeleted": false,
			"id": "A75GcgHPLszS_UobObmvJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 285.0465573433049,
			"y": -170.07412504600998,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4031864228481936,
			"height": 10.523898171360884,
			"seed": 1792269056,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.4031864228481084
				],
				[
					0.7015932114240968,
					5.612745691392462
				],
				[
					1.4031864228481936,
					9.822304959936844
				],
				[
					1.4031864228481936,
					10.523898171360884
				],
				[
					1.4031864228481936,
					9.120711748512775
				],
				[
					1.4031864228481936,
					8.419118537088707
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17691799998283386,
				0.2339239865541458,
				0.22765548527240753,
				0.17888489365577698,
				0.023976227268576622,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 63,
			"versionNonce": 34058514,
			"isDeleted": false,
			"id": "6DBSKW8ZuP7FrEDeyErEa",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 285.0465573433049,
			"y": -170.77571825743405,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.717525325664724,
			"height": 9.120711748512775,
			"seed": 1158208256,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7015932114240968,
					0
				],
				[
					2.1047796342721767,
					0
				],
				[
					3.5079660571203704,
					0.7015932114240684
				],
				[
					5.612745691392547,
					1.4031864228481368
				],
				[
					7.015932114240627,
					2.1047796342721767
				],
				[
					7.717525325664724,
					3.5079660571203135
				],
				[
					7.717525325664724,
					4.911152479968422
				],
				[
					7.717525325664724,
					6.31433890281653
				],
				[
					7.717525325664724,
					7.015932114240599
				],
				[
					7.015932114240627,
					7.717525325664667
				],
				[
					5.612745691392547,
					8.419118537088707
				],
				[
					4.2095592685443535,
					9.120711748512775
				],
				[
					2.1047796342721767,
					9.120711748512775
				],
				[
					2.1047796342721767,
					7.717525325664667
				],
				[
					2.1047796342721767,
					7.015932114240599
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1694592833518982,
				0.21206381916999817,
				0.23324358463287354,
				0.2347181737422943,
				0.2397412359714508,
				0.24561333656311035,
				0.25144094228744507,
				0.2514890730381012,
				0.25024425983428955,
				0.24704696238040924,
				0.24842342734336853,
				0.23832449316978455,
				0.20196972787380219,
				0.009600677527487278,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1213538574,
			"isDeleted": false,
			"id": "kJARCul6bohb3Rlvhi4_E",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 293.46567588039363,
			"y": -166.5661589888897,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.419118537088707,
			"height": 0.7015932114240684,
			"seed": 761232128,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4031864228481936,
					0.7015932114240684
				],
				[
					4.91115247996845,
					0.7015932114240684
				],
				[
					7.717525325664724,
					0.7015932114240684
				],
				[
					8.419118537088707,
					0.7015932114240684
				],
				[
					8.419118537088707,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.22520898282527924,
				0.30548399686813354,
				0.32106733322143555,
				0.1543620228767395,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 61,
			"versionNonce": 1809039058,
			"isDeleted": false,
			"id": "I5_fOuEdn2U_9ifgCRdH7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 62.12895638392308,
			"y": -50.39806651804736,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.00052392087838,
			"height": 22.750916861537235,
			"seed": 900193024,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.8125327450549094
				],
				[
					-2.437598235164728,
					-0.8125327450549094
				],
				[
					-4.06266372527449,
					0.8125327450549094
				],
				[
					-5.687729215384309,
					1.6250654901098187
				],
				[
					-5.687729215384309,
					4.062663725274547
				],
				[
					-0.8125327450549094,
					8.937860195603946
				],
				[
					4.06266372527449,
					13.000523920878436
				],
				[
					7.3127947054940705,
					17.063187646152926
				],
				[
					6.500261960439218,
					19.500785881317654
				],
				[
					2.4375982351646712,
					21.938384116482325
				],
				[
					-3.2501309802196374,
					21.938384116482325
				],
				[
					-5.687729215384309,
					20.313318626372563
				],
				[
					-5.687729215384309,
					19.500785881317654
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09235140681266785,
				0.1358218640089035,
				0.1565922200679779,
				0.18050839006900787,
				0.1720111072063446,
				0.17837801575660706,
				0.17595095932483673,
				0.21623212099075317,
				0.24623751640319824,
				0.23486992716789246,
				0.08366613835096359,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 62,
			"versionNonce": 996790094,
			"isDeleted": false,
			"id": "IPs7ftXjtW12k8B9FdjyN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 69.44175108941715,
			"y": -39.02260808727874,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.187991175823527,
			"height": 9.750392940658799,
			"seed": 418462464,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.8125327450549094
				],
				[
					0.8125327450549094,
					0
				],
				[
					2.437598235164728,
					4.875196470329399
				],
				[
					4.062663725274547,
					7.312794705494127
				],
				[
					4.062663725274547,
					4.06266372527449
				],
				[
					4.875196470329456,
					0.8125327450549094
				],
				[
					6.500261960439218,
					0.8125327450549094
				],
				[
					7.312794705494127,
					4.06266372527449
				],
				[
					8.125327450549037,
					4.875196470329399
				],
				[
					9.750392940658855,
					0
				],
				[
					11.375458430768617,
					-2.4375982351646712
				],
				[
					12.187991175823527,
					0
				],
				[
					11.375458430768617,
					6.500261960439218
				],
				[
					11.375458430768617,
					6.500261960439218
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07072997838258743,
				0.1823819875717163,
				0.22833047807216644,
				0.20198193192481995,
				0.10827856510877609,
				0.10434552282094955,
				0.17789138853549957,
				0.218612939119339,
				0.16067615151405334,
				0.08757574111223221,
				0.14104092121124268,
				0.2473527193069458,
				0.0662975162267685,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 1683494034,
			"isDeleted": false,
			"id": "QnUE3TNHyw-aG3nVwJwwL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 85.69240599051517,
			"y": -38.21007534222383,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.500261960439218,
			"height": 7.312794705494127,
			"seed": 1905998592,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8125327450548525,
					0
				],
				[
					-1.6250654901097619,
					0
				],
				[
					-1.6250654901097619,
					2.437598235164728
				],
				[
					0,
					4.875196470329399
				],
				[
					3.2501309802196374,
					5.687729215384309
				],
				[
					4.875196470329456,
					2.437598235164728
				],
				[
					4.062663725274547,
					-0.8125327450549094
				],
				[
					0.8125327450549094,
					-1.6250654901098187
				],
				[
					-1.6250654901097619,
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
				0.09359399229288101,
				0.11493398994207382,
				0.1618734449148178,
				0.18289510905742645,
				0.17850418388843536,
				0.1859021931886673,
				0.2166970819234848,
				0.19026128947734833,
				0.028840484097599983,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1011791246,
			"isDeleted": false,
			"id": "auy-3QuEfbtI212akfcLX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 87.31747148062499,
			"y": -37.39754259716892,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.500261960439218,
			"height": 1.6250654901098187,
			"seed": 837507840,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8125327450549094,
					0.8125327450549094
				],
				[
					1.6250654901098187,
					0.8125327450549094
				],
				[
					5.687729215384309,
					1.6250654901098187
				],
				[
					6.500261960439218,
					1.6250654901098187
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10396698117256165,
				0.15628398954868317,
				0.08999377489089966,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 2102112850,
			"isDeleted": false,
			"id": "WObEiePmlWy4LNBYj-GXL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 94.63026618611912,
			"y": -41.46020632244341,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.875196470329399,
			"height": 8.93786019560389,
			"seed": 241900288,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8125327450549094
				],
				[
					0.8125327450549094,
					4.06266372527449
				],
				[
					1.6250654901098187,
					7.3127947054940705
				],
				[
					2.4375982351646712,
					6.500261960439161
				],
				[
					4.875196470329399,
					-1.6250654901098187
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
				0.1203639805316925,
				0.14965854585170746,
				0.14441369473934174,
				0.13866333663463593,
				0.06212319806218147,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 339530702,
			"isDeleted": false,
			"id": "xj63zT_rsODANgRa4xZJG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 107.6307901069975,
			"y": -55.27326298837676,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.6250654901098187,
			"height": 21.93838411648227,
			"seed": 547666688,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.8125327450549094
				],
				[
					0,
					-1.6250654901097619
				],
				[
					0,
					1.6250654901098187
				],
				[
					0.8125327450549094,
					12.187991175823527
				],
				[
					1.6250654901098187,
					20.313318626372507
				],
				[
					1.6250654901098187,
					20.313318626372507
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.03999999910593033,
				0.1162709966301918,
				0.21111199259757996,
				0.25307801365852356,
				0.04813629016280174,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 2038798354,
			"isDeleted": false,
			"id": "JCfQI8c-iJJOoO88Qcxzo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 101.94306089161324,
			"y": -43.08527181255323,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.00052392087838,
			"height": 0.8125327450549094,
			"seed": 1945746176,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8125327450548525,
					0
				],
				[
					2.4375982351646712,
					0
				],
				[
					4.875196470329399,
					0.8125327450549094
				],
				[
					12.18799117582347,
					0.8125327450549094
				],
				[
					13.00052392087838,
					0.8125327450549094
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16250799596309662,
				0.2322940081357956,
				0.18446633219718933,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 61,
			"versionNonce": 2102209038,
			"isDeleted": false,
			"id": "S0LiXSkAmv3H2h5W2WWRT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 62.12895638392308,
			"y": -14.646625735631687,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.00052392087838,
			"height": 8.93786019560389,
			"seed": 474618624,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.6250654901097619,
					4.06266372527449
				],
				[
					3.2501309802195806,
					8.93786019560389
				],
				[
					3.2501309802195806,
					8.12532745054898
				],
				[
					4.06266372527449,
					3.2501309802195806
				],
				[
					5.687729215384309,
					0.8125327450549094
				],
				[
					8.12532745054898,
					4.06266372527449
				],
				[
					8.93786019560389,
					8.12532745054898
				],
				[
					9.750392940658799,
					2.4375982351646712
				],
				[
					11.375458430768617,
					0
				],
				[
					13.00052392087838,
					2.4375982351646712
				],
				[
					13.00052392087838,
					7.3127947054940705
				],
				[
					13.00052392087838,
					8.93786019560389
				],
				[
					13.00052392087838,
					8.93786019560389
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.18172378838062286,
				0.14993195235729218,
				0.09402047842741013,
				0.06118563935160637,
				0.11973602324724197,
				0.1915026307106018,
				0.19467602670192719,
				0.06268258392810822,
				0.1273926943540573,
				0.21839214861392975,
				0.2318316102027893,
				0.12384673953056335,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 687654354,
			"isDeleted": false,
			"id": "1PdO84A2zHnl-JQXrW0sm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 79.19214403007601,
			"y": -12.209027500467016,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.93786019560389,
			"height": 7.3127947054940705,
			"seed": 2052815616,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8125327450549094,
					0
				],
				[
					1.6250654901097619,
					0
				],
				[
					3.2501309802195806,
					-0.8125327450549094
				],
				[
					4.06266372527449,
					-1.6250654901097619
				],
				[
					2.4375982351646712,
					-1.6250654901097619
				],
				[
					0,
					0.8125327450549094
				],
				[
					0,
					4.875196470329399
				],
				[
					7.3127947054940705,
					5.687729215384309
				],
				[
					8.93786019560389,
					4.875196470329399
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08923999220132828,
				0.13415399193763733,
				0.18751800060272217,
				0.18046584725379944,
				0.15952883660793304,
				0.16386370360851288,
				0.23460064828395844,
				0.026117127388715744,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 108574798,
			"isDeleted": false,
			"id": "BPK9bA2LKIYulnOG397QL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 93.0052006960093,
			"y": -27.647149656510123,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.6250654901098187,
			"height": 21.938384116482325,
			"seed": 870210304,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8125327450549094,
					0.8125327450549094
				],
				[
					-0.8125327450549094,
					4.06266372527449
				],
				[
					0,
					11.375458430768617
				],
				[
					0.8125327450549094,
					18.688253136262745
				],
				[
					0.8125327450549094,
					21.938384116482325
				],
				[
					0,
					21.125851371427416
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13548599183559418,
				0.23798798024654388,
				0.25915515422821045,
				0.2001495659351349,
				0.026771819218993187,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1153973138,
			"isDeleted": false,
			"id": "YQ6qBFqKNH_AZO30zC9ee",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 88.1300042256799,
			"y": -15.459158480686597,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.93786019560389,
			"height": 0.8125327450549094,
			"seed": 2073254656,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8125327450549094,
					-0.8125327450549094
				],
				[
					1.6250654901098187,
					-0.8125327450549094
				],
				[
					8.93786019560389,
					-0.8125327450549094
				],
				[
					8.93786019560389,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08731399476528168,
				0.1628478765487671,
				0.10051098465919495,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 2006482574,
			"isDeleted": false,
			"id": "dSKLuGNxK6VbCZ7NVtav3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 102.7555936366681,
			"y": -14.646625735631687,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.3127947054940705,
			"height": 8.937860195603946,
			"seed": 2048072448,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8125327450549094,
					0
				],
				[
					1.6250654901098187,
					0
				],
				[
					2.437598235164728,
					-0.8125327450549094
				],
				[
					4.062663725274547,
					-1.6250654901098187
				],
				[
					3.2501309802196374,
					-2.437598235164728
				],
				[
					0.8125327450549094,
					-1.6250654901098187
				],
				[
					-1.6250654901097619,
					2.4375982351646712
				],
				[
					-1.6250654901097619,
					6.500261960439218
				],
				[
					4.875196470329399,
					5.687729215384309
				],
				[
					5.687729215384309,
					4.875196470329399
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09067599475383759,
				0.11896798759698868,
				0.15825000405311584,
				0.13259223103523254,
				0.12994539737701416,
				0.1600656360387802,
				0.19168978929519653,
				0.01415405236184597,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1260321106,
			"isDeleted": false,
			"id": "OFI9scxHqah_e5t66jwNx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 109.25585559710731,
			"y": -17.896756715851325,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.312794705494127,
			"height": 10.562925685713708,
			"seed": 2057476864,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8125327450549094
				],
				[
					0,
					2.437598235164728
				],
				[
					0.8125327450549094,
					7.312794705494127
				],
				[
					1.6250654901098187,
					10.562925685713708
				],
				[
					2.437598235164728,
					8.937860195603946
				],
				[
					4.875196470329399,
					3.2501309802196374
				],
				[
					7.312794705494127,
					0
				],
				[
					7.312794705494127,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15454599261283875,
				0.16265012323856354,
				0.15075531601905823,
				0.1384277045726776,
				0.11011120676994324,
				0.05086169391870499,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 62,
			"versionNonce": 895843534,
			"isDeleted": false,
			"id": "0AIlRFxzGtsA_i6PDKDQR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 81.62974226524068,
			"y": 8.104291125905547,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.562925685713708,
			"height": 21.938384116482325,
			"seed": 925686528,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8125327450549094,
					0
				],
				[
					0.8125327450549094,
					1.6250654901097619
				],
				[
					1.6250654901098187,
					3.2501309802195806
				],
				[
					4.875196470329399,
					13.813056665933289
				],
				[
					4.875196470329399,
					21.125851371427416
				],
				[
					3.2501309802196374,
					19.500785881317597
				],
				[
					0,
					13.00052392087838
				],
				[
					-0.8125327450549094,
					4.875196470329399
				],
				[
					4.06266372527449,
					-0.8125327450549094
				],
				[
					8.937860195603946,
					-0.8125327450549094
				],
				[
					9.750392940658799,
					4.06266372527449
				],
				[
					7.312794705494127,
					8.12532745054898
				],
				[
					4.06266372527449,
					8.12532745054898
				],
				[
					4.06266372527449,
					7.3127947054940705
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09005200117826462,
				0.1240520030260086,
				0.14360599219799042,
				0.16596053540706635,
				0.16364078223705292,
				0.1310325562953949,
				0.05507702752947807,
				0.04815039038658142,
				0.12164074927568436,
				0.1818784475326538,
				0.22002722322940826,
				0.19737793505191803,
				0.011599060148000717,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1532493586,
			"isDeleted": false,
			"id": "S50vUjQeX6nISPYwTOQbO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 93.0052006960093,
			"y": 6.4792256357957285,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.687729215384309,
			"height": 9.750392940658799,
			"seed": 1419172608,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.8125327450549094
				],
				[
					0.8125327450549094,
					0
				],
				[
					1.6250654901098187,
					4.875196470329399
				],
				[
					1.6250654901098187,
					8.93786019560389
				],
				[
					1.6250654901098187,
					8.12532745054898
				],
				[
					3.2501309802196374,
					3.2501309802195806
				],
				[
					5.687729215384309,
					-0.8125327450549094
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
				0.1560399830341339,
				0.1962137520313263,
				0.1996156871318817,
				0.14243453741073608,
				0.1018776223063469,
				0.005807678215205669,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 628667150,
			"isDeleted": false,
			"id": "uJqw6gQWJ5T6BGctuIRXL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 104.38065912677791,
			"y": 7.291758380850638,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.12532745054898,
			"height": 10.562925685713708,
			"seed": 368425728,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8125327450549094,
					0
				],
				[
					-1.6250654901098187,
					0.8125327450549094
				],
				[
					-3.2501309802195806,
					4.06266372527449
				],
				[
					-2.4375982351646712,
					7.3127947054940705
				],
				[
					1.6250654901098187,
					8.12532745054898
				],
				[
					4.06266372527449,
					4.875196470329399
				],
				[
					4.875196470329399,
					0
				],
				[
					0.8125327450549094,
					-2.437598235164728
				],
				[
					-2.4375982351646712,
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
				0.03999999910593033,
				0.045715972781181335,
				0.16272400319576263,
				0.19016478955745697,
				0.15595586597919464,
				0.13707061111927032,
				0.10066702216863632,
				0.09187207370996475,
				0.030841369181871414,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 300567762,
			"isDeleted": false,
			"id": "B2Q5-jEZlPnXyBjSXaZtq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 111.69345383227204,
			"y": -2.4586345598081607,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.12532745054898,
			"height": 16.250654901098017,
			"seed": 2067127040,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.6250654901097619
				],
				[
					0,
					4.875196470329399
				],
				[
					-0.8125327450549094,
					12.18799117582347
				],
				[
					-0.8125327450549094,
					13.00052392087838
				],
				[
					0.8125327450549094,
					11.37545843076856
				],
				[
					4.875196470329399,
					8.93786019560389
				],
				[
					7.3127947054940705,
					10.562925685713708
				],
				[
					6.500261960439218,
					13.813056665933289
				],
				[
					2.4375982351646712,
					16.250654901098017
				],
				[
					-0.8125327450549094,
					14.625589410988198
				],
				[
					-0.8125327450549094,
					13.813056665933289
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11803198605775833,
				0.1415531039237976,
				0.16508588194847107,
				0.13928677141666412,
				0.0970187708735466,
				0.09752056747674942,
				0.15443499386310577,
				0.22439545392990112,
				0.21423599123954773,
				0.020649811252951622,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 306913614,
			"isDeleted": false,
			"id": "Z9_2KactQEeDhSfakyMDl",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 122.25637951798575,
			"y": -8.14636377519247,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8125327450549094,
			"height": 21.938384116482325,
			"seed": 1849817856,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8125327450549094,
					0.8125327450548525
				],
				[
					0,
					8.93786019560389
				],
				[
					0,
					18.688253136262688
				],
				[
					0,
					21.938384116482325
				],
				[
					0,
					21.125851371427416
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17360800504684448,
				0.22692334651947021,
				0.23506414890289307,
				0.05749468877911568,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1684857490,
			"isDeleted": false,
			"id": "H5xPVZ4JvK0z0d9eKhmlh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 126.31904324326024,
			"y": 7.291758380850638,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.500261960439218,
			"height": 8.125327450549037,
			"seed": 1180326656,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8125327450549094,
					0
				],
				[
					1.6250654901098187,
					0
				],
				[
					3.2501309802195806,
					0
				],
				[
					4.875196470329399,
					-1.6250654901098187
				],
				[
					4.06266372527449,
					-2.437598235164728
				],
				[
					0.8125327450549094,
					-1.6250654901098187
				],
				[
					-0.8125327450549094,
					2.4375982351646712
				],
				[
					0.8125327450549094,
					5.687729215384309
				],
				[
					4.875196470329399,
					5.687729215384309
				],
				[
					5.687729215384309,
					5.687729215384309
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06799399107694626,
				0.07527108490467072,
				0.13173162937164307,
				0.17202971875667572,
				0.1638103872537613,
				0.16671091318130493,
				0.22515787184238434,
				0.28417283296585083,
				0.18087078630924225,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 62,
			"versionNonce": 255182734,
			"isDeleted": false,
			"id": "YNi9-mOOLrfmLAmS9sQoS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 134.44437069380928,
			"y": 4.85416014568591,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.18799117582347,
			"height": 8.125327450549037,
			"seed": 1040833280,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8125327450549094
				],
				[
					2.4375982351646712,
					4.875196470329399
				],
				[
					3.2501309802195806,
					7.312794705494127
				],
				[
					4.06266372527449,
					5.687729215384309
				],
				[
					4.06266372527449,
					3.2501309802196374
				],
				[
					5.687729215384309,
					3.2501309802196374
				],
				[
					6.500261960439161,
					4.875196470329399
				],
				[
					7.3127947054940705,
					5.687729215384309
				],
				[
					8.12532745054898,
					3.2501309802196374
				],
				[
					9.750392940658799,
					2.437598235164728
				],
				[
					11.37545843076856,
					4.06266372527449
				],
				[
					12.18799117582347,
					7.312794705494127
				],
				[
					12.18799117582347,
					8.125327450549037
				],
				[
					12.18799117582347,
					7.312794705494127
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17760998010635376,
				0.24128399789333344,
				0.1975499540567398,
				0.08404693752527237,
				0.09666876494884491,
				0.1699073165655136,
				0.2020367681980133,
				0.16000890731811523,
				0.12280221283435822,
				0.17746493220329285,
				0.27849870920181274,
				0.27393287420272827,
				0.03597961366176605,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 77,
			"versionNonce": 2107031634,
			"isDeleted": false,
			"id": "zpk6rbdvI3JrKxjkOPnvX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 140.13209990919358,
			"y": -41.46020632244341,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 33.31384254725094,
			"height": 35.751440782415614,
			"seed": 24369920,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8125327450549094,
					0
				],
				[
					-1.6250654901098187,
					0
				],
				[
					-1.6250654901098187,
					0.8125327450549094
				],
				[
					-4.062663725274547,
					2.4375982351646712
				],
				[
					-5.687729215384309,
					6.500261960439161
				],
				[
					-5.687729215384309,
					13.00052392087838
				],
				[
					-4.062663725274547,
					19.500785881317597
				],
				[
					0,
					24.375982351646996
				],
				[
					5.687729215384252,
					27.626113331866634
				],
				[
					11.37545843076856,
					28.438646076921486
				],
				[
					18.688253136262688,
					24.375982351646996
				],
				[
					25.188515096701906,
					17.87572039120778
				],
				[
					26.813580586811725,
					13.00052392087838
				],
				[
					27.626113331866634,
					8.93786019560389
				],
				[
					27.626113331866634,
					4.875196470329399
				],
				[
					26.813580586811725,
					1.6250654901097619
				],
				[
					26.001047841756815,
					-1.6250654901098187
				],
				[
					24.375982351646996,
					-4.062663725274547
				],
				[
					21.125851371427416,
					-5.687729215384309
				],
				[
					18.688253136262688,
					-7.312794705494127
				],
				[
					15.438122156043107,
					-7.312794705494127
				],
				[
					11.37545843076856,
					-7.312794705494127
				],
				[
					8.12532745054898,
					-7.312794705494127
				],
				[
					4.875196470329399,
					-6.500261960439218
				],
				[
					1.6250654901097619,
					-4.875196470329399
				],
				[
					-0.8125327450549094,
					-3.2501309802196374
				],
				[
					-4.062663725274547,
					-1.6250654901098187
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
				0.06868793070316315,
				0.10003683716058731,
				0.1740100085735321,
				0.21195127069950104,
				0.24625277519226074,
				0.28088924288749695,
				0.3086548447608948,
				0.3098822832107544,
				0.31590619683265686,
				0.3239717185497284,
				0.32306140661239624,
				0.2968977987766266,
				0.33487531542778015,
				0.3496336042881012,
				0.32784467935562134,
				0.31578201055526733,
				0.3244500458240509,
				0.33226674795150757,
				0.35038435459136963,
				0.3545261025428772,
				0.36055654287338257,
				0.3654389977455139,
				0.3751751184463501,
				0.37202706933021545,
				0.3603334426879883,
				0.10299749672412872,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1550951886,
			"isDeleted": false,
			"id": "_iURmg3pK7N1z1ZzWaPiY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 142.56969814435826,
			"y": -36.58500985211401,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 20.313318626372563,
			"height": 1.6250654901098187,
			"seed": 384252672,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8125327450549094,
					0
				],
				[
					-0.8125327450549094,
					0.8125327450549094
				],
				[
					-1.6250654901098187,
					0.8125327450549094
				],
				[
					0,
					0.8125327450549094
				],
				[
					3.2501309802195806,
					0.8125327450549094
				],
				[
					8.93786019560389,
					0
				],
				[
					14.625589410988198,
					0
				],
				[
					17.875720391207835,
					-0.8125327450549094
				],
				[
					18.688253136262745,
					0
				],
				[
					18.688253136262745,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.009999999776482582,
				0.05920089781284332,
				0.13364645838737488,
				0.19775177538394928,
				0.25317224860191345,
				0.3077830672264099,
				0.3100958466529846,
				0.302053302526474,
				0.3105084300041199,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 72,
			"versionNonce": 423552530,
			"isDeleted": false,
			"id": "LCnfrxCYyKopa5qFgN6MY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 140.94463265424844,
			"y": -34.95994436200425,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.688253136262688,
			"height": 13.813056665933289,
			"seed": 1581693696,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8125327450548525,
					0
				],
				[
					-0.8125327450548525,
					0.8125327450549094
				],
				[
					0,
					4.875196470329456
				],
				[
					1.6250654901098187,
					9.750392940658855
				],
				[
					2.437598235164728,
					11.375458430768617
				],
				[
					2.437598235164728,
					12.187991175823527
				],
				[
					2.437598235164728,
					11.375458430768617
				],
				[
					3.2501309802196374,
					11.375458430768617
				],
				[
					5.687729215384309,
					11.375458430768617
				],
				[
					8.937860195603946,
					10.562925685713765
				],
				[
					12.187991175823527,
					10.562925685713765
				],
				[
					14.625589410988255,
					10.562925685713765
				],
				[
					16.250654901098017,
					10.562925685713765
				],
				[
					17.063187646152926,
					10.562925685713765
				],
				[
					17.063187646152926,
					9.750392940658855
				],
				[
					17.875720391207835,
					9.750392940658855
				],
				[
					17.875720391207835,
					8.937860195603946
				],
				[
					17.875720391207835,
					7.312794705494127
				],
				[
					17.875720391207835,
					4.875196470329456
				],
				[
					17.875720391207835,
					2.437598235164728
				],
				[
					17.875720391207835,
					0
				],
				[
					17.063187646152926,
					-0.8125327450548525
				],
				[
					17.063187646152926,
					-1.6250654901097619
				],
				[
					16.250654901098017,
					-1.6250654901097619
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1347009539604187,
				0.17026236653327942,
				0.19184698164463043,
				0.20611272752285004,
				0.2042740136384964,
				0.191802516579628,
				0.17589901387691498,
				0.21388684213161469,
				0.24020697176456451,
				0.2551308870315552,
				0.2679744064807892,
				0.2666994631290436,
				0.2553271949291229,
				0.24632461369037628,
				0.2279212325811386,
				0.22402401268482208,
				0.21095550060272217,
				0.1853952258825302,
				0.17884069681167603,
				0.17204473912715912,
				0.17568503320217133,
				0.18562564253807068,
				0.11325555294752121,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1259846670,
			"isDeleted": false,
			"id": "1YqBrZGd99KSk7w2a_82A",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 145.00729637952298,
			"y": -34.95994436200425,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.2501309802195806,
			"height": 10.562925685713765,
			"seed": 1934818048,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.6250654901097619,
					4.875196470329456
				],
				[
					2.4375982351646712,
					10.562925685713765
				],
				[
					3.2501309802195806,
					10.562925685713765
				],
				[
					2.4375982351646712,
					9.750392940658855
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.24966000020503998,
				0.270027756690979,
				0.040264617651700974,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1616663506,
			"isDeleted": false,
			"id": "U1sQLZ547-cahP6I2OdL2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 150.6950255949073,
			"y": -34.95994436200425,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.4375982351646712,
			"height": 9.750392940658855,
			"seed": 1167768320,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8125327450548525,
					0
				],
				[
					0.8125327450548525,
					1.6250654901098187
				],
				[
					0.8125327450548525,
					3.2501309802196374
				],
				[
					1.6250654901097619,
					8.125327450549037
				],
				[
					2.4375982351646712,
					9.750392940658855
				],
				[
					2.4375982351646712,
					8.937860195603946
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16608697175979614,
				0.2056039720773697,
				0.26646798849105835,
				0.12515349686145782,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 555813454,
			"isDeleted": false,
			"id": "VFoYIetHk6FFvZ9CTo9Ua",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 206.38562791849142,
			"y": -41.09362414908776,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.623409186589754,
			"height": 25.04089308267578,
			"seed": 488962816,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7588149418992884,
					3.7940747094963285
				],
				[
					4.552889651395617,
					15.176298837985314
				],
				[
					4.552889651395617,
					24.28207814077649
				],
				[
					3.7940747094963285,
					25.04089308267578
				],
				[
					1.51762988379852,
					18.970373547481643
				],
				[
					0,
					10.623409186589697
				],
				[
					4.552889651395617,
					2.2764448256977516
				],
				[
					9.864594244690466,
					0
				],
				[
					10.623409186589754,
					4.55288965139556
				],
				[
					8.346964360891945,
					9.864594244690466
				],
				[
					6.8293344770934254,
					9.105779302791177
				],
				[
					6.8293344770934254,
					9.105779302791177
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11425989121198654,
				0.13962331414222717,
				0.1480710506439209,
				0.15067043900489807,
				0.10061587393283844,
				0.07801812887191772,
				0.11465618759393692,
				0.14646431803703308,
				0.17476162314414978,
				0.2001403570175171,
				0.01642724685370922,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1158023570,
			"isDeleted": false,
			"id": "uWfL-wZBAk9x_H9iwvora",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 218.5266669888797,
			"y": -38.05836438149072,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.105779302791177,
			"height": 9.864594244690466,
			"seed": 1967241984,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7588149418992884,
					0
				],
				[
					3.035259767597097,
					-0.7588149418992884
				],
				[
					5.311704593294849,
					-2.2764448256978085
				],
				[
					3.7940747094963285,
					-3.03525976759704
				],
				[
					0.7588149418992884,
					-2.2764448256978085
				],
				[
					-1.51762988379852,
					1.51762988379852
				],
				[
					-0.7588149418992884,
					6.070519535194137
				],
				[
					2.2764448256978085,
					6.8293344770934254
				],
				[
					6.8293344770934254,
					3.7940747094963285
				],
				[
					7.588149418992657,
					3.035259767597097
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09909957647323608,
				0.1339537352323532,
				0.15982653200626373,
				0.15981753170490265,
				0.15546640753746033,
				0.18997088074684143,
				0.2192918062210083,
				0.1893164962530136,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 2103873678,
			"isDeleted": false,
			"id": "qXCJBhV0GRYg93lDj9INi",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 226.11481640787235,
			"y": -40.33480920718853,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.311704593294849,
			"height": 8.346964360891945,
			"seed": 1491155712,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7588149418992316,
					0.7588149418992884
				],
				[
					-0.7588149418992316,
					1.51762988379852
				],
				[
					0,
					4.552889651395617
				],
				[
					0,
					8.346964360891945
				],
				[
					0.7588149418992884,
					7.588149418992657
				],
				[
					1.51762988379852,
					3.035259767597097
				],
				[
					4.552889651395617,
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
				0.05854901298880577,
				0.12258416414260864,
				0.13862819969654083,
				0.15410397946834564,
				0.1486118733882904,
				0.12325375527143478,
				0.023000000044703484,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 68,
			"versionNonce": 1584596818,
			"isDeleted": false,
			"id": "wuU8JTkRbkPKQ8KKDBGAr",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 235.2205957106636,
			"y": -40.33480920718853,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.382224128488986,
			"height": 10.623409186589754,
			"seed": 1769741056,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7588149418992316,
					0
				],
				[
					0.7588149418992316,
					-0.7588149418992316
				],
				[
					0,
					-1.51762988379852
				],
				[
					-2.2764448256978085,
					-0.7588149418992316
				],
				[
					-2.2764448256978085,
					0.7588149418992884
				],
				[
					0,
					3.7940747094963285
				],
				[
					1.51762988379852,
					6.8293344770934254
				],
				[
					0,
					8.346964360891945
				],
				[
					-1.5176298837985769,
					7.588149418992657
				],
				[
					-1.5176298837985769,
					5.311704593294905
				],
				[
					0,
					5.311704593294905
				],
				[
					1.51762988379852,
					6.8293344770934254
				],
				[
					3.03525976759704,
					7.588149418992657
				],
				[
					5.311704593294849,
					6.8293344770934254
				],
				[
					7.588149418992657,
					4.552889651395617
				],
				[
					9.105779302791177,
					1.51762988379852
				],
				[
					6.829334477093369,
					-1.51762988379852
				],
				[
					3.7940747094963285,
					-2.2764448256978085
				],
				[
					1.51762988379852,
					2.2764448256978085
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
				0.007932708598673344,
				0.07464776933193207,
				0.13659609854221344,
				0.1677619069814682,
				0.15567424893379211,
				0.1358458548784256,
				0.13861267268657684,
				0.17928753793239594,
				0.1226058378815651,
				0.0664016455411911,
				0.08100192248821259,
				0.11361303925514221,
				0.12654660642147064,
				0.14264580607414246,
				0.16677524149417877,
				0.18267260491847992,
				0.17337368428707123,
				0.17365707457065582,
				0.028938964009284973,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1000427214,
			"isDeleted": false,
			"id": "Fw-PC8XfH450OJsGumCF9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 244.32637501345476,
			"y": -39.57599426528924,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.070519535194137,
			"height": 8.346964360891945,
			"seed": 1885502208,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7588149418992884
				],
				[
					0,
					0
				],
				[
					1.51762988379852,
					3.03525976759704
				],
				[
					2.2764448256978653,
					4.552889651395617
				],
				[
					2.2764448256978653,
					3.03525976759704
				],
				[
					3.7940747094963285,
					-0.7588149418992884
				],
				[
					5.311704593294905,
					-2.2764448256978085
				],
				[
					6.070519535194137,
					1.51762988379852
				],
				[
					5.311704593294905,
					5.311704593294849
				],
				[
					5.311704593294905,
					6.070519535194137
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13283981382846832,
				0.1559457629919052,
				0.15380707383155823,
				0.08101672679185867,
				0.08489138633012772,
				0.1435401290655136,
				0.19288544356822968,
				0.03525582700967789,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1157254418,
			"isDeleted": false,
			"id": "O96RJAMkR4ReFbI9astex",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 252.6733393743467,
			"y": -39.57599426528924,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.07051953519408,
			"height": 8.346964360891945,
			"seed": 14809856,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7588149418992316,
					1.51762988379852
				],
				[
					-0.7588149418992316,
					3.7940747094963285
				],
				[
					1.5176298837985769,
					5.311704593294849
				],
				[
					4.552889651395617,
					4.552889651395617
				],
				[
					5.311704593294849,
					0.7588149418992316
				],
				[
					4.552889651395617,
					-2.2764448256978085
				],
				[
					0.7588149418992316,
					-3.035259767597097
				],
				[
					-0.7588149418992316,
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
				0.15908798575401306,
				0.1570664346218109,
				0.18641097843647003,
				0.21067148447036743,
				0.23605282604694366,
				0.19408737123012543,
				0.02111828699707985,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1483359502,
			"isDeleted": false,
			"id": "G3KACTn9vpgPKheobH5Ti",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 257.98504396764156,
			"y": -37.29954943959143,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.03525976759704,
			"height": 1.51762988379852,
			"seed": 1042381568,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7588149418992316
				],
				[
					3.03525976759704,
					1.51762988379852
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
				0.13871988654136658,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1846729426,
			"isDeleted": false,
			"id": "eCh-RR6OjP2kSR2vhqQb9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 265.5731933866342,
			"y": -53.99347816137532,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.03525976759704,
			"height": 22.00563331507874,
			"seed": 1133067008,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7588149418992316,
					1.51762988379852
				],
				[
					-0.7588149418992316,
					3.7940747094963285
				],
				[
					-0.7588149418992316,
					12.141039070388274
				],
				[
					1.5176298837985769,
					22.00563331507874
				],
				[
					2.2764448256978085,
					22.00563331507874
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11232198774814606,
				0.15688547492027283,
				0.25532999634742737,
				0.08148260414600372,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1429893966,
			"isDeleted": false,
			"id": "4zzLzYBrxIt3be6TawJyy",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 232.94415088496578,
			"y": -12.258656356915651,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.899854012287506,
			"height": 9.864594244690466,
			"seed": 1883872000,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7588149418992316,
					4.552889651395617
				],
				[
					3.03525976759704,
					8.346964360891945
				],
				[
					6.070519535194137,
					6.070519535194137
				],
				[
					6.829334477093369,
					0.7588149418992884
				],
				[
					6.070519535194137,
					0
				],
				[
					6.070519535194137,
					3.7940747094963285
				],
				[
					7.588149418992657,
					7.588149418992657
				],
				[
					10.623409186589754,
					7.588149418992657
				],
				[
					12.899854012287506,
					2.2764448256978085
				],
				[
					12.899854012287506,
					-1.51762988379852
				],
				[
					12.899854012287506,
					-1.51762988379852
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1950637847185135,
				0.18143469095230103,
				0.1549498587846756,
				0.12704388797283173,
				0.12559042870998383,
				0.14273996651172638,
				0.15708710253238678,
				0.15878427028656006,
				0.1647985279560089,
				0.12049612402915955,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 139702418,
			"isDeleted": false,
			"id": "pqRrJqZhbcKEg_qvDLLpZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 249.63807960674967,
			"y": -13.017471298814883,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.5176298837984632,
			"height": 6.070519535194137,
			"seed": 926792448,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7588149418992316
				],
				[
					0,
					1.51762988379852
				],
				[
					0,
					4.55288965139556
				],
				[
					0.7588149418992316,
					6.070519535194137
				],
				[
					1.5176298837984632,
					6.070519535194137
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06951998919248581,
				0.1298534870147705,
				0.21548998355865479,
				0.03797311335802078,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 476764558,
			"isDeleted": false,
			"id": "T4_zWXAJdmO0SFu6FQrKO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 250.3968945486489,
			"y": -17.5703609502105,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7588149418992316,
			"height": 1.51762988379852,
			"seed": 1947081472,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7588149418992884
				],
				[
					-0.7588149418992316,
					-1.51762988379852
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
				0.06654678285121918,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 61,
			"versionNonce": 1467207250,
			"isDeleted": false,
			"id": "QujUHl2O5f6ypkAk_6yYg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 254.1909692581453,
			"y": -10.741026473117131,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.864594244690466,
			"height": 32.62904250166844,
			"seed": 125688576,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					4.552889651395503,
					-3.03525976759704
				],
				[
					8.346964360891889,
					-10.623409186589697
				],
				[
					7.588149418992657,
					-15.935113779884603
				],
				[
					4.552889651395503,
					-16.693928721783834
				],
				[
					2.2764448256978085,
					-12.899854012287506
				],
				[
					2.2764448256978085,
					-6.829334477093369
				],
				[
					4.552889651395503,
					-0.7588149418992316
				],
				[
					8.346964360891889,
					6.070519535194137
				],
				[
					9.864594244690466,
					11.382224128489042
				],
				[
					9.864594244690466,
					14.417483896086082
				],
				[
					6.07051953519408,
					15.935113779884603
				],
				[
					1.5176298837984632,
					14.417483896086082
				],
				[
					1.5176298837984632,
					10.623409186589754
				],
				[
					1.5176298837984632,
					10.623409186589754
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.18758200109004974,
				0.19548392295837402,
				0.15329009294509888,
				0.14170199632644653,
				0.13716396689414978,
				0.1374325007200241,
				0.15187934041023254,
				0.1534978598356247,
				0.1639862060546875,
				0.1943211704492569,
				0.19659683108329773,
				0.15504074096679688,
				0.02335192821919918,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1697937358,
			"isDeleted": false,
			"id": "4cJmhAwnLrvbrVuy6BI74",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 268.60845315423137,
			"y": -14.53510118261346,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.5176298837984632,
			"height": 6.070519535194137,
			"seed": 1659362048,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.5176298837985769
				],
				[
					0.7588149418992316,
					6.070519535194137
				],
				[
					1.5176298837984632,
					6.070519535194137
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.20144400000572205,
				0.00812823511660099,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 273298450,
			"isDeleted": false,
			"id": "qN52Sz3fWxXO4o0vgGVlG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 269.3672680961306,
			"y": -19.08799083400902,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7588149418992316,
			"height": 1.5176298837985769,
			"seed": 798948096,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7588149418992884
				],
				[
					-0.7588149418992316,
					-1.5176298837985769
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
				0.0399063415825367,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 397430286,
			"isDeleted": false,
			"id": "FNQg2P9iDr_jFpGZA0BXL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 276.95541751512326,
			"y": -24.399695427303925,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.588149418992657,
			"height": 20.48800343128022,
			"seed": 1491516160,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7588149418992316
				],
				[
					0,
					-1.51762988379852
				],
				[
					0.7588149418992316,
					-3.7940747094963285
				],
				[
					3.7940747094962717,
					-5.311704593294849
				],
				[
					6.8293344770934254,
					-4.55288965139556
				],
				[
					7.588149418992657,
					-1.51762988379852
				],
				[
					6.8293344770934254,
					3.035259767597097
				],
				[
					4.552889651395617,
					6.8293344770934254
				],
				[
					3.7940747094962717,
					10.623409186589754
				],
				[
					5.311704593294849,
					15.176298837985371
				],
				[
					5.311704593294849,
					15.176298837985371
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.13578549027442932,
				0.21234799921512604,
				0.2392181158065796,
				0.22966979444026947,
				0.2505646347999573,
				0.24512700736522675,
				0.22214892506599426,
				0.025185760110616684,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 885907922,
			"isDeleted": false,
			"id": "6m42DdSNbMVoDVNnbiK-O",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 284.5435669341159,
			"y": -6.946951763620746,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7588149418992316,
			"height": 0.7588149418992316,
			"seed": 646372096,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7588149418992316
				],
				[
					0.7588149418992316,
					0.7588149418992316
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
				0.15019695460796356,
				0.11455105245113373,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 819420238,
			"isDeleted": false,
			"id": "Vllcx7j2U-VNxlxN6Fdsw",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 323.587382203253,
			"y": -89.70839671508492,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.78403383138675,
			"height": 10.811118561706735,
			"seed": 946248448,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6756949101066425
				],
				[
					-1.3513898202133419,
					-0.6756949101066425
				],
				[
					-4.054169460640026,
					0.6756949101066994
				],
				[
					-4.729864370746668,
					2.027084730320041
				],
				[
					-2.7027796404266837,
					4.729864370746725
				],
				[
					0.6756949101066994,
					7.432644011173409
				],
				[
					2.027084730320041,
					9.459728741493393
				],
				[
					0,
					10.135423651600092
				],
				[
					-4.729864370746668,
					10.135423651600092
				],
				[
					-6.756949101066709,
					10.135423651600092
				],
				[
					-4.729864370746668,
					8.78403383138675
				],
				[
					-4.054169460640026,
					8.78403383138675
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06691998243331909,
				0.1190689355134964,
				0.1172974556684494,
				0.1266712099313736,
				0.12293719500303268,
				0.12748120725154877,
				0.15087249875068665,
				0.17715737223625183,
				0.18785080313682556,
				0.15106920897960663,
				0.0050493162125349045,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1880479634,
			"isDeleted": false,
			"id": "qRuYE7tU14dnqTyBe5--T",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 328.31724657399974,
			"y": -85.65422725444489,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.108338921280051,
			"height": 8.108338921280051,
			"seed": 2133547776,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6756949101066425,
					0
				],
				[
					1.3513898202133419,
					-0.6756949101066425
				],
				[
					2.7027796404266837,
					-1.3513898202133419
				],
				[
					3.3784745505333262,
					-2.7027796404266837
				],
				[
					0.6756949101066425,
					-2.7027796404266837
				],
				[
					-2.7027796404266837,
					0
				],
				[
					-3.378474550533383,
					3.378474550533383
				],
				[
					-1.3513898202133419,
					5.4055592808533675
				],
				[
					4.054169460640026,
					4.729864370746725
				],
				[
					4.729864370746668,
					4.054169460640026
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.026605987921357155,
				0.07217498868703842,
				0.11983504891395569,
				0.12708230316638947,
				0.13704141974449158,
				0.16980373859405518,
				0.2016936093568802,
				0.21417725086212158,
				0.04080819711089134,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 646095502,
			"isDeleted": false,
			"id": "gfwlLyKtlITcdC--ejCUx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 337.77697531549313,
			"y": -87.68131198476487,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.081254190960067,
			"height": 7.432644011173352,
			"seed": 1700453120,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6756949101066994,
					0
				],
				[
					-1.3513898202133419,
					0.6756949101066425
				],
				[
					-2.027084730320041,
					1.3513898202133419
				],
				[
					-3.378474550533383,
					3.3784745505333262
				],
				[
					-2.7027796404266837,
					6.756949101066709
				],
				[
					0,
					7.432644011173352
				],
				[
					2.0270847303199844,
					7.432644011173352
				],
				[
					2.7027796404266837,
					6.756949101066709
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.011076233349740505,
				0.0873742401599884,
				0.14799199998378754,
				0.20222997665405273,
				0.21186645328998566,
				0.1522616297006607,
				0.012398132123053074,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 1918440786,
			"isDeleted": false,
			"id": "YDAq6Pilx3ZJ5D61WCKo1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 342.5068396862398,
			"y": -85.65422725444489,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.729864370746668,
			"height": 5.4055592808533675,
			"seed": 613751552,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6756949101066994
				],
				[
					0,
					1.3513898202133419
				],
				[
					-0.6756949101066425,
					2.7027796404266837
				],
				[
					1.3513898202133419,
					4.054169460640026
				],
				[
					2.7027796404266837,
					3.378474550533383
				],
				[
					4.054169460640026,
					-1.3513898202133419
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
				0.09143200516700745,
				0.16636599600315094,
				0.21323703229427338,
				0.23458530008792877,
				0.07315240800380707,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1265311950,
			"isDeleted": false,
			"id": "qMjpqRSymFhSCqmDNh-jR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 350.61517860751985,
			"y": -88.35700689487157,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.756949101066709,
			"height": 6.756949101066709,
			"seed": 201284352,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6756949101066425,
					3.378474550533383
				],
				[
					1.3513898202133419,
					6.756949101066709
				],
				[
					2.7027796404266837,
					2.7027796404266837
				],
				[
					6.756949101066709,
					0
				],
				[
					6.756949101066709,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.20022161304950714,
				0.23565633594989777,
				0.16139847040176392,
				0.013006470166146755,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1290705682,
			"isDeleted": false,
			"id": "7QW6WfrVJ88s4Xa2Siu6S",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 358.0478226186932,
			"y": -87.00561707465823,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3513898202133419,
			"height": 6.081254190960067,
			"seed": 551795456,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6756949101066994
				],
				[
					0,
					2.027084730320041
				],
				[
					0,
					3.378474550533383
				],
				[
					0.6756949101066994,
					6.081254190960067
				],
				[
					1.3513898202133419,
					6.081254190960067
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08867798000574112,
				0.13310198485851288,
				0.11183974891901016,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 858380046,
			"isDeleted": false,
			"id": "lfBMrn04IH4OGTN1J6Su2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 360.7506022591199,
			"y": -91.05978653529826,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6756949101066425,
			"height": 0,
			"seed": 1416895232,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6756949101066425,
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
				0.006161987315863371,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1313695954,
			"isDeleted": false,
			"id": "26qWTldSWpDzNv8q7mNcu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 368.1832462702933,
			"y": -104.57368473743168,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.7027796404266837,
			"height": 22.97362694362681,
			"seed": 1635990272,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6756949101066994,
					0
				],
				[
					-0.6756949101066994,
					2.7027796404266837
				],
				[
					0.6756949101066425,
					12.838203292026776
				],
				[
					0,
					20.946542213306827
				],
				[
					-1.3513898202133419,
					22.97362694362681
				],
				[
					-2.027084730320041,
					22.97362694362681
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09618597477674484,
				0.15659146010875702,
				0.19382205605506897,
				0.1812809407711029,
				0.025111572816967964,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 372753742,
			"isDeleted": false,
			"id": "e9GOoFDaNua2CKI7rfL1C",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 362.10199207933323,
			"y": -88.35700689487157,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.108338921280051,
			"height": 0.6756949101066994,
			"seed": 240663296,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6756949101066994,
					0
				],
				[
					1.3513898202133419,
					0
				],
				[
					7.432644011173409,
					0
				],
				[
					8.108338921280051,
					0.6756949101066994
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06927798688411713,
				0.05855599790811539,
				0.0702688917517662,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1577877138,
			"isDeleted": false,
			"id": "z7qtFcYE2AcDou1ZA6d3u",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 371.5617208208266,
			"y": -88.35700689487157,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.432644011173352,
			"height": 4.054169460640026,
			"seed": 732953344,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6756949101066994
				],
				[
					0.6756949101066994,
					0.6756949101066994
				],
				[
					2.027084730320041,
					1.3513898202133419
				],
				[
					6.756949101066709,
					3.378474550533383
				],
				[
					7.432644011173352,
					4.054169460640026
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06905798614025116,
				0.12227786332368851,
				0.05524478107690811,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 904784782,
			"isDeleted": false,
			"id": "LheRP3xSQsCSBgzFbQZr9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 383.7242292027467,
			"y": -89.70839671508492,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.108338921280051,
			"height": 20.270847303200128,
			"seed": 193485568,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6756949101066994,
					0.6756949101066994
				],
				[
					-1.3513898202133419,
					1.3513898202133419
				],
				[
					-4.054169460640026,
					9.459728741493393
				],
				[
					-7.432644011173409,
					19.59515239309343
				],
				[
					-8.108338921280051,
					20.270847303200128
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16214199364185333,
				0.28809797763824463,
				0.15025772154331207,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 1491262546,
			"isDeleted": false,
			"id": "TRt2fiPlc7IlRRmr4Yp4U",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 326.2901618436797,
			"y": -58.62643085017805,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.4055592808533675,
			"height": 12.162508381920077,
			"seed": 613202688,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6756949101066994
				],
				[
					0,
					0
				],
				[
					0.6756949101066994,
					4.054169460640026
				],
				[
					0.6756949101066994,
					10.135423651600036
				],
				[
					0.6756949101066994,
					11.486813471813377
				],
				[
					1.3513898202133419,
					7.432644011173352
				],
				[
					4.729864370746725,
					2.0270847303199844
				],
				[
					5.4055592808533675,
					2.0270847303199844
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06371819972991943,
				0.14652863144874573,
				0.18371666967868805,
				0.18502560257911682,
				0.15451836585998535,
				0.09867013245820999,
				0.009482177905738354,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1082477006,
			"isDeleted": false,
			"id": "pjLw02QQnZQvQEJDf2iEA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 334.39850076495975,
			"y": -55.92365120975137,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.108338921280051,
			"height": 8.78403383138675,
			"seed": 686750464,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6756949101066994,
					0
				],
				[
					2.027084730320041,
					0
				],
				[
					4.054169460640026,
					-0.6756949101066994
				],
				[
					4.729864370746725,
					-2.027084730320041
				],
				[
					2.7027796404266837,
					-2.027084730320041
				],
				[
					0,
					0.6756949101066425
				],
				[
					-0.6756949101066425,
					4.729864370746668
				],
				[
					2.027084730320041,
					6.756949101066709
				],
				[
					6.756949101066709,
					6.08125419096001
				],
				[
					7.432644011173409,
					5.4055592808533675
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.03623773157596588,
				0.10451806336641312,
				0.14667193591594696,
				0.14069855213165283,
				0.12033908069133759,
				0.15111862123012543,
				0.22756323218345642,
				0.24223507940769196,
				0.07126693427562714,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1822917138,
			"isDeleted": false,
			"id": "4V1gQ7IfF6z8EnvJUqbZq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 347.23670405698647,
			"y": -68.76185450177815,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6756949101066425,
			"height": 18.919457482986786,
			"seed": 1521384192,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6756949101066425
				],
				[
					-0.6756949101066425,
					-0.6756949101066425
				],
				[
					-0.6756949101066425,
					1.3513898202133419
				],
				[
					-0.6756949101066425,
					8.108338921280051
				],
				[
					-0.6756949101066425,
					14.86528802234676
				],
				[
					-0.6756949101066425,
					18.243762572880144
				],
				[
					-0.6756949101066425,
					18.243762572880144
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0784110426902771,
				0.12968221306800842,
				0.16934137046337128,
				0.21408069133758545,
				0.2194155901670456,
				0.020423492416739464,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 890691598,
			"isDeleted": false,
			"id": "g7Lh6jvXms3VKANjjzthX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 351.9665684277332,
			"y": -57.27504102996471,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6756949101066425,
			"height": 6.08125419096001,
			"seed": 2015107840,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6756949101066425
				],
				[
					0,
					2.0270847303199844
				],
				[
					0,
					3.3784745505333262
				],
				[
					0,
					6.08125419096001
				],
				[
					0.6756949101066425,
					6.08125419096001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12399133294820786,
				0.17225201427936554,
				0.06890719383955002,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1951494098,
			"isDeleted": false,
			"id": "EXtJwVJsV6O6OoaZYXniO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 352.64226333783984,
			"y": -62.68060031081808,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.0001,
			"height": 0.0001,
			"seed": 1893235456,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
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
			"version": 56,
			"versionNonce": 1201385038,
			"isDeleted": false,
			"id": "jIkulAY2sabv8SN6G3IY9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 356.69643279847986,
			"y": -55.92365120975137,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.4055592808533675,
			"height": 6.756949101066709,
			"seed": 1925602048,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6756949101066425,
					0.6756949101066425
				],
				[
					-0.6756949101066425,
					2.0270847303199844
				],
				[
					-0.6756949101066425,
					4.054169460640026
				],
				[
					2.027084730320041,
					4.729864370746668
				],
				[
					4.054169460640026,
					3.3784745505333262
				],
				[
					4.729864370746725,
					-0.6756949101066994
				],
				[
					0.6756949101066994,
					-2.027084730320041
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
				0.07866747677326202,
				0.14710599184036255,
				0.1728433221578598,
				0.1861601620912552,
				0.22449402511119843,
				0.04230285808444023,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1408738706,
			"isDeleted": false,
			"id": "5jp_kXzYY1p997iptc38i",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 359.39921243890655,
			"y": -53.896566479431385,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.378474550533383,
			"height": 0,
			"seed": 1624587008,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6756949101066994,
					0
				],
				[
					3.378474550533383,
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
				0.11595398187637329,
				0.11844003200531006,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 61,
			"versionNonce": 1156363406,
			"isDeleted": false,
			"id": "4BuMIbSUssswx-qXvzsPc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 366.15616153997325,
			"y": -66.7347697714581,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.432644011173409,
			"height": 16.216677842560102,
			"seed": 1013775104,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6756949101066425,
					-0.6756949101066994
				],
				[
					-0.6756949101066425,
					-1.3513898202133419
				],
				[
					-0.6756949101066425,
					-0.6756949101066994
				],
				[
					-0.6756949101066425,
					4.729864370746668
				],
				[
					-0.6756949101066425,
					9.459728741493393
				],
				[
					-0.6756949101066425,
					10.811118561706735
				],
				[
					0.6756949101066994,
					10.135423651600036
				],
				[
					4.054169460640026,
					9.459728741493393
				],
				[
					6.081254190960067,
					11.486813471813377
				],
				[
					4.729864370746725,
					14.189593112240061
				],
				[
					0.6756949101066994,
					14.86528802234676
				],
				[
					-1.3513898202133419,
					14.86528802234676
				],
				[
					-0.6756949101066425,
					14.189593112240061
				],
				[
					0,
					13.513898202133419
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1166086420416832,
				0.15944039821624756,
				0.20390066504478455,
				0.22649721801280975,
				0.18409082293510437,
				0.14338818192481995,
				0.13763552904129028,
				0.18471276760101318,
				0.2581714391708374,
				0.24781738221645355,
				0.1616915911436081,
				0.008318847976624966,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1422992210,
			"isDeleted": false,
			"id": "inFAZW3YY3kWkTDnx6E2y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 373.58880555114666,
			"y": -56.59934611985807,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.351389820213285,
			"height": 6.081254190960067,
			"seed": 1167522560,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6756949101066994
				],
				[
					0.6756949101066425,
					2.027084730320041
				],
				[
					0.6756949101066425,
					4.054169460640026
				],
				[
					1.351389820213285,
					6.081254190960067
				],
				[
					1.351389820213285,
					6.081254190960067
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.19166699051856995,
				0.25885599851608276,
				0.135487362742424,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1992487630,
			"isDeleted": false,
			"id": "ez1f-3iriv8xYES7SkpRG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 376.2915851915733,
			"y": -60.653515580498095,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6756949101066425,
			"height": 0,
			"seed": 525294336,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6756949101066425,
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
			"version": 52,
			"versionNonce": 20244754,
			"isDeleted": false,
			"id": "L8ieQOO4FJxJyPpbWQKaL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 383.04853429264,
			"y": -72.14032905231147,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.027084730320041,
			"height": 18.919457482986786,
			"seed": 995523328,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6756949101066425
				],
				[
					0,
					6.08125419096001
				],
				[
					1.3513898202133419,
					15.540982932453403
				],
				[
					2.027084730320041,
					18.919457482986786
				],
				[
					2.027084730320041,
					18.243762572880087
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11883798241615295,
				0.22551998496055603,
				0.2694700062274933,
				0.02877935767173767,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 129460494,
			"isDeleted": false,
			"id": "hW5U157qsczoqVDVEzWgs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 387.7783986633867,
			"y": -59.977820670391395,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6756949101066425,
			"height": 6.08125419096001,
			"seed": 1870584576,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6756949101066425
				],
				[
					0,
					1.3513898202133419
				],
				[
					0,
					2.0270847303199844
				],
				[
					0,
					5.4055592808533675
				],
				[
					0.6756949101066425,
					6.08125419096001
				],
				[
					0.6756949101066425,
					6.08125419096001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08227398991584778,
				0.10334277153015137,
				0.1757747232913971,
				0.19752074778079987,
				0.0399009995162487,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 10090194,
			"isDeleted": false,
			"id": "VIOwOjw2lqoz7IlDjRD9W",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 390.4811783038134,
			"y": -65.38337995124476,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 0.6756949101066994,
			"seed": 783538944,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6756949101066994
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
				0.14411526918411255,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1732450126,
			"isDeleted": false,
			"id": "AUyC9_i7jz5DwlLCU5NW9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 397.2381274048801,
			"y": -74.84310869273816,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3513898202133419,
			"height": 23.649321853733454,
			"seed": 468384512,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6756949101066425
				],
				[
					1.3513898202133419,
					6.756949101066709
				],
				[
					1.3513898202133419,
					18.243762572880087
				],
				[
					0.6756949101066425,
					23.649321853733454
				],
				[
					0.6756949101066425,
					22.297932033520112
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13332806527614594,
				0.20719991624355316,
				0.24428726732730865,
				0.023573027923703194,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1939295378,
			"isDeleted": false,
			"id": "eIgIfYfT03ZNzrUUUzc0P",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 392.5082630341334,
			"y": -61.32921049060474,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.78403383138675,
			"height": 1.3513898202133419,
			"seed": 472079104,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405044,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6756949101066994,
					0
				],
				[
					1.3513898202133419,
					0
				],
				[
					8.108338921280051,
					1.3513898202133419
				],
				[
					8.78403383138675,
					1.3513898202133419
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10808200389146805,
				0.12588366866111755,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 767491470,
			"isDeleted": false,
			"id": "gZb3N_L00NTugC3pxdU-a",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 403.3193815958401,
			"y": -60.653515580498095,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.7569491010666525,
			"height": 2.7027796404266837,
			"seed": 1856183040,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6756949101066994,
					0.6756949101066994
				],
				[
					6.08125419096001,
					2.027084730320041
				],
				[
					6.7569491010666525,
					2.7027796404266837
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06667406857013702,
				0.06567056477069855,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1340336722,
			"isDeleted": false,
			"id": "LP4gmqqQdwTGAyXEALJ-x",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 414.13050015754686,
			"y": -62.004905400711436,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.108338921280051,
			"height": 26.352101494160138,
			"seed": 1045576448,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6756949101066994
				],
				[
					-0.6756949101066994,
					2.027084730320041
				],
				[
					-3.378474550533383,
					14.189593112240118
				],
				[
					-7.432644011173409,
					25.000711673946796
				],
				[
					-8.108338921280051,
					26.352101494160138
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11795999109745026,
				0.2162735015153885,
				0.3333350121974945,
				0.20435039699077606,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 6560718,
			"isDeleted": false,
			"id": "069Z3wtP-odhFSR4NyaI2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 416.52347171157584,
			"y": -102.34907012512355,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.293992908158657,
			"height": 19.30290834771415,
			"seed": 389192448,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7149225313968373
				],
				[
					0.7149225313967804,
					6.434302782571422
				],
				[
					2.144767594190455,
					15.728295690730079
				],
				[
					2.144767594190455,
					18.58798581631737
				],
				[
					0,
					15.013373159333298
				],
				[
					-0.7149225313968373,
					7.864147845365039
				],
				[
					1.4298450627936177,
					1.4298450627936745
				],
				[
					5.7193802511745275,
					-0.7149225313967804
				],
				[
					8.57907037676182,
					1.4298450627936745
				],
				[
					7.149225313968202,
					6.434302782571422
				],
				[
					4.28953518838091,
					9.293992908158714
				],
				[
					2.8596901255872353,
					9.293992908158714
				],
				[
					2.8596901255872353,
					8.579070376761877
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15867798030376434,
				0.17844364047050476,
				0.16898904740810394,
				0.1608729213476181,
				0.10805642604827881,
				0.0924062505364418,
				0.14724093675613403,
				0.19219696521759033,
				0.22194162011146545,
				0.24600869417190552,
				0.19285565614700317,
				0.006347137503325939,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1012322322,
			"isDeleted": false,
			"id": "6BxNsKYUFltOFAHD5WHQP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 427.96223221392495,
			"y": -100.91922506232987,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.149225313968202,
			"height": 9.293992908158714,
			"seed": 122944256,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7149225313968373,
					0
				],
				[
					-1.4298450627936177,
					0.7149225313968373
				],
				[
					-1.4298450627936177,
					1.4298450627936177
				],
				[
					-2.144767594190455,
					5.719380251174584
				],
				[
					0.7149225313968373,
					7.864147845365039
				],
				[
					4.289535188380967,
					7.149225313968202
				],
				[
					5.004457719777747,
					2.859690125587292
				],
				[
					4.289535188380967,
					-0.7149225313968373
				],
				[
					0,
					-1.4298450627936745
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
				0.08289999514818192,
				0.12521399557590485,
				0.17504599690437317,
				0.2371719926595688,
				0.22926662862300873,
				0.20639489591121674,
				0.2123592495918274,
				0.21694906055927277,
				0.033144377171993256,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1967878670,
			"isDeleted": false,
			"id": "2Ipxr9Du22nzfOM8K1i59",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 428.6771547453218,
			"y": -97.3446124053458,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.28953518838091,
			"height": 1.4298450627936745,
			"seed": 2137791232,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7149225313968373
				],
				[
					0.7149225313968373,
					0.7149225313968373
				],
				[
					2.144767594190455,
					1.4298450627936745
				],
				[
					4.28953518838091,
					1.4298450627936745
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
				0.11331597715616226,
				0.15672799944877625,
				0.10448602586984634,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1827077586,
			"isDeleted": false,
			"id": "nWgcFs-MF_uRkG5fd9DHi",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 439.4009927162741,
			"y": -101.63414759372671,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.28953518838091,
			"height": 8.579070376761877,
			"seed": 224467712,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7149225313968373,
					-0.7149225313968373
				],
				[
					-1.4298450627936745,
					-0.7149225313968373
				],
				[
					-2.859690125587292,
					0
				],
				[
					-2.144767594190455,
					2.144767594190455
				],
				[
					0,
					5.719380251174584
				],
				[
					0.7149225313967804,
					7.864147845365039
				],
				[
					-0.7149225313968373,
					7.864147845365039
				],
				[
					-3.5746126569841294,
					6.434302782571422
				],
				[
					-3.5746126569841294,
					5.719380251174584
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08221200853586197,
				0.09724200516939163,
				0.1399913877248764,
				0.15944357216358185,
				0.15149837732315063,
				0.17094586789608002,
				0.21447217464447021,
				0.021549195051193237,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 2003697742,
			"isDeleted": false,
			"id": "vAasxhiKCFfk0Wz8yT23s",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 445.1203729674487,
			"y": -103.77891518791716,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.434302782571422,
			"height": 11.438760502349112,
			"seed": 698874624,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.4298450627936745,
					0.7149225313968373
				],
				[
					-2.859690125587292,
					1.4298450627936177
				],
				[
					-3.5746126569841294,
					2.144767594190455
				],
				[
					-3.5746126569841294,
					3.5746126569841294
				],
				[
					0,
					6.434302782571365
				],
				[
					2.144767594190455,
					9.293992908158657
				],
				[
					1.4298450627936177,
					10.723837970952331
				],
				[
					-2.1447675941905118,
					11.438760502349112
				],
				[
					-4.289535188380967,
					8.579070376761877
				],
				[
					-3.5746126569841294,
					8.579070376761877
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09794998168945312,
				0.14590200781822205,
				0.16499698162078857,
				0.15623721480369568,
				0.15579503774642944,
				0.2193404883146286,
				0.19440200924873352,
				0.002031982410699129,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 2125165458,
			"isDeleted": false,
			"id": "Njh8eSsCG_WRL-MozS6TF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 450.12483068722645,
			"y": -102.34907012512355,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.008915439555551,
			"height": 8.57907037676182,
			"seed": 770145024,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7149225313968373,
					0
				],
				[
					-1.4298450627936745,
					1.4298450627936745
				],
				[
					-2.1447675941905118,
					5.004457719777747
				],
				[
					0,
					7.864147845365039
				],
				[
					2.144767594190455,
					7.149225313968259
				],
				[
					2.859690125587292,
					2.859690125587292
				],
				[
					3.5746126569841294,
					1.4298450627936745
				],
				[
					3.5746126569841294,
					4.289535188380967
				],
				[
					4.289535188380853,
					7.864147845365039
				],
				[
					7.149225313968202,
					7.864147845365039
				],
				[
					7.864147845365039,
					2.859690125587292
				],
				[
					7.149225313968202,
					-0.7149225313967804
				],
				[
					7.149225313968202,
					-0.7149225313967804
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12058526277542114,
				0.18836401402950287,
				0.2181200534105301,
				0.1828135997056961,
				0.12423733621835709,
				0.10593200474977493,
				0.12411490082740784,
				0.15979604423046112,
				0.1873423159122467,
				0.20367111265659332,
				0.039486113935709,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 715441806,
			"isDeleted": false,
			"id": "9rXTg3tirvvZ0rQZHDH7i",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 464.4232813151629,
			"y": -110.21321797048859,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.579070376761933,
			"height": 17.158140753523753,
			"seed": 1566890752,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4298450627935608,
					2.859690125587292
				],
				[
					2.8596901255872353,
					8.579070376761877
				],
				[
					2.8596901255872353,
					10.008915439555551
				],
				[
					0.7149225313967236,
					9.293992908158714
				],
				[
					-2.859690125587349,
					9.293992908158714
				],
				[
					-4.2895351883810235,
					12.868605565142786
				],
				[
					-2.1447675941905118,
					16.443218222126916
				],
				[
					4.28953518838091,
					17.158140753523753
				],
				[
					4.28953518838091,
					17.158140753523753
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.20758400857448578,
				0.2470303624868393,
				0.21628311276435852,
				0.14644671976566315,
				0.12121545523405075,
				0.19555670022964478,
				0.30499932169914246,
				0.13530544936656952,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 63,
			"versionNonce": 1406873938,
			"isDeleted": false,
			"id": "jiv1SGHGbteiym0-APGIO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 439.4009927162741,
			"y": -63.02833089829835,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.298450627936404,
			"height": 9.293992908158714,
			"seed": 2072230656,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7149225313968373,
					0
				],
				[
					-2.144767594190455,
					0
				],
				[
					-3.5746126569841294,
					1.4298450627936745
				],
				[
					-5.004457719777747,
					5.719380251174584
				],
				[
					-2.859690125587292,
					9.293992908158714
				],
				[
					0.7149225313967804,
					9.293992908158714
				],
				[
					2.144767594190455,
					7.864147845365039
				],
				[
					2.144767594190455,
					8.579070376761877
				],
				[
					4.28953518838091,
					9.293992908158714
				],
				[
					7.864147845365039,
					8.579070376761877
				],
				[
					9.293992908158657,
					5.004457719777747
				],
				[
					7.864147845365039,
					1.4298450627936745
				],
				[
					3.5746126569840726,
					0
				],
				[
					1.4298450627936177,
					3.5746126569841294
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
				0.08104800432920456,
				0.14981000125408173,
				0.2028486281633377,
				0.21337106823921204,
				0.1797337681055069,
				0.11889651417732239,
				0.10346725583076477,
				0.13971762359142303,
				0.16332781314849854,
				0.17697487771511078,
				0.18342261016368866,
				0.18370452523231506,
				0.17441369593143463,
				0.024809418246150017,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1336460494,
			"isDeleted": false,
			"id": "DC7AG7O5a8_MISDZGIzXL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 450.12483068722645,
			"y": -62.31340836690151,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.434302782571365,
			"height": 7.864147845365039,
			"seed": 1429928704,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7149225313967804,
					2.144767594190455
				],
				[
					2.144767594190455,
					5.719380251174584
				],
				[
					3.5746126569841294,
					0.7149225313968373
				],
				[
					5.7193802511745275,
					-1.4298450627936745
				],
				[
					6.434302782571365,
					1.4298450627936177
				],
				[
					6.434302782571365,
					6.434302782571365
				],
				[
					6.434302782571365,
					5.719380251174584
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1716659814119339,
				0.18725766241550446,
				0.062470581382513046,
				0.09804104268550873,
				0.1934090256690979,
				0.03941876068711281,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1875719954,
			"isDeleted": false,
			"id": "q3jqe8KQMyLXKE45v1A5W",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 457.27405600119465,
			"y": -63.74325342969519,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.8641478453649825,
			"height": 8.57907037676182,
			"seed": 1217960704,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7149225313968373
				],
				[
					2.1447675941905118,
					4.289535188380967
				],
				[
					2.8596901255872353,
					5.719380251174584
				],
				[
					3.5746126569840726,
					2.1447675941905118
				],
				[
					5.719380251174584,
					-0.7149225313967804
				],
				[
					7.149225313968259,
					0.7149225313968373
				],
				[
					7.8641478453649825,
					6.434302782571422
				],
				[
					7.149225313968259,
					7.864147845365039
				],
				[
					7.149225313968259,
					7.864147845365039
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14183862507343292,
				0.2132926881313324,
				0.15685434639453888,
				0.06839410215616226,
				0.07631344348192215,
				0.17313137650489807,
				0.22276058793067932,
				0.03919891268014908,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 672332558,
			"isDeleted": false,
			"id": "hJGln1EqIsEVvzTv3UTuK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 469.42773903494066,
			"y": -63.02833089829835,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.149225313968259,
			"height": 7.149225313968202,
			"seed": 1183808256,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7149225313967236,
					0
				],
				[
					2.144767594190398,
					0
				],
				[
					2.8596901255872353,
					-0.7149225313968373
				],
				[
					2.144767594190398,
					-1.4298450627936177
				],
				[
					-0.7149225313968373,
					-0.7149225313968373
				],
				[
					-2.1447675941905118,
					2.144767594190455
				],
				[
					0,
					5.719380251174584
				],
				[
					5.004457719777747,
					5.004457719777747
				],
				[
					5.004457719777747,
					4.28953518838091
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07686600089073181,
				0.13590601086616516,
				0.18376514315605164,
				0.17417526245117188,
				0.1507929414510727,
				0.20117804408073425,
				0.2261914312839508,
				0.047624360769987106,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 1392018642,
			"isDeleted": false,
			"id": "hpIOou0jd7GEgudQ9f4OC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 479.43665447449615,
			"y": -64.45817596109197,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.29399290815877,
			"height": 7.149225313968202,
			"seed": 143809280,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7149225313968373,
					0
				],
				[
					-1.4298450627936745,
					0.7149225313967804
				],
				[
					-3.5746126569841863,
					1.4298450627936177
				],
				[
					-4.2895351883810235,
					4.28953518838091
				],
				[
					-3.5746126569841863,
					6.434302782571365
				],
				[
					0.7149225313967236,
					7.149225313968202
				],
				[
					4.28953518838091,
					4.28953518838091
				],
				[
					5.004457719777747,
					3.5746126569840726
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09109597653150558,
				0.11193197965621948,
				0.14168792963027954,
				0.18149249255657196,
				0.21780596673488617,
				0.17567571997642517,
				0.007313293404877186,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1516005710,
			"isDeleted": false,
			"id": "pZnzLQpboY52leD6GN4G1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 485.87095725706746,
			"y": -76.61185899483797,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4298450627936745,
			"height": 20.732753410507826,
			"seed": 275553024,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7149225313967804
				],
				[
					0,
					-1.4298450627936177
				],
				[
					0,
					3.5746126569841294
				],
				[
					0.7149225313968373,
					11.438760502349169
				],
				[
					1.4298450627936745,
					18.58798581631737
				],
				[
					1.4298450627936745,
					19.302908347714208
				],
				[
					1.4298450627936745,
					19.302908347714208
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10251397639513016,
				0.19569799304008484,
				0.23709768056869507,
				0.21687231957912445,
				0.10120837390422821,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1458838162,
			"isDeleted": false,
			"id": "b98WHlqjXNeit9RHNk5ms",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 482.2963446000834,
			"y": -66.60294355528242,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.008915439555494,
			"height": 0.7149225313968373,
			"seed": 1559640832,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7149225313968373,
					0
				],
				[
					2.859690125587349,
					0
				],
				[
					9.293992908158657,
					-0.7149225313968373
				],
				[
					10.008915439555494,
					-0.7149225313968373
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05598599091172218,
				0.12430243194103241,
				0.013594421558082104,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1440616334,
			"isDeleted": false,
			"id": "0jrfBffqHhDdyGdZdtMKp",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 493.0201825710357,
			"y": -65.88802102388564,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4298450627936745,
			"height": 6.434302782571422,
			"seed": 1808661248,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7149225313968373
				],
				[
					0,
					2.859690125587292
				],
				[
					0,
					4.289535188380967
				],
				[
					1.4298450627936745,
					6.434302782571422
				],
				[
					1.4298450627936745,
					6.434302782571422
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08901800215244293,
				0.10896200686693192,
				0.02433895878493786,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 175568978,
			"isDeleted": false,
			"id": "BMrHB0KGl2OF3-unnBjB4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 494.4500276338294,
			"y": -70.89247874366339,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4298450627936745,
			"height": 0,
			"seed": 963009280,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7149225313968373,
					0
				],
				[
					-1.4298450627936745,
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
				0.005499481223523617,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 919662030,
			"isDeleted": false,
			"id": "UfDUDlabI1ARinPsLlB6v",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 498.02464029081347,
			"y": -63.02833089829835,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.149225313968259,
			"height": 8.579070376761877,
			"seed": 2108037888,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					2.144767594190455
				],
				[
					1.4298450627936745,
					2.859690125587292
				],
				[
					2.1447675941905118,
					3.5746126569841294
				],
				[
					4.28953518838091,
					2.144767594190455
				],
				[
					5.004457719777747,
					-2.859690125587292
				],
				[
					1.4298450627936745,
					-5.004457719777747
				],
				[
					-2.1447675941905118,
					-5.004457719777747
				],
				[
					-1.4298450627936745,
					-1.4298450627936177
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
				0.11150399595499039,
				0.13429999351501465,
				0.15200680494308472,
				0.1190657690167427,
				0.13021600246429443,
				0.10134720057249069,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 223878674,
			"isDeleted": false,
			"id": "dsu0aXeL5ZZnAIAw4pvgP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 503.0290980105912,
			"y": -68.0327886180761,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.008915439555437,
			"height": 6.434302782571422,
			"seed": 431332096,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7149225313968373
				],
				[
					0.7149225313968373,
					0.7149225313968373
				],
				[
					1.4298450627936745,
					2.859690125587292
				],
				[
					2.859690125587349,
					5.719380251174584
				],
				[
					3.5746126569840726,
					4.28953518838091
				],
				[
					5.004457719777747,
					0.7149225313968373
				],
				[
					7.864147845365096,
					0
				],
				[
					10.008915439555437,
					6.434302782571422
				],
				[
					10.008915439555437,
					6.434302782571422
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0835539847612381,
				0.12174798548221588,
				0.20889998972415924,
				0.21452850103378296,
				0.10203881561756134,
				0.040327057242393494,
				0.1195305809378624,
				0.20912350714206696,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 709755918,
			"isDeleted": false,
			"id": "aMySvvyPVubyi7mu4WNzr",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 333.59245806954453,
			"y": -15.128521294711277,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.719380251174584,
			"height": 8.57907037676182,
			"seed": 600603392,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7149225313968373,
					0
				],
				[
					-2.1447675941905118,
					0.7149225313967804
				],
				[
					-3.5746126569841294,
					2.859690125587292
				],
				[
					-3.5746126569841294,
					6.434302782571365
				],
				[
					-2.1447675941905118,
					8.57907037676182
				],
				[
					1.4298450627936177,
					7.149225313968202
				],
				[
					2.144767594190455,
					7.149225313968202
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04725173860788345,
				0.11107473820447922,
				0.13517175614833832,
				0.15388867259025574,
				0.16292181611061096,
				0.019604399800300598,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1821281234,
			"isDeleted": false,
			"id": "vu0vTpCLQMjkkFUNexo-n",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 337.88199325792544,
			"y": -13.69867623191766,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.57907037676182,
			"height": 7.864147845365039,
			"seed": 796531456,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7149225313968373
				],
				[
					-0.7149225313968373,
					0.7149225313968373
				],
				[
					-1.4298450627936177,
					2.144767594190455
				],
				[
					-1.4298450627936177,
					5.004457719777747
				],
				[
					1.4298450627936177,
					6.434302782571422
				],
				[
					5.004457719777747,
					5.004457719777747
				],
				[
					7.149225313968202,
					0.7149225313968373
				],
				[
					6.434302782571422,
					-1.4298450627936177
				],
				[
					6.434302782571422,
					-1.4298450627936177
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07819399982690811,
				0.09522897005081177,
				0.12659478187561035,
				0.11961392313241959,
				0.11108031868934631,
				0.06980941444635391,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1380864590,
			"isDeleted": false,
			"id": "c_03Yud6inBr_nd4HjCCi",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 349.3207537602746,
			"y": -17.27328888890179,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.149225313968202,
			"height": 9.293992908158714,
			"seed": 1835072256,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7149225313968373,
					0
				],
				[
					-1.4298450627936745,
					0
				],
				[
					-2.859690125587292,
					1.4298450627936745
				],
				[
					-0.7149225313968373,
					4.289535188380967
				],
				[
					2.8596901255872353,
					6.434302782571422
				],
				[
					4.28953518838091,
					8.579070376761877
				],
				[
					1.4298450627936177,
					9.293992908158714
				],
				[
					-1.4298450627936745,
					7.864147845365039
				],
				[
					-1.4298450627936745,
					7.149225313968259
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04163198918104172,
				0.09314040839672089,
				0.10356857627630234,
				0.09641540795564651,
				0.1021246612071991,
				0.14468319714069366,
				0.1704053282737732,
				0.016672637313604355,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 2117157266,
			"isDeleted": false,
			"id": "5RN-p7w3l83t_zeHaIsC7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 359.3296691998301,
			"y": -28.7120493912509,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.144767594190455,
			"height": 20.01783087911099,
			"seed": 1163123456,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7149225313968373,
					0
				],
				[
					-1.4298450627936745,
					2.144767594190455
				],
				[
					-0.7149225313968373,
					8.579070376761877
				],
				[
					0,
					15.728295690730079
				],
				[
					0.7149225313967804,
					20.01783087911099
				],
				[
					0,
					20.01783087911099
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12537899613380432,
				0.18880599737167358,
				0.1901937574148178,
				0.028087280690670013,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 699062414,
			"isDeleted": false,
			"id": "-DI_ca_K0VT96nhlUY4NS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 352.8953664172587,
			"y": -15.128521294711277,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.723837970952331,
			"height": 0.7149225313968373,
			"seed": 529062656,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7149225313968373
				],
				[
					1.4298450627936745,
					-0.7149225313968373
				],
				[
					10.008915439555494,
					-0.7149225313968373
				],
				[
					10.723837970952331,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07036999613046646,
				0.030589722096920013,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1031225170,
			"isDeleted": false,
			"id": "KHwBBNammw7kSt8L1WHJn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 364.33412691960785,
			"y": -15.843443826108114,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.579070376761877,
			"height": 7.864147845365039,
			"seed": 132684544,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7149225313968373,
					1.4298450627936177
				],
				[
					-1.4298450627936745,
					2.859690125587292
				],
				[
					-1.4298450627936745,
					4.28953518838091
				],
				[
					1.4298450627936177,
					6.434302782571365
				],
				[
					5.719380251174584,
					5.719380251174584
				],
				[
					7.149225313968202,
					2.144767594190455
				],
				[
					5.004457719777747,
					-0.7149225313968373
				],
				[
					0.7149225313968373,
					-1.4298450627936745
				],
				[
					-1.4298450627936745,
					3.5746126569841294
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
				0.0749879777431488,
				0.09827600419521332,
				0.13576199114322662,
				0.14234976470470428,
				0.11725210398435593,
				0.09865759313106537,
				0.08969174325466156,
				0.09788626432418823,
				0.01216201763600111,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 61,
			"versionNonce": 1746704078,
			"isDeleted": false,
			"id": "pVs8UYLZjUR9-dgEglTg3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 370.05350717078244,
			"y": -16.55836635750495,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.723837970952275,
			"height": 7.864147845365039,
			"seed": 1014807296,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7149225313968373
				],
				[
					2.144767594190455,
					3.5746126569841294
				],
				[
					3.5746126569840726,
					6.434302782571422
				],
				[
					3.5746126569840726,
					5.004457719777747
				],
				[
					4.28953518838091,
					0
				],
				[
					5.7193802511745275,
					-1.4298450627936177
				],
				[
					6.434302782571365,
					1.4298450627936745
				],
				[
					6.434302782571365,
					5.004457719777747
				],
				[
					7.149225313968202,
					3.5746126569841294
				],
				[
					8.57907037676182,
					-0.7149225313968373
				],
				[
					10.008915439555494,
					-1.4298450627936177
				],
				[
					10.723837970952275,
					3.5746126569841294
				],
				[
					10.008915439555494,
					6.434302782571422
				],
				[
					9.293992908158657,
					6.434302782571422
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06899847090244293,
				0.13902734220027924,
				0.13461638987064362,
				0.07265603542327881,
				0.018435761332511902,
				0.054870057851076126,
				0.12637698650360107,
				0.14490850269794464,
				0.06615646183490753,
				0.029553283005952835,
				0.12351071089506149,
				0.18338283896446228,
				0.06333377212285995,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 649561362,
			"isDeleted": false,
			"id": "kzOZHTZ5grNi88qjG3i2K",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 384.35195779871884,
			"y": -16.55836635750495,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.719380251174584,
			"height": 7.149225313968202,
			"seed": 1311161088,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7149225313968373,
					0
				],
				[
					1.4298450627936177,
					0
				],
				[
					2.144767594190455,
					-0.7149225313968373
				],
				[
					1.4298450627936177,
					-2.144767594190455
				],
				[
					-1.4298450627936177,
					-0.7149225313968373
				],
				[
					-2.144767594190455,
					2.859690125587292
				],
				[
					0.7149225313968373,
					5.004457719777747
				],
				[
					3.5746126569841294,
					4.289535188380967
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
				0.05517953634262085,
				0.12301458418369293,
				0.11689135432243347,
				0.10213525593280792,
				0.1287507861852646,
				0.16079601645469666,
				0.1447952538728714,
				0.00984802283346653,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1715244302,
			"isDeleted": false,
			"id": "LJF51WNwSWT465ifp-HUn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 389.3564155184966,
			"y": -19.418056483092244,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.719380251174584,
			"height": 10.008915439555494,
			"seed": 575027968,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.4298450627936745
				],
				[
					-0.7149225313968373,
					2.144767594190455
				],
				[
					-0.7149225313968373,
					5.719380251174584
				],
				[
					0,
					8.579070376761877
				],
				[
					0,
					9.293992908158714
				],
				[
					1.4298450627936745,
					5.004457719777747
				],
				[
					5.004457719777747,
					-0.7149225313967804
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
				0.06780456751585007,
				0.08234778046607971,
				0.1591004580259323,
				0.16481760144233704,
				0.14590591192245483,
				0.1201443150639534,
				0.04997595399618149,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 325653202,
			"isDeleted": false,
			"id": "v_jFXO_XiKqrFO0E6Muzm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 424.3876195569409,
			"y": -20.84790154588586,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.723837970952331,
			"height": 10.008915439555551,
			"seed": 2080447232,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7149225313967804,
					0
				],
				[
					1.4298450627936177,
					0
				],
				[
					4.28953518838091,
					-1.4298450627936745
				],
				[
					5.7193802511745275,
					-2.859690125587292
				],
				[
					3.5746126569840726,
					-4.289535188380967
				],
				[
					0,
					-2.144767594190455
				],
				[
					-1.4298450627936745,
					2.144767594190455
				],
				[
					1.4298450627936177,
					5.719380251174584
				],
				[
					5.7193802511745275,
					5.719380251174584
				],
				[
					9.293992908158657,
					2.859690125587292
				],
				[
					9.293992908158657,
					2.144767594190455
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09805856645107269,
				0.1243012398481369,
				0.15043005347251892,
				0.13530148565769196,
				0.09808621555566788,
				0.0971352830529213,
				0.14938712120056152,
				0.18031159043312073,
				0.1367710828781128,
				0.009926635771989822,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 25410382,
			"isDeleted": false,
			"id": "n3Kjy_wu3Up9VWObqmSYs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 430.82192233951224,
			"y": -23.707591671473153,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.864147845365039,
			"height": 5.719380251174584,
			"seed": 1623538432,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7149225313968373
				],
				[
					0,
					1.4298450627936177
				],
				[
					1.4298450627936745,
					2.144767594190455
				],
				[
					5.004457719777747,
					5.004457719777747
				],
				[
					7.864147845365039,
					5.719380251174584
				],
				[
					7.864147845365039,
					5.719380251174584
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1021822839975357,
				0.15145999193191528,
				0.18663360178470612,
				0.022921325638890266,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 371386514,
			"isDeleted": false,
			"id": "FGscJDEMKlv_UcPg4Wyhq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 439.4009927162741,
			"y": -26.567281797060446,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.579070376761877,
			"height": 10.723837970952331,
			"seed": 731527936,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7149225313968373,
					0
				],
				[
					-1.4298450627936745,
					0.7149225313968373
				],
				[
					-4.289535188380967,
					4.28953518838091
				],
				[
					-8.579070376761877,
					9.293992908158657
				],
				[
					-7.149225313968202,
					10.723837970952331
				],
				[
					-6.434302782571422,
					10.723837970952331
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0776856392621994,
				0.1769700050354004,
				0.22020645439624786,
				0.06174716353416443,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 4923790,
			"isDeleted": false,
			"id": "cXvz8yIr0Re2UIUQ3ALBv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 440.83083777906774,
			"y": -25.137436734266828,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.293992908158714,
			"height": 20.732753410507826,
			"seed": 292502272,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7149225313968373
				],
				[
					0,
					1.4298450627936745
				],
				[
					0,
					2.859690125587292
				],
				[
					1.4298450627936745,
					10.008915439555551
				],
				[
					1.4298450627936745,
					18.58798581631737
				],
				[
					0.7149225313968373,
					19.302908347714208
				],
				[
					-0.7149225313968373,
					11.438760502349169
				],
				[
					1.4298450627936745,
					2.1447675941905118
				],
				[
					7.149225313968202,
					-1.4298450627936177
				],
				[
					8.579070376761877,
					2.859690125587292
				],
				[
					5.719380251174584,
					7.864147845365039
				],
				[
					4.289535188380967,
					9.293992908158714
				],
				[
					4.289535188380967,
					8.579070376761877
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06096194311976433,
				0.10475426912307739,
				0.16097113490104675,
				0.16309374570846558,
				0.14602746069431305,
				0.07030364871025085,
				0.027800781652331352,
				0.060385435819625854,
				0.1655615270137787,
				0.1859397292137146,
				0.019946197047829628,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 61,
			"versionNonce": 1453065810,
			"isDeleted": false,
			"id": "l6b6t5FWii48kw1mTfB96",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 451.55467575002007,
			"y": -22.992669140076316,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.008915439555494,
			"height": 8.57907037676182,
			"seed": 795122432,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7149225313968373
				],
				[
					1.4298450627936745,
					-0.7149225313968373
				],
				[
					2.1447675941905118,
					-1.4298450627936745
				],
				[
					2.8596901255872353,
					-2.1447675941905118
				],
				[
					2.1447675941905118,
					-2.859690125587292
				],
				[
					-0.7149225313968373,
					-0.7149225313968373
				],
				[
					-0.7149225313968373,
					3.5746126569840726
				],
				[
					2.1447675941905118,
					5.004457719777747
				],
				[
					5.004457719777747,
					1.4298450627936177
				],
				[
					7.149225313968259,
					-2.1447675941905118
				],
				[
					8.57907037676182,
					-2.859690125587292
				],
				[
					9.293992908158657,
					1.4298450627936177
				],
				[
					8.57907037676182,
					5.7193802511745275
				],
				[
					8.57907037676182,
					5.004457719777747
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13710223138332367,
				0.14730365574359894,
				0.16545987129211426,
				0.1409764438867569,
				0.15733352303504944,
				0.2063056379556656,
				0.20944955945014954,
				0.14739766716957092,
				0.11428844928741455,
				0.195190891623497,
				0.24206015467643738,
				0.21203720569610596,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 63,
			"versionNonce": 1976287182,
			"isDeleted": false,
			"id": "2_EnKHs-CAdyfPsnjnXSA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 466.5680489093533,
			"y": -27.282204328457283,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.583528096539567,
			"height": 10.008915439555494,
			"seed": 89037568,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7149225313968373,
					0
				],
				[
					-2.8596901255872353,
					0
				],
				[
					-3.5746126569840726,
					0.7149225313968373
				],
				[
					-3.5746126569840726,
					2.859690125587292
				],
				[
					-1.4298450627936745,
					6.434302782571422
				],
				[
					-0.7149225313968373,
					8.579070376761877
				],
				[
					-1.4298450627936745,
					9.293992908158714
				],
				[
					-2.144767594190398,
					7.864147845365039
				],
				[
					0,
					5.004457719777747
				],
				[
					3.5746126569840726,
					2.859690125587292
				],
				[
					5.719380251174584,
					1.4298450627936745
				],
				[
					5.004457719777747,
					0.7149225313968373
				],
				[
					2.859690125587349,
					3.5746126569841294
				],
				[
					2.1447675941905118,
					8.579070376761877
				],
				[
					9.293992908158657,
					10.008915439555494
				],
				[
					10.008915439555494,
					9.293992908158714
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.03999999910593033,
				0.11424798518419266,
				0.15612798929214478,
				0.18205685913562775,
				0.14846539497375488,
				0.1414860486984253,
				0.1331785023212433,
				0.09707852452993393,
				0.10529889166355133,
				0.11509799212217331,
				0.14468689262866974,
				0.14103619754314423,
				0.16957491636276245,
				0.22245477139949799,
				0.1797102391719818,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 90,
			"versionNonce": 1839950866,
			"isDeleted": false,
			"id": "laukCnO9rVhwQlT3Esmqe",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 224.64427858249667,
			"y": -61.46758459855141,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 103.12668680965635,
			"height": 98.43911013649011,
			"seed": 1611520768,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.562525557722097,
					0
				],
				[
					-7.031365009749322,
					2.3437883365830885
				],
				[
					-13.28146724063754,
					6.250102230888274
				],
				[
					-17.969043913803773,
					10.93767890405445
				],
				[
					-21.8753578081089,
					14.843992798359636
				],
				[
					-26.562934481275136,
					20.31283225038686
				],
				[
					-28.906722817858224,
					25.781671702414087
				],
				[
					-28.906722817858224,
					32.81303671216335
				],
				[
					-28.125460038997176,
					42.18819005849576
				],
				[
					-26.562934481275136,
					52.344606183689166
				],
				[
					-21.8753578081089,
					64.06354786660467
				],
				[
					-15.625255577220685,
					74.21996399179807
				],
				[
					-7.031365009749322,
					80.47006622268634
				],
				[
					1.56252555772204,
					84.37638011699153
				],
				[
					10.93767890405445,
					87.50143123243566
				],
				[
					21.094095029247853,
					88.28269401129666
				],
				[
					31.250511154441313,
					89.0639567901577
				],
				[
					41.406927279634715,
					89.84521956901875
				],
				[
					50.782080625967126,
					86.72016845357462
				],
				[
					57.81344563571639,
					82.03259178040844
				],
				[
					64.84481064546566,
					78.12627788610325
				],
				[
					70.31365009749294,
					72.65743843407603
				],
				[
					72.65743843407603,
					67.1885989820488
				],
				[
					74.21996399179812,
					62.501022308882625
				],
				[
					74.21996399179812,
					55.4696572991333
				],
				[
					73.43870121293702,
					47.65702951052299
				],
				[
					71.87617565521492,
					37.500613385329586
				],
				[
					70.31365009749294,
					28.906722817858224
				],
				[
					67.96986176090985,
					21.8753578081089
				],
				[
					66.40733620318775,
					15.625255577220628
				],
				[
					64.06354786660467,
					10.93767890405445
				],
				[
					60.15723397229948,
					6.250102230888274
				],
				[
					56.250920077994294,
					1.562525557722097
				],
				[
					52.344606183689166,
					-1.56252555772204
				],
				[
					46.87576673166194,
					-3.125051115444137
				],
				[
					40.62566450077367,
					-4.687576673166177
				],
				[
					34.37556226988539,
					-5.468839452027225
				],
				[
					28.906722817858167,
					-5.468839452027225
				],
				[
					23.437883365830942,
					-5.468839452027225
				],
				[
					17.969043913803716,
					-5.468839452027225
				],
				[
					14.062730019498588,
					-7.0313650097492655
				],
				[
					7.0313650097492655,
					-8.593890567471362
				],
				[
					6.250102230888274,
					-7.812627788610314
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.27689799666404724,
				0.3105030655860901,
				0.3186494708061218,
				0.3305540680885315,
				0.33684784173965454,
				0.33537232875823975,
				0.3444931209087372,
				0.3551080524921417,
				0.3677155375480652,
				0.38202226161956787,
				0.39173781871795654,
				0.3938904404640198,
				0.372287780046463,
				0.387666791677475,
				0.393951952457428,
				0.41380730271339417,
				0.42840784788131714,
				0.46525347232818604,
				0.47096720337867737,
				0.4817233681678772,
				0.47199320793151855,
				0.45770463347435,
				0.45993828773498535,
				0.4337013363838196,
				0.42345041036605835,
				0.4319847524166107,
				0.4272659718990326,
				0.44217193126678467,
				0.4876081049442291,
				0.4975978136062622,
				0.5058834552764893,
				0.5062791109085083,
				0.4977002739906311,
				0.5049275159835815,
				0.5093490481376648,
				0.5190053582191467,
				0.5211414098739624,
				0.5171746611595154,
				0.5103580951690674,
				0.5109466314315796,
				0.4650445580482483,
				0.23926229774951935,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 639538702,
			"isDeleted": false,
			"id": "mXvR6Ipn0lHuKV9H_-FNV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 226.98806691907976,
			"y": -91.93683297413168,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.625255577220628,
			"height": 15.625255577220628,
			"seed": 2121136896,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7812627788610484,
					0
				],
				[
					-1.56252555772204,
					0
				],
				[
					-0.7812627788610484,
					0.7812627788610484
				],
				[
					5.468839452027225,
					6.250102230888274
				],
				[
					11.7189416829155,
					12.500204461776548
				],
				[
					14.062730019498588,
					15.625255577220628
				],
				[
					13.28146724063754,
					14.843992798359636
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1205659806728363,
				0.16317600011825562,
				0.23586998879909515,
				0.24201275408267975,
				0.0328511968255043,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1095244242,
			"isDeleted": false,
			"id": "tAe48V3qtC-2xDE0w8Qoc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 238.70700860199526,
			"y": -91.93683297413168,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.062730019498588,
			"height": 15.625255577220628,
			"seed": 275487488,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7812627788610484,
					0
				],
				[
					-3.125051115444137,
					0.7812627788610484
				],
				[
					-8.593890567471362,
					7.031365009749322
				],
				[
					-14.062730019498588,
					14.062730019498588
				],
				[
					-14.062730019498588,
					15.625255577220628
				],
				[
					-14.062730019498588,
					15.625255577220628
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.19002899527549744,
				0.2764979898929596,
				0.3325279951095581,
				0.09077093750238419,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 75,
			"versionNonce": 1782359118,
			"isDeleted": false,
			"id": "b0z_F8XVX-XNCZKaAFUPb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 326.20843983443086,
			"y": -96.62440964729785,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 21.8753578081089,
			"height": 105.47047514623938,
			"seed": 115383040,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7812627788609916,
					0
				],
				[
					-1.562525557722097,
					0
				],
				[
					-3.9063138943051854,
					-0.7812627788610484
				],
				[
					-8.593890567471362,
					0
				],
				[
					-13.28146724063754,
					2.3437883365830885
				],
				[
					-16.40651835608162,
					6.250102230888274
				],
				[
					-18.750306692664708,
					11.7189416829155
				],
				[
					-19.531569471525813,
					17.187781134942725
				],
				[
					-18.750306692664708,
					24.21914614469199
				],
				[
					-16.40651835608162,
					29.687985596719216
				],
				[
					-13.28146724063754,
					35.93808782760749
				],
				[
					-11.718941682915442,
					41.406927279634715
				],
				[
					-11.718941682915442,
					46.09450395280089
				],
				[
					-14.843992798359636,
					50.00081784710608
				],
				[
					-17.187781134942725,
					53.125868962550214
				],
				[
					-17.969043913803716,
					55.4696572991333
				],
				[
					-16.40651835608162,
					57.81344563571639
				],
				[
					-13.28146724063754,
					60.93849675116053
				],
				[
					-10.93767890405445,
					65.6260734243267
				],
				[
					-10.93767890405445,
					70.31365009749288
				],
				[
					-11.718941682915442,
					75.78248954952016
				],
				[
					-13.28146724063754,
					82.03259178040838
				],
				[
					-14.843992798359636,
					89.8452195690187
				],
				[
					-14.843992798359636,
					97.65784735762907
				],
				[
					-12.500204461776548,
					102.34542403079524
				],
				[
					-5.468839452027169,
					104.68921236737833
				],
				[
					1.562525557722097,
					103.12668680965629
				],
				[
					2.3437883365830885,
					102.34542403079524
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05291299521923065,
				0.072434201836586,
				0.15398846566677094,
				0.1945275217294693,
				0.21937145292758942,
				0.2404017299413681,
				0.24034860730171204,
				0.25859495997428894,
				0.28274673223495483,
				0.2945815622806549,
				0.3071646988391876,
				0.33427050709724426,
				0.34533166885375977,
				0.3413026034832001,
				0.35648244619369507,
				0.36321625113487244,
				0.37716615200042725,
				0.3894121050834656,
				0.4119264483451843,
				0.4396876096725464,
				0.4444790482521057,
				0.4154003858566284,
				0.40942203998565674,
				0.4357925057411194,
				0.46013113856315613,
				0.3954848647117615,
				0.1297772228717804,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1619595154,
			"isDeleted": false,
			"id": "zM7LBbMeXuHbheOBPdkDN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -57.39158458633608,
			"y": -47.404854579052824,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.9063138943051854,
			"height": 10.156416125193402,
			"seed": 1821334272,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7812627788610484,
					-3.9063138943051854
				],
				[
					2.343788336583117,
					-7.0313650097492655
				],
				[
					3.9063138943051854,
					-9.37515334633241
				],
				[
					3.9063138943051854,
					-10.156416125193402
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2663557231426239,
				0.2567160129547119,
				0.13011550903320312,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 335473294,
			"isDeleted": false,
			"id": "Zcs-MEQ9xLChg5vKaM9rH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -48.01643124000367,
			"y": -67.71768682943969,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.031365009749294,
			"height": 11.718941682915442,
			"seed": 2114919168,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7812627788609916
				],
				[
					0,
					-1.56252555772204
				],
				[
					2.3437883365830885,
					-6.250102230888217
				],
				[
					4.687576673166177,
					-9.375153346332354
				],
				[
					6.2501022308882455,
					-11.718941682915442
				],
				[
					7.031365009749294,
					-11.718941682915442
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10762197524309158,
				0.21747399866580963,
				0.28582799434661865,
				0.27314063906669617,
				0.03910369798541069,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1604668754,
			"isDeleted": false,
			"id": "KozpiviBJxy24jo7WrCqu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -34.73496399936613,
			"y": -88.81178185868754,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.468839452027225,
			"height": 8.593890567471362,
			"seed": 2030312192,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7812627788610484
				],
				[
					1.5625255577220685,
					-3.125051115444137
				],
				[
					3.906313894305157,
					-6.250102230888274
				],
				[
					5.468839452027225,
					-8.593890567471362
				],
				[
					5.468839452027225,
					-8.593890567471362
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05559399351477623,
				0.2217099964618683,
				0.18318243324756622,
				0.0363650806248188,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1377724622,
			"isDeleted": false,
			"id": "WvO6fVAyEcHDHufKVFE9x",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -19.890971201006522,
			"y": -108.34335133021335,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.812627788610342,
			"height": 9.375153346332382,
			"seed": 113277696,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.78126277886102
				],
				[
					0,
					-2.3437883365830885
				],
				[
					3.125051115444137,
					-4.687576673166205
				],
				[
					7.031365009749294,
					-9.375153346332382
				],
				[
					7.812627788610342,
					-9.375153346332382
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13675500452518463,
				0.24285800755023956,
				0.2594960033893585,
				0.034638457000255585,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 871617298,
			"isDeleted": false,
			"id": "KGukAvd95j0WMgGpAu51K",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1.1406645083417288,
			"y": -130.21870913832225,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.593890567471362,
			"height": 7.031365009749294,
			"seed": 371776256,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.78126277886102,
					-0.7812627788610484
				],
				[
					1.5625255577220685,
					-2.343788336583117
				],
				[
					4.687576673166205,
					-4.687576673166205
				],
				[
					8.593890567471362,
					-6.250102230888274
				],
				[
					8.593890567471362,
					-7.031365009749294
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13910526037216187,
				0.22608798742294312,
				0.24240536987781525,
				0.03162804991006851,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 338960142,
			"isDeleted": false,
			"id": "ajTEGFmT6wYk9glgU6TyU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 12.14080273229581,
			"y": -140.37512526351568,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.031365009749294,
			"height": 3.906313894305157,
			"seed": 12401408,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.78126277886102
				],
				[
					2.343788336583117,
					-1.5625255577220685
				],
				[
					6.250102230888274,
					-3.125051115444137
				],
				[
					7.031365009749294,
					-3.906313894305157
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08827920258045197,
				0.20798198878765106,
				0.04807742312550545,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 267100370,
			"isDeleted": false,
			"id": "HKDyCspYTbOmobi0q3LQ5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 25.42226997293335,
			"y": -152.09406694643118,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.062730019498588,
			"height": 13.281467240637568,
			"seed": 1314192128,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.78126277886102
				],
				[
					3.9063138943051854,
					-3.1250511154441085
				],
				[
					10.937678904054508,
					-4.687576673166177
				],
				[
					14.062730019498588,
					-5.468839452027225
				],
				[
					13.281467240637596,
					-2.3437883365830885
				],
				[
					10.937678904054508,
					0.7812627788610484
				],
				[
					8.593890567471362,
					5.468839452027225
				],
				[
					6.250102230888274,
					7.812627788610342
				],
				[
					7.031365009749322,
					7.812627788610342
				],
				[
					7.031365009749322,
					7.812627788610342
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14054599404335022,
				0.3374119997024536,
				0.3651279807090759,
				0.3470342457294464,
				0.3247223198413849,
				0.3703896999359131,
				0.4451860785484314,
				0.4917592704296112,
				0.14191223680973053,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1857621326,
			"isDeleted": false,
			"id": "NlGTcqSy3WaJY0l40tc6t",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 83.2357156086498,
			"y": -143.50017637895982,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.56252555772204,
			"height": 13.281467240637568,
			"seed": 1460960000,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7812627788610484
				],
				[
					-0.7812627788610484,
					2.343788336583117
				],
				[
					-0.7812627788610484,
					7.031365009749294
				],
				[
					0,
					12.50020446177652
				],
				[
					0.7812627788609916,
					13.281467240637568
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.2000429928302765,
				0.27299702167510986,
				0.07101131975650787,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1059305106,
			"isDeleted": false,
			"id": "BvcCQ42NR-zwfq0nHS-wC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 83.2357156086498,
			"y": -121.62481857085092,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.56252555772204,
			"height": 11.7189416829155,
			"seed": 1291639552,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7812627788610484
				],
				[
					0,
					2.343788336583117
				],
				[
					0,
					4.687576673166205
				],
				[
					0.7812627788609916,
					8.593890567471362
				],
				[
					0.7812627788609916,
					10.93767890405448
				],
				[
					1.56252555772204,
					11.7189416829155
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08274499326944351,
				0.21942199766635895,
				0.25199201703071594,
				0.18480297923088074,
				0.034775298088788986,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 2131112846,
			"isDeleted": false,
			"id": "IdnSE2LThiCQTYwiGNXpM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 84.79824116637184,
			"y": -98.96819798388094,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.562525557722097,
			"height": 10.156416125193402,
			"seed": 775019264,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7812627788609916
				],
				[
					0,
					1.56252555772204
				],
				[
					-0.7812627788610484,
					4.687576673166177
				],
				[
					0,
					7.812627788610314
				],
				[
					0.7812627788610484,
					9.375153346332354
				],
				[
					0.7812627788610484,
					10.156416125193402
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15414641797542572,
				0.2500779926776886,
				0.23399367928504944,
				0.03669729456305504,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 38999122,
			"isDeleted": false,
			"id": "0Vq-AQV_HKSEkM01kilVQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 85.57950394523289,
			"y": -79.43662851235513,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7812627788610484,
			"height": 10.156416125193402,
			"seed": 1248254720,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7812627788609916
				],
				[
					0,
					1.56252555772204
				],
				[
					0,
					3.12505111544408
				],
				[
					0,
					6.250102230888217
				],
				[
					0.7812627788610484,
					8.593890567471306
				],
				[
					0.7812627788610484,
					10.156416125193402
				],
				[
					0.7812627788610484,
					10.156416125193402
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10838598757982254,
				0.17046399414539337,
				0.22629599273204803,
				0.24614660441875458,
				0.020244872197508812,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1330942414,
			"isDeleted": false,
			"id": "EO2q2n3dg5XxUFWh6vgrk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 80.89192727206665,
			"y": -63.03011015627345,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.500204461776548,
			"height": 11.7189416829155,
			"seed": 1466465024,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.562525557722097,
					2.3437883365830885
				],
				[
					3.9063138943051854,
					6.250102230888217
				],
				[
					6.250102230888274,
					8.593890567471362
				],
				[
					7.031365009749322,
					8.593890567471362
				],
				[
					7.812627788610371,
					4.687576673166177
				],
				[
					10.15641612519346,
					0
				],
				[
					12.500204461776548,
					-2.3437883365830885
				],
				[
					12.500204461776548,
					-3.125051115444137
				],
				[
					12.500204461776548,
					-3.125051115444137
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.22806799411773682,
				0.26390576362609863,
				0.259040892124176,
				0.24558374285697937,
				0.29029980301856995,
				0.33478909730911255,
				0.3209121823310852,
				0.06781966984272003,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1800452626,
			"isDeleted": false,
			"id": "WP-R-NW7wE9sbNQDAU1qs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -12.07834341239618,
			"y": 0.2521749314701651,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 51.56334340482812,
			"height": 0.7812627788610484,
			"seed": 1930124032,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7812627788610484
				],
				[
					3.125051115444137,
					-0.7812627788610484
				],
				[
					14.062730019498588,
					0
				],
				[
					26.562934481275107,
					0
				],
				[
					38.28187616419058,
					0
				],
				[
					48.43829228938404,
					-0.7812627788610484
				],
				[
					51.56334340482812,
					-0.7812627788610484
				],
				[
					50.782080625967126,
					0
				],
				[
					48.43829228938404,
					0
				],
				[
					48.43829228938404,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11377047747373581,
				0.23605599999427795,
				0.3369300067424774,
				0.40623000264167786,
				0.42752471566200256,
				0.4483311176300049,
				0.4466804563999176,
				0.42072129249572754,
				0.16370706260204315,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 985475086,
			"isDeleted": false,
			"id": "koBuGHn97FFk9MXlCSELW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 44.17257666559817,
			"y": -8.341715636001197,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.28146724063754,
			"height": 11.7189416829155,
			"seed": 154852096,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7812627788610484,
					0
				],
				[
					1.56252555772204,
					0.7812627788610484
				],
				[
					5.468839452027225,
					2.3437883365830885
				],
				[
					9.375153346332354,
					3.9063138943051854
				],
				[
					12.500204461776491,
					5.468839452027225
				],
				[
					12.500204461776491,
					6.250102230888274
				],
				[
					10.93767890405445,
					7.0313650097492655
				],
				[
					8.593890567471362,
					8.593890567471362
				],
				[
					5.468839452027225,
					10.93767890405445
				],
				[
					3.125051115444137,
					11.7189416829155
				],
				[
					2.3437883365830885,
					11.7189416829155
				],
				[
					4.687576673166177,
					10.156416125193402
				],
				[
					4.687576673166177,
					10.156416125193402
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11392797529697418,
				0.3279379904270172,
				0.34792980551719666,
				0.3141421377658844,
				0.29992741346359253,
				0.31202274560928345,
				0.3117906153202057,
				0.32665929198265076,
				0.4089038372039795,
				0.4857926070690155,
				0.4470524787902832,
				0.1848279982805252,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 957589458,
			"isDeleted": false,
			"id": "HwsGXAE7Ra3eS9IVjCKvA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 140.03346187647887,
			"y": -6.184078636382537,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.773641019028105,
			"height": 0.8207578343904629,
			"seed": 1558461184,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8207578343904629,
					0
				],
				[
					-0.8207578343904629,
					0.8207578343904629
				],
				[
					0,
					0.8207578343904629
				],
				[
					4.924547006342664,
					0.8207578343904629
				],
				[
					10.669851847075847,
					0.8207578343904629
				],
				[
					13.952883184637642,
					0.8207578343904629
				],
				[
					13.132125350247179,
					0.8207578343904629
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0594019778072834,
				0.12252499163150787,
				0.25515198707580566,
				0.31490403413772583,
				0.3375909626483917,
				0.35171329975128174,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1362687566,
			"isDeleted": false,
			"id": "RESCAdKhVW6XskYix2qG3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 159.73164990184964,
			"y": -9.467109973944332,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.669851847075847,
			"height": 9.028336178294921,
			"seed": 64609024,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8207578343904629,
					0
				],
				[
					-0.8207578343904629,
					0.8207578343904629
				],
				[
					3.2830313375617948,
					3.2830313375617948
				],
				[
					7.3868205095140524,
					6.5660626751235895
				],
				[
					9.849094012685384,
					9.028336178294921
				],
				[
					9.849094012685384,
					8.207578343904459
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.18212664127349854,
				0.2676220238208771,
				0.285743772983551,
				0.19513897597789764,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 867360146,
			"isDeleted": false,
			"id": "LZ0SbVU3ptHgYi1fm_VQO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 168.75998608014456,
			"y": -11.108625642725258,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.311367515856716,
			"height": 13.132125350247236,
			"seed": 2014239488,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8207578343904061,
					0
				],
				[
					-3.2830313375617948,
					1.6415156687809258
				],
				[
					-8.207578343904459,
					8.207578343904515
				],
				[
					-11.490609681466253,
					13.132125350247236
				],
				[
					-12.311367515856716,
					13.132125350247236
				],
				[
					-9.849094012685384,
					11.49060968146631
				],
				[
					-9.028336178294921,
					10.669851847075847
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.21357199549674988,
				0.3085939884185791,
				0.3854820132255554,
				0.33228668570518494,
				0.10140515118837357,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1000406158,
			"isDeleted": false,
			"id": "RjroUNyTqu-8AreULPKWx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 176.1468065896586,
			"y": -7.004836470773,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.028336178294921,
			"height": 1.6415156687809258,
			"seed": 1745910528,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8207578343904061,
					0
				],
				[
					-0.8207578343904061,
					0.8207578343904629
				],
				[
					1.6415156687809258,
					0
				],
				[
					5.7453048407331835,
					-0.8207578343904629
				],
				[
					8.207578343904515,
					-0.8207578343904629
				],
				[
					8.207578343904515,
					-0.8207578343904629
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11653799563646317,
				0.1450119912624359,
				0.23913198709487915,
				0.2790215015411377,
				0.10656381398439407,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 140860242,
			"isDeleted": false,
			"id": "chfpuh-Xy9Pk1BvH4-3BS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 185.1751427679536,
			"y": -13.57089914589659,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.669851847075847,
			"height": 10.669851847075847,
			"seed": 1134918400,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8207578343904629,
					0
				],
				[
					-1.6415156687809258,
					0
				],
				[
					-1.6415156687809258,
					0.8207578343904629
				],
				[
					2.462273503171332,
					1.6415156687809258
				],
				[
					7.386820509513996,
					3.2830313375617948
				],
				[
					9.028336178294921,
					4.924547006342721
				],
				[
					8.207578343904459,
					5.745304840733127
				],
				[
					4.103789171952201,
					8.207578343904515
				],
				[
					1.641515668780869,
					9.849094012685384
				],
				[
					1.641515668780869,
					10.669851847075847
				],
				[
					3.2830313375617948,
					10.669851847075847
				],
				[
					4.103789171952201,
					9.849094012685384
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16729998588562012,
				0.2693459987640381,
				0.31185799837112427,
				0.3105287551879883,
				0.29868099093437195,
				0.3209454119205475,
				0.3770136833190918,
				0.45735031366348267,
				0.4003757834434509,
				0.11681536585092545,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 531512014,
			"isDeleted": false,
			"id": "SufXvbfd2P5PtY1RXpXeH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 139.2127040420884,
			"y": 24.18396123606408,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.132125350247179,
			"height": 41.03789171952246,
			"seed": 1491221248,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.8207578343904629
				],
				[
					0,
					-1.6415156687809258
				],
				[
					-0.8207578343904629,
					2.462273503171332
				],
				[
					-1.641515668780869,
					9.849094012685384
				],
				[
					0.8207578343904629,
					20.51894585976123
				],
				[
					4.103789171952258,
					27.905766369275284
				],
				[
					8.207578343904515,
					36.11334471317974
				],
				[
					9.849094012685384,
					39.39637605074154
				],
				[
					10.669851847075847,
					39.39637605074154
				],
				[
					11.49060968146631,
					38.57561821635113
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.21453598141670227,
				0.29024797677993774,
				0.3473295271396637,
				0.3939838111400604,
				0.39666157960891724,
				0.41148367524147034,
				0.4086344242095947,
				0.14862363040447235,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 629285138,
			"isDeleted": false,
			"id": "vpi6y1AelqNzhAU5gH93Z",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 153.16558722672605,
			"y": 67.68412645875787,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.132125350247179,
			"height": 17.235914522199437,
			"seed": 1606531840,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8207578343904629,
					0
				],
				[
					3.2830313375617948,
					3.2830313375617948
				],
				[
					6.5660626751235895,
					6.5660626751235895
				],
				[
					7.3868205095140524,
					7.3868205095140524
				],
				[
					7.3868205095140524,
					3.2830313375617948
				],
				[
					10.669851847075847,
					-4.924547006342664
				],
				[
					13.132125350247179,
					-9.849094012685384
				],
				[
					13.132125350247179,
					-9.028336178294921
				],
				[
					13.132125350247179,
					-9.028336178294921
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.281482994556427,
				0.35060200095176697,
				0.36888208985328674,
				0.32393592596054077,
				0.31755027174949646,
				0.338373601436615,
				0.32721784710884094,
				0.0728762224316597,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 66695438,
			"isDeleted": false,
			"id": "9q0DRcv_UOvIgcwlS3NcI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 168.75998608014456,
			"y": 67.68412645875787,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.235914522199437,
			"height": 10.669851847075847,
			"seed": 229415680,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.8207578343904629
				],
				[
					0.8207578343904629,
					1.6415156687809258
				],
				[
					0.8207578343904629,
					2.462273503171332
				],
				[
					4.924547006342721,
					5.7453048407331835
				],
				[
					10.669851847075847,
					9.028336178294978
				],
				[
					14.773641019028105,
					9.849094012685384
				],
				[
					16.41515668780903,
					9.849094012685384
				],
				[
					17.235914522199437,
					9.849094012685384
				],
				[
					16.41515668780903,
					9.849094012685384
				],
				[
					16.41515668780903,
					10.669851847075847
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13270598649978638,
				0.23769597709178925,
				0.34326502680778503,
				0.4324920177459717,
				0.49306797981262207,
				0.488627552986145,
				0.4439288377761841,
				0.25505757331848145,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 377499346,
			"isDeleted": false,
			"id": "3MvrXXcH6t2-EvE08AvBo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 190.09968977429625,
			"y": 70.96715779631967,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.311367515856773,
			"height": 11.49060968146631,
			"seed": 603724544,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8207578343904629,
					0
				],
				[
					-0.8207578343904629,
					0.8207578343904629
				],
				[
					4.924547006342721,
					4.103789171952258
				],
				[
					9.849094012685384,
					8.207578343904515
				],
				[
					11.49060968146631,
					9.849094012685384
				],
				[
					8.207578343904515,
					10.669851847075847
				],
				[
					4.103789171952258,
					11.49060968146631
				],
				[
					2.462273503171332,
					11.49060968146631
				],
				[
					3.2830313375617948,
					11.49060968146631
				],
				[
					4.103789171952258,
					10.669851847075847
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15122875571250916,
				0.2854840159416199,
				0.3233959972858429,
				0.3474276661872864,
				0.3618188798427582,
				0.3986290991306305,
				0.4953141510486603,
				0.47506871819496155,
				0.18427114188671112,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 872177486,
			"isDeleted": false,
			"id": "UpUoLP-d1BzSxhiGNAcA7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 212.88120048565392,
			"y": 74.84825471783938,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.8546187980473405,
			"height": 11.424900069886974,
			"seed": 789289728,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7140562543679039,
					0
				],
				[
					-1.4281125087358646,
					0
				],
				[
					-2.856225017471729,
					2.1421687631038253
				],
				[
					-3.57028127183969,
					5.712450034943515
				],
				[
					-2.856225017471729,
					9.996787561151109
				],
				[
					0,
					11.424900069886974
				],
				[
					3.57028127183969,
					9.282731306783205
				],
				[
					4.284337526207651,
					8.568675052415244
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10701379179954529,
				0.1403275728225708,
				0.18099871277809143,
				0.22670172154903412,
				0.24225787818431854,
				0.09482574462890625,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 1609991314,
			"isDeleted": false,
			"id": "wlQVfq8myWwPWfSF2bM6a",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 222.8779880468051,
			"y": 77.70447973531111,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.568675052415244,
			"height": 8.568675052415244,
			"seed": 743824128,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7140562543679039,
					0
				],
				[
					0.7140562543679039,
					-0.7140562543679039
				],
				[
					0,
					-1.4281125087358646
				],
				[
					-2.856225017471786,
					0.7140562543679607
				],
				[
					-3.57028127183969,
					4.284337526207651
				],
				[
					-1.4281125087358646,
					7.14056254367938
				],
				[
					4.284337526207594,
					5.712450034943515
				],
				[
					4.9983937805755545,
					4.9983937805755545
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14103998243808746,
				0.1709219366312027,
				0.17842577397823334,
				0.23209735751152039,
				0.2714668810367584,
				0.2601698338985443,
				0.03660043329000473,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 604980622,
			"isDeleted": false,
			"id": "hTaLEUPeSzbsTEXmehEmx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 232.8747756079562,
			"y": 66.27957966542408,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4281125087358646,
			"height": 19.993575122302275,
			"seed": 2110790400,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7140562543679039,
					-0.7140562543679039
				],
				[
					-0.7140562543679039,
					-1.4281125087358646
				],
				[
					-0.7140562543679039,
					0
				],
				[
					-0.7140562543679039,
					8.568675052415301
				],
				[
					-0.7140562543679039,
					18.56546261356641
				],
				[
					0.7140562543679607,
					14.281125087358816
				],
				[
					0.7140562543679607,
					13.567068832990856
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15994198620319366,
				0.1969199776649475,
				0.2757900059223175,
				0.2917602062225342,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1536959058,
			"isDeleted": false,
			"id": "CQ7gZE8KCT8LBskEezEBO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 236.44505687979589,
			"y": 59.1390171217447,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.1421687631038253,
			"height": 25.70602515724579,
			"seed": 107592448,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.4281125087359214
				],
				[
					0,
					2.856225017471786
				],
				[
					0.7140562543679607,
					7.14056254367938
				],
				[
					1.4281125087359214,
					18.56546261356641
				],
				[
					1.4281125087359214,
					25.70602515724579
				],
				[
					2.1421687631038253,
					24.991968902877886
				],
				[
					2.1421687631038253,
					24.991968902877886
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11339199542999268,
				0.1598540097475052,
				0.20910999178886414,
				0.31176602840423584,
				0.3289070129394531,
				0.14296136796474457,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1433101262,
			"isDeleted": false,
			"id": "CcUOI_f1CEV7Zi9tNbQA0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 244.29967567784323,
			"y": 75.56231097220729,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.426506289311419,
			"height": 7.8546187980473405,
			"seed": 321870592,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7140562543679607,
					0
				],
				[
					-1.4281125087358646,
					1.4281125087359214
				],
				[
					-1.4281125087358646,
					4.284337526207651
				],
				[
					1.4281125087358646,
					6.426506289311476
				],
				[
					4.284337526207651,
					4.998393780575611
				],
				[
					4.9983937805755545,
					1.4281125087359214
				],
				[
					4.9983937805755545,
					-1.4281125087358646
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
				0.15612000226974487,
				0.21604199707508087,
				0.2225065976381302,
				0.2249826043844223,
				0.1918114274740219,
				0.0357472226023674,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 340264978,
			"isDeleted": false,
			"id": "Uim1eYhrcEnbvmWlCM-tl",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 254.2964632389944,
			"y": 58.4249608673768,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4281125087359214,
			"height": 25.70602515724579,
			"seed": 886979328,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7140562543679607,
					0
				],
				[
					-1.4281125087359214,
					0.7140562543679039
				],
				[
					-1.4281125087359214,
					2.1421687631038253
				],
				[
					-0.7140562543679607,
					10.71084381551907
				],
				[
					-0.7140562543679607,
					22.1357438854061
				],
				[
					0,
					25.70602515724579
				],
				[
					0,
					24.99196890287783
				],
				[
					0,
					24.27791264850987
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08365631103515625,
				0.15449413657188416,
				0.21355700492858887,
				0.26306384801864624,
				0.15980447828769684,
				0.013036835007369518,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 975813134,
			"isDeleted": false,
			"id": "By9qf2mjFvWnCw9moIPDS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 258.58080076520196,
			"y": 75.56231097220729,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.14056254367938,
			"height": 7.14056254367938,
			"seed": 1231059712,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.714056254367847,
					1.4281125087359214
				],
				[
					-2.1421687631037685,
					2.856225017471786
				],
				[
					-2.1421687631037685,
					4.284337526207651
				],
				[
					-0.714056254367847,
					6.426506289311476
				],
				[
					2.856225017471843,
					6.426506289311476
				],
				[
					4.998393780575611,
					2.856225017471786
				],
				[
					4.284337526207651,
					0
				],
				[
					0.7140562543679607,
					-0.7140562543679039
				],
				[
					-1.4281125087358078,
					1.4281125087359214
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
				0.13161998987197876,
				0.18540799617767334,
				0.21246600151062012,
				0.18193520605564117,
				0.1704225093126297,
				0.2059876024723053,
				0.20649759471416473,
				0.021814636886119843,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 569456082,
			"isDeleted": false,
			"id": "89uEXznv0nwg8IVGzkFb_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 260.72296952830584,
			"y": 78.41853598967907,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.712450034943458,
			"height": 1.4281125087358646,
			"seed": 86547200,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7140562543679607,
					0
				],
				[
					1.4281125087358078,
					0.7140562543679039
				],
				[
					4.998393780575498,
					1.4281125087358646
				],
				[
					5.712450034943458,
					1.4281125087358646
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10810498148202896,
				0.18716198205947876,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 423839822,
			"isDeleted": false,
			"id": "YUlp6TwHZeiR9blD6aHwh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 267.14947581761726,
			"y": 74.13419846347142,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.14056254367938,
			"height": 9.996787561151166,
			"seed": 582507264,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					2.856225017471786
				],
				[
					0.7140562543679607,
					4.284337526207651
				],
				[
					1.4281125087359214,
					6.426506289311476
				],
				[
					2.856225017471729,
					3.57028127183969
				],
				[
					6.426506289311419,
					-3.57028127183969
				],
				[
					7.14056254367938,
					-3.57028127183969
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12104998528957367,
				0.1536339968442917,
				0.15571221709251404,
				0.12292401492595673,
				0.05186651647090912,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 95333266,
			"isDeleted": false,
			"id": "W0DmOb-RBt8c9l2xlxVUq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 251.4402382215226,
			"y": 91.98560482266987,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.568675052415273,
			"height": 10.71084381551907,
			"seed": 1886214912,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7140562543679607
				],
				[
					1.4281125087358646,
					4.998393780575611
				],
				[
					3.57028127183969,
					9.282731306783205
				],
				[
					3.57028127183969,
					9.996787561151166
				],
				[
					3.57028127183969,
					4.998393780575611
				],
				[
					4.998393780575583,
					2.1421687631038253
				],
				[
					7.140562543679351,
					2.1421687631038253
				],
				[
					8.568675052415273,
					6.426506289311476
				],
				[
					7.854618798047312,
					10.71084381551907
				],
				[
					7.854618798047312,
					9.996787561151166
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13068008422851562,
				0.15508508682250977,
				0.16800177097320557,
				0.14083382487297058,
				0.09666668623685837,
				0.1223876029253006,
				0.1778447926044464,
				0.19527292251586914,
				0.014437622390687466,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 1922109070,
			"isDeleted": false,
			"id": "4ti7Y2_ORkGsDBx-B-2aO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 262.15108203704165,
			"y": 94.84182984014166,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.282731306783262,
			"height": 11.42490006988703,
			"seed": 1134353152,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7140562543679607,
					0
				],
				[
					1.4281125087359214,
					0
				],
				[
					2.142168763103882,
					0
				],
				[
					2.856225017471843,
					0
				],
				[
					4.284337526207651,
					-2.1421687631038253
				],
				[
					4.284337526207651,
					-4.284337526207651
				],
				[
					1.4281125087359214,
					-3.57028127183969
				],
				[
					0,
					0.7140562543679039
				],
				[
					1.4281125087359214,
					5.712450034943515
				],
				[
					4.998393780575611,
					7.14056254367938
				],
				[
					9.282731306783262,
					2.1421687631038253
				],
				[
					9.282731306783262,
					0.7140562543679039
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08986398577690125,
				0.11795324832201004,
				0.1387338489294052,
				0.13875854015350342,
				0.12651635706424713,
				0.14333687722682953,
				0.19027669727802277,
				0.22436022758483887,
				0.147275909781456,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 95906130,
			"isDeleted": false,
			"id": "-hQJ5F9FDLQvbCiXhYs4Z",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 275.0040946156646,
			"y": 84.13098602462259,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4281125087359214,
			"height": 17.13735010483049,
			"seed": 577870592,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7140562543679607,
					0
				],
				[
					-1.4281125087359214,
					1.4281125087358646
				],
				[
					-1.4281125087359214,
					7.14056254367938
				],
				[
					0,
					14.28112508735876
				],
				[
					0,
					17.13735010483049
				],
				[
					0,
					16.423293850462585
				],
				[
					0,
					15.709237596094624
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14015600085258484,
				0.21272000670433044,
				0.22390130162239075,
				0.13643570244312286,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1657539790,
			"isDeleted": false,
			"id": "CprXo_8aR-xSALCmgaLzx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 270.005700835089,
			"y": 92.69966107703783,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.996787561151109,
			"height": 0.7140562543679607,
			"seed": 1901804288,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.142168763103882,
					-0.7140562543679607
				],
				[
					9.282731306783262,
					-0.7140562543679607
				],
				[
					9.996787561151109,
					-0.7140562543679607
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19076797366142273,
				0.04541568085551262,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 157445906,
			"isDeleted": false,
			"id": "ZJkRhqufUsudYuRhx-WXx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 282.85871341371194,
			"y": 91.27154856830197,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.568675052415188,
			"height": 7.8546187980473405,
			"seed": 1777752832,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7140562543679039
				],
				[
					0.714056254367847,
					4.9983937805755545
				],
				[
					2.1421687631037685,
					7.14056254367938
				],
				[
					3.57028127183969,
					4.284337526207594
				],
				[
					3.57028127183969,
					0.7140562543679039
				],
				[
					3.57028127183969,
					1.4281125087358646
				],
				[
					4.284337526207651,
					4.9983937805755545
				],
				[
					6.426506289311419,
					6.426506289311419
				],
				[
					8.568675052415188,
					3.57028127183969
				],
				[
					8.568675052415188,
					-0.7140562543679607
				],
				[
					7.8546187980473405,
					-0.7140562543679607
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16809996962547302,
				0.163310244679451,
				0.14325283467769623,
				0.10406887531280518,
				0.06660311669111252,
				0.07836062461137772,
				0.10898767411708832,
				0.12847353518009186,
				0.13605152070522308,
				0.048768430948257446,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 126698254,
			"isDeleted": false,
			"id": "KMMaSVjgp16f3_90MMFWT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 294.9976697379668,
			"y": 91.98560482266987,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.426506289311419,
			"height": 7.8546187980473405,
			"seed": 1009941248,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.4281125087358078,
					0.7140562543679607
				],
				[
					-1.4281125087358078,
					2.856225017471786
				],
				[
					0.7140562543679607,
					4.998393780575611
				],
				[
					3.57028127183969,
					4.284337526207651
				],
				[
					4.284337526207651,
					0
				],
				[
					2.142168763103882,
					-2.856225017471729
				],
				[
					-1.4281125087358078,
					-2.1421687631037685
				],
				[
					-2.1421687631037685,
					1.4281125087359214
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
				0.07634100317955017,
				0.1426900029182434,
				0.1559394896030426,
				0.14091669023036957,
				0.12198299914598465,
				0.1256597936153412,
				0.12881655991077423,
				0.02505340613424778,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1965472978,
			"isDeleted": false,
			"id": "HNjXzwnxySEWaVZDbzEA7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 299.28200726417447,
			"y": 88.41532355083018,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.426506289311419,
			"height": 8.568675052415301,
			"seed": 347208448,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7140562543679607
				],
				[
					0.7140562543679607,
					2.856225017471786
				],
				[
					2.142168763103882,
					7.14056254367938
				],
				[
					2.142168763103882,
					8.568675052415301
				],
				[
					2.856225017471729,
					6.426506289311476
				],
				[
					5.712450034943572,
					2.1421687631038253
				],
				[
					6.426506289311419,
					1.4281125087359214
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06333297491073608,
				0.11217688024044037,
				0.14665460586547852,
				0.1661706268787384,
				0.14709702134132385,
				0.0861104428768158,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1666036046,
			"isDeleted": false,
			"id": "604980mo34WvAPbw9MAou",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 311.42096358842946,
			"y": 73.42014220910352,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.1421687631037685,
			"height": 22.135743885406043,
			"seed": 976198400,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7140562543679039
				],
				[
					-0.7140562543679607,
					2.1421687631037685
				],
				[
					0,
					7.854618798047284
				],
				[
					0.7140562543679607,
					17.13735010483049
				],
				[
					1.4281125087358078,
					22.135743885406043
				],
				[
					0.7140562543679607,
					20.70763137667018
				],
				[
					0.7140562543679607,
					19.993575122302275
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11550799757242203,
				0.18001998960971832,
				0.22188079357147217,
				0.15934878587722778,
				0.009547119028866291,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 110842514,
			"isDeleted": false,
			"id": "KUQvDTFdPFSRilTWz6ns7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 311.42096358842946,
			"y": 86.98721104209432,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.8546187980473405,
			"height": 5.712450034943515,
			"seed": 56179456,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7140562543679607,
					0
				],
				[
					1.4281125087358078,
					-0.7140562543679607
				],
				[
					7.14056254367938,
					-5.712450034943515
				],
				[
					7.8546187980473405,
					-5.712450034943515
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0826762393116951,
				0.1762779802083969,
				0.09398550540208817,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1097226126,
			"isDeleted": false,
			"id": "lRpVbNqq3I6Yp9LqP643-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 314.2771886059012,
			"y": 87.70126729646228,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.14056254367938,
			"height": 4.9983937805755545,
			"seed": 737213184,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4281125087359214,
					2.1421687631038253
				],
				[
					2.856225017471729,
					3.57028127183969
				],
				[
					6.426506289311419,
					4.9983937805755545
				],
				[
					7.14056254367938,
					4.9983937805755545
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11137399077415466,
				0.16774798929691315,
				0.09938369691371918,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 813117522,
			"isDeleted": false,
			"id": "3CpUgtaHjX8TgswPbglD3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 288.5711634486554,
			"y": 56.99684835864093,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.27951886793437,
			"height": 26.42008141161375,
			"seed": 1874377472,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7140562543679607,
					1.4281125087358646
				],
				[
					1.4281125087359214,
					4.284337526207594
				],
				[
					4.284337526207651,
					10.71084381551907
				],
				[
					4.998393780575611,
					9.282731306783148
				],
				[
					7.8546187980473405,
					0
				],
				[
					18.56546261356641,
					-15.709237596094681
				],
				[
					19.27951886793437,
					-15.709237596094681
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15010400116443634,
				0.2006399780511856,
				0.2328919917345047,
				0.20126202702522278,
				0.19966888427734375,
				0.05618664622306824,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 437269966,
			"isDeleted": false,
			"id": "nmFOQ3aIvNCtX4mB5y-6_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 272.36122344723134,
			"y": -73.30844148597339,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 32.73596318620514,
			"height": 42.55675214206667,
			"seed": 1537104640,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.636798159310274,
					-4.910394477930765
				],
				[
					9.00238987620645,
					-18.823178832067924
				],
				[
					18.004779752412844,
					-29.462366867584592
				],
				[
					26.1887705489641,
					-37.646357664135905
				],
				[
					31.099165026894866,
					-41.738353062411534
				],
				[
					31.917564106550003,
					-42.55675214206667
				],
				[
					32.73596318620514,
					-42.55675214206667
				],
				[
					32.73596318620514,
					-42.55675214206667
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16549310088157654,
				0.23715990781784058,
				0.274551659822464,
				0.2850300669670105,
				0.2791488766670227,
				0.2835640609264374,
				0.11918194591999054,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1989236242,
			"isDeleted": false,
			"id": "j0LzoCJ3dqC4_ZuGGHNtZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 317.3731728282634,
			"y": -126.50438166355673,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.82078895586153,
			"height": 11.457587115171805,
			"seed": 1148754688,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.818399079655137,
					0
				],
				[
					0.818399079655137,
					-0.818399079655137
				],
				[
					5.728793557585902,
					-0.818399079655137
				],
				[
					9.002389876206394,
					-0.818399079655137
				],
				[
					7.365591716896176,
					2.4551972389653827
				],
				[
					2.455197238965411,
					7.365591716896148
				],
				[
					0.818399079655137,
					10.639188035516668
				],
				[
					2.455197238965411,
					9.82078895586153
				],
				[
					2.455197238965411,
					9.82078895586153
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06667254865169525,
				0.2733760178089142,
				0.3178960084915161,
				0.29244542121887207,
				0.3146415054798126,
				0.3454315960407257,
				0.3885074257850647,
				0.13151395320892334,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 1986284558,
			"isDeleted": false,
			"id": "djDS4m2Qk33PU65rIdgNP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 329.86076001852234,
			"y": -136.46616186796544,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.61633554109676,
			"height": 6.923941400997052,
			"seed": 1852799744,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.692394140099708
				],
				[
					-0.6923941400997364,
					2.769576560398832
				],
				[
					-0.6923941400997364,
					3.46197070049854
				],
				[
					0,
					4.846758980697956
				],
				[
					2.769576560398775,
					5.539153120797664
				],
				[
					5.539153120797607,
					4.154364840598248
				],
				[
					6.231547260897344,
					0.692394140099708
				],
				[
					4.154364840598191,
					-1.3847882801993876
				],
				[
					0.6923941400996796,
					-0.6923941400996796
				],
				[
					-1.384788280199416,
					3.46197070049854
				],
				[
					0.6923941400996796,
					4.846758980697956
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
				0.08432348817586899,
				0.12147931009531021,
				0.1463232785463333,
				0.15123000741004944,
				0.14102892577648163,
				0.13486017286777496,
				0.13322827219963074,
				0.14753015339374542,
				0.12035180628299713,
				0.010396911762654781,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1239466962,
			"isDeleted": false,
			"id": "klAh3tjIAs-FriWUWqDFm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 334.01512485912053,
			"y": -137.15855600806512,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.385912101495592,
			"height": 20.079430062891447,
			"seed": 2129451776,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6923941400996796,
					0
				],
				[
					-1.384788280199416,
					0.6923941400996796
				],
				[
					-1.384788280199416,
					3.4619707004985116
				],
				[
					1.384788280199416,
					7.61633554109676
				],
				[
					4.154364840598248,
					12.463094521794687
				],
				[
					4.8467589806979845,
					16.617459362392935
				],
				[
					3.4619707004985685,
					19.38703592279174
				],
				[
					-1.384788280199416,
					20.079430062891447
				],
				[
					-5.539153120797607,
					18.00224764259235
				],
				[
					-5.539153120797607,
					14.540276942093811
				],
				[
					-4.846758980697928,
					13.847882801994103
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08237799257040024,
				0.1009579747915268,
				0.15838399529457092,
				0.14943744242191315,
				0.1672835350036621,
				0.18656152486801147,
				0.20800915360450745,
				0.19052225351333618,
				0.12469872832298279,
				0.008846741169691086,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1415289422,
			"isDeleted": false,
			"id": "sphu1xVtjLsqn2IIThtw5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 337.4770955596191,
			"y": -135.77376772786573,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.92394140099708,
			"height": 6.231547260897372,
			"seed": 949549824,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6923941400997364,
					0
				],
				[
					-2.0771824202991525,
					2.077182420299124
				],
				[
					-0.6923941400997364,
					4.846758980697956
				],
				[
					2.769576560398775,
					5.539153120797664
				],
				[
					4.846758980697928,
					3.46197070049854
				],
				[
					4.846758980697928,
					0.692394140099708
				],
				[
					2.0771824202990956,
					-0.692394140099708
				],
				[
					-0.6923941400997364,
					1.384788280199416
				],
				[
					-0.6923941400997364,
					4.154364840598248
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
				0.052904725074768066,
				0.15334799885749817,
				0.16314557194709778,
				0.12885287404060364,
				0.11292389035224915,
				0.0879882201552391,
				0.10454754531383514,
				0.12546373903751373,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1685879186,
			"isDeleted": false,
			"id": "Knh8NbIdQ_0TSqHtvYFIU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 343.0162486804167,
			"y": -137.15855600806512,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.308729681196496,
			"height": 5.539153120797636,
			"seed": 277945088,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6923941400996796,
					0.6923941400996796
				],
				[
					-1.384788280199416,
					2.0771824202990956
				],
				[
					-1.384788280199416,
					4.15436484059822
				],
				[
					2.0771824202991525,
					4.846758980697928
				],
				[
					4.8467589806979845,
					3.4619707004985116
				],
				[
					5.539153120797664,
					0.6923941400996796
				],
				[
					2.769576560398832,
					-0.692394140099708
				],
				[
					-1.384788280199416,
					0
				],
				[
					-2.769576560398832,
					2.7695765603988036
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
				0.11128699034452438,
				0.16038399934768677,
				0.14390841126441956,
				0.12059701234102249,
				0.1170148029923439,
				0.11656545847654343,
				0.11127438396215439,
				0.011693542823195457,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 181346446,
			"isDeleted": false,
			"id": "KY9R_BKhiKsZ5jbxayXwl",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 352.0173725017129,
			"y": -145.46728568926162,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.308729681196496,
			"height": 13.847882801994132,
			"seed": 190135040,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.692394140099708
				],
				[
					0,
					1.384788280199416
				],
				[
					0,
					5.539153120797664
				],
				[
					1.384788280199416,
					9.693517961395884
				],
				[
					2.0771824202991525,
					10.385912101495592
				],
				[
					0.6923941400997364,
					9.001123821296176
				],
				[
					-2.0771824202990956,
					8.308729681196496
				],
				[
					-4.846758980697928,
					11.0783062415953
				],
				[
					-4.154364840598191,
					13.847882801994132
				],
				[
					3.4619707004985685,
					13.847882801994132
				],
				[
					3.4619707004985685,
					13.155488661894424
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09656115621328354,
				0.1749259978532791,
				0.20798926055431366,
				0.15312157571315765,
				0.0961356833577156,
				0.07891479134559631,
				0.15634551644325256,
				0.2461228370666504,
				0.0719524547457695,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 65,
			"versionNonce": 630945618,
			"isDeleted": false,
			"id": "qlT4Wiu8Rx17Q4daCZuW3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 369.32722600420556,
			"y": -137.85095014816483,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.92394140099708,
			"height": 27.003371463888527,
			"seed": 1566923520,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6923941400996796,
					-0.692394140099708
				],
				[
					1.384788280199416,
					-2.769576560398832
				],
				[
					2.769576560398832,
					-4.846758980697956
				],
				[
					3.4619707004985116,
					-7.616335541096788
				],
				[
					4.154364840598248,
					-11.770700381695008
				],
				[
					2.769576560398832,
					-12.463094521794716
				],
				[
					0.6923941400996796,
					-10.385912101495592
				],
				[
					-0.6923941400997364,
					-6.92394140099708
				],
				[
					0,
					-2.077182420299124
				],
				[
					2.0771824202990956,
					4.846758980697928
				],
				[
					3.4619707004985116,
					10.385912101495563
				],
				[
					2.769576560398832,
					13.847882801994103
				],
				[
					0.6923941400996796,
					14.540276942093811
				],
				[
					-2.0771824202990956,
					13.155488661894395
				],
				[
					-2.769576560398832,
					10.385912101495563
				],
				[
					-1.384788280199416,
					5.539153120797636
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
				0.0894400030374527,
				0.12665197253227234,
				0.14687857031822205,
				0.13711966574192047,
				0.13348324596881866,
				0.1503380388021469,
				0.1634049117565155,
				0.17503881454467773,
				0.18665793538093567,
				0.18728558719158173,
				0.18775439262390137,
				0.15974947810173035,
				0.13437047600746155,
				0.0997912585735321,
				0.006029998883605003,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 762830542,
			"isDeleted": false,
			"id": "LIzoeXI0LN9LqNgliLPzs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 375.5587732651029,
			"y": -139.92813256846395,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.92394140099708,
			"height": 7.61633554109676,
			"seed": 1170856704,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6923941400996796,
					0.692394140099708
				],
				[
					-2.0771824202990956,
					2.077182420299124
				],
				[
					-2.769576560398832,
					5.539153120797636
				],
				[
					-0.6923941400996796,
					6.923941400997052
				],
				[
					2.0771824202990956,
					6.231547260897344
				],
				[
					4.154364840598248,
					2.769576560398832
				],
				[
					3.4619707004985116,
					-0.692394140099708
				],
				[
					0,
					-0.692394140099708
				],
				[
					-2.769576560398832,
					2.077182420299124
				],
				[
					-1.384788280199416,
					4.846758980697928
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
				0.09445998817682266,
				0.15042349696159363,
				0.1621398627758026,
				0.13136474788188934,
				0.10565194487571716,
				0.07763565331697464,
				0.10150347650051117,
				0.09963721036911011,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1838464274,
			"isDeleted": false,
			"id": "9zQ690LK2Zx6BXbwGJ-Te",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 380.4055322458008,
			"y": -141.31292084866337,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.539153120797664,
			"height": 6.231547260897344,
			"seed": 1641978624,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6923941400996796,
					0.692394140099708
				],
				[
					-0.6923941400996796,
					2.077182420299124
				],
				[
					-0.6923941400996796,
					3.46197070049854
				],
				[
					-0.6923941400996796,
					5.539153120797636
				],
				[
					0.6923941400997364,
					5.539153120797636
				],
				[
					2.769576560398832,
					2.077182420299124
				],
				[
					4.8467589806979845,
					-0.692394140099708
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
				0.09726998955011368,
				0.13218601047992706,
				0.14102569222450256,
				0.1269679218530655,
				0.14474639296531677,
				0.0843377411365509,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 1894700302,
			"isDeleted": false,
			"id": "-QnXAo2243QU_zvmI3pZP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 397.7153857482935,
			"y": -142.69770912886278,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.001123821296176,
			"height": 8.308729681196468,
			"seed": 2006285056,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6923941400997364,
					0.692394140099708
				],
				[
					-2.0771824202991525,
					2.077182420299124
				],
				[
					-2.769576560398832,
					4.846758980697956
				],
				[
					0.6923941400996796,
					6.923941400997052
				],
				[
					4.154364840598248,
					6.231547260897344
				],
				[
					5.539153120797664,
					2.077182420299124
				],
				[
					3.4619707004985116,
					-1.384788280199416
				],
				[
					-1.384788280199416,
					-1.384788280199416
				],
				[
					-3.4619707004985116,
					1.384788280199416
				],
				[
					-2.0771824202991525,
					3.46197070049854
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
				0.12071600556373596,
				0.18107400834560394,
				0.17475780844688416,
				0.14528726041316986,
				0.12350012362003326,
				0.10761751979589462,
				0.1126256138086319,
				0.07640249282121658,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 2044676818,
			"isDeleted": false,
			"id": "2ZHM80SUurpri3he9v1-k",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 407.40890370968935,
			"y": -155.1608036506575,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6923941400996796,
			"height": 20.079430062891475,
			"seed": 1758608128,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6923941400996796,
					2.077182420299124
				],
				[
					-0.6923941400996796,
					5.539153120797664
				],
				[
					0,
					15.232671082193548
				],
				[
					0,
					20.079430062891475
				],
				[
					-0.6923941400996796,
					20.079430062891475
				],
				[
					-0.6923941400996796,
					19.387035922791767
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16225799918174744,
				0.18461200594902039,
				0.23423543572425842,
				0.1956852376461029,
				0.06815914809703827,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 246219598,
			"isDeleted": false,
			"id": "bhRsfXSZJTI7HX421Phxa",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 401.177356448792,
			"y": -142.00531498876308,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.385912101495592,
			"height": 0,
			"seed": 380058368,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6923941400997364,
					0
				],
				[
					4.846758980697928,
					0
				],
				[
					9.693517961395912,
					0
				],
				[
					10.385912101495592,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.137053981423378,
				0.2113809883594513,
				0.05513226240873337,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 1091707026,
			"isDeleted": false,
			"id": "JJRjXXXBT-GlnoDhBcEf4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 412.948056830487,
			"y": -154.4684095105578,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.539153120797664,
			"height": 20.079430062891475,
			"seed": 1824455424,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.692394140099708
				],
				[
					0,
					2.077182420299124
				],
				[
					1.384788280199416,
					9.001123821296176
				],
				[
					1.384788280199416,
					16.617459362392964
				],
				[
					0.6923941400997364,
					18.00224764259235
				],
				[
					0.6923941400997364,
					15.925065222293256
				],
				[
					1.384788280199416,
					11.770700381695008
				],
				[
					4.154364840598248,
					9.693517961395884
				],
				[
					5.539153120797664,
					13.847882801994132
				],
				[
					4.846758980697928,
					18.00224764259235
				],
				[
					4.154364840598248,
					19.387035922791767
				],
				[
					4.154364840598248,
					18.69464178269206
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07413565367460251,
				0.1399683803319931,
				0.188690647482872,
				0.20878851413726807,
				0.17482410371303558,
				0.07931515574455261,
				0.025301819667220116,
				0.09708276391029358,
				0.19891732931137085,
				0.23272903263568878,
				0.06403116136789322,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 688613774,
			"isDeleted": false,
			"id": "MLsgL07qQWF19jCftVolN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 422.64157479188293,
			"y": -140.62052670856366,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.231547260897344,
			"height": 6.923941400997052,
			"seed": 257669888,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6923941400996796,
					0
				],
				[
					1.3847882801993592,
					0
				],
				[
					2.0771824202990956,
					-0.692394140099708
				],
				[
					2.0771824202990956,
					-2.769576560398832
				],
				[
					-0.6923941400997364,
					-2.769576560398832
				],
				[
					-2.769576560398832,
					0.692394140099708
				],
				[
					-1.384788280199416,
					4.15436484059822
				],
				[
					3.4619707004985116,
					4.15436484059822
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
				0.1122879907488823,
				0.13778997957706451,
				0.12430499494075775,
				0.09888079762458801,
				0.11908355355262756,
				0.16680435836315155,
				0.18381689488887787,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1323581010,
			"isDeleted": false,
			"id": "uJmcJF5zR-si3ehtMQm8L",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 426.7959396324811,
			"y": -142.69770912886278,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.92394140099708,
			"height": 9.001123821296204,
			"seed": 1543191296,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.692394140099708
				],
				[
					0,
					3.46197070049854
				],
				[
					0.6923941400997364,
					5.539153120797664
				],
				[
					2.0771824202991525,
					3.46197070049854
				],
				[
					4.8467589806979845,
					-0.692394140099708
				],
				[
					6.92394140099708,
					-2.769576560398832
				],
				[
					6.92394140099708,
					-3.46197070049854
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09409597516059875,
				0.13287539780139923,
				0.14830151200294495,
				0.12112072855234146,
				0.12361358851194382,
				0.043164610862731934,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 792922062,
			"isDeleted": false,
			"id": "cOcM9jD7461MS2cFldtB8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 443.41339899487406,
			"y": -146.15967982936132,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.30872968119644,
			"height": 7.61633554109676,
			"seed": 554752768,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6923941400996796,
					0
				],
				[
					-2.0771824202990956,
					1.384788280199416
				],
				[
					-2.0771824202990956,
					3.46197070049854
				],
				[
					-2.0771824202990956,
					5.539153120797664
				],
				[
					0,
					6.92394140099708
				],
				[
					3.4619707004985685,
					6.231547260897372
				],
				[
					4.154364840598248,
					2.769576560398832
				],
				[
					3.4619707004985685,
					0
				],
				[
					-0.6923941400996796,
					-0.6923941400996796
				],
				[
					-4.154364840598191,
					3.46197070049854
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
				0.05543197691440582,
				0.1272977888584137,
				0.154246523976326,
				0.1567268967628479,
				0.14549969136714935,
				0.16729742288589478,
				0.18205124139785767,
				0.14895856380462646,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 539796498,
			"isDeleted": false,
			"id": "GQdHRwCrss6M1r9Fg7aBM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 445.4905814151732,
			"y": -142.00531498876308,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.846758980697928,
			"height": 2.769576560398832,
			"seed": 619027200,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.692394140099708
				],
				[
					1.384788280199416,
					2.077182420299124
				],
				[
					4.154364840598248,
					2.769576560398832
				],
				[
					4.846758980697928,
					2.769576560398832
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15092194080352783,
				0.13463491201400757,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1097653774,
			"isDeleted": false,
			"id": "TtPhYMGaaBG1n5smdShO5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 454.4917052364694,
			"y": -146.852073969461,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.30872968119644,
			"height": 16.617459362392935,
			"seed": 280320768,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6923941400996796
				],
				[
					0.6923941400996796,
					6.923941400997052
				],
				[
					1.384788280199416,
					15.23267108219352
				],
				[
					0,
					16.617459362392935
				],
				[
					-1.384788280199416,
					11.77070038169498
				],
				[
					-0.6923941400997364,
					4.846758980697928
				],
				[
					4.154364840598248,
					0.6923941400996796
				],
				[
					6.923941400997023,
					1.3847882801993876
				],
				[
					6.231547260897344,
					5.539153120797636
				],
				[
					4.846758980697928,
					8.308729681196468
				],
				[
					4.154364840598248,
					8.308729681196468
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09588522464036942,
				0.13519753515720367,
				0.16728024184703827,
				0.1717420071363449,
				0.07671090960502625,
				0.03651992976665497,
				0.0552787184715271,
				0.09565918147563934,
				0.1111648827791214,
				0.011387634091079235,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 2128761298,
			"isDeleted": false,
			"id": "ZPVWfFhX9CWOQ5uq5g2cI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 462.10804077756615,
			"y": -146.852073969461,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.30872968119644,
			"height": 17.309853502492643,
			"seed": 1016167168,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6923941400996796
				],
				[
					0.6923941400996796,
					5.539153120797636
				],
				[
					1.384788280199416,
					14.540276942093811
				],
				[
					-0.6923941400997364,
					17.309853502492643
				],
				[
					-2.0771824202990956,
					13.847882801994103
				],
				[
					-1.384788280199416,
					4.846758980697928
				],
				[
					3.4619707004985116,
					0
				],
				[
					6.231547260897344,
					1.3847882801993876
				],
				[
					5.539153120797664,
					5.539153120797636
				],
				[
					2.769576560398832,
					9.001123821296176
				],
				[
					2.769576560398832,
					8.308729681196468
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07199975848197937,
				0.11989092826843262,
				0.17893563210964203,
				0.19339397549629211,
				0.11243774741888046,
				0.031622953712940216,
				0.032962553203105927,
				0.08801257610321045,
				0.15271350741386414,
				0.05479476973414421,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 344058958,
			"isDeleted": false,
			"id": "RlDfRh4ZCa4kz9U03djfB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 473.1863470191614,
			"y": -160.00756263135543,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6923941400997364,
			"height": 20.771824202991183,
			"seed": 2025429760,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6923941400997364,
					-0.692394140099708
				],
				[
					0.6923941400997364,
					0
				],
				[
					0.6923941400997364,
					7.61633554109676
				],
				[
					0.6923941400997364,
					18.00224764259235
				],
				[
					0.6923941400997364,
					20.079430062891475
				],
				[
					0.6923941400997364,
					18.69464178269206
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09241598844528198,
				0.14645400643348694,
				0.22194799780845642,
				0.24909652769565582,
				0.01154327392578125,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1578911634,
			"isDeleted": false,
			"id": "K8rTv11QD13fk5-51-RsS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 477.3407118597597,
			"y": -146.15967982936132,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6923941400996227,
			"height": 6.92394140099708,
			"seed": 1093573376,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.692394140099708
				],
				[
					0,
					2.077182420299124
				],
				[
					0,
					6.92394140099708
				],
				[
					0.6923941400996227,
					6.92394140099708
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.054066650569438934,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1448817294,
			"isDeleted": false,
			"id": "FcC4JzI08GY0AW5NQT1bj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 478.7255001399591,
			"y": -151.00643881005925,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.0001,
			"height": 0.0001,
			"seed": 574511872,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
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
			"version": 68,
			"versionNonce": 907117906,
			"isDeleted": false,
			"id": "AhpWQfsO7omhRw0rIlmMt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 484.9570474008565,
			"y": -148.23686224966042,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.385912101495592,
			"height": 9.001123821296176,
			"seed": 58211072,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6923941400997364,
					0.692394140099708
				],
				[
					-2.0771824202992093,
					2.7695765603988036
				],
				[
					-2.769576560398832,
					6.231547260897344
				],
				[
					0,
					9.001123821296176
				],
				[
					3.461970700498455,
					8.308729681196468
				],
				[
					4.846758980697928,
					5.539153120797636
				],
				[
					4.154364840598191,
					2.7695765603988036
				],
				[
					2.0771824202990956,
					2.0771824202990956
				],
				[
					0,
					4.15436484059822
				],
				[
					0.6923941400996227,
					6.231547260897344
				],
				[
					2.0771824202990956,
					6.923941400997052
				],
				[
					4.154364840598191,
					7.61633554109676
				],
				[
					5.53915312079755,
					7.61633554109676
				],
				[
					6.231547260897287,
					6.923941400997052
				],
				[
					7.61633554109676,
					4.846758980697928
				],
				[
					7.61633554109676,
					2.7695765603988036
				],
				[
					6.923941400997023,
					0.692394140099708
				],
				[
					4.154364840598191,
					0
				],
				[
					2.0771824202990956,
					1.384788280199416
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
				0.11177399009466171,
				0.18952402472496033,
				0.17380104959011078,
				0.13372085988521576,
				0.11026391386985779,
				0.09538888186216354,
				0.0936734601855278,
				0.1119627058506012,
				0.1185261532664299,
				0.1151404082775116,
				0.11491366475820541,
				0.1294836401939392,
				0.12963180243968964,
				0.13808178901672363,
				0.13917765021324158,
				0.13428045809268951,
				0.07890533655881882,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 296857806,
			"isDeleted": false,
			"id": "q9KZFMM-8W-1-6-4n-WIc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 490.49620052165403,
			"y": -144.7748915491619,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.846758980698041,
			"height": 4.154364840598248,
			"seed": 822254336,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.692394140099708
				],
				[
					0.6923941400997364,
					2.769576560398832
				],
				[
					4.154364840598305,
					4.154364840598248
				],
				[
					4.846758980698041,
					4.154364840598248
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.18285198509693146,
				0.06535983085632324,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1612253970,
			"isDeleted": false,
			"id": "pwkyH3MY190s__STT8_gL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 497.42014192265117,
			"y": -161.39235091155484,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.0771824202990956,
			"height": 22.849006623290308,
			"seed": 588405504,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.384788280199416
				],
				[
					0.6923941400996227,
					4.154364840598248
				],
				[
					1.3847882801993592,
					9.693517961395884
				],
				[
					2.0771824202990956,
					20.079430062891475
				],
				[
					1.3847882801993592,
					22.849006623290308
				],
				[
					0.6923941400996227,
					22.849006623290308
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0660419911146164,
				0.12424490600824356,
				0.10919659584760666,
				0.13781237602233887,
				0.04626422002911568,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 303982350,
			"isDeleted": false,
			"id": "I0BCv5d2npwnsatP6Qz9D",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 494.65056536225234,
			"y": -147.5444681095607,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.693517961395855,
			"height": 0.692394140099708,
			"seed": 1992776448,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.769576560398832,
					0
				],
				[
					4.154364840598191,
					-0.692394140099708
				],
				[
					9.001123821296119,
					-0.692394140099708
				],
				[
					9.693517961395855,
					-0.692394140099708
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0913594663143158,
				0.08259524405002594,
				0.030149536207318306,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1923733714,
			"isDeleted": false,
			"id": "SAoFVu6CFG-wfRblAEo8k",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 505.72887160384767,
			"y": -148.92925638976013,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.0771824202990956,
			"height": 8.308729681196468,
			"seed": 2118589184,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.692394140099708
				],
				[
					0.6923941400996227,
					4.846758980697928
				],
				[
					1.3847882801993592,
					8.308729681196468
				],
				[
					2.0771824202990956,
					8.308729681196468
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.061317991465330124,
				0.1557973027229309,
				0.0681578665971756,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1209685326,
			"isDeleted": false,
			"id": "pt09aeutulSY_b3WCWJf8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 507.113659884047,
			"y": -153.08362123035837,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 0.692394140099708,
			"seed": 1391909632,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.692394140099708
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
				0.0028197632636874914,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 492498578,
			"isDeleted": false,
			"id": "tw1YAuv43DiBJiKYsKdUQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 508.4984481642464,
			"y": -145.46728568926162,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.2315472608974005,
			"height": 7.61633554109676,
			"seed": 911080192,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.692394140099708
				],
				[
					0,
					2.769576560398832
				],
				[
					1.3847882801994729,
					3.46197070049854
				],
				[
					4.846758980698041,
					4.154364840598248
				],
				[
					6.2315472608974005,
					0.692394140099708
				],
				[
					4.846758980698041,
					-3.4619707004985116
				],
				[
					1.3847882801994729,
					-3.4619707004985116
				],
				[
					0,
					-0.692394140099708
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
				0.12022198736667633,
				0.15478798747062683,
				0.15605151653289795,
				0.1338435709476471,
				0.10744421184062958,
				0.0767384022474289,
				0.005869110114872456,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 754875278,
			"isDeleted": false,
			"id": "dt98sfBN6cqQXB1R0HC-a",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 514.037601285044,
			"y": -147.5444681095607,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.846758980697928,
			"height": 6.231547260897344,
			"seed": 831355648,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.692394140099708
				],
				[
					0,
					1.3847882801993876
				],
				[
					0,
					2.7695765603988036
				],
				[
					1.3847882801994729,
					3.4619707004985116
				],
				[
					2.769576560398832,
					0.692394140099708
				],
				[
					4.154364840598305,
					-1.384788280199416
				],
				[
					4.846758980697928,
					1.3847882801993876
				],
				[
					4.154364840598305,
					4.846758980697928
				],
				[
					4.154364840598305,
					4.846758980697928
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07301098853349686,
				0.08468926697969437,
				0.11395828425884247,
				0.12762826681137085,
				0.03646108880639076,
				0,
				0.0985829159617424,
				0.040550291538238525,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 82005074,
			"isDeleted": false,
			"id": "ZK2W0VNvc0uSOwDuVEeIT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 524.4235133865396,
			"y": -151.69883295015896,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.923941400997023,
			"height": 10.385912101495592,
			"seed": 240147200,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6923941400996227,
					0
				],
				[
					-2.0771824202990956,
					0.692394140099708
				],
				[
					-2.769576560398832,
					2.769576560398832
				],
				[
					0.6923941400997364,
					5.539153120797636
				],
				[
					2.0771824202990956,
					7.61633554109676
				],
				[
					0.6923941400997364,
					9.001123821296176
				],
				[
					-3.461970700498455,
					9.693517961395884
				],
				[
					-4.846758980697928,
					10.385912101495592
				],
				[
					-4.846758980697928,
					10.385912101495592
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07682596147060394,
				0.11396072059869766,
				0.09525524824857712,
				0.0798666700720787,
				0.15099182724952698,
				0.17267462611198425,
				0.06517724692821503,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 62,
			"versionNonce": 654563790,
			"isDeleted": false,
			"id": "K7fvI0K4-xF5ea4l9Zfzn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 325.31627284123556,
			"y": 64.91692012145984,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 22.464324813187318,
			"height": 24.788220483516966,
			"seed": 111098624,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7746318901099585,
					0.7746318901099016
				],
				[
					-0.7746318901099585,
					1.5492637802198033
				],
				[
					0.7746318901098448,
					2.323895670329705
				],
				[
					3.0985275604396065,
					2.323895670329705
				],
				[
					6.197055120879213,
					1.5492637802198033
				],
				[
					9.29558268131882,
					-2.323895670329705
				],
				[
					11.619478351648581,
					-6.971687010989115
				],
				[
					12.394110241758426,
					-11.619478351648581
				],
				[
					13.168742131868385,
					-14.718005912088188
				],
				[
					14.718005912088188,
					-18.591165362637753
				],
				[
					17.816533472527794,
					-21.68969292307736
				],
				[
					20.140429142857556,
					-22.46432481318726
				],
				[
					21.68969292307736,
					-22.46432481318726
				],
				[
					21.68969292307736,
					-21.68969292307736
				],
				[
					20.9150610329674,
					-21.68969292307736
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06563442945480347,
				0.1546364724636078,
				0.17959490418434143,
				0.1999862641096115,
				0.2194155901670456,
				0.23371051251888275,
				0.21793533861637115,
				0.21574215590953827,
				0.2392922043800354,
				0.267999529838562,
				0.2925587594509125,
				0.30562832951545715,
				0.306823194026947,
				0.21885479986667633,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 521794066,
			"isDeleted": false,
			"id": "eu-A6vLFlW3vhMmXeG-PI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 351.6537571049723,
			"y": 36.25554018739331,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.520950791208975,
			"height": 7.746318901099073,
			"seed": 476699392,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7746318901099585,
					0
				],
				[
					1.5492637802198033,
					0
				],
				[
					6.197055120879213,
					0
				],
				[
					7.746318901099016,
					1.5492637802198033
				],
				[
					5.422423230769368,
					4.647791340659467
				],
				[
					2.3238956703297617,
					7.746318901099073
				],
				[
					3.0985275604396065,
					7.746318901099073
				],
				[
					3.873159450549565,
					6.9716870109891715
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15609918534755707,
				0.22845400869846344,
				0.2393915057182312,
				0.23846834897994995,
				0.2970854640007019,
				0.3481571674346924,
				0.16371197998523712,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1833136142,
			"isDeleted": false,
			"id": "xGzTwrRFujIS8nZvFDun-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 369.98097218907105,
			"y": 29.916980073811658,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1901580561735727,
			"height": 2.975395140434159,
			"seed": 618928896,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5950790280868432,
					0
				],
				[
					-1.1901580561735727,
					0
				],
				[
					-1.1901580561735727,
					0.5950790280868432
				],
				[
					-1.1901580561735727,
					1.1901580561736864
				],
				[
					-1.1901580561735727,
					1.7852370842605296
				],
				[
					-1.1901580561735727,
					2.380316112347316
				],
				[
					-1.1901580561735727,
					2.975395140434159
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
				0,
				0,
				0,
				0,
				0,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 250994642,
			"isDeleted": false,
			"id": "Shoc2NpbAnQUDZyZEJqCM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 367.6006560767238,
			"y": 31.107138129985344,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.355711252781475,
			"height": 10.71142250556295,
			"seed": 1493891840,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5950790280868432
				],
				[
					0.5950790280868432,
					0.5950790280868432
				],
				[
					0.5950790280868432,
					1.1901580561736296
				],
				[
					2.380316112347259,
					-0.5950790280868432
				],
				[
					4.165553196607789,
					-3.5704741685210024
				],
				[
					5.355711252781475,
					-5.355711252781475
				],
				[
					4.760632224694632,
					-4.760632224694632
				],
				[
					4.760632224694632,
					-2.380316112347316
				],
				[
					4.760632224694632,
					1.7852370842604728
				],
				[
					4.760632224694632,
					5.355711252781475
				],
				[
					5.355711252781475,
					5.355711252781475
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06530346721410751,
				0.08442220836877823,
				0.15772277116775513,
				0.15325653553009033,
				0.1442120373249054,
				0.15602990984916687,
				0.17456158995628357,
				0.21078293025493622,
				0.22900286316871643,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1807105614,
			"isDeleted": false,
			"id": "hPUBHL8YvdotGEAwuM73U",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 377.12192052611306,
			"y": 33.48745424233266,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.380316112347373,
			"height": 6.545869308955105,
			"seed": 1472404224,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5950790280868432
				],
				[
					-1.1901580561736864,
					-0.5950790280868432
				],
				[
					-1.7852370842605296,
					0.5950790280868432
				],
				[
					-1.1901580561736864,
					1.7852370842604728
				],
				[
					0.5950790280868432,
					4.165553196607789
				],
				[
					0.5950790280868432,
					5.950790280868262
				],
				[
					-0.5950790280868432,
					5.950790280868262
				],
				[
					-1.1901580561736864,
					4.760632224694632
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
				0.056139253079891205,
				0.12331979721784592,
				0.14782842993736267,
				0.12992584705352783,
				0.14113400876522064,
				0.19227533042430878,
				0.15667258203029633,
				0.00798333715647459,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 9311634,
			"isDeleted": false,
			"id": "xLi80JSwAq_cv-ii2URkM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 382.47763177889453,
			"y": 26.9415849333775,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1901580561736864,
			"height": 11.901580561736637,
			"seed": 1347590912,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					2.975395140434159
				],
				[
					0.5950790280868432,
					10.116343477476107
				],
				[
					1.1901580561736864,
					11.901580561736637
				],
				[
					0.5950790280868432,
					10.71142250556295
				],
				[
					0.5950790280868432,
					10.116343477476107
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2088720053434372,
				0.2732210159301758,
				0.1989639550447464,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 657802382,
			"isDeleted": false,
			"id": "NnJlAG1uei9hXGLNahOpA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 378.9071576103736,
			"y": 33.48745424233266,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.140948337041891,
			"height": 1.7852370842604728,
			"seed": 1600060160,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5950790280868432
				],
				[
					2.9753951404341024,
					0
				],
				[
					7.140948337041891,
					0.5950790280868432
				],
				[
					7.140948337041891,
					1.1901580561736296
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.058641478419303894,
				0.2483699917793274,
				0.11012481898069382,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 66,
			"versionNonce": 85562194,
			"isDeleted": false,
			"id": "KoznGCVyC_7gezhu9DNzu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 364.6252609362896,
			"y": 22.77603173676971,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 32.729346544775694,
			"height": 27.373635291994162,
			"seed": 950450944,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.1901580561735727,
					0
				],
				[
					-2.380316112347259,
					2.380316112347316
				],
				[
					-2.9753951404341024,
					6.545869308955105
				],
				[
					-1.785237084260416,
					10.71142250556295
				],
				[
					1.1901580561736864,
					14.87697570217074
				],
				[
					4.1655531966079025,
					19.042528898778585
				],
				[
					8.926185421302534,
					21.4228450111259
				],
				[
					14.28189667408401,
					22.61300306729953
				],
				[
					20.232686954952214,
					21.4228450111259
				],
				[
					24.99331917964696,
					17.8523708426049
				],
				[
					27.37363529199422,
					12.496659589823423
				],
				[
					27.37363529199422,
					7.140948337041948
				],
				[
					24.99331917964696,
					2.380316112347316
				],
				[
					20.827765983039058,
					-1.7852370842604728
				],
				[
					13.686817645997166,
					-4.760632224694632
				],
				[
					5.355711252781475,
					-2.975395140434159
				],
				[
					-2.380316112347259,
					2.975395140434159
				],
				[
					-5.355711252781475,
					8.331106393215634
				],
				[
					-4.760632224694632,
					8.926185421302478
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07753970474004745,
				0.16633331775665283,
				0.21811780333518982,
				0.26065096259117126,
				0.27969199419021606,
				0.2762082815170288,
				0.2662651240825653,
				0.2687269151210785,
				0.272927850484848,
				0.24952350556850433,
				0.29588231444358826,
				0.28993767499923706,
				0.2687035799026489,
				0.2565107047557831,
				0.24753844738006592,
				0.2653496265411377,
				0.26008281111717224,
				0.10474615544080734,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 561611470,
			"isDeleted": false,
			"id": "s_ojJvYpYxjH4wtQ9b45k",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 395.56937039680474,
			"y": 34.0825332704195,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.736027365128848,
			"height": 1.1901580561736864,
			"seed": 1702615808,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.380316112347373,
					0
				],
				[
					5.355711252781475,
					0
				],
				[
					7.736027365128848,
					-1.1901580561736864
				],
				[
					7.736027365128848,
					-1.1901580561736864
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2488200068473816,
				0.3010839819908142,
				0.08872467279434204,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1861179666,
			"isDeleted": false,
			"id": "xPX4NhGtsnj9Os8bjwd5I",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 407.4709509585414,
			"y": 29.321901045724815,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.331106393215691,
			"height": 7.140948337042005,
			"seed": 2073795328,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5950790280868432,
					0
				],
				[
					2.9753951404341024,
					0
				],
				[
					7.140948337042005,
					1.1901580561736864
				],
				[
					7.736027365128848,
					2.975395140434159
				],
				[
					4.760632224694632,
					5.355711252781475
				],
				[
					1.7852370842605296,
					7.140948337042005
				],
				[
					1.1901580561736864,
					7.140948337042005
				],
				[
					2.9753951404341024,
					6.545869308955162
				],
				[
					3.5704741685209456,
					5.950790280868318
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.2449599951505661,
				0.22817052900791168,
				0.22356531023979187,
				0.2903134226799011,
				0.3514373004436493,
				0.34869518876075745,
				0.1252427101135254,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1025243406,
			"isDeleted": false,
			"id": "I2WAxNzYw2xzc-2y7oLdu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 420.5626895764517,
			"y": 27.536663961464342,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.736027365128734,
			"height": 9.521264449389264,
			"seed": 1098021632,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5950790280868432,
					0.5950790280868432
				],
				[
					-0.5950790280868432,
					1.7852370842604728
				],
				[
					0,
					5.355711252781475
				],
				[
					4.760632224694632,
					7.140948337041948
				],
				[
					7.140948337041891,
					2.975395140434159
				],
				[
					6.545869308955048,
					-1.1901580561736296
				],
				[
					3.5704741685209456,
					-2.380316112347316
				],
				[
					-0.5950790280868432,
					0
				],
				[
					1.785237084260416,
					3.5704741685210024
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
				0.05339599773287773,
				0.12804639339447021,
				0.20438598096370697,
				0.19346776604652405,
				0.1294710338115692,
				0.12245699763298035,
				0.1400982290506363,
				0.15381750464439392,
				0.01252993755042553,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 763782866,
			"isDeleted": false,
			"id": "rsPryzaROUQzJ3R3sKf-Z",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 424.7282427730595,
			"y": 26.346505905290712,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.331106393215578,
			"height": 21.422845011125844,
			"seed": 1073388288,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5950790280868432,
					1.1901580561736296
				],
				[
					-0.5950790280868432,
					2.380316112347316
				],
				[
					0.5950790280868432,
					6.545869308955105
				],
				[
					2.9753951404341024,
					13.09173861791021
				],
				[
					2.9753951404341024,
					17.8523708426049
				],
				[
					0,
					21.422845011125844
				],
				[
					-4.165553196607789,
					21.422845011125844
				],
				[
					-5.355711252781475,
					16.06713375834437
				],
				[
					-5.355711252781475,
					15.472054730257582
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10313799977302551,
				0.1535317748785019,
				0.2039465308189392,
				0.25848108530044556,
				0.2780722975730896,
				0.23791241645812988,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 563455822,
			"isDeleted": false,
			"id": "3nR59ekXH7Lnx7bBnIP_2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 429.4888749977541,
			"y": 26.9415849333775,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.140948337042005,
			"height": 7.736027365128791,
			"seed": 1597078272,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.1901580561736864,
					0.5950790280868432
				],
				[
					-1.7852370842605296,
					1.7852370842605296
				],
				[
					-1.7852370842605296,
					2.975395140434159
				],
				[
					-0.5950790280868432,
					5.355711252781475
				],
				[
					2.9753951404341024,
					4.760632224694689
				],
				[
					5.355711252781475,
					1.7852370842605296
				],
				[
					4.165553196607789,
					-1.1901580561736296
				],
				[
					1.1901580561736864,
					-2.380316112347316
				],
				[
					-1.1901580561736864,
					-0.5950790280867864
				],
				[
					0,
					1.7852370842605296
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
				0.056499481201171875,
				0.08372427523136139,
				0.15391598641872406,
				0.17979134619235992,
				0.14208398759365082,
				0.11628931015729904,
				0.11817172169685364,
				0.13354137539863586,
				0.10426623374223709,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 695581842,
			"isDeleted": false,
			"id": "kD8zRKvJ7CXYAv4xvuj8W",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 434.24950722244876,
			"y": 26.9415849333775,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.545869308955162,
			"height": 8.331106393215634,
			"seed": 258882304,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5950790280868432,
					0.5950790280868432
				],
				[
					-1.1901580561736864,
					1.1901580561736864
				],
				[
					-1.1901580561736864,
					2.380316112347316
				],
				[
					0.5950790280868432,
					4.760632224694689
				],
				[
					3.5704741685209456,
					4.760632224694689
				],
				[
					5.355711252781475,
					1.7852370842605296
				],
				[
					4.760632224694632,
					-1.7852370842604728
				],
				[
					1.7852370842605296,
					-3.5704741685209456
				],
				[
					-0.5950790280868432,
					-1.1901580561736296
				],
				[
					0,
					2.380316112347316
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
				0.07987399399280548,
				0.12338000535964966,
				0.16653800010681152,
				0.14447277784347534,
				0.1341676265001297,
				0.1391371190547943,
				0.1315474510192871,
				0.12099142372608185,
				0.008971069008111954,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 524258702,
			"isDeleted": false,
			"id": "infXLhZc1LQ56TdqS4ABD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 443.770771671838,
			"y": 17.420320483988235,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.92618542130242,
			"height": 14.281896674083953,
			"seed": 307952384,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.1901580561736864
				],
				[
					0.5950790280868432,
					3.5704741685210024
				],
				[
					1.1901580561736864,
					9.521264449389264
				],
				[
					1.7852370842605296,
					11.306501533649794
				],
				[
					0,
					10.71142250556295
				],
				[
					-2.9753951404341024,
					9.521264449389264
				],
				[
					-4.760632224694632,
					11.306501533649794
				],
				[
					-4.165553196607789,
					13.68681764599711
				],
				[
					-0.5950790280868432,
					14.281896674083953
				],
				[
					3.5704741685209456,
					13.091738617910266
				],
				[
					4.165553196607789,
					12.496659589823423
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1147649809718132,
				0.16124099493026733,
				0.2223755121231079,
				0.22618438303470612,
				0.14741958677768707,
				0.10058379918336868,
				0.14407561719417572,
				0.2288695126771927,
				0.2279323786497116,
				0.1318436563014984,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 67,
			"versionNonce": 544496210,
			"isDeleted": false,
			"id": "rGEee2IbtUNmssxWBKvXl",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 461.02806348635613,
			"y": 26.9415849333775,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.92618542130242,
			"height": 30.34903043242832,
			"seed": 1863523072,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5950790280868432,
					-0.5950790280867864
				],
				[
					1.785237084260416,
					-2.380316112347316
				],
				[
					3.5704741685209456,
					-4.760632224694632
				],
				[
					5.355711252781475,
					-7.736027365128791
				],
				[
					7.140948337041891,
					-14.281896674083896
				],
				[
					5.950790280868205,
					-17.257291814518055
				],
				[
					3.5704741685209456,
					-16.662212786431212
				],
				[
					1.1901580561735727,
					-13.686817645997053
				],
				[
					0,
					-9.521264449389264
				],
				[
					1.1901580561735727,
					-2.9753951404341024
				],
				[
					3.5704741685209456,
					4.165553196607846
				],
				[
					4.760632224694632,
					9.52126444938932
				],
				[
					4.165553196607789,
					12.496659589823423
				],
				[
					1.785237084260416,
					13.091738617910266
				],
				[
					-1.1901580561736864,
					11.901580561736637
				],
				[
					-1.7852370842605296,
					8.331106393215634
				],
				[
					0,
					4.165553196607846
				],
				[
					3.5704741685209456,
					1.1901580561736864
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
				0.06819473206996918,
				0.12478320300579071,
				0.160246342420578,
				0.135514497756958,
				0.10427819937467575,
				0.11614346504211426,
				0.13626635074615479,
				0.14369283616542816,
				0.16018207371234894,
				0.1734512597322464,
				0.18903738260269165,
				0.1905282586812973,
				0.16751578450202942,
				0.13531158864498138,
				0.10775619745254517,
				0.07565063238143921,
				0.0037042235489934683,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 324185038,
			"isDeleted": false,
			"id": "OiwlkIA5_y-n6Q96JbHLH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 468.76409085148487,
			"y": 25.156347849117026,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.355711252781475,
			"height": 7.140948337041948,
			"seed": 1814878976,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5950790280868432,
					1.1901580561736864
				],
				[
					-0.5950790280868432,
					1.7852370842604728
				],
				[
					-1.1901580561736864,
					2.975395140434159
				],
				[
					0,
					4.760632224694632
				],
				[
					2.380316112347373,
					4.760632224694632
				],
				[
					4.165553196607789,
					2.380316112347316
				],
				[
					3.5704741685209456,
					-1.1901580561736296
				],
				[
					1.1901580561736864,
					-2.380316112347316
				],
				[
					-1.1901580561736864,
					2.380316112347316
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
				0.07981298863887787,
				0.09328000247478485,
				0.13384398818016052,
				0.1513356864452362,
				0.12461340427398682,
				0.12462872266769409,
				0.10260836780071259,
				0.08045803755521774,
				0.01895083673298359,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 22626322,
			"isDeleted": false,
			"id": "4xD2164pOdPoF-MwN3njs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 472.92964404809265,
			"y": 24.561268821030183,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.545869308955162,
			"height": 7.736027365128791,
			"seed": 500759296,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5950790280868432,
					2.975395140434159
				],
				[
					-0.5950790280868432,
					4.165553196607846
				],
				[
					1.1901580561736864,
					4.760632224694632
				],
				[
					2.975395140434216,
					1.7852370842605296
				],
				[
					5.950790280868318,
					-2.380316112347316
				],
				[
					5.950790280868318,
					-2.975395140434159
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12642599642276764,
				0.15710800886154175,
				0.14953933656215668,
				0.12166962027549744,
				0.0602310486137867,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 61,
			"versionNonce": 1273496078,
			"isDeleted": false,
			"id": "NCMX1Dc4jepHtnzYZbhM0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 486.6164616940898,
			"y": 22.180952708682867,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.521264449389264,
			"height": 7.140948337042005,
			"seed": 1223555840,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.1901580561736864
				],
				[
					1.1901580561735727,
					4.165553196607846
				],
				[
					1.785237084260416,
					5.950790280868318
				],
				[
					1.785237084260416,
					4.760632224694632
				],
				[
					2.9753951404341024,
					0.5950790280868432
				],
				[
					4.760632224694632,
					-0.5950790280868432
				],
				[
					5.355711252781475,
					2.975395140434159
				],
				[
					5.355711252781475,
					5.950790280868318
				],
				[
					5.950790280868205,
					4.760632224694632
				],
				[
					7.736027365128734,
					1.1901580561736864
				],
				[
					8.92618542130242,
					0.5950790280868432
				],
				[
					9.521264449389264,
					2.975395140434159
				],
				[
					8.92618542130242,
					6.545869308955162
				],
				[
					8.92618542130242,
					6.545869308955162
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15167614817619324,
				0.16394662857055664,
				0.13738355040550232,
				0.06606228649616241,
				0.03215274214744568,
				0.09125479310750961,
				0.1602109670639038,
				0.19349393248558044,
				0.10590911656618118,
				0.04556707665324211,
				0.12924587726593018,
				0.2072686403989792,
				0.07033059746026993,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 1209757138,
			"isDeleted": false,
			"id": "R0MUnzQY_toPTTfDS1QE_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 500.3032793400869,
			"y": 22.77603173676971,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.736027365128734,
			"height": 7.736027365128791,
			"seed": 806877952,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5950790280868432,
					0
				],
				[
					-1.1901580561736864,
					0.5950790280868432
				],
				[
					-1.7852370842605296,
					1.1901580561736864
				],
				[
					-2.9753951404341024,
					4.165553196607789
				],
				[
					-1.1901580561736864,
					5.355711252781475
				],
				[
					2.380316112347373,
					4.760632224694632
				],
				[
					4.165553196607789,
					1.7852370842604728
				],
				[
					2.9753951404341024,
					-1.1901580561736864
				],
				[
					-1.1901580561736864,
					-2.380316112347316
				],
				[
					-3.5704741685209456,
					1.7852370842604728
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
				0.12204397469758987,
				0.16335998475551605,
				0.2195960134267807,
				0.20997607707977295,
				0.18924853205680847,
				0.1621471792459488,
				0.15186196565628052,
				0.12845160067081451,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 1811451982,
			"isDeleted": false,
			"id": "laGxOZEIvoxDLnjDjmu6J",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 503.8737535086078,
			"y": 22.180952708682867,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.165553196607789,
			"height": 7.736027365128791,
			"seed": 1391770368,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.1901580561735727,
					0
				],
				[
					-1.785237084260416,
					0
				],
				[
					0.5950790280868432,
					2.380316112347316
				],
				[
					2.380316112347373,
					4.760632224694632
				],
				[
					2.380316112347373,
					7.140948337041948
				],
				[
					-0.5950790280868432,
					7.736027365128791
				],
				[
					-1.1901580561735727,
					5.355711252781475
				],
				[
					-1.1901580561735727,
					4.760632224694632
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12754400074481964,
				0.12240912020206451,
				0.14182934165000916,
				0.2329152524471283,
				0.21294231712818146,
				0.01537023950368166,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1506927506,
			"isDeleted": false,
			"id": "8YZ0SR7xagT8kiApTCM-_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 510.419622817563,
			"y": 11.469530203119916,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.9753951404341024,
			"height": 18.44744987069174,
			"seed": 1968634624,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					2.380316112347316
				],
				[
					1.1901580561736864,
					11.306501533649794
				],
				[
					2.9753951404341024,
					18.44744987069174
				],
				[
					1.7852370842605296,
					17.257291814518112
				],
				[
					1.1901580561736864,
					16.66221278643127
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16701099276542664,
				0.2458139955997467,
				0.2539435029029846,
				0.012246246449649334,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1331517070,
			"isDeleted": false,
			"id": "aBKrk_XKFIyyswQGBnGy-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 506.84914864904204,
			"y": 21.585873680596023,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.521264449389264,
			"height": 1.7852370842605296,
			"seed": 118446848,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5950790280868432,
					0
				],
				[
					1.1901580561735727,
					0
				],
				[
					5.355711252781475,
					0.5950790280868432
				],
				[
					9.521264449389264,
					1.7852370842605296
				],
				[
					9.521264449389264,
					1.7852370842605296
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12822699546813965,
				0.27501800656318665,
				0.12316973507404327,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 1622384978,
			"isDeleted": false,
			"id": "1DyIiHg8JKGUR825-Q19P",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 340.8220998128164,
			"y": 79.30853940501856,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 33.91950460094927,
			"height": 24.398240151560003,
			"seed": 770947840,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.1901580561736864,
					0
				],
				[
					4.760632224694632,
					2.975395140434159
				],
				[
					7.140948337042005,
					7.736027365128791
				],
				[
					7.140948337042005,
					11.306501533649794
				],
				[
					8.331106393215578,
					15.472054730257582
				],
				[
					10.71142250556295,
					19.042528898778585
				],
				[
					15.472054730257582,
					21.4228450111259
				],
				[
					22.613003067299587,
					23.208082095386374
				],
				[
					29.158872376254635,
					23.208082095386374
				],
				[
					33.91950460094927,
					22.61300306729953
				],
				[
					31.539188488602008,
					23.803161123473217
				],
				[
					30.944109460515165,
					24.398240151560003
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13427050411701202,
				0.20121124386787415,
				0.2172103226184845,
				0.2327292412519455,
				0.2654581069946289,
				0.2869488596916199,
				0.3095499575138092,
				0.3431389629840851,
				0.38311415910720825,
				0.38933661580085754,
				0.06228234991431236,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1859081422,
			"isDeleted": false,
			"id": "xbxxWBKYuRq8HGLGnXD3O",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 380.692394694634,
			"y": 97.7559892757103,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.521264449389378,
			"height": 9.521264449389264,
			"seed": 289438464,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5950790280868432,
					0
				],
				[
					3.5704741685210593,
					1.7852370842604728
				],
				[
					7.736027365128848,
					4.165553196607789
				],
				[
					8.926185421302534,
					5.950790280868262
				],
				[
					7.140948337042005,
					7.736027365128791
				],
				[
					4.165553196607789,
					9.521264449389264
				],
				[
					2.975395140434216,
					9.521264449389264
				],
				[
					4.760632224694632,
					8.331106393215634
				],
				[
					5.355711252781475,
					8.331106393215634
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.26363855600357056,
				0.25502729415893555,
				0.2714746594429016,
				0.3388199508190155,
				0.4142468571662903,
				0.43113604187965393,
				0.12286468595266342,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 672638738,
			"isDeleted": false,
			"id": "eEL8RZWPdBA-oWFnZDu2d",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 442.58061361566433,
			"y": 38.843165495114135,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7852370842605296,
			"height": 13.091738617910266,
			"seed": 65231616,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5950790280868432,
					0
				],
				[
					0,
					0.5950790280867864
				],
				[
					1.1901580561736864,
					3.5704741685209456
				],
				[
					1.1901580561736864,
					8.92618542130242
				],
				[
					0.5950790280868432,
					12.496659589823423
				],
				[
					0.5950790280868432,
					13.091738617910266
				],
				[
					0.5950790280868432,
					11.90158056173658
				],
				[
					0.5950790280868432,
					11.90158056173658
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06150833144783974,
				0.18519918620586395,
				0.23631027340888977,
				0.3036605417728424,
				0.32587146759033203,
				0.2543891668319702,
				0.04621044918894768,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1139247886,
			"isDeleted": false,
			"id": "TnNtlToCGVQnsdW1_KKJG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 435.43966527862244,
			"y": 56.695536337719034,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.257291814518,
			"height": 2.380316112347316,
			"seed": 1249745664,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405045,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.1901580561736864,
					0
				],
				[
					0.5950790280868432,
					0
				],
				[
					5.950790280868205,
					-1.1901580561736864
				],
				[
					12.496659589823366,
					-2.380316112347316
				],
				[
					16.067133758344312,
					-2.380316112347316
				],
				[
					14.87697570217074,
					-1.7852370842605296
				],
				[
					14.87697570217074,
					-1.1901580561736864
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0731215551495552,
				0.23130200803279877,
				0.3261120021343231,
				0.40483999252319336,
				0.3710947632789612,
				0.06361837685108185,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 2020930770,
			"isDeleted": false,
			"id": "xe4-RJxclH9T7abKWlHVu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 441.9855345875775,
			"y": 59.67093147815319,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7852370842605296,
			"height": 14.281896674083896,
			"seed": 1810316032,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5950790280868432
				],
				[
					0.5950790280868432,
					1.1901580561736296
				],
				[
					1.7852370842605296,
					6.545869308955105
				],
				[
					1.1901580561736864,
					11.90158056173658
				],
				[
					0.5950790280868432,
					13.686817645997053
				],
				[
					0.5950790280868432,
					13.686817645997053
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1997559815645218,
				0.28888997435569763,
				0.339758038520813,
				0.054793089628219604,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 757004622,
			"isDeleted": false,
			"id": "uQ6Cc0t18023SjHJZy0R0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 435.43966527862244,
			"y": 77.52330232075809,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.901580561736523,
			"height": 6.545869308955105,
			"seed": 1958492928,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.1901580561735727,
					2.380316112347316
				],
				[
					3.5704741685209456,
					3.5704741685209456
				],
				[
					7.140948337041891,
					1.7852370842604728
				],
				[
					9.521264449389264,
					-1.1901580561736864
				],
				[
					11.30650153364968,
					-2.975395140434159
				],
				[
					11.901580561736523,
					-2.975395140434159
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19926156103610992,
				0.24049849808216095,
				0.2801809012889862,
				0.26140984892845154,
				0.04436489939689636,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 1935837842,
			"isDeleted": false,
			"id": "e2ph1q_71jvWAYuPraYim",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 394.8244686330336,
			"y": 104.20543696520761,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.720169410278686,
			"height": 17.98081881634704,
			"seed": 412171008,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6200282350464477
				],
				[
					-0.6200282350464477,
					-1.2400564700928953
				],
				[
					0,
					1.2400564700928953
				],
				[
					1.860084705139343,
					8.060367055603876
				],
				[
					3.1001411752322383,
					16.120734111207696
				],
				[
					3.1001411752322383,
					16.740762346254144
				],
				[
					1.2400564700928953,
					14.260649406068353
				],
				[
					1.2400564700928953,
					13.640621171021905
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0508238822221756,
				0.10297875851392746,
				0.14778463542461395,
				0.15891693532466888,
				0.10086172819137573,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 1372495758,
			"isDeleted": false,
			"id": "ZHMeuDnNht4nUIgCHxsLA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 393.5844121629407,
			"y": 104.82546520025406,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.580254115418029,
			"height": 8.060367055603876,
			"seed": 961772288,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6200282350464477
				],
				[
					0,
					-1.860084705139343
				],
				[
					0.6200282350464477,
					-2.4801129401857906
				],
				[
					3.1001411752322383,
					-3.1001411752322383
				],
				[
					5.580254115418029,
					-1.2400564700928953
				],
				[
					5.580254115418029,
					2.4801129401857906
				],
				[
					2.4801129401857906,
					4.960225880371638
				],
				[
					2.4801129401857906,
					4.3401976453251905
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.01954168640077114,
				0.05750378593802452,
				0.10683175921440125,
				0.11897674202919006,
				0.12850506603717804,
				0.018205992877483368,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1872193618,
			"isDeleted": false,
			"id": "IPITCyVL2a_Zs_zgoda3U",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 401.02475098349805,
			"y": 101.10529578997537,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.200282350464477,
			"height": 7.440338820557372,
			"seed": 944093952,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6200282350464477,
					0
				],
				[
					1.2400564700928953,
					3.1001411752322383
				],
				[
					1.860084705139343,
					6.200282350464477
				],
				[
					1.860084705139343,
					5.580254115418029
				],
				[
					3.1001411752322383,
					1.2400564700928953
				],
				[
					5.580254115418029,
					-0.6200282350464477
				],
				[
					6.200282350464477,
					-1.2400564700928953
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05849621444940567,
				0.11210467666387558,
				0.10798434168100357,
				0.078469417989254,
				0.0731038823723793,
				0.007865844294428825,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 103775694,
			"isDeleted": false,
			"id": "0oFBp1hcR4qKUwYdjNaWW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 409.08511803910187,
			"y": 101.72532402502182,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.200282350464477,
			"height": 8.680395290650267,
			"seed": 227236608,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6200282350464477
				],
				[
					-1.2400564700928953,
					2.4801129401857906
				],
				[
					-0.6200282350464477,
					4.960225880371581
				],
				[
					1.860084705139343,
					5.580254115418029
				],
				[
					3.720169410278686,
					3.720169410278686
				],
				[
					4.340197645325134,
					0
				],
				[
					1.860084705139343,
					-3.1001411752322383
				],
				[
					-1.2400564700928953,
					-3.1001411752322383
				],
				[
					-1.860084705139343,
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
				0.12060800194740295,
				0.14304016530513763,
				0.12579943239688873,
				0.11933474987745285,
				0.11002395302057266,
				0.0893765240907669,
				0.07442153990268707,
				0.02199060097336769,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 1424657938,
			"isDeleted": false,
			"id": "YFQHbn05_e53VBO2gtKgT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 414.6653721545199,
			"y": 91.18484402923215,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.820310585511038,
			"height": 14.8806776411148,
			"seed": 2108128000,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6200282350464477,
					0.6200282350464477
				],
				[
					0,
					4.960225880371638
				],
				[
					0,
					9.92045176074322
				],
				[
					-0.6200282350464477,
					10.540479995789667
				],
				[
					0.6200282350465613,
					9.92045176074322
				],
				[
					3.7201694102787997,
					8.680395290650324
				],
				[
					6.20028235046459,
					10.540479995789667
				],
				[
					6.20028235046459,
					13.640621171021905
				],
				[
					2.4801129401859043,
					14.8806776411148
				],
				[
					-0.6200282350464477,
					14.260649406068353
				],
				[
					-0.6200282350464477,
					12.40056470092901
				],
				[
					0,
					11.780536465882562
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09294592589139938,
				0.1253027617931366,
				0.150054931640625,
				0.12222198396921158,
				0.09970168769359589,
				0.1178484782576561,
				0.1594187319278717,
				0.19585931301116943,
				0.19753655791282654,
				0.13998642563819885,
				0.012845397926867008,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 794465294,
			"isDeleted": false,
			"id": "GQY2N9xr717PvJFuSM-_S",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 423.3457674451703,
			"y": 88.08470285399991,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2400564700928953,
			"height": 19.220875286439934,
			"seed": 124009216,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6200282350464477
				],
				[
					-0.6200282350464477,
					1.860084705139343
				],
				[
					0,
					7.440338820557429
				],
				[
					0.6200282350464477,
					15.500705876161248
				],
				[
					0,
					19.220875286439934
				],
				[
					-0.6200282350464477,
					18.600847051393487
				],
				[
					-0.6200282350464477,
					17.98081881634704
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1218971237540245,
				0.20125798881053925,
				0.24319332838058472,
				0.1517697125673294,
				0.011619018390774727,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 2018704338,
			"isDeleted": false,
			"id": "fTRm2SiN0lRANoyKs1JJ7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 427.06593685544897,
			"y": 102.34535226006827,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.780536465882506,
			"height": 7.440338820557372,
			"seed": 1582947072,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6200282350464477,
					0
				],
				[
					1.2400564700928953,
					0
				],
				[
					3.1001411752322383,
					0
				],
				[
					3.1001411752322383,
					-1.860084705139343
				],
				[
					0.6200282350464477,
					-1.860084705139343
				],
				[
					-1.2400564700928953,
					1.2400564700928953
				],
				[
					0,
					4.960225880371581
				],
				[
					3.720169410278686,
					5.580254115418029
				],
				[
					9.300423525696715,
					1.860084705139343
				],
				[
					10.54047999578961,
					0.6200282350464477
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.05874740704894066,
				0.10600680857896805,
				0.08098431676626205,
				0.09447811543941498,
				0.19504910707473755,
				0.27921199798583984,
				0.19131246209144592,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 61,
			"versionNonce": 659087950,
			"isDeleted": false,
			"id": "sli7lq9d0MEhwHGUvYWfb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 433.8862474409599,
			"y": 101.10529578997537,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.680395290650267,
			"height": 8.06036705560382,
			"seed": 1120492288,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6200282350464477,
					3.1001411752322383
				],
				[
					1.2400564700928953,
					4.340197645325134
				],
				[
					1.860084705139343,
					4.340197645325134
				],
				[
					2.4801129401857906,
					0
				],
				[
					4.340197645325134,
					-1.860084705139343
				],
				[
					4.960225880371581,
					1.2400564700928953
				],
				[
					4.960225880371581,
					4.960225880371581
				],
				[
					5.580254115418029,
					5.580254115418029
				],
				[
					6.820310585510924,
					0.6200282350464477
				],
				[
					8.06036705560382,
					-1.860084705139343
				],
				[
					8.680395290650267,
					0
				],
				[
					8.06036705560382,
					4.340197645325134
				],
				[
					8.06036705560382,
					6.200282350464477
				],
				[
					8.06036705560382,
					5.580254115418029
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.18201673030853271,
				0.1647047996520996,
				0.08704705536365509,
				0.04833975061774254,
				0.09581536799669266,
				0.1535293012857437,
				0.20516595244407654,
				0.1401141732931137,
				0.052777037024497986,
				0.0787036120891571,
				0.1709403097629547,
				0.23317575454711914,
				0.11614175140857697,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 2011672978,
			"isDeleted": false,
			"id": "d4XuIDd90SAtWNUzasGDU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 447.52686861198185,
			"y": 100.48526755492892,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.20028235046459,
			"height": 7.440338820557372,
			"seed": 1462983424,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6200282350464477
				],
				[
					-1.860084705139343,
					-0.6200282350464477
				],
				[
					-1.860084705139343,
					1.860084705139343
				],
				[
					0.6200282350464477,
					4.340197645325134
				],
				[
					1.860084705139343,
					6.200282350464477
				],
				[
					-0.6200282350464477,
					6.820310585510924
				],
				[
					-4.340197645325247,
					4.960225880371581
				],
				[
					-3.7201694102787997,
					4.960225880371581
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.03358297795057297,
				0.18638800084590912,
				0.18642163276672363,
				0.17358675599098206,
				0.19411687552928925,
				0.2435562163591385,
				0.09295431524515152,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 550725774,
			"isDeleted": false,
			"id": "WezU3Ds_WQZUkpyyh_xy2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 463.6476027231895,
			"y": 101.10529578997537,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.580254115418029,
			"height": 8.680395290650267,
			"seed": 969775872,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.2400564700928953,
					0
				],
				[
					-1.860084705139343,
					1.860084705139343
				],
				[
					-0.6200282350464477,
					4.340197645325134
				],
				[
					2.4801129401857906,
					5.580254115418029
				],
				[
					3.720169410278686,
					3.1001411752322383
				],
				[
					3.1001411752322383,
					-1.2400564700928953
				],
				[
					0,
					-3.1001411752322383
				],
				[
					-1.860084705139343,
					-1.2400564700928953
				],
				[
					-1.860084705139343,
					1.2400564700928953
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
				0.10199273377656937,
				0.1604880690574646,
				0.191832035779953,
				0.16940344870090485,
				0.14745374023914337,
				0.12977972626686096,
				0.138977512717247,
				0.11673706024885178,
				0.014666992239654064,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 63,
			"versionNonce": 383758162,
			"isDeleted": false,
			"id": "TH5s-42FJiANpc5ussawY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 467.9878003685146,
			"y": 102.34535226006827,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.300423525696715,
			"height": 30.38138351727605,
			"seed": 1245821696,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.2400564700928953,
					-0.6200282350464477
				],
				[
					5.580254115418029,
					-4.960225880371581
				],
				[
					6.820310585510924,
					-11.160508230836115
				],
				[
					4.340197645325134,
					-14.8806776411148
				],
				[
					1.860084705139343,
					-15.500705876161248
				],
				[
					1.2400564700928953,
					-11.160508230836115
				],
				[
					1.2400564700928953,
					-5.580254115418029
				],
				[
					3.720169410278686,
					1.2400564700928953
				],
				[
					4.960225880371581,
					8.680395290650324
				],
				[
					3.720169410278686,
					13.640621171021905
				],
				[
					0.6200282350464477,
					14.8806776411148
				],
				[
					-1.860084705139343,
					11.160508230836115
				],
				[
					-0.6200282350464477,
					7.440338820557429
				],
				[
					2.4801129401857906,
					3.1001411752322383
				],
				[
					6.820310585510924,
					-0.6200282350464477
				],
				[
					7.440338820557372,
					-0.6200282350464477
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1671355962753296,
				0.17573824524879456,
				0.1562596708536148,
				0.1397918164730072,
				0.1349714994430542,
				0.13945794105529785,
				0.14275100827217102,
				0.14955365657806396,
				0.13960900902748108,
				0.13365136086940765,
				0.13191403448581696,
				0.11999692022800446,
				0.12872421741485596,
				0.16754351556301117,
				0.0871596410870552,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 196290254,
			"isDeleted": false,
			"id": "y-SYv4smoAPkfXuNnoXgo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 489.06876036009396,
			"y": 88.70473108904636,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.300423525696715,
			"height": 17.36079058130059,
			"seed": 1350105856,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6200282350464477
				],
				[
					0.6200282350464477,
					2.4801129401857906
				],
				[
					1.2400564700928953,
					8.680395290650324
				],
				[
					1.860084705139343,
					11.160508230836115
				],
				[
					1.2400564700928953,
					9.92045176074322
				],
				[
					-1.2400564700928953,
					8.680395290650324
				],
				[
					-4.340197645325134,
					8.680395290650324
				],
				[
					-6.820310585510924,
					11.780536465882562
				],
				[
					-5.580254115418029,
					15.500705876161248
				],
				[
					-1.860084705139343,
					16.740762346254144
				],
				[
					2.4801129401857906,
					13.640621171021905
				],
				[
					2.4801129401857906,
					13.020592935975458
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08435998857021332,
				0.19724398851394653,
				0.24828600883483887,
				0.24491995573043823,
				0.16678278148174286,
				0.12485876679420471,
				0.16646093130111694,
				0.22034023702144623,
				0.25659215450286865,
				0.24983486533164978,
				0.008190124295651913,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 428995858,
			"isDeleted": false,
			"id": "hRl1T2Dqrw5wLHVc5YeD7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 494.649014475512,
			"y": 99.24521108483603,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.440338820557372,
			"height": 8.06036705560382,
			"seed": 93698816,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6200282350464477,
					-0.6200282350464477
				],
				[
					1.2400564700928953,
					-0.6200282350464477
				],
				[
					1.860084705139343,
					-1.2400564700928953
				],
				[
					2.4801129401857906,
					-2.4801129401857906
				],
				[
					1.2400564700928953,
					-3.1001411752322383
				],
				[
					-1.860084705139343,
					-1.2400564700928953
				],
				[
					-2.4801129401857906,
					1.860084705139343
				],
				[
					-1.2400564700928953,
					4.340197645325134
				],
				[
					1.860084705139343,
					4.960225880371581
				],
				[
					4.340197645325134,
					3.1001411752322383
				],
				[
					4.960225880371581,
					3.1001411752322383
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.03300372138619423,
				0.060393769294023514,
				0.0992949828505516,
				0.14001229405403137,
				0.16218301653862,
				0.20490311086177826,
				0.2464437186717987,
				0.2616564929485321,
				0.1717718541622162,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 2021727502,
			"isDeleted": false,
			"id": "7P_MkUfVPF1hg7eOCQ3fL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 503.9494380012087,
			"y": 96.76509814465024,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.060367055603933,
			"height": 8.680395290650267,
			"seed": 114678528,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6200282350464477,
					-0.6200282350464477
				],
				[
					-1.860084705139343,
					-1.2400564700928953
				],
				[
					-2.4801129401857906,
					-0.6200282350464477
				],
				[
					-2.4801129401857906,
					0.6200282350464477
				],
				[
					-0.6200282350464477,
					3.720169410278686
				],
				[
					0,
					6.200282350464477
				],
				[
					-1.2400564700928953,
					7.440338820557372
				],
				[
					-1.860084705139343,
					5.580254115418029
				],
				[
					0.6200282350464477,
					1.860084705139343
				],
				[
					3.7201694102787997,
					1.860084705139343
				],
				[
					4.960225880371695,
					4.960225880371581
				],
				[
					5.580254115418143,
					6.820310585510924
				],
				[
					5.580254115418143,
					6.820310585510924
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09226559102535248,
				0.142225980758667,
				0.17747780680656433,
				0.1649453192949295,
				0.19453021883964539,
				0.210948184132576,
				0.1058848574757576,
				0.07983484119176865,
				0.15513284504413605,
				0.25470250844955444,
				0.06810741871595383,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 561349330,
			"isDeleted": false,
			"id": "QGZ98VkzSa-_DNlJDkgo3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 509.52969211662685,
			"y": 91.8048722642786,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2400564700928953,
			"height": 0,
			"seed": 1541356288,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6200282350464477,
					0
				],
				[
					-1.2400564700928953,
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
				0.09165798872709274,
				0.05513140931725502,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 2092321614,
			"isDeleted": false,
			"id": "irfkUc1WpFgoDTZZx_2yw",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 513.869889761952,
			"y": 96.76509814465024,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.300423525696715,
			"height": 5.580254115418029,
			"seed": 1744239360,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.2400564700928953,
					0.6200282350464477
				],
				[
					-1.860084705139343,
					1.860084705139343
				],
				[
					-1.860084705139343,
					4.340197645325134
				],
				[
					1.860084705139343,
					4.960225880371581
				],
				[
					4.960225880371581,
					3.1001411752322383
				],
				[
					4.340197645325134,
					0
				],
				[
					0,
					-0.6200282350464477
				],
				[
					-4.340197645325134,
					3.1001411752322383
				],
				[
					-0.6200282350464477,
					4.960225880371581
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
				0.08196999877691269,
				0.10136999189853668,
				0.17995397746562958,
				0.1816633641719818,
				0.15871816873550415,
				0.19237029552459717,
				0.20770785212516785,
				0.1398102045059204,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 153180306,
			"isDeleted": false,
			"id": "4Z-sc6njooTRKaRBlHC2X",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 516.3500027021378,
			"y": 96.76509814465024,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.54047999578961,
			"height": 22.94104469671862,
			"seed": 1731140352,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6200282350464477,
					1.860084705139343
				],
				[
					1.860084705139343,
					7.440338820557372
				],
				[
					3.1001411752322383,
					14.8806776411148
				],
				[
					0.6200282350464477,
					21.080959991579277
				],
				[
					-4.340197645325134,
					22.94104469671862
				],
				[
					-7.440338820557372,
					16.120734111207696
				],
				[
					-7.440338820557372,
					15.500705876161248
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1683879941701889,
				0.20510552823543549,
				0.22338448464870453,
				0.2724584937095642,
				0.22096097469329834,
				0.008844512514770031,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 380350862,
			"isDeleted": false,
			"id": "JHXi0zw-q6z1b5EDfLKH6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 518.2100874072771,
			"y": 95.52504167455734,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.820310585510924,
			"height": 6.200282350464477,
			"seed": 1021885184,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6200282350464477
				],
				[
					1.2400564700928953,
					4.340197645325134
				],
				[
					2.4801129401857906,
					6.200282350464477
				],
				[
					3.720169410278686,
					3.1001411752322383
				],
				[
					4.960225880371581,
					0
				],
				[
					6.200282350464477,
					1.860084705139343
				],
				[
					6.200282350464477,
					6.200282350464477
				],
				[
					6.820310585510924,
					6.200282350464477
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12394800037145615,
				0.20310598611831665,
				0.19501397013664246,
				0.10110900551080704,
				0.09557086229324341,
				0.215177983045578,
				0.1831456869840622,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 1078752850,
			"isDeleted": false,
			"id": "QnDHSP_QDLwjvAzfpuTom",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 559.0930017210302,
			"y": 68.42598527216893,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.7309292502765175,
			"height": 9.93976617892693,
			"seed": 1045101312,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5522092321626815,
					0
				],
				[
					1.1044184643252493,
					0
				],
				[
					4.417673857300883,
					-1.656627696487817
				],
				[
					6.626510785951382,
					-3.8654646251382587
				],
				[
					5.522092321626019,
					-5.522092321626076
				],
				[
					3.313255392975634,
					-4.969883089463451
				],
				[
					0.5522092321626815,
					-2.761046160813038
				],
				[
					0,
					0.5522092321626246
				],
				[
					1.656627696487817,
					3.3132553929756625
				],
				[
					4.417673857300883,
					4.417673857300855
				],
				[
					7.7309292502765175,
					1.656627696487817
				],
				[
					7.7309292502765175,
					1.656627696487817
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08071517944335938,
				0.11314303427934647,
				0.18434850871562958,
				0.1698434203863144,
				0.1520148664712906,
				0.162565678358078,
				0.17868207395076752,
				0.20540539920330048,
				0.23275946080684662,
				0.2254333794116974,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 295325646,
			"isDeleted": false,
			"id": "GfiPUFQBdnJvQyclJZGg3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 566.2717217391441,
			"y": 65.66493911135589,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.0743015537887,
			"height": 4.96988308946348,
			"seed": 2078784256,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.6566276964877034,
					1.1044184643252208
				],
				[
					4.41767385730077,
					3.8654646251382587
				],
				[
					6.0743015537887,
					4.96988308946348
				],
				[
					6.0743015537887,
					4.417673857300855
				],
				[
					6.0743015537887,
					3.8654646251382587
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2103940099477768,
				0.21466653048992157,
				0.12748226523399353,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 667802642,
			"isDeleted": false,
			"id": "ercgSrnHK2OYPj6ObLGT_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 573.450441757258,
			"y": 63.45610218270548,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.626510785951268,
			"height": 7.178720018113893,
			"seed": 2079857408,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321625678,
					0
				],
				[
					-1.1044184643251356,
					0
				],
				[
					-2.7610461608130663,
					1.1044184643251924
				],
				[
					-6.0743015537887,
					4.969883089463451
				],
				[
					-6.626510785951268,
					7.178720018113893
				],
				[
					-6.626510785951268,
					7.178720018113893
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10774999856948853,
				0.21740399301052094,
				0.26900601387023926,
				0.1524200141429901,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 1771775502,
			"isDeleted": false,
			"id": "2JbJZZXC7orVcx2RPscLW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 576.7636971502336,
			"y": 63.45610218270548,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.730929250276404,
			"height": 14.357440036227814,
			"seed": 1038949120,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5522092321626246
				],
				[
					0,
					0
				],
				[
					0.5522092321625678,
					2.2088369286504133
				],
				[
					2.2088369286504985,
					8.83534771460171
				],
				[
					2.2088369286504985,
					13.80523080406519
				],
				[
					0.5522092321625678,
					13.253021571902565
				],
				[
					-1.1044184643251356,
					7.730929250276489
				],
				[
					0,
					1.656627696487817
				],
				[
					4.417673857300883,
					-0.5522092321626246
				],
				[
					6.626510785951268,
					2.2088369286504133
				],
				[
					4.417673857300883,
					6.074301553788672
				],
				[
					3.313255392975634,
					5.522092321626076
				],
				[
					3.313255392975634,
					4.969883089463451
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13765399158000946,
				0.16668599843978882,
				0.1997258961200714,
				0.19444400072097778,
				0.14807254076004028,
				0.048687346279621124,
				0.030137786641716957,
				0.091897152364254,
				0.16397900879383087,
				0.1825224608182907,
				0.01681658998131752,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1838975442,
			"isDeleted": false,
			"id": "_qjMwwXZu8HXep5YetNXn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 585.5990448648354,
			"y": 65.1127298791933,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.835347714601767,
			"height": 8.283138482439114,
			"seed": 1851685632,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5522092321626246
				],
				[
					0.5522092321625678,
					-0.5522092321626246
				],
				[
					1.656627696487817,
					-0.5522092321626246
				],
				[
					3.313255392975634,
					-1.656627696487817
				],
				[
					3.313255392975634,
					-2.761046160813038
				],
				[
					0.5522092321625678,
					-2.2088369286504417
				],
				[
					-2.2088369286504985,
					0.5522092321625962
				],
				[
					-1.656627696487817,
					3.8654646251382587
				],
				[
					1.656627696487817,
					5.522092321626076
				],
				[
					6.0743015537887,
					3.8654646251382587
				],
				[
					6.626510785951268,
					3.313255392975634
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05597299337387085,
				0.05077047646045685,
				0.14484798908233643,
				0.16598807275295258,
				0.15035653114318848,
				0.128814697265625,
				0.18644528090953827,
				0.2686469256877899,
				0.3021586835384369,
				0.09668871760368347,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 799487054,
			"isDeleted": false,
			"id": "Hum0cxGgEJH9O5hKiQ0-B",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 591.1211371864615,
			"y": 63.45610218270548,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.178720018113836,
			"height": 6.626510785951297,
			"seed": 761699072,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5522092321625678,
					0
				],
				[
					1.6566276964877034,
					2.761046160813038
				],
				[
					2.208836928650385,
					4.417673857300855
				],
				[
					3.313255392975634,
					2.761046160813038
				],
				[
					5.522092321626019,
					-0.5522092321626246
				],
				[
					7.178720018113836,
					-0.5522092321626246
				],
				[
					7.178720018113836,
					3.8654646251382303
				],
				[
					6.626510785951268,
					6.074301553788672
				],
				[
					6.626510785951268,
					5.522092321626076
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10736413300037384,
				0.17730797827243805,
				0.1841510385274887,
				0.07984308153390884,
				0.050535887479782104,
				0.13567358255386353,
				0.18196094036102295,
				0.0516541451215744,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 61,
			"versionNonce": 1758429074,
			"isDeleted": false,
			"id": "PkAv59IgBwmSv9JpwUQo-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 602.7175310618761,
			"y": 61.79947448621763,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.939766178926902,
			"height": 9.387556946764334,
			"seed": 136149760,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321625678,
					-0.5522092321625962
				],
				[
					-1.6566276964877034,
					0
				],
				[
					-2.7610461608129526,
					1.6566276964878455
				],
				[
					-1.1044184643251356,
					4.417673857300883
				],
				[
					1.104418464325363,
					6.626510785951297
				],
				[
					1.104418464325363,
					8.283138482439114
				],
				[
					-1.6566276964877034,
					8.835347714601738
				],
				[
					-2.208836928650271,
					8.283138482439114
				],
				[
					0,
					6.626510785951297
				],
				[
					3.8654646251383156,
					4.96988308946348
				],
				[
					6.0743015537887,
					6.0743015537887
				],
				[
					7.17872001811395,
					8.835347714601738
				],
				[
					7.17872001811395,
					8.283138482439114
				],
				[
					7.17872001811395,
					7.7309292502765175
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10560699552297592,
				0.16742800176143646,
				0.18515905737876892,
				0.18145138025283813,
				0.1903228461742401,
				0.24379916489124298,
				0.26810210943222046,
				0.19671911001205444,
				0.0939558744430542,
				0.08836166560649872,
				0.23655179142951965,
				0.30838248133659363,
				0.07067550718784332,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1838643854,
			"isDeleted": false,
			"id": "NjZKLzaIeK804_jCSgf80",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 609.8962510799901,
			"y": 58.486219093242,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.656627696487817,
			"height": 0,
			"seed": 1615297280,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321625678,
					0
				],
				[
					-1.1044184643252493,
					0
				],
				[
					-1.656627696487817,
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
				0.17562749981880188,
				0.08498382568359375,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 1973271890,
			"isDeleted": false,
			"id": "yxR8WgJO4CU1HJ36n7QoP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 613.2095064729658,
			"y": 63.45610218270548,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.730929250276631,
			"height": 6.626510785951297,
			"seed": 1032837888,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321626815,
					0
				],
				[
					-1.104418464325363,
					0.5522092321625962
				],
				[
					-0.5522092321626815,
					3.313255392975634
				],
				[
					1.6566276964877034,
					6.074301553788672
				],
				[
					4.9698830894633375,
					4.969883089463451
				],
				[
					6.626510785951268,
					0.5522092321625962
				],
				[
					5.522092321626019,
					-0.5522092321626246
				],
				[
					5.522092321626019,
					-0.5522092321626246
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12343798577785492,
				0.1911040097475052,
				0.23320379853248596,
				0.2379942387342453,
				0.23277521133422852,
				0.060138121247291565,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 170195150,
			"isDeleted": false,
			"id": "mgPq_3hJPmJRnM7Um33fP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 622.0448541875675,
			"y": 64.00831141486807,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.835347714601767,
			"height": 7.178720018113893,
			"seed": 780802816,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5522092321626815,
					0
				],
				[
					1.656627696487817,
					0
				],
				[
					2.208836928650385,
					-1.1044184643252208
				],
				[
					0.5522092321626815,
					-1.656627696487817
				],
				[
					-2.7610461608130663,
					1.1044184643252208
				],
				[
					-1.1044184643252493,
					4.96988308946348
				],
				[
					5.522092321626019,
					5.522092321626076
				],
				[
					6.0743015537887,
					5.522092321626076
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10417807102203369,
				0.20137600600719452,
				0.2331319898366928,
				0.21633441746234894,
				0.25802257657051086,
				0.37702998518943787,
				0.1522119790315628,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1365132050,
			"isDeleted": false,
			"id": "RgwbzEsN5hA9bDFPNoF8_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 562.4062571140058,
			"y": 87.20109916569757,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.969883089463451,
			"height": 10.491975411089584,
			"seed": 397695744,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321625678,
					0
				],
				[
					-1.656627696487817,
					0
				],
				[
					-2.7610461608129526,
					0
				],
				[
					-3.313255392975634,
					1.1044184643252493
				],
				[
					-3.313255392975634,
					3.313255392975691
				],
				[
					0,
					7.178720018113893
				],
				[
					1.656627696487817,
					9.387556946764334
				],
				[
					-0.5522092321625678,
					10.491975411089584
				],
				[
					-3.313255392975634,
					10.491975411089584
				],
				[
					-1.656627696487817,
					7.7309292502765175
				],
				[
					-1.1044184643252493,
					7.178720018113893
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1096596047282219,
				0.1386929601430893,
				0.1623583436012268,
				0.17888903617858887,
				0.17925991117954254,
				0.19704248011112213,
				0.23838186264038086,
				0.22532138228416443,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 753446670,
			"isDeleted": false,
			"id": "6ElywxNzQNnf7uk4H6Sj-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 565.7195125069816,
			"y": 81.67900684407152,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.17872001811395,
			"height": 15.461858500553006,
			"seed": 892369664,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321626815,
					0
				],
				[
					0,
					1.1044184643252208
				],
				[
					1.1044184643251356,
					4.969883089463451
				],
				[
					1.1044184643251356,
					11.044184643252123
				],
				[
					1.1044184643251356,
					14.909649268390382
				],
				[
					1.1044184643251356,
					15.461858500553006
				],
				[
					1.1044184643251356,
					13.253021571902565
				],
				[
					2.208836928650271,
					9.93976617892693
				],
				[
					4.9698830894633375,
					8.283138482439114
				],
				[
					6.626510785951268,
					9.387556946764306
				],
				[
					6.626510785951268,
					12.70081233973994
				],
				[
					6.074301553788587,
					13.80523080406519
				],
				[
					6.074301553788587,
					13.80523080406519
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08028280735015869,
				0.17476357519626617,
				0.22379454970359802,
				0.26462996006011963,
				0.2644118666648865,
				0.2343214750289917,
				0.17548660933971405,
				0.15484842658042908,
				0.1699257493019104,
				0.21955901384353638,
				0.26919928193092346,
				0.03774520754814148,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 1988628690,
			"isDeleted": false,
			"id": "ckSt2IlHfKIW1tTxbR5AJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 576.211487918071,
			"y": 90.51435455867326,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.417673857300997,
			"height": 5.522092321626076,
			"seed": 1741544192,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321625678,
					0.5522092321625678
				],
				[
					-1.1044184643252493,
					1.1044184643251924
				],
				[
					-1.656627696487817,
					2.208836928650385
				],
				[
					-1.1044184643252493,
					4.4176738573008265
				],
				[
					0.5522092321625678,
					4.969883089463451
				],
				[
					2.2088369286504985,
					3.313255392975634
				],
				[
					2.2088369286504985,
					0.5522092321625678
				],
				[
					0,
					-0.5522092321626246
				],
				[
					-2.2088369286504985,
					1.1044184643251924
				],
				[
					-2.2088369286504985,
					3.313255392975634
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
				0.10061999410390854,
				0.14664998650550842,
				0.1858321875333786,
				0.17949597537517548,
				0.1825440675020218,
				0.1935131549835205,
				0.19127096235752106,
				0.1481572538614273,
				0.010528595186769962,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 576429390,
			"isDeleted": false,
			"id": "bjz_pAXXQqMMKDGXjErLn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 578.4203248467215,
			"y": 89.40993609434801,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.522092321626019,
			"height": 7.7309292502765175,
			"seed": 1826790144,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5522092321625678,
					2.2088369286504417
				],
				[
					1.6566276964877034,
					6.0743015537887
				],
				[
					2.208836928650271,
					6.626510785951325
				],
				[
					2.7610461608129526,
					2.7610461608130663
				],
				[
					4.9698830894633375,
					-1.1044184643251924
				],
				[
					5.522092321626019,
					-1.1044184643251924
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1491278111934662,
				0.18550188839435577,
				0.16426968574523926,
				0.12460681051015854,
				0.0209122933447361,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 2024941202,
			"isDeleted": false,
			"id": "1g2QHL8554-XYXH-OZg5Y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 590.0167187221361,
			"y": 81.67900684407152,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.5522092321626815,
			"height": 13.80523080406519,
			"seed": 1012374272,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5522092321625962
				],
				[
					0,
					1.656627696487817
				],
				[
					0,
					6.626510785951297
				],
				[
					0.5522092321626815,
					12.148603107577372
				],
				[
					0.5522092321626815,
					13.80523080406519
				],
				[
					0,
					13.253021571902565
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07465799152851105,
				0.07465799152851105,
				0.2217269241809845,
				0.2220565527677536,
				0.0484745167195797,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1071039374,
			"isDeleted": false,
			"id": "mwV7uxY0_wjYZ84OH8UEJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 586.151254096998,
			"y": 88.85772686218539,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.7309292502765175,
			"height": 0.5522092321625678,
			"seed": 114072320,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5522092321625678,
					-0.5522092321625678
				],
				[
					1.6566276964879307,
					-0.5522092321625678
				],
				[
					7.17872001811395,
					0
				],
				[
					7.7309292502765175,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10412698239088058,
				0.17329998314380646,
				0.1464480310678482,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1620280402,
			"isDeleted": false,
			"id": "VBXwEhSG9SdHuoGixdugS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 609.3440418478275,
			"y": 86.64888993353497,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.626510785951268,
			"height": 8.283138482439085,
			"seed": 1810520832,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321626815,
					-0.5522092321625962
				],
				[
					-2.208836928650385,
					0
				],
				[
					-3.313255392975634,
					0.5522092321625962
				],
				[
					-4.969883089463451,
					3.3132553929756625
				],
				[
					-4.969883089463451,
					6.074301553788672
				],
				[
					-2.208836928650385,
					7.730929250276489
				],
				[
					1.1044184643252493,
					6.626510785951297
				],
				[
					1.656627696487817,
					6.626510785951297
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10591857880353928,
				0.1968458890914917,
				0.21137619018554688,
				0.22399459779262543,
				0.23674243688583374,
				0.23228338360786438,
				0.06051937863230705,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1200824782,
			"isDeleted": false,
			"id": "M9NzzRFSvRjD75JbfGHRB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 614.8661341694535,
			"y": 87.20109916569757,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.522092321626019,
			"height": 7.178720018113893,
			"seed": 633641728,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321625678,
					0
				],
				[
					-1.6566276964877034,
					1.656627696487817
				],
				[
					-1.6566276964877034,
					4.417673857300883
				],
				[
					0.5522092321625678,
					5.522092321626076
				],
				[
					2.7610461608130663,
					5.522092321626076
				],
				[
					3.8654646251383156,
					2.2088369286504417
				],
				[
					2.7610461608130663,
					-1.1044184643251924
				],
				[
					-0.5522092321625678,
					-1.656627696487817
				],
				[
					-1.6566276964877034,
					2.2088369286504417
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
				0.14017577469348907,
				0.21333499252796173,
				0.20425216853618622,
				0.1707330346107483,
				0.1469283401966095,
				0.13851302862167358,
				0.14448794722557068,
				0.03318426385521889,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 134425106,
			"isDeleted": false,
			"id": "zU_xb0v14ppR6om-f0qLy",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 618.1793895624292,
			"y": 86.64888993353497,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.283138482439199,
			"height": 6.626510785951268,
			"seed": 349747968,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5522092321625962
				],
				[
					0.5522092321626815,
					0.5522092321625962
				],
				[
					2.2088369286504985,
					3.865464625138287
				],
				[
					2.7610461608130663,
					4.96988308946348
				],
				[
					2.7610461608130663,
					2.761046160813038
				],
				[
					3.313255392975634,
					0
				],
				[
					3.8654646251383156,
					1.1044184643252208
				],
				[
					4.969883089463565,
					3.3132553929756625
				],
				[
					5.522092321626133,
					3.3132553929756625
				],
				[
					6.626510785951268,
					0
				],
				[
					8.283138482439199,
					-0.5522092321625962
				],
				[
					8.283138482439199,
					3.3132553929756625
				],
				[
					7.730929250276631,
					6.074301553788672
				],
				[
					7.730929250276631,
					6.074301553788672
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.030024506151676178,
				0.1573435664176941,
				0.1985449194908142,
				0.17493240535259247,
				0.06716296076774597,
				0.06606002897024155,
				0.14363592863082886,
				0.1634964942932129,
				0.10771096497774124,
				0.07327447831630707,
				0.11966220289468765,
				0.19810424745082855,
				0.04211892560124397,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1286191118,
			"isDeleted": false,
			"id": "XHa1Cmq9QkkOH47IVedVC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 629.2235742056814,
			"y": 87.20109916569757,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 0.5522092321626246,
			"seed": 1854061312,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5522092321626246
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
			"version": 60,
			"versionNonce": 1979193298,
			"isDeleted": false,
			"id": "ucIoxWqThPndAzwBb3Ufr",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 628.1191557413562,
			"y": 86.64888993353497,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.283138482439085,
			"height": 7.178720018113893,
			"seed": 1033411328,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5522092321625962
				],
				[
					0,
					0
				],
				[
					1.656627696487817,
					3.3132553929756625
				],
				[
					2.208836928650385,
					5.522092321626104
				],
				[
					2.208836928650385,
					3.865464625138287
				],
				[
					2.7610461608129526,
					0.5522092321625962
				],
				[
					3.865464625138202,
					0
				],
				[
					4.969883089463451,
					3.3132553929756625
				],
				[
					5.522092321626019,
					4.96988308946348
				],
				[
					6.074301553788587,
					2.2088369286504133
				],
				[
					7.17872001811395,
					0
				],
				[
					7.7309292502765175,
					1.6566276964878455
				],
				[
					7.7309292502765175,
					6.626510785951297
				],
				[
					8.283138482439085,
					6.626510785951297
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12436026334762573,
				0.17782825231552124,
				0.1889345943927765,
				0.13967359066009521,
				0.10027307271957397,
				0.14787673950195312,
				0.21129891276359558,
				0.21358059346675873,
				0.10034798830747604,
				0.09237063676118851,
				0.17673955857753754,
				0.04677655175328255,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 387155534,
			"isDeleted": false,
			"id": "GhT7iAaYtbQ5Yko54R_GC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 638.0589219202831,
			"y": 87.20109916569757,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.969883089463565,
			"height": 6.0743015537887,
			"seed": 729979648,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321626815,
					1.656627696487817
				],
				[
					0,
					3.8654646251382587
				],
				[
					2.7610461608130663,
					4.417673857300883
				],
				[
					4.417673857300883,
					1.656627696487817
				],
				[
					3.313255392975634,
					-1.656627696487817
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
				0.12954400479793549,
				0.1934790015220642,
				0.1889510452747345,
				0.1371999830007553,
				0.010634185746312141,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 982076818,
			"isDeleted": false,
			"id": "_kQmRMd9n5doN7NH1wFYs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 643.5810142419091,
			"y": 86.64888993353497,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.0743015537887,
			"height": 5.522092321626076,
			"seed": 1867266816,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5522092321625962
				],
				[
					0.5522092321626815,
					3.3132553929756625
				],
				[
					1.6566276964879307,
					4.96988308946348
				],
				[
					2.7610461608130663,
					2.2088369286504133
				],
				[
					3.8654646251383156,
					-0.5522092321625962
				],
				[
					4.417673857300997,
					1.1044184643252208
				],
				[
					4.969883089463565,
					4.96988308946348
				],
				[
					5.522092321626133,
					3.865464625138287
				],
				[
					6.0743015537887,
					3.3132553929756625
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11082598567008972,
				0.17351998388767242,
				0.1448156088590622,
				0.08377960324287415,
				0.09609765559434891,
				0.18279889225959778,
				0.21548382937908173,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 128552078,
			"isDeleted": false,
			"id": "yea9a1BGb1v3jPBzP8xVA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 650.759734260023,
			"y": 87.7533083978602,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.656627696487817,
			"height": 4.969883089463451,
			"seed": 952572672,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5522092321626246
				],
				[
					0.5522092321626815,
					1.656627696487817
				],
				[
					1.1044184643252493,
					4.969883089463451
				],
				[
					1.656627696487817,
					4.969883089463451
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11052200198173523,
				0.149959996342659,
				0.09299059957265854,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1257098066,
			"isDeleted": false,
			"id": "FE6D2LGFEi5R7tO5Xp2Gb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 652.4163619565109,
			"y": 82.78342530839674,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1044184643251356,
			"height": 0.5522092321626246,
			"seed": 762764032,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321625678,
					-0.5522092321626246
				],
				[
					-1.1044184643251356,
					-0.5522092321626246
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
				0.09528298676013947,
				0.05212542787194252,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 61,
			"versionNonce": 2082785998,
			"isDeleted": false,
			"id": "i7HBZdJuSseAtZqF_1yS9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 657.3862450459744,
			"y": 87.20109916569757,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.939766178927016,
			"height": 6.626510785951268,
			"seed": 1263966976,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321626815,
					0
				],
				[
					-2.2088369286504985,
					0.5522092321626246
				],
				[
					-3.313255392975748,
					1.656627696487817
				],
				[
					-3.313255392975748,
					3.313255392975691
				],
				[
					-2.2088369286504985,
					5.522092321626076
				],
				[
					1.1044184643251356,
					5.522092321626076
				],
				[
					2.208836928650271,
					4.417673857300883
				],
				[
					2.7610461608129526,
					4.969883089463508
				],
				[
					3.865464625138202,
					5.522092321626076
				],
				[
					6.074301553788587,
					5.522092321626076
				],
				[
					6.626510785951268,
					3.313255392975691
				],
				[
					6.074301553788587,
					0.5522092321626246
				],
				[
					3.313255392975634,
					-1.1044184643251924
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
				0.12287799268960953,
				0.1621820032596588,
				0.16666638851165771,
				0.16599252820014954,
				0.09429769963026047,
				0.05999874696135521,
				0.10459069907665253,
				0.14018838107585907,
				0.14649060368537903,
				0.16124175488948822,
				0.186085045337677,
				0.04478808492422104,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1568444690,
			"isDeleted": false,
			"id": "o0Azih42rHmX_VZ63Rvix",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 663.460546599763,
			"y": 89.96214532651064,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.0743015537887,
			"height": 1.1044184643252493,
			"seed": 1618295552,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5522092321626815,
					0
				],
				[
					1.656627696487817,
					0
				],
				[
					5.522092321626019,
					-0.5522092321626246
				],
				[
					6.0743015537887,
					-1.1044184643252493
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06530798226594925,
				0.0292435921728611,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 857620750,
			"isDeleted": false,
			"id": "5QNWUklLy3YLw-9Vv1-iZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 671.1914758500395,
			"y": 77.26133298677067,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1044184643251356,
			"height": 14.90964926839041,
			"seed": 67959552,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321625678,
					0.5522092321625962
				],
				[
					-0.5522092321625678,
					1.1044184643251924
				],
				[
					-0.5522092321625678,
					3.313255392975634
				],
				[
					0,
					9.939766178926902
				],
				[
					0.5522092321625678,
					14.357440036227786
				],
				[
					0.5522092321625678,
					14.90964926839041
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08930398523807526,
				0.11330398917198181,
				0.13617001473903656,
				0.15693344175815582,
				0.08000274747610092,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1168940754,
			"isDeleted": false,
			"id": "9yEV0iHfvJb94w8ns4ca1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 667.3260112249013,
			"y": 86.64888993353497,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.9698830894633375,
			"height": 0.5522092321625962,
			"seed": 992082688,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5522092321625678,
					0
				],
				[
					1.1044184643251356,
					0
				],
				[
					4.41767385730077,
					0
				],
				[
					4.9698830894633375,
					0.5522092321625962
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13250958919525146,
				0.09553772211074829,
				0.03008987382054329,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 806285134,
			"isDeleted": false,
			"id": "fa65mD3055oq-vY-90IjF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 677.2657774038282,
			"y": 87.7533083978602,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.5522092321625678,
			"height": 3.8654646251382587,
			"seed": 640269056,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.1044184643251924
				],
				[
					-0.5522092321625678,
					2.2088369286504417
				],
				[
					-0.5522092321625678,
					3.8654646251382587
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
				0.13659600913524628,
				0.053410645574331284,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1343550610,
			"isDeleted": false,
			"id": "yOB3FKgMGl6KbBqV2qU90",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 678.3701958681534,
			"y": 82.23121607623412,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1044184643251356,
			"height": 0,
			"seed": 611982080,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321625678,
					0
				],
				[
					-1.1044184643251356,
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
				0.11118597537279129,
				0.012842376716434956,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 525325710,
			"isDeleted": false,
			"id": "NapZn_LRiGqu1YcXwNs1E",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 680.5790327968039,
			"y": 86.64888993353497,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.626510785951268,
			"height": 7.178720018113893,
			"seed": 1995037440,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321625678,
					1.1044184643252208
				],
				[
					-0.5522092321625678,
					3.3132553929756625
				],
				[
					0,
					4.417673857300855
				],
				[
					2.7610461608130663,
					4.96988308946348
				],
				[
					4.969883089463451,
					2.761046160813038
				],
				[
					4.969883089463451,
					-0.5522092321625962
				],
				[
					2.2088369286504985,
					-2.2088369286504133
				],
				[
					-1.656627696487817,
					1.6566276964878455
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
				0.11890597641468048,
				0.1632779836654663,
				0.15245874226093292,
				0.12984423339366913,
				0.13858215510845184,
				0.15923961997032166,
				0.01565448008477688,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 510431826,
			"isDeleted": false,
			"id": "OVqc_oi2L9ibPsp2PuabI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 684.4444974219421,
			"y": 86.64888993353497,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.17872001811395,
			"height": 7.7309292502765175,
			"seed": 56187648,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5522092321625962
				],
				[
					1.1044184643252493,
					2.2088369286504133
				],
				[
					2.2088369286504985,
					3.865464625138287
				],
				[
					3.313255392975634,
					0.5522092321625962
				],
				[
					5.522092321626133,
					-2.2088369286504133
				],
				[
					6.626510785951268,
					0.5522092321625962
				],
				[
					7.17872001811395,
					5.522092321626104
				],
				[
					7.17872001811395,
					5.522092321626104
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06892798095941544,
				0.1603291630744934,
				0.13335391879081726,
				0.05845217779278755,
				0.06499606370925903,
				0.1726762354373932,
				0.1862299144268036,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 974779342,
			"isDeleted": false,
			"id": "brOPCkuRsSjdwey69JAxb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 563.5106755783311,
			"y": 112.05051461301494,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.0743015537887,
			"height": 9.939766178926902,
			"seed": 242457344,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321625678,
					0
				],
				[
					-2.2088369286504985,
					0
				],
				[
					-3.313255392975634,
					0.5522092321626246
				],
				[
					-3.865464625138202,
					2.2088369286504417
				],
				[
					-1.656627696487817,
					4.4176738573008265
				],
				[
					0.5522092321625678,
					6.074301553788644
				],
				[
					1.1044184643251356,
					8.283138482439085
				],
				[
					-1.656627696487817,
					9.387556946764334
				],
				[
					-4.969883089463565,
					9.939766178926902
				],
				[
					-4.417673857300883,
					8.283138482439085
				],
				[
					-3.865464625138202,
					8.283138482439085
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09396731853485107,
				0.11004647612571716,
				0.12518584728240967,
				0.11235867440700531,
				0.09576251357793808,
				0.12426108121871948,
				0.15997757017612457,
				0.14568307995796204,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 59406354,
			"isDeleted": false,
			"id": "sI3RiGhqlu1v7kb__NfMr",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 565.1673032748189,
			"y": 112.60272384517756,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.491975411089584,
			"height": 9.939766178926902,
			"seed": 824687360,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5522092321626815,
					0
				],
				[
					2.208836928650385,
					4.969883089463451
				],
				[
					3.313255392975634,
					8.283138482439085
				],
				[
					3.313255392975634,
					7.178720018113893
				],
				[
					3.313255392975634,
					2.7610461608130095
				],
				[
					3.8654646251383156,
					0.5522092321625678
				],
				[
					5.522092321626019,
					3.313255392975634
				],
				[
					6.0743015537887,
					6.626510785951268
				],
				[
					6.626510785951268,
					6.626510785951268
				],
				[
					7.7309292502765175,
					2.208836928650385
				],
				[
					9.939766178926902,
					1.1044184643251924
				],
				[
					10.491975411089584,
					4.969883089463451
				],
				[
					10.491975411089584,
					9.939766178926902
				],
				[
					10.491975411089584,
					9.387556946764278
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0767015665769577,
				0.11381194740533829,
				0.12055788934230804,
				0.06492803990840912,
				0.018360596150159836,
				0.02598138339817524,
				0.07879296690225601,
				0.11392102390527725,
				0.07703360170125961,
				0.021030243486166,
				0.06321334838867188,
				0.1394629180431366,
				0.02382919378578663,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 713443854,
			"isDeleted": false,
			"id": "i5pzImAX7sCTKampJH_-r",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 578.4203248467215,
			"y": 116.46818847031577,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.626510785951268,
			"height": 7.7309292502765175,
			"seed": 215071488,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5522092321626246
				],
				[
					-0.5522092321626815,
					2.7610461608130663
				],
				[
					2.208836928650271,
					4.417673857300883
				],
				[
					5.522092321626019,
					3.313255392975691
				],
				[
					6.074301553788587,
					-0.5522092321625678
				],
				[
					2.7610461608129526,
					-3.313255392975634
				],
				[
					-0.5522092321626815,
					-1.656627696487817
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
				0.10239797830581665,
				0.10987686365842819,
				0.09365569800138474,
				0.10619775205850601,
				0.1185801699757576,
				0.014143310487270355,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1600497106,
			"isDeleted": false,
			"id": "OZLfQgkjky3H9g2d4DQ5l",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 582.2857894718597,
			"y": 118.12481616680358,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.313255392975634,
			"height": 0.5522092321626246,
			"seed": 79469312,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5522092321625678,
					0
				],
				[
					1.1044184643251356,
					0.5522092321626246
				],
				[
					3.313255392975634,
					0.5522092321626246
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
				0.01596160978078842,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1871566926,
			"isDeleted": false,
			"id": "08TvFTUXWtIkC0lv0nZer",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 587.8078817934859,
			"y": 105.97621305922624,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.208836928650385,
			"height": 14.357440036227786,
			"seed": 252246784,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321626815,
					0
				],
				[
					-0.5522092321626815,
					1.656627696487817
				],
				[
					-0.5522092321626815,
					8.83534771460171
				],
				[
					1.1044184643251356,
					14.357440036227786
				],
				[
					1.6566276964877034,
					13.805230804065218
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.15901800990104675,
				0.019203796982765198,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 2064980882,
			"isDeleted": false,
			"id": "HXUlpaicv7-4DuDpzj_-A",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 591.1211371864615,
			"y": 104.87179459490105,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1044184643251356,
			"height": 16.566276964878227,
			"seed": 1560369920,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.1044184643251924
				],
				[
					0,
					3.8654646251382587
				],
				[
					0.5522092321625678,
					11.59639387541472
				],
				[
					1.1044184643251356,
					16.566276964878227
				],
				[
					1.1044184643251356,
					16.566276964878227
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07472799718379974,
				0.16911999881267548,
				0.09968005120754242,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 66,
			"versionNonce": 1091149454,
			"isDeleted": false,
			"id": "KHQ58zlo-QfzGQJfK-3z-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 609.3440418478275,
			"y": 104.87179459490105,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.805230804065104,
			"height": 16.014067732715603,
			"seed": 136690432,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5522092321625678
				],
				[
					0,
					2.7610461608130095
				],
				[
					1.1044184643252493,
					11.044184643252152
				],
				[
					1.1044184643252493,
					11.59639387541472
				],
				[
					-0.5522092321626815,
					9.939766178926902
				],
				[
					-3.8654646251383156,
					8.83534771460171
				],
				[
					-7.17872001811395,
					11.044184643252152
				],
				[
					-7.7309292502765175,
					14.90964926839041
				],
				[
					-4.417673857300883,
					16.014067732715603
				],
				[
					-0.5522092321626815,
					13.805230804065161
				],
				[
					1.1044184643252493,
					13.253021571902536
				],
				[
					1.656627696487817,
					15.461858500552978
				],
				[
					3.313255392975634,
					16.014067732715603
				],
				[
					4.969883089463451,
					14.90964926839041
				],
				[
					6.074301553788587,
					12.148603107577344
				],
				[
					4.969883089463451,
					9.939766178926902
				],
				[
					3.313255392975634,
					7.7309292502765175
				],
				[
					1.656627696487817,
					7.7309292502765175
				],
				[
					1.656627696487817,
					9.387556946764334
				],
				[
					1.656627696487817,
					9.387556946764334
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12236599624156952,
				0.12202444672584534,
				0.20333069562911987,
				0.18765683472156525,
				0.10754052549600601,
				0.07151641696691513,
				0.10111309587955475,
				0.12649203836917877,
				0.11357394605875015,
				0.061769288033246994,
				0.06385689973831177,
				0.1410365253686905,
				0.15806879103183746,
				0.15222933888435364,
				0.16675610840320587,
				0.17631997168064117,
				0.1803174763917923,
				0.11429034173488617,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1691343186,
			"isDeleted": false,
			"id": "CET9T8eh6bE_Qx0eOMAd7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 616.5227618659414,
			"y": 115.9159792381532,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.41767385730077,
			"height": 2.208836928650385,
			"seed": 629635840,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.1044184643251924
				],
				[
					0.5522092321625678,
					1.656627696487817
				],
				[
					1.1044184643251356,
					2.208836928650385
				],
				[
					3.865464625138202,
					1.656627696487817
				],
				[
					4.41767385730077,
					1.1044184643251924
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09809572994709015,
				0.10656710714101791,
				0.012275390326976776,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1941085390,
			"isDeleted": false,
			"id": "6K57hUzkkbyZjETm5TgRZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 624.8059003483804,
			"y": 102.11074843408798,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1044184643252493,
			"height": 14.90964926839041,
			"seed": 1792006912,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321625678,
					4.417673857300883
				],
				[
					0,
					12.1486031075774
				],
				[
					0.5522092321626815,
					14.90964926839041
				],
				[
					0,
					14.357440036227786
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17314797639846802,
				0.21586401760578156,
				0.016163207590579987,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1273814802,
			"isDeleted": false,
			"id": "qZRji2L5xfXdnNUaMYKDh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 619.2838080267544,
			"y": 110.94609614868969,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.17872001811395,
			"height": 0.5522092321626246,
			"seed": 1911528192,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.656627696487817,
					0
				],
				[
					6.0743015537887,
					0
				],
				[
					7.17872001811395,
					0.5522092321626246
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11098437756299973,
				0.030381347984075546,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 1562497806,
			"isDeleted": false,
			"id": "Rjah6A5p_NdpSyVMBLLwR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 628.1191557413562,
			"y": 114.81156077382795,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.730929250276631,
			"height": 7.7309292502765175,
			"seed": 567196416,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5522092321626815,
					0.5522092321626246
				],
				[
					0,
					3.313255392975634
				],
				[
					3.313255392975634,
					3.8654646251382587
				],
				[
					6.074301553788587,
					1.656627696487817
				],
				[
					7.17872001811395,
					-1.656627696487817
				],
				[
					5.522092321626019,
					-3.8654646251382587
				],
				[
					1.656627696487817,
					-2.7610461608130095
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
				0.08722647279500961,
				0.1001572534441948,
				0.1111837774515152,
				0.13468898832798004,
				0.17581787705421448,
				0.033252228051424026,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1558392018,
			"isDeleted": false,
			"id": "2EkhUDljUt-AitM7T6utN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 634.1934572951448,
			"y": 115.36377000599057,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.522092321626133,
			"height": 1.1044184643251924,
			"seed": 1373215488,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.104418464325363,
					0.5522092321626246
				],
				[
					2.2088369286504985,
					1.1044184643251924
				],
				[
					4.969883089463565,
					1.1044184643251924
				],
				[
					5.522092321626133,
					1.1044184643251924
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1394379884004593,
				0.14661873877048492,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 68,
			"versionNonce": 936395086,
			"isDeleted": false,
			"id": "-_OhW4NyxPsfGGySmCyUv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 552.4664909350789,
			"y": 61.79947448621763,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.044184643252265,
			"height": 63.50406169869984,
			"seed": 1990810368,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.656627696487817,
					-1.1044184643251924
				],
				[
					-2.7610461608130663,
					-1.1044184643251924
				],
				[
					-5.522092321626019,
					2.2088369286504417
				],
				[
					-6.0743015537887,
					6.626510785951297
				],
				[
					-5.522092321626019,
					11.044184643252152
				],
				[
					-4.417673857300883,
					16.566276964878227
				],
				[
					-4.969883089463451,
					25.953833911642562
				],
				[
					-4.969883089463451,
					26.506043143805186
				],
				[
					-5.522092321626019,
					27.058252375967754
				],
				[
					-6.626510785951382,
					28.162670840293003
				],
				[
					-7.17872001811395,
					28.714880072455628
				],
				[
					-6.626510785951382,
					29.81929853678082
				],
				[
					-4.969883089463451,
					31.475926233268638
				],
				[
					-3.8654646251383156,
					34.236972394081704
				],
				[
					-3.8654646251383156,
					36.99801855489471
				],
				[
					-4.969883089463451,
					41.4156924121956
				],
				[
					-5.522092321626019,
					46.38557550165905
				],
				[
					-5.522092321626019,
					51.907667823285124
				],
				[
					-4.417673857300883,
					56.877550912748575
				],
				[
					-1.656627696487817,
					59.63859707356164
				],
				[
					3.313255392975634,
					61.847434002212026
				],
				[
					3.8654646251383156,
					62.39964323437465
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09016726911067963,
				0.13518136739730835,
				0.19101367890834808,
				0.2168692648410797,
				0.24018889665603638,
				0.26603934168815613,
				0.2565157115459442,
				0.24106082320213318,
				0.24096199870109558,
				0.25509878993034363,
				0.2655215263366699,
				0.26692113280296326,
				0.28920331597328186,
				0.3366797864437103,
				0.38121214509010315,
				0.4075571596622467,
				0.41612550616264343,
				0.44018903374671936,
				0.4459052085876465,
				0.44959259033203125,
				0.2290928065776825,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 61,
			"versionNonce": 491373202,
			"isDeleted": false,
			"id": "53cDhTco14BGDyeOOn-wY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 320.59955100343905,
			"y": 112.89484093608192,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 36.050798119498495,
			"height": 100.48201177987886,
			"seed": 1304976128,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7670382578617136,
					0
				],
				[
					-0.7670382578617136,
					0.7670382578617136
				],
				[
					-0.7670382578617136,
					6.903344320755082
				],
				[
					-1.5340765157234273,
					19.942994704403475
				],
				[
					-1.5340765157234273,
					34.51672160377518
				],
				[
					0.7670382578616,
					49.8574867610086
				],
				[
					5.3692678050316545,
					64.43121366038031
				],
				[
					11.505573867925023,
					78.23790230189041
				],
				[
					17.64187993081839,
					86.67532313836875
				],
				[
					24.54522425157336,
					93.57866745912384
				],
				[
					29.914492056605127,
					98.18089700629383
				],
				[
					32.982645088051754,
					100.48201177987886
				],
				[
					34.51672160377507,
					100.48201177987886
				],
				[
					34.51672160377507,
					98.94793526415549
				],
				[
					34.51672160377507,
					98.94793526415549
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07886703312397003,
				0.13837170600891113,
				0.20231136679649353,
				0.2730781137943268,
				0.35395798087120056,
				0.41115403175354004,
				0.4284511208534241,
				0.43465790152549744,
				0.45587870478630066,
				0.4818563461303711,
				0.4971855580806732,
				0.5253294110298157,
				0.5063924789428711,
				0.1299680769443512,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 118941582,
			"isDeleted": false,
			"id": "UIGBnIoNlCpJuw9c2fr2W",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 363.5536934436925,
			"y": 202.63831710589736,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.738535610063423,
			"height": 13.039650383648393,
			"seed": 590281472,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7670382578616,
					0
				],
				[
					0.7670382578617136,
					2.3011147735850273
				],
				[
					5.369267805031768,
					6.903344320755025
				],
				[
					8.437420836478395,
					10.738535610063423
				],
				[
					8.437420836478395,
					11.50557386792508
				],
				[
					4.6022295471700545,
					11.50557386792508
				],
				[
					0.7670382578617136,
					12.272612125786736
				],
				[
					-2.3011147735850273,
					13.039650383648393
				],
				[
					-1.5340765157233136,
					13.039650383648393
				],
				[
					-1.5340765157233136,
					13.039650383648393
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11858200281858444,
				0.29666998982429504,
				0.306168794631958,
				0.2935139238834381,
				0.3182709217071533,
				0.36654841899871826,
				0.39837637543678284,
				0.3672823905944824,
				0.10749953985214233,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 1205313618,
			"isDeleted": false,
			"id": "S8F1534U78WTk1TFRQMgA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 386.56484117954267,
			"y": 199.57016407445067,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.272612125786736,
			"height": 19.17595644654176,
			"seed": 1961786112,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7670382578617136,
					0
				],
				[
					-2.3011147735850273,
					0.7670382578617136
				],
				[
					-3.835191289308341,
					0.7670382578617136
				],
				[
					-4.6022295471700545,
					1.5340765157233704
				],
				[
					-6.136306062893368,
					3.068153031446684
				],
				[
					-3.068153031446741,
					6.903344320755082
				],
				[
					0.7670382578616,
					11.50557386792508
				],
				[
					1.5340765157233136,
					14.573726899371763
				],
				[
					-2.3011147735850273,
					17.641879930818448
				],
				[
					-8.437420836478395,
					19.17595644654176
				],
				[
					-10.738535610063423,
					19.17595644654176
				],
				[
					-9.971497352201709,
					16.107803415095077
				],
				[
					-9.204459094340109,
					15.34076515723342
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.060312990099191666,
				0.0950009748339653,
				0.12918061017990112,
				0.15034537017345428,
				0.1863367259502411,
				0.2092965990304947,
				0.21750515699386597,
				0.24065393209457397,
				0.27110517024993896,
				0.258433997631073,
				0.2158093899488449,
				0.023711638525128365,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 2066662862,
			"isDeleted": false,
			"id": "UMDozWecypgDlFPkfOh3J",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 383.4966881480959,
			"y": 191.899781495834,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.068153031446627,
			"height": 33.74968334591347,
			"seed": 189520640,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7670382578616568
				],
				[
					-0.7670382578616,
					3.068153031446684
				],
				[
					-0.7670382578616,
					6.903344320755025
				],
				[
					-0.7670382578616,
					13.039650383648393
				],
				[
					-2.3011147735849136,
					28.380415540881813
				],
				[
					-3.068153031446627,
					33.74968334591347
				],
				[
					-2.3011147735849136,
					28.380415540881813
				],
				[
					-1.5340765157233136,
					27.613377283020156
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14388799667358398,
				0.20500998198986053,
				0.23272399604320526,
				0.2741454541683197,
				0.2179521769285202,
				0.04158996418118477,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 677627410,
			"isDeleted": false,
			"id": "5nOC-DRAxqf6BiDgh6uYE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 387.33187943740427,
			"y": 195.73497278514233,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.5340765157233136,
			"height": 27.613377283020156,
			"seed": 1095113472,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7670382578616568
				],
				[
					-0.7670382578616,
					1.5340765157233704
				],
				[
					-0.7670382578616,
					3.835191289308341
				],
				[
					-0.7670382578616,
					14.573726899371763
				],
				[
					-1.5340765157233136,
					26.8463390251585
				],
				[
					-0.7670382578616,
					27.613377283020156
				],
				[
					-0.7670382578616,
					26.8463390251585
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.15151748061180115,
				0.2614299952983856,
				0.3061319887638092,
				0.1687869280576706,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 61,
			"versionNonce": 1429265422,
			"isDeleted": false,
			"id": "iHYYRJSlL7G3ofROp9X0y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 394.2025696622781,
			"y": 213.14168245734845,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.52407388128961,
			"height": 10.71458311645074,
			"seed": 1428142848,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5952546175806219,
					0
				],
				[
					1.190509235161187,
					0
				],
				[
					2.976273087902996,
					-0.5952546175805651
				],
				[
					4.166782323064183,
					-2.381018470322374
				],
				[
					4.166782323064183,
					-4.166782323064183
				],
				[
					1.785763852741809,
					-5.35729155822537
				],
				[
					-0.5952546175805651,
					-4.762036940644748
				],
				[
					-1.785763852741809,
					-2.976273087902996
				],
				[
					-1.785763852741809,
					0
				],
				[
					0,
					2.976273087902996
				],
				[
					2.381018470322374,
					4.762036940644805
				],
				[
					4.762036940644805,
					5.35729155822537
				],
				[
					6.547800793386614,
					5.35729155822537
				],
				[
					7.143055410967179,
					4.762036940644805
				],
				[
					7.738310028547801,
					4.762036940644805
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06129458546638489,
				0.16321027278900146,
				0.209026038646698,
				0.19922789931297302,
				0.17911316454410553,
				0.1666414737701416,
				0.1575099229812622,
				0.17442010343074799,
				0.2073988914489746,
				0.23541446030139923,
				0.25899648666381836,
				0.26747050881385803,
				0.25855010747909546,
				0.014831970445811749,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 2011509714,
			"isDeleted": false,
			"id": "7C-Qh9z2dkI8UazDJ--lt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 403.72664354356766,
			"y": 208.3796455167037,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.143055410967179,
			"height": 8.333564646128366,
			"seed": 366631680,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5952546175805651
				],
				[
					0.5952546175806219,
					0.5952546175805651
				],
				[
					1.1905092351612439,
					1.785763852741752
				],
				[
					4.762036940644805,
					5.35729155822537
				],
				[
					7.143055410967179,
					8.333564646128366
				],
				[
					7.143055410967179,
					8.333564646128366
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08099719136953354,
				0.11904729902744293,
				0.18605399131774902,
				0.21366000175476074,
				0.029386717826128006,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1259743822,
			"isDeleted": false,
			"id": "lBhutRTJczb-g1DCyWUmD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 412.65546280727665,
			"y": 207.18913628154246,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.333564646128366,
			"height": 10.71458311645074,
			"seed": 563043072,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5952546175805651,
					-0.5952546175805651
				],
				[
					-1.785763852741809,
					-0.5952546175805651
				],
				[
					-4.762036940644748,
					2.976273087902996
				],
				[
					-7.738310028547744,
					8.333564646128423
				],
				[
					-8.333564646128366,
					10.119328498870175
				],
				[
					-7.738310028547744,
					10.119328498870175
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16630199551582336,
				0.2349179983139038,
				0.28105399012565613,
				0.14899712800979614,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 62,
			"versionNonce": 947054994,
			"isDeleted": false,
			"id": "c5AuN7FcECAnXWg9gSF0t",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 416.22699051276027,
			"y": 209.5701547518649,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.309837734031362,
			"height": 23.21493008564329,
			"seed": 1749310208,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5952546175806219
				],
				[
					0,
					0
				],
				[
					0.5952546175805651,
					4.762036940644748
				],
				[
					1.785763852741752,
					14.286110821934358
				],
				[
					1.785763852741752,
					20.238656997740293
				],
				[
					1.190509235161187,
					19.643402380159728
				],
				[
					-0.5952546175806219,
					14.881365439514923
				],
				[
					-1.785763852741809,
					7.738310028547744
				],
				[
					0,
					1.190509235161187
				],
				[
					4.762036940644748,
					-2.976273087902996
				],
				[
					8.333564646128366,
					-1.785763852741809
				],
				[
					9.524073881289553,
					2.381018470322374
				],
				[
					8.928819263708931,
					5.35729155822537
				],
				[
					4.762036940644748,
					6.547800793386557
				],
				[
					2.976273087902996,
					5.35729155822537
				],
				[
					2.976273087902996,
					5.35729155822537
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16040201485157013,
				0.19889162480831146,
				0.2364998459815979,
				0.19465380907058716,
				0.1402485966682434,
				0.07862918078899384,
				0.047019775956869125,
				0.09490304440259933,
				0.1664702147245407,
				0.20263943076133728,
				0.24409307539463043,
				0.24066191911697388,
				0.14838647842407227,
				0.027927977964282036,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1807200398,
			"isDeleted": false,
			"id": "FRzK6rNTpLbKe4LVZsUr4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 428.7273374819528,
			"y": 210.16540936944546,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.333564646128366,
			"height": 10.714583116450797,
			"seed": 756259584,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5952546175805651,
					0
				],
				[
					1.190509235161187,
					0
				],
				[
					2.976273087902996,
					-1.190509235161187
				],
				[
					3.571527705483561,
					-2.976273087902996
				],
				[
					1.190509235161187,
					-4.166782323064183
				],
				[
					-1.785763852741809,
					-2.381018470322374
				],
				[
					-2.976273087902996,
					2.381018470322431
				],
				[
					-1.785763852741809,
					5.952546175805992
				],
				[
					1.190509235161187,
					6.547800793386614
				],
				[
					4.762036940644805,
					5.357291558225427
				],
				[
					5.35729155822537,
					4.762036940644805
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10418277233839035,
				0.190566286444664,
				0.19035540521144867,
				0.16142156720161438,
				0.15839962661266327,
				0.18377447128295898,
				0.27830448746681213,
				0.26322799921035767,
				0.0982929989695549,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 289662802,
			"isDeleted": false,
			"id": "papT7zQGfqHiiUf6aJGnf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 434.0846290401782,
			"y": 209.5701547518649,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.333564646128366,
			"height": 10.714583116450797,
			"seed": 197638912,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5952546175806219
				],
				[
					1.190509235161187,
					0.5952546175805651
				],
				[
					2.381018470322374,
					4.166782323064183
				],
				[
					2.976273087902996,
					5.952546175805992
				],
				[
					2.976273087902996,
					2.381018470322374
				],
				[
					4.762036940644805,
					-2.381018470322431
				],
				[
					6.547800793386614,
					-3.571527705483618
				],
				[
					8.333564646128366,
					0
				],
				[
					8.333564646128366,
					5.35729155822537
				],
				[
					7.738310028547801,
					7.143055410967179
				],
				[
					7.143055410967179,
					6.547800793386557
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.053997498005628586,
				0.1444854736328125,
				0.19369736313819885,
				0.17562463879585266,
				0.07184848189353943,
				0,
				0.06601367145776749,
				0.24920599162578583,
				0.27329501509666443,
				0.1352808177471161,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 47083214,
			"isDeleted": false,
			"id": "-VkmeasvgD_gxNB_LhfEC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 450.7517583324349,
			"y": 206.5938816639619,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.143055410967179,
			"height": 9.524073881289553,
			"seed": 1539824384,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5952546175805651,
					0
				],
				[
					-1.785763852741752,
					0
				],
				[
					-2.976273087902939,
					0
				],
				[
					-5.35729155822537,
					1.190509235161187
				],
				[
					-4.762036940644748,
					3.571527705483561
				],
				[
					-1.190509235161187,
					5.952546175805992
				],
				[
					0.5952546175806219,
					8.333564646128366
				],
				[
					0,
					9.524073881289553
				],
				[
					-4.166782323064183,
					9.524073881289553
				],
				[
					-6.547800793386557,
					8.928819263708988
				],
				[
					-3.571527705483561,
					7.738310028547744
				],
				[
					-2.976273087902939,
					7.143055410967179
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10722997784614563,
				0.14979000389575958,
				0.19486834108829498,
				0.19762976467609406,
				0.19552594423294067,
				0.20553909242153168,
				0.253433495759964,
				0.27753543853759766,
				0.24029427766799927,
				0.013057159259915352,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 716123410,
			"isDeleted": false,
			"id": "sGDrP1ZQAGe_i7jT2lWFa",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 455.5137952730797,
			"y": 208.3796455167037,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.190509235161187,
			"height": 7.738310028547744,
			"seed": 56400640,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5952546175805651
				],
				[
					0,
					1.785763852741752
				],
				[
					0,
					5.35729155822537
				],
				[
					0.5952546175806219,
					7.738310028547744
				],
				[
					1.190509235161187,
					7.143055410967179
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1776520013809204,
				0.2999599874019623,
				0.04358239844441414,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 2096325902,
			"isDeleted": false,
			"id": "f2MThXacNKONg92aBnM-C",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 455.5137952730797,
			"y": 202.4270993408977,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.5952546175806219,
			"height": 0.5952546175806219,
			"seed": 1101593344,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5952546175806219,
					-0.5952546175806219
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
				0.1043899804353714,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 170638034,
			"isDeleted": false,
			"id": "RujWramVRYBpwTMZdO53J",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 534.4992143091379,
			"y": 154.97144987670958,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.17504601432131,
			"height": 11.751628645586777,
			"seed": 1582463744,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758951885,
					-0.5109403758950748
				],
				[
					-1.0218807517901496,
					-0.5109403758950748
				],
				[
					-1.532821127685338,
					-0.5109403758950748
				],
				[
					-3.0656422553704488,
					0.5109403758950748
				],
				[
					-5.109403758950748,
					2.0437615035803276
				],
				[
					-6.642224886636086,
					5.109403758950776
				],
				[
					-7.153165262531161,
					8.175046014321225
				],
				[
					-5.620344134845936,
					10.729747893796628
				],
				[
					-3.5765826312656372,
					11.240688269691702
				],
				[
					0.5109403758949611,
					9.196926766111403
				],
				[
					1.0218807517901496,
					8.6859863902163
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09750198572874069,
				0.13298998773097992,
				0.15481197834014893,
				0.18498654663562775,
				0.21072781085968018,
				0.24373187124729156,
				0.28531384468078613,
				0.31772711873054504,
				0.31818529963493347,
				0.09610669314861298,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1268749134,
			"isDeleted": false,
			"id": "-wybJrtsb7VAxPiQmFgkU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 538.0757969404033,
			"y": 163.1464958910308,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.153165262531047,
			"height": 13.284449773272001,
			"seed": 1893374720,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5109403758951885,
					0
				],
				[
					2.043761503580299,
					-3.0656422553704488
				],
				[
					4.598463383055787,
					-8.6859863902163
				],
				[
					5.620344134845936,
					-12.262569021481823
				],
				[
					5.109403758950748,
					-10.218807517901524
				],
				[
					5.620344134845936,
					-6.1312845107408975
				],
				[
					6.642224886636086,
					-1.0218807517901496
				],
				[
					7.153165262531047,
					1.021880751790178
				],
				[
					6.1312845107408975,
					0.5109403758950748
				],
				[
					5.620344134845936,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17799799144268036,
				0.21825554966926575,
				0.19814608991146088,
				0.15455667674541473,
				0.2187780737876892,
				0.26599448919296265,
				0.2938476800918579,
				0.24570691585540771,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 1850773650,
			"isDeleted": false,
			"id": "IvBUxwDKMKX6JaFUH_Swv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 539.6086180680886,
			"y": 161.1027343874505,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.1312845107408975,
			"height": 0,
			"seed": 1915362048,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.5547018794752603,
					0
				],
				[
					6.1312845107408975,
					0
				],
				[
					6.1312845107408975,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.26041001081466675,
				0.14117670059204102,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 59,
			"versionNonce": 1227618702,
			"isDeleted": false,
			"id": "aSQnGy60JWkSopkFEtokV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 550.8493063377803,
			"y": 154.97144987670958,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.707867142006421,
			"height": 14.817270900957226,
			"seed": 762919680,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5109403758950748
				],
				[
					0,
					-1.5328211276852244
				],
				[
					0,
					-1.0218807517901496
				],
				[
					0.5109403758950748,
					3.576582631265552
				],
				[
					1.5328211276852244,
					8.6859863902163
				],
				[
					1.5328211276852244,
					10.729747893796628
				],
				[
					1.5328211276852244,
					9.707867142006478
				],
				[
					1.0218807517901496,
					7.1531652625310755
				],
				[
					0,
					3.065642255370477
				],
				[
					-1.0218807517901496,
					-0.5109403758950748
				],
				[
					-1.5328211276852244,
					-3.0656422553704488
				],
				[
					-1.0218807517901496,
					-3.5765826312655236
				],
				[
					1.5328211276852244,
					-4.087523007160598
				],
				[
					5.109403758950748,
					-4.087523007160598
				],
				[
					7.664105638426122,
					-2.043761503580299
				],
				[
					8.175046014321197,
					0
				],
				[
					7.153165262531047,
					2.5547018794754024
				],
				[
					4.598463383055673,
					3.065642255370477
				],
				[
					2.554701879475374,
					3.065642255370477
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
				0.09577499330043793,
				0.15759021043777466,
				0.1935887485742569,
				0.23090389370918274,
				0.21725015342235565,
				0.14835529029369354,
				0.11713501065969467,
				0.1066407784819603,
				0.12872284650802612,
				0.1749265491962433,
				0.2378302961587906,
				0.2909955680370331,
				0.33566930890083313,
				0.379733681678772,
				0.3784460425376892,
				0.3815709948539734,
				0.2973998785018921,
				0.0642319917678833,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 718581330,
			"isDeleted": false,
			"id": "FNWohVe2y0ajtAhA-IYwI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 564.1337561110522,
			"y": 152.4167479972342,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.685986390216385,
			"height": 12.262569021481852,
			"seed": 1948490496,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5109403758950748
				],
				[
					-0.5109403758949611,
					-0.5109403758950748
				],
				[
					-2.043761503580299,
					2.043761503580299
				],
				[
					-3.5765826312655236,
					6.131284510740926
				],
				[
					-4.087523007160598,
					9.196926766111375
				],
				[
					-2.554701879475374,
					11.240688269691674
				],
				[
					0,
					11.751628645586777
				],
				[
					2.5547018794754877,
					11.240688269691674
				],
				[
					4.598463383055787,
					8.6859863902163
				],
				[
					4.087523007160598,
					8.175046014321225
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14691101014614105,
				0.225739985704422,
				0.26465919613838196,
				0.3067786991596222,
				0.33859705924987793,
				0.33405619859695435,
				0.3259254992008209,
				0.33379220962524414,
				0.04486038163304329,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 483497934,
			"isDeleted": false,
			"id": "l5DwuorwvUKWdJkCZqOhq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 563.1118753592621,
			"y": 157.0152113802899,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.1312845107408975,
			"height": 0.5109403758950748,
			"seed": 1878203136,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5109403758951885,
					0
				],
				[
					3.5765826312656372,
					0.5109403758950748
				],
				[
					6.1312845107408975,
					0.5109403758950748
				],
				[
					6.1312845107408975,
					0.5109403758950748
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.27343201637268066,
				0.32452601194381714,
				0.010558257810771465,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 76485650,
			"isDeleted": false,
			"id": "UGC4z_IPTEWaPEoXZUYI7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 562.0899946074719,
			"y": 150.3729864936539,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.196926766111346,
			"height": 2.043761503580299,
			"seed": 329440000,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5109403758950748,
					0
				],
				[
					0.5109403758950748,
					-0.5109403758950748
				],
				[
					1.0218807517901496,
					-0.5109403758950748
				],
				[
					5.109403758950748,
					0
				],
				[
					8.685986390216385,
					1.0218807517901496
				],
				[
					9.196926766111346,
					1.5328211276852244
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06398599594831467,
				0.12703198194503784,
				0.21568988263607025,
				0.30883798003196716,
				0.1401066929101944,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 514420238,
			"isDeleted": false,
			"id": "TP_B91iWixqP-8IYlkydT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 573.8416232530587,
			"y": 150.3729864936539,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.175046014321197,
			"height": 9.196926766111375,
			"seed": 1859640064,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5109403758949611,
					0.5109403758950748
				],
				[
					3.57658263126541,
					3.0656422553704488
				],
				[
					6.642224886635972,
					7.1531652625310755
				],
				[
					7.664105638426122,
					9.196926766111375
				],
				[
					8.175046014321197,
					9.196926766111375
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2304459810256958,
				0.3047719895839691,
				0.22046169638633728,
				0.0077290344052016735,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 225886674,
			"isDeleted": false,
			"id": "ciLU6AedNSJoDRpgw8fc_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 582.527609643275,
			"y": 149.86204611775884,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.707867142006421,
			"height": 10.729747893796599,
			"seed": 1145846528,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758950748,
					0
				],
				[
					-1.5328211276852244,
					0
				],
				[
					-3.0656422553705625,
					1.5328211276852244
				],
				[
					-8.17504601432131,
					7.66410563842615
				],
				[
					-9.707867142006421,
					10.729747893796599
				],
				[
					-9.707867142006421,
					10.729747893796599
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.17638598382472992,
				0.25140297412872314,
				0.3497999906539917,
				0.1964816302061081,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1001159758,
			"isDeleted": false,
			"id": "dFJQ5xSRzDlQqwp5Shoq8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 527.8569894225018,
			"y": 181.5403494232536,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.707867142006421,
			"height": 10.72974789379657,
			"seed": 1478572800,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.0218807517901496,
					1.0218807517901496
				],
				[
					-2.043761503580299,
					2.043761503580299
				],
				[
					-2.554701879475374,
					4.598463383055673
				],
				[
					-1.5328211276852244,
					8.685986390216272
				],
				[
					2.043761503580299,
					10.72974789379657
				],
				[
					5.109403758950748,
					10.218807517901496
				],
				[
					6.642224886636086,
					6.642224886635972
				],
				[
					7.153165262531047,
					3.0656422553704488
				],
				[
					4.087523007160598,
					0.5109403758950748
				],
				[
					1.0218807517901496,
					0.5109403758950748
				],
				[
					-0.5109403758950748,
					3.5765826312655236
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
				0.12253399938344955,
				0.1763479858636856,
				0.21892206370830536,
				0.2155715674161911,
				0.20070181787014008,
				0.17396560311317444,
				0.1601460576057434,
				0.17739728093147278,
				0.18694815039634705,
				0.02800503559410572,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 10663826,
			"isDeleted": false,
			"id": "iQB8I2kARQ2wIKV9vWjbj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 538.0757969404033,
			"y": 181.0294090473585,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.196926766111346,
			"height": 14.306330525062123,
			"seed": 1079417600,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758949611,
					0
				],
				[
					-0.5109403758949611,
					3.0656422553704488
				],
				[
					1.0218807517901496,
					8.685986390216272
				],
				[
					2.043761503580299,
					11.75162864558672
				],
				[
					2.043761503580299,
					10.218807517901496
				],
				[
					1.0218807517901496,
					5.620344134845823
				],
				[
					0.5109403758951885,
					1.0218807517901496
				],
				[
					2.043761503580299,
					-2.0437615035803276
				],
				[
					5.620344134845936,
					-2.5547018794754024
				],
				[
					8.17504601432131,
					0
				],
				[
					8.685986390216385,
					2.554701879475374
				],
				[
					6.642224886636086,
					4.598463383055673
				],
				[
					4.087523007160598,
					3.5765826312655236
				],
				[
					4.087523007160598,
					3.0656422553704488
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13994435966014862,
				0.19025573134422302,
				0.21118475496768951,
				0.1463024914264679,
				0.07829168438911438,
				0.09712985157966614,
				0.1503777801990509,
				0.19715377688407898,
				0.26064369082450867,
				0.312964528799057,
				0.2759498953819275,
				0.03491082787513733,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1504952974,
			"isDeleted": false,
			"id": "TpuINIa4Y6spe2GvZ3Hx7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 551.3602467136753,
			"y": 180.5184686714634,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.196926766111346,
			"height": 11.240688269691674,
			"seed": 1916836608,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5109403758950748
				],
				[
					-1.0218807517901496,
					0
				],
				[
					-2.554701879475374,
					3.065642255370477
				],
				[
					-3.0656422553704488,
					7.1531652625310755
				],
				[
					-2.043761503580299,
					9.70786714200645
				],
				[
					1.0218807517901496,
					10.729747893796599
				],
				[
					4.087523007160598,
					9.70786714200645
				],
				[
					6.1312845107408975,
					6.642224886636001
				],
				[
					5.620344134845823,
					6.131284510740926
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.2175079882144928,
				0.2577488422393799,
				0.31885164976119995,
				0.3417758345603943,
				0.33211150765419006,
				0.31701967120170593,
				0.03563299402594566,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 508163410,
			"isDeleted": false,
			"id": "g2pdFnNZ2Xdi5oAnP4LkQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 551.8711870895704,
			"y": 183.5841109268339,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.1312845107408975,
			"height": 0.5109403758950748,
			"seed": 1228372736,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5109403758950748
				],
				[
					2.043761503580299,
					0.5109403758950748
				],
				[
					5.109403758950748,
					0.5109403758950748
				],
				[
					6.1312845107408975,
					0.5109403758950748
				],
				[
					6.1312845107408975,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14077205955982208,
				0.2928540110588074,
				0.27870598435401917,
				0.03244674578309059,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 997736654,
			"isDeleted": false,
			"id": "WhP1k_s59D0R5cxTtujWL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 550.8493063377803,
			"y": 178.4747071678831,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.685986390216272,
			"height": 0.5109403758950748,
			"seed": 343923456,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.5328211276852244,
					0
				],
				[
					5.620344134845823,
					0
				],
				[
					8.685986390216272,
					0.5109403758950748
				],
				[
					8.685986390216272,
					0.5109403758950748
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2971959710121155,
				0.31528598070144653,
				0.0659012421965599,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 130251538,
			"isDeleted": false,
			"id": "Kdb_yZuG4yuzp1JweYqAe",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 561.0681138556818,
			"y": 179.49658791967326,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.175046014321197,
			"height": 5.620344134845851,
			"seed": 396335872,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5109403758950748,
					0
				],
				[
					1.5328211276852244,
					1.0218807517901496
				],
				[
					5.109403758950748,
					3.576582631265552
				],
				[
					8.175046014321197,
					5.620344134845851
				],
				[
					8.175046014321197,
					5.620344134845851
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.19035598635673523,
				0.2421155422925949,
				0.02930731140077114,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1687353102,
			"isDeleted": false,
			"id": "eN7fCBNTIIU_ymV7HXlgO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 568.732219494108,
			"y": 179.49658791967326,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.729747893796684,
			"height": 10.729747893796599,
			"seed": 1330379520,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758951885,
					-0.5109403758950748
				],
				[
					-2.043761503580299,
					0
				],
				[
					-5.620344134845936,
					4.087523007160627
				],
				[
					-9.707867142006535,
					9.196926766111375
				],
				[
					-10.729747893796684,
					10.218807517901524
				],
				[
					-10.21880751790161,
					9.70786714200645
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14141598343849182,
				0.27454400062561035,
				0.3441200256347656,
				0.4098900258541107,
				0.13909952342510223,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 461785298,
			"isDeleted": false,
			"id": "H7h--rhiToEZhxGHx1rCD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 591.2135960334913,
			"y": 152.4167479972342,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.642224886635972,
			"height": 1.0218807517901496,
			"seed": 392231680,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758950748,
					0
				],
				[
					1.5328211276852244,
					0.5109403758950748
				],
				[
					4.598463383055673,
					0.5109403758950748
				],
				[
					5.620344134845936,
					0.5109403758950748
				],
				[
					6.1312845107408975,
					1.0218807517901496
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08545675873756409,
				0.3215879797935486,
				0.37868401408195496,
				0.1099359467625618,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 2105337166,
			"isDeleted": false,
			"id": "jfQhRcuYulGkd1YwTjYDP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 600.9214631754978,
			"y": 149.86204611775884,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.1312845107408975,
			"height": 7.1531652625310755,
			"seed": 945380096,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758951885,
					0
				],
				[
					-1.0218807517901496,
					0
				],
				[
					0.5109403758949611,
					1.0218807517901496
				],
				[
					3.57658263126541,
					2.554701879475374
				],
				[
					5.109403758950748,
					3.5765826312655236
				],
				[
					4.5984633830555595,
					4.598463383055673
				],
				[
					1.5328211276851107,
					6.131284510740926
				],
				[
					-1.0218807517901496,
					6.642224886636001
				],
				[
					-0.5109403758951885,
					7.1531652625310755
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09396200627088547,
				0.11796200275421143,
				0.2560519874095917,
				0.25799378752708435,
				0.2607665956020355,
				0.3203541338443756,
				0.36765679717063904,
				0.3446078300476074,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1361665682,
			"isDeleted": false,
			"id": "oEpcUNZBaYUm1qijGtqbe",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 610.1183899416092,
			"y": 149.86204611775884,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.0218807517901496,
			"height": 6.642224886636001,
			"seed": 675822336,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5109403758950748
				],
				[
					0,
					1.0218807517901496
				],
				[
					0.5109403758949611,
					2.554701879475374
				],
				[
					1.0218807517901496,
					5.620344134845823
				],
				[
					1.0218807517901496,
					6.642224886636001
				],
				[
					1.0218807517901496,
					6.642224886636001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1474279761314392,
				0.1857679784297943,
				0.19983193278312683,
				0.04647543281316757,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 932121486,
			"isDeleted": false,
			"id": "igklPBjk7kgchGLM9mykZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 611.1402706933993,
			"y": 146.28546348649328,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.0218807517901496,
			"height": 0.5109403758950748,
			"seed": 1915648,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758951885,
					0
				],
				[
					-1.0218807517901496,
					-0.5109403758950748
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
				0.18661749362945557,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 358857810,
			"isDeleted": false,
			"id": "H1Bk9InzWpH6nLWScn9-0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 613.6949725728747,
			"y": 150.3729864936539,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.109403758950748,
			"height": 5.620344134845823,
			"seed": 1169488640,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.0218807517901496
				],
				[
					0.5109403758950748,
					2.043761503580299
				],
				[
					0.5109403758950748,
					3.0656422553704488
				],
				[
					1.5328211276852244,
					4.598463383055673
				],
				[
					2.043761503580299,
					2.043761503580299
				],
				[
					4.087523007160598,
					-1.0218807517901496
				],
				[
					5.109403758950748,
					-1.0218807517901496
				],
				[
					4.598463383055673,
					3.0656422553704488
				],
				[
					4.087523007160598,
					4.598463383055673
				],
				[
					4.087523007160598,
					4.598463383055673
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1202724277973175,
				0.17469199001789093,
				0.20069198310375214,
				0.16089703142642975,
				0.06960458308458328,
				0.05060766637325287,
				0.17978143692016602,
				0.24127031862735748,
				0.0623893141746521,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 822241742,
			"isDeleted": false,
			"id": "CPdTzLyTf91I4dO6sZVC1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 624.4247204666713,
			"y": 147.81828461417854,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.598463383055673,
			"height": 8.175046014321225,
			"seed": 1047821056,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758950748,
					0
				],
				[
					-2.043761503580299,
					0
				],
				[
					-2.554701879475374,
					0
				],
				[
					-1.5328211276852244,
					2.043761503580299
				],
				[
					1.0218807517901496,
					4.598463383055673
				],
				[
					2.043761503580299,
					6.642224886635972
				],
				[
					0.5109403758950748,
					8.175046014321225
				],
				[
					-2.043761503580299,
					7.664105638426122
				],
				[
					-1.5328211276852244,
					5.109403758950748
				],
				[
					-1.5328211276852244,
					4.598463383055673
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08790792524814606,
				0.13771027326583862,
				0.16069619357585907,
				0.1694711595773697,
				0.21701425313949585,
				0.2842463254928589,
				0.2477588802576065,
				0.027751006186008453,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 638345746,
			"isDeleted": false,
			"id": "9FqavBL-exV7YRqviU6NL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 630.0450646015171,
			"y": 141.17605972754254,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.5109403758950748,
			"height": 14.306330525062123,
			"seed": 66321152,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758950748,
					0
				],
				[
					-0.5109403758950748,
					1.5328211276852244
				],
				[
					0,
					7.66410563842615
				],
				[
					0,
					14.306330525062123
				],
				[
					-0.5109403758950748,
					13.795390149167048
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15620675683021545,
				0.25237399339675903,
				0.30281999707221985,
				0.30045512318611145,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1492123662,
			"isDeleted": false,
			"id": "Lt3m7J2qDurc4zA_ULlhh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 625.4466012184614,
			"y": 147.81828461417854,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.218807517901496,
			"height": 1.5328211276852244,
			"seed": 407657216,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.0218807517901496,
					0
				],
				[
					5.620344134845936,
					-0.5109403758950748
				],
				[
					9.707867142006535,
					1.0218807517901496
				],
				[
					10.218807517901496,
					1.0218807517901496
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.21523800492286682,
				0.16686493158340454,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1847218130,
			"isDeleted": false,
			"id": "ztuPVd_KgbPYeHa5BZK7H",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 636.1763491122581,
			"y": 150.3729864936539,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.1312845107408975,
			"height": 6.642224886635972,
			"seed": 2014059264,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758951885,
					0.5109403758950748
				],
				[
					-1.0218807517901496,
					2.043761503580299
				],
				[
					-1.0218807517901496,
					3.0656422553704488
				],
				[
					0,
					3.5765826312655236
				],
				[
					3.0656422553704488,
					4.087523007160598
				],
				[
					5.109403758950748,
					2.043761503580299
				],
				[
					5.109403758950748,
					-1.0218807517901496
				],
				[
					1.5328211276851107,
					-2.554701879475374
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
				0.11910653859376907,
				0.17596600949764252,
				0.1861521303653717,
				0.20508025586605072,
				0.1967546045780182,
				0.19077084958553314,
				0.013861022889614105,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1397804622,
			"isDeleted": false,
			"id": "fLrauq3qqGq6KzdlNWv_f",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 640.2638721194187,
			"y": 150.883926869549,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.0656422553704488,
			"height": 1.5328211276852244,
			"seed": 1796971264,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5109403758950748
				],
				[
					1.0218807517901496,
					1.0218807517901496
				],
				[
					3.0656422553704488,
					1.5328211276852244
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
				0.0925459936261177,
				0.01810256950557232,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1638172050,
			"isDeleted": false,
			"id": "zP3HUaDIrmac9Yy-OTdXQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 646.9060970060546,
			"y": 136.57759634448684,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.532821127685338,
			"height": 16.861032404537525,
			"seed": 642251520,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5109403758950748
				],
				[
					0.5109403758951885,
					2.5547018794754024
				],
				[
					1.0218807517902633,
					11.751628645586777
				],
				[
					1.0218807517902633,
					16.861032404537525
				],
				[
					1.532821127685338,
					16.861032404537525
				],
				[
					1.532821127685338,
					16.35009202864245
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12692569196224213,
				0.2018197923898697,
				0.28888800740242004,
				0.3021340072154999,
				0.04352383315563202,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1560138894,
			"isDeleted": false,
			"id": "9JaPCpkP9vsQmuXvip8RM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 651.5045603891103,
			"y": 135.0447752168016,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.0218807517901496,
			"height": 20.948555411698152,
			"seed": 844954368,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.5328211276852244
				],
				[
					0,
					4.087523007160627
				],
				[
					0.5109403758950748,
					13.284449773272001
				],
				[
					0.5109403758950748,
					19.4157342840129
				],
				[
					1.0218807517901496,
					20.948555411698152
				],
				[
					1.0218807517901496,
					20.948555411698152
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1186625063419342,
				0.14498797059059143,
				0.26020002365112305,
				0.35752400755882263,
				0.22752682864665985,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1507984210,
			"isDeleted": false,
			"id": "V_SI_j0AWxluYdMYFMBC_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 655.0811430203759,
			"y": 149.35110574186376,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.1312845107408975,
			"height": 7.1531652625310755,
			"seed": 426900224,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5109403758950748
				],
				[
					-1.0218807517901496,
					2.043761503580299
				],
				[
					-0.5109403758950748,
					3.0656422553704488
				],
				[
					1.0218807517901496,
					4.598463383055673
				],
				[
					3.5765826312655236,
					4.087523007160598
				],
				[
					5.109403758950748,
					0.5109403758950748
				],
				[
					4.087523007160598,
					-2.5547018794754024
				],
				[
					0.5109403758950748,
					-2.5547018794754024
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
				0.08530456572771072,
				0.17497000098228455,
				0.21758124232292175,
				0.22273416817188263,
				0.21562722325325012,
				0.19301386177539825,
				0.013580200262367725,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 800068302,
			"isDeleted": false,
			"id": "nhIQ4W-QMLLZ1YBzhEqeR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 657.1249045239562,
			"y": 150.883926869549,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.620344134845823,
			"height": 0.5109403758950748,
			"seed": 2125560576,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5109403758950748,
					0.5109403758950748
				],
				[
					1.5328211276852244,
					0.5109403758950748
				],
				[
					5.109403758950748,
					0.5109403758950748
				],
				[
					5.620344134845823,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14139987528324127,
				0.08493780344724655,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1898563858,
			"isDeleted": false,
			"id": "62rTs7L6BNLpWnBT7DG-9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 665.8108909141724,
			"y": 135.55571559269669,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.0218807517901496,
			"height": 17.882913156327675,
			"seed": 1478048512,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5109403758950748
				],
				[
					-0.5109403758949611,
					4.087523007160627
				],
				[
					0,
					7.66410563842615
				],
				[
					0.5109403758951885,
					14.306330525062151
				],
				[
					0.5109403758951885,
					17.882913156327675
				],
				[
					0.5109403758951885,
					17.882913156327675
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1644660085439682,
				0.23341399431228638,
				0.28582900762557983,
				0.023990783840417862,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1711311118,
			"isDeleted": false,
			"id": "WZU4DEa0fX4vzYV3IqMQB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 661.7233679070118,
			"y": 145.26358273470314,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.1312845107408975,
			"height": 1.0218807517901496,
			"seed": 250493696,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5109403758950748,
					-0.5109403758950748
				],
				[
					2.043761503580299,
					-0.5109403758950748
				],
				[
					5.620344134845936,
					0
				],
				[
					6.1312845107408975,
					0.5109403758950748
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13910949230194092,
				0.1827619969844818,
				0.08436281979084015,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1592973010,
			"isDeleted": false,
			"id": "oowW0l_9_ZhepLhXjLgI3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 672.9640561767035,
			"y": 147.30734423828346,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.5109403758951885,
			"height": 4.598463383055673,
			"seed": 1137048320,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5109403758950748
				],
				[
					0,
					2.043761503580299
				],
				[
					0,
					4.598463383055673
				],
				[
					0.5109403758951885,
					4.598463383055673
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1645672619342804,
				0.07433202862739563,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1600665422,
			"isDeleted": false,
			"id": "ON6hTPH-mCQTmsnqppBys",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 673.9859369284936,
			"y": 142.1979404793327,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.0218807517901496,
			"height": 0.5109403758950748,
			"seed": 1674427136,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5109403758950748
				],
				[
					-0.5109403758949611,
					-0.5109403758950748
				],
				[
					-1.0218807517901496,
					-0.5109403758950748
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
				0.1339459866285324,
				0.021221984177827835,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1406413970,
			"isDeleted": false,
			"id": "DCE5yPqs7RwqSF0OhPEAO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 676.0296984320739,
			"y": 147.30734423828346,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.1312845107408975,
			"height": 6.642224886636001,
			"seed": 1654528768,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5109403758950748
				],
				[
					-1.0218807517901496,
					1.5328211276852244
				],
				[
					-0.5109403758949611,
					3.0656422553704488
				],
				[
					1.0218807517901496,
					4.087523007160598
				],
				[
					3.5765826312656372,
					3.5765826312655236
				],
				[
					4.598463383055787,
					0.5109403758950748
				],
				[
					3.0656422553704488,
					-2.5547018794754024
				],
				[
					0,
					-2.5547018794754024
				],
				[
					-1.5328211276851107,
					0.5109403758950748
				],
				[
					-1.0218807517901496,
					2.554701879475374
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
				0.09133700281381607,
				0.1026134043931961,
				0.20828454196453094,
				0.2559892535209656,
				0.20672374963760376,
				0.1196729764342308,
				0.11367779225111008,
				0.13429699838161469,
				0.05554092302918434,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 608181646,
			"isDeleted": false,
			"id": "OimamjXhPbOXh1absktgO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 680.1172214392345,
			"y": 145.7745231105982,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.598463383055787,
			"height": 6.642224886636001,
			"seed": 1245895424,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5109403758950748
				],
				[
					0,
					2.0437615035803276
				],
				[
					0.5109403758951885,
					3.576582631265552
				],
				[
					1.532821127685338,
					4.087523007160627
				],
				[
					3.0656422553705625,
					1.5328211276852528
				],
				[
					4.087523007160712,
					1.0218807517901496
				],
				[
					4.598463383055787,
					3.576582631265552
				],
				[
					4.087523007160712,
					6.131284510740926
				],
				[
					4.087523007160712,
					6.642224886636001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.18335799872875214,
				0.25551000237464905,
				0.19416290521621704,
				0.014295989647507668,
				0.08045965433120728,
				0.26211798191070557,
				0.23536600172519684,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1434765906,
			"isDeleted": false,
			"id": "pU4J4st5ml6gwH2w8kbUZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 578.9510270120095,
			"y": 183.5841109268339,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.1312845107408975,
			"height": 1.0218807517901496,
			"seed": 1864481536,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.554701879475374,
					-0.5109403758950748
				],
				[
					5.109403758950748,
					-1.0218807517901496
				],
				[
					6.1312845107408975,
					-1.0218807517901496
				],
				[
					6.1312845107408975,
					-1.0218807517901496
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2589460015296936,
				0.24413195252418518,
				0.0291327815502882,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1237400526,
			"isDeleted": false,
			"id": "1uBig34JAXqPp_RODb0gI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 588.6588941540159,
			"y": 179.49658791967326,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.685986390216272,
			"height": 7.1531652625310755,
			"seed": 1197046528,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758950748,
					0
				],
				[
					-2.043761503580299,
					0
				],
				[
					-2.554701879475374,
					0
				],
				[
					-2.043761503580299,
					1.0218807517901496
				],
				[
					1.5328211276852244,
					2.5547018794754024
				],
				[
					5.109403758950748,
					4.087523007160627
				],
				[
					6.1312845107408975,
					5.109403758950776
				],
				[
					4.598463383055673,
					6.131284510740926
				],
				[
					1.5328211276852244,
					7.1531652625310755
				],
				[
					0.5109403758950748,
					7.1531652625310755
				],
				[
					1.0218807517901496,
					6.642224886636001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15207000076770782,
				0.25629401206970215,
				0.3138680160045624,
				0.3438074290752411,
				0.3202979862689972,
				0.30211421847343445,
				0.340718150138855,
				0.3674941658973694,
				0.32847580313682556,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 450605074,
			"isDeleted": false,
			"id": "kWqXvh8jLkAjFD9HgKK8m",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 601.943343927288,
			"y": 179.49658791967326,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.620344134845709,
			"height": 8.6859863902163,
			"seed": 2122423040,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5109403758950748
				],
				[
					0,
					0.5109403758950748
				],
				[
					0.5109403758949611,
					4.087523007160627
				],
				[
					1.0218807517901496,
					6.131284510740926
				],
				[
					2.043761503580299,
					3.576582631265552
				],
				[
					4.087523007160598,
					-0.5109403758950748
				],
				[
					5.620344134845709,
					-2.554701879475374
				],
				[
					5.620344134845709,
					-0.5109403758950748
				],
				[
					5.109403758950748,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.010141723789274693,
				0.20361365377902985,
				0.20856726169586182,
				0.17736709117889404,
				0.15542471408843994,
				0.16741757094860077,
				0.1278068572282791,
				0.005680755712091923,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1443140110,
			"isDeleted": false,
			"id": "Q3OWQVljdJ5HX-5Y_J1Jz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 608.5855688139238,
			"y": 180.00752829556833,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.642224886636086,
			"height": 6.131284510740926,
			"seed": 538475264,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5109403758950748
				],
				[
					-0.5109403758949611,
					0
				],
				[
					-1.0218807517901496,
					3.065642255370477
				],
				[
					1.0218807517901496,
					5.109403758950776
				],
				[
					4.087523007160598,
					4.598463383055702
				],
				[
					5.620344134845936,
					1.021880751790178
				],
				[
					5.109403758950862,
					-1.0218807517901496
				],
				[
					5.109403758950862,
					-1.0218807517901496
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06339999288320541,
				0.15124310553073883,
				0.18230219185352325,
				0.17539438605308533,
				0.14737823605537415,
				0.07554138451814651,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1741675986,
			"isDeleted": false,
			"id": "k13lo78aWWT3MUV5PQc87",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 614.7168533246648,
			"y": 178.4747071678831,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.1312845107408975,
			"height": 7.1531652625310755,
			"seed": 1556790016,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758950748,
					0
				],
				[
					-0.5109403758950748,
					0.5109403758950748
				],
				[
					0.5109403758950748,
					4.087523007160627
				],
				[
					1.0218807517901496,
					5.620344134845851
				],
				[
					2.554701879475374,
					3.065642255370477
				],
				[
					4.087523007160598,
					-1.0218807517901496
				],
				[
					5.109403758950748,
					-1.0218807517901496
				],
				[
					5.620344134845823,
					2.5547018794754024
				],
				[
					5.620344134845823,
					6.131284510740926
				],
				[
					5.620344134845823,
					6.131284510740926
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0762839987874031,
				0.11099603027105331,
				0.15989725291728973,
				0.1433900147676468,
				0.059244874864816666,
				0.03596670553088188,
				0.11879724264144897,
				0.20653463900089264,
				0.054681211709976196,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 604184654,
			"isDeleted": false,
			"id": "i-yftRrzzo92HuY3aMRan",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 621.8700185871959,
			"y": 177.45282641609296,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.1312845107408975,
			"height": 7.1531652625310755,
			"seed": 1525299968,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5109403758950748,
					3.0656422553704488
				],
				[
					1.5328211276852244,
					6.131284510740926
				],
				[
					2.554701879475374,
					4.087523007160627
				],
				[
					4.598463383055673,
					0
				],
				[
					5.620344134845823,
					-0.5109403758950748
				],
				[
					5.620344134845823,
					3.0656422553704488
				],
				[
					5.620344134845823,
					6.642224886636001
				],
				[
					6.1312845107408975,
					6.642224886636001
				],
				[
					6.1312845107408975,
					6.131284510740926
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1877879947423935,
				0.21183404326438904,
				0.10621847212314606,
				0.03956710919737816,
				0.12028930336236954,
				0.22405272722244263,
				0.2244795858860016,
				0.05717114359140396,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1769493394,
			"isDeleted": false,
			"id": "Bq4jE8h4T_og-nJ7szy-9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 631.5778857292023,
			"y": 177.96376679198804,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.5109403758951885,
			"height": 5.620344134845851,
			"seed": 1663376128,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.0218807517901496
				],
				[
					0,
					2.043761503580299
				],
				[
					0,
					3.576582631265552
				],
				[
					0.5109403758951885,
					5.620344134845851
				],
				[
					0.5109403758951885,
					5.620344134845851
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15180999040603638,
				0.18754999339580536,
				0.09369592368602753,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 1201006222,
			"isDeleted": false,
			"id": "qL9tzREMBgpH5MImshhNZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 632.5997664809925,
			"y": 173.36530340893236,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.5109403758949611,
			"height": 0,
			"seed": 1342274304,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758949611,
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
				0.09036599844694138,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 302780754,
			"isDeleted": false,
			"id": "1rwKFLNUC6W5k7GeIr0Fm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 634.6435279845728,
			"y": 176.4309456643028,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.1312845107408975,
			"height": 5.620344134845851,
			"seed": 414489344,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.0218807517901496
				],
				[
					0,
					2.043761503580299
				],
				[
					1.0218807517901496,
					4.598463383055702
				],
				[
					2.043761503580299,
					4.598463383055702
				],
				[
					3.5765826312656372,
					1.0218807517901496
				],
				[
					5.620344134845936,
					-1.0218807517901496
				],
				[
					6.1312845107408975,
					2.043761503580299
				],
				[
					5.620344134845936,
					4.598463383055702
				],
				[
					5.620344134845936,
					4.598463383055702
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10518200695514679,
				0.14613598585128784,
				0.1923079788684845,
				0.14979247748851776,
				0.04510968178510666,
				0.07385684549808502,
				0.1844586431980133,
				0.09412417560815811,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1903551694,
			"isDeleted": false,
			"id": "VKpt5xHAgnJ0nuC-zNlWB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 643.8404547506841,
			"y": 176.4309456643028,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.642224886635972,
			"height": 6.131284510740926,
			"seed": 1613462272,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758949611,
					0.5109403758950748
				],
				[
					-1.0218807517901496,
					1.5328211276852244
				],
				[
					-1.5328211276851107,
					3.0656422553704488
				],
				[
					0,
					5.620344134845851
				],
				[
					3.5765826312656372,
					5.620344134845851
				],
				[
					5.109403758950862,
					2.043761503580299
				],
				[
					3.5765826312656372,
					-0.5109403758950748
				],
				[
					0.5109403758951885,
					-0.5109403758950748
				],
				[
					0,
					3.5765826312655236
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
				0.1481579840183258,
				0.21763800084590912,
				0.21381841599941254,
				0.1662878692150116,
				0.1988562047481537,
				0.21474669873714447,
				0.007433990482240915,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1960974098,
			"isDeleted": false,
			"id": "vHZpVJEERL9cz5u328VhR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 647.4170373819497,
			"y": 176.9418860401979,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.153165262531161,
			"height": 14.306330525062123,
			"seed": 571710208,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758951885,
					0.5109403758950748
				],
				[
					-0.5109403758951885,
					1.0218807517901496
				],
				[
					-0.5109403758951885,
					2.043761503580299
				],
				[
					1.0218807517901496,
					5.620344134845851
				],
				[
					1.5328211276852244,
					10.729747893796599
				],
				[
					-1.532821127685338,
					14.306330525062123
				],
				[
					-5.109403758950748,
					12.773509397376898
				],
				[
					-5.620344134845936,
					12.262569021481823
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08061020076274872,
				0.1266520619392395,
				0.20458929240703583,
				0.2994140088558197,
				0.31722962856292725,
				0.15626680850982666,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 1396448014,
			"isDeleted": false,
			"id": "RumuUr1kzfPmudN_n36H2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 520.7038241599707,
			"y": 150.883926869549,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.685986390216272,
			"height": 42.91899157518645,
			"seed": 1969085184,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758950748,
					0
				],
				[
					-2.554701879475374,
					0
				],
				[
					-4.598463383055673,
					1.0218807517901496
				],
				[
					-6.1312845107408975,
					3.5765826312655236
				],
				[
					-6.1312845107408975,
					9.196926766111375
				],
				[
					-4.087523007160598,
					14.306330525062151
				],
				[
					-2.554701879475374,
					17.3719727804326
				],
				[
					-2.043761503580299,
					17.882913156327675
				],
				[
					-3.5765826312655236,
					18.904793908117824
				],
				[
					-5.109403758950748,
					19.4157342840129
				],
				[
					-5.109403758950748,
					20.43761503580305
				],
				[
					-4.598463383055673,
					21.9704361634883
				],
				[
					-2.554701879475374,
					24.0141976670686
				],
				[
					-2.554701879475374,
					27.07983992243905
				],
				[
					-3.5765826312655236,
					30.6564225537046
				],
				[
					-5.109403758950748,
					34.7439455608652
				],
				[
					-5.109403758950748,
					39.85334931981595
				],
				[
					-2.554701879475374,
					42.91899157518645
				],
				[
					2.043761503580299,
					42.91899157518645
				],
				[
					2.554701879475374,
					42.40805119929132
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09718533605337143,
				0.15999777615070343,
				0.18840853869915009,
				0.22951143980026245,
				0.27231475710868835,
				0.27503108978271484,
				0.2526589334011078,
				0.2420019507408142,
				0.2715817391872406,
				0.3005601167678833,
				0.3060610592365265,
				0.3327324092388153,
				0.3725462555885315,
				0.38303685188293457,
				0.40976402163505554,
				0.4365676939487457,
				0.44117847084999084,
				0.14857687056064606,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 577856722,
			"isDeleted": false,
			"id": "7CnlkEdY3ism0MyP-6mwU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 454.79251566950586,
			"y": 189.71539543757478,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 32.189243681389826,
			"height": 16.861032404537497,
			"seed": 1038588672,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5109403758950748
				],
				[
					0,
					-1.0218807517901496
				],
				[
					1.5328211276852244,
					-2.554701879475374
				],
				[
					10.218807517901553,
					-10.218807517901524
				],
				[
					20.43761503580305,
					-15.328211276852272
				],
				[
					27.590780298334153,
					-15.839151652747347
				],
				[
					31.167362929599676,
					-16.350092028642422
				],
				[
					32.189243681389826,
					-16.350092028642422
				],
				[
					32.189243681389826,
					-16.861032404537497
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.062004975974559784,
				0.07282574474811554,
				0.13739165663719177,
				0.24259799718856812,
				0.2861059904098511,
				0.28521570563316345,
				0.3099363446235657,
				0.11153537034988403,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 56723790,
			"isDeleted": false,
			"id": "NcNxFzxu4KRlh1nZQOmkv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 500.2662091241677,
			"y": 167.23401889819144,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.707867142006421,
			"height": 8.175046014321225,
			"seed": 188644096,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5109403758950748,
					0
				],
				[
					-0.5109403758950748,
					-0.5109403758950748
				],
				[
					3.0656422553704488,
					0.5109403758950748
				],
				[
					7.664105638426122,
					2.554701879475374
				],
				[
					9.196926766111346,
					4.598463383055673
				],
				[
					7.664105638426122,
					6.642224886636001
				],
				[
					5.620344134845823,
					7.66410563842615
				],
				[
					4.598463383055673,
					7.66410563842615
				],
				[
					5.620344134845823,
					7.66410563842615
				],
				[
					5.620344134845823,
					7.66410563842615
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09026668965816498,
				0.2105100154876709,
				0.2915459871292114,
				0.3358602225780487,
				0.33877691626548767,
				0.3904910385608673,
				0.4531868100166321,
				0.42967313528060913,
				0.12939901649951935,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 72415890,
			"isDeleted": false,
			"id": "iF0ajiIxsvD0eYbRHZBQL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 460.44465349129473,
			"y": 208.1500509049436,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.781535238376421,
			"height": 10.278284868224773,
			"seed": 834534144,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.9271784127921592
				],
				[
					0.642392804264091,
					5.781535238376421
				],
				[
					1.9271784127921592,
					7.066320846904546
				],
				[
					2.5695712170561933,
					4.4967496298483525
				],
				[
					4.4967496298483525,
					0
				],
				[
					5.781535238376421,
					-3.2119640213202274
				],
				[
					5.781535238376421,
					-2.5695712170561933
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12707988917827606,
				0.15647472441196442,
				0.14650802314281464,
				0.11513363569974899,
				0.10663839429616928,
				0.036701202392578125,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1631530894,
			"isDeleted": false,
			"id": "XmIDpv4cZK8zUqT6VAswz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 470.08054555525547,
			"y": 210.07722931773577,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.351106455432614,
			"height": 8.993499259696648,
			"seed": 163289856,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.2847856085280682,
					0
				],
				[
					1.9271784127921023,
					-0.6423928042640341
				],
				[
					2.5695712170561364,
					-1.284785608528125
				],
				[
					3.8543568255842615,
					-2.5695712170561933
				],
				[
					3.2119640213202274,
					-3.8543568255842615
				],
				[
					1.2847856085280682,
					-3.8543568255842615
				],
				[
					-1.9271784127921592,
					-0.6423928042640341
				],
				[
					-1.9271784127921592,
					2.5695712170561933
				],
				[
					1.9271784127921023,
					4.496749629848296
				],
				[
					5.781535238376421,
					5.139142434112387
				],
				[
					6.423928042640455,
					5.139142434112387
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08090090751647949,
				0.10792282223701477,
				0.11794009059667587,
				0.11438412219285965,
				0.0976591482758522,
				0.11635912954807281,
				0.14860543608665466,
				0.1832888424396515,
				0.20882336795330048,
				0.11370962858200073,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 959961170,
			"isDeleted": false,
			"id": "wIynlLw-JPE5nPHQ68j_9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 502.8042560907137,
			"y": 267.900329757733,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.67966835182574,
			"height": 10.633386948681732,
			"seed": 853423360,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5907437193712326,
					0.5907437193711758
				],
				[
					-1.1814874387424652,
					2.3629748774848167
				],
				[
					-0.5907437193712326,
					5.907437193712042
				],
				[
					1.7722311581135841,
					8.270412071196859
				],
				[
					4.135206035598401,
					8.861155790568091
				],
				[
					5.907437193712042,
					5.316693474340866
				],
				[
					6.498180913083274,
					0
				],
				[
					5.907437193712042,
					-1.1814874387424652
				],
				[
					5.316693474340866,
					-1.772231158113641
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07817599177360535,
				0.12132266163825989,
				0.15040625631809235,
				0.17180871963500977,
				0.16869589686393738,
				0.15943719446659088,
				0.16706439852714539,
				0.07620284706354141,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 2030964174,
			"isDeleted": false,
			"id": "AJahmY3Sd6dOY7WY3vO85",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 512.256155600653,
			"y": 267.3095860383618,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.679668351825626,
			"height": 9.451899509939324,
			"seed": 113857792,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5907437193711758,
					0
				],
				[
					0.5907437193712894,
					2.3629748774848167
				],
				[
					1.772231158113641,
					5.907437193712099
				],
				[
					1.772231158113641,
					7.088924632454507
				],
				[
					2.9537185968559925,
					2.9537185968560493
				],
				[
					6.498180913083274,
					-2.3629748774848167
				],
				[
					7.08892463245445,
					-2.3629748774848167
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08001288026571274,
				0.09434408694505692,
				0.1111106276512146,
				0.09337212890386581,
				0.06803256273269653,
				0.020448150113224983,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1895628306,
			"isDeleted": false,
			"id": "f0fJdmL3l8jgu9bF3Bd2q",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 522.2987988299635,
			"y": 254.31322421219522,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.861155790568091,
			"height": 18.903799019878647,
			"seed": 1393669376,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5907437193711758,
					0
				],
				[
					-1.1814874387423515,
					-0.5907437193712326
				],
				[
					-0.5907437193711758,
					2.9537185968560493
				],
				[
					0.5907437193711758,
					10.633386948681732
				],
				[
					0,
					15.950080423022598
				],
				[
					0,
					15.359336703651365
				],
				[
					0.5907437193711758,
					11.81487438742414
				],
				[
					4.135206035598458,
					10.0426432293105
				],
				[
					7.08892463245445,
					11.81487438742414
				],
				[
					7.67966835182574,
					15.950080423022598
				],
				[
					4.725949754969633,
					18.313055300507415
				],
				[
					0.5907437193711758,
					16.540824142393774
				],
				[
					0.5907437193711758,
					15.950080423022598
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.05784521624445915,
				0.12302710115909576,
				0.15002569556236267,
				0.14854495227336884,
				0.11222494393587112,
				0.09369100630283356,
				0.10847952216863632,
				0.14662021398544312,
				0.19474396109580994,
				0.21288707852363586,
				0.017057372257113457,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1743201294,
			"isDeleted": false,
			"id": "XX9vkqISLACDMacMPDXxm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 533.5229294980164,
			"y": 267.3095860383618,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.67966835182574,
			"height": 7.088924632454507,
			"seed": 1520063744,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5907437193711758,
					0.5907437193712326
				],
				[
					-1.772231158113641,
					2.3629748774848167
				],
				[
					-2.3629748774848167,
					3.544462316227225
				],
				[
					-1.1814874387424652,
					5.316693474340866
				],
				[
					2.3629748774848167,
					5.316693474340866
				],
				[
					4.725949754969747,
					3.544462316227225
				],
				[
					5.316693474340923,
					0
				],
				[
					2.9537185968559925,
					-1.772231158113641
				],
				[
					-0.5907437193711758,
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
				0.11744998395442963,
				0.16157598793506622,
				0.21002252399921417,
				0.18870492279529572,
				0.17799532413482666,
				0.18557095527648926,
				0.19511620700359344,
				0.01386477705091238,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1217883090,
			"isDeleted": false,
			"id": "80YNYBjObEI0c0s36BFtN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 535.8859043755012,
			"y": 270.2633046352178,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.907437193712099,
			"height": 0.5907437193711758,
			"seed": 1447048448,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5907437193711758,
					0
				],
				[
					1.772231158113641,
					0.5907437193711758
				],
				[
					5.316693474340809,
					0.5907437193711758
				],
				[
					5.907437193712099,
					0.5907437193711758
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10624847561120987,
				0.05532089248299599,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1069773390,
			"isDeleted": false,
			"id": "06Cr3RKhud_aOZ1jEKZiV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 541.202597849842,
			"y": 264.3558674415057,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.861155790568205,
			"height": 8.270412071196915,
			"seed": 1741976832,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5907437193712894,
					1.1814874387424084
				],
				[
					2.3629748774849304,
					5.907437193712099
				],
				[
					3.544462316227282,
					7.679668351825683
				],
				[
					4.135206035598458,
					5.316693474340866
				],
				[
					5.907437193712212,
					1.1814874387424084
				],
				[
					7.67966835182574,
					0.5907437193712326
				],
				[
					8.270412071196915,
					4.135206035598458
				],
				[
					8.270412071196915,
					7.679668351825683
				],
				[
					8.861155790568205,
					8.270412071196915
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14205627143383026,
				0.18941724300384521,
				0.14962823688983917,
				0.06519988924264908,
				0.03734881430864334,
				0.14070379734039307,
				0.2268846482038498,
				0.11412100493907928,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 639508882,
			"isDeleted": false,
			"id": "y6OT8H4q6FxdlnDUOSUPp",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 582.7370703301771,
			"y": 230.0930493826955,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.395684193287593,
			"height": 15.112231547917872,
			"seed": 170366208,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405046,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					2.798561397762569
				],
				[
					0.5597122795525138,
					5.037410515972624
				],
				[
					2.238849118210055,
					8.95539647284022
				],
				[
					2.798561397762569,
					9.515108752392734
				],
				[
					2.238849118210055,
					8.395684193287707
				],
				[
					0,
					6.7165473546301655
				],
				[
					-2.238849118210055,
					6.7165473546301655
				],
				[
					-4.477698236419997,
					8.95539647284022
				],
				[
					-5.597122795525024,
					12.873382429707817
				],
				[
					-3.917985956867483,
					15.112231547917872
				],
				[
					1.6791368386575414,
					13.433094709260331
				],
				[
					2.238849118210055,
					12.873382429707817
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10650933533906937,
				0.12989801168441772,
				0.1639203131198883,
				0.1388486921787262,
				0.09991354495286942,
				0.09146252274513245,
				0.11467254906892776,
				0.14350128173828125,
				0.17869442701339722,
				0.19330215454101562,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 1803286670,
			"isDeleted": false,
			"id": "HklKeixKFqgwXvsEU_4dJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 588.8939054052547,
			"y": 237.9290212964307,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.95539647284022,
			"height": 6.7165473546301655,
			"seed": 2110706944,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5597122795525138,
					0
				],
				[
					1.1194245591050276,
					-0.5597122795525138
				],
				[
					1.1194245591050276,
					-1.1194245591050276
				],
				[
					0,
					-1.6791368386575414
				],
				[
					-2.238849118210055,
					0
				],
				[
					-2.798561397762569,
					3.3582736773150828
				],
				[
					-1.6791368386575414,
					5.037410515972624
				],
				[
					1.1194245591050276,
					3.9179859568675965
				],
				[
					3.3582736773150828,
					0.5597122795525138
				],
				[
					4.47769823642011,
					-1.6791368386575414
				],
				[
					5.037410515972624,
					-0.5597122795525138
				],
				[
					5.037410515972624,
					2.798561397762569
				],
				[
					5.597122795525138,
					4.47769823642011
				],
				[
					6.156835075077652,
					4.47769823642011
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.053091857582330704,
				0.12205813825130463,
				0.14128652215003967,
				0.13643689453601837,
				0.1330679953098297,
				0.15725134313106537,
				0.16967657208442688,
				0.1494799554347992,
				0.09847381711006165,
				0.0870598778128624,
				0.19409707188606262,
				0.25036031007766724,
				0.10415161401033401,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 348659538,
			"isDeleted": false,
			"id": "4Ltbmyw-P1XTeiCvwH1qx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 600.088150996305,
			"y": 235.13045989866814,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.95539647284022,
			"height": 7.276259634182679,
			"seed": 453301504,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5597122795525138,
					0
				],
				[
					-1.6791368386575414,
					0
				],
				[
					-2.798561397762569,
					0.5597122795525138
				],
				[
					-3.3582736773150828,
					1.1194245591050276
				],
				[
					-1.6791368386575414,
					2.798561397762569
				],
				[
					0.5597122795525138,
					5.037410515972624
				],
				[
					1.1194245591050276,
					6.7165473546301655
				],
				[
					0,
					7.276259634182679
				],
				[
					-1.6791368386575414,
					6.7165473546301655
				],
				[
					-1.1194245591050276,
					4.47769823642011
				],
				[
					2.238849118210055,
					2.798561397762569
				],
				[
					5.037410515972624,
					3.3582736773150828
				],
				[
					5.597122795525138,
					6.7165473546301655
				],
				[
					5.597122795525138,
					6.156835075077652
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10412399470806122,
				0.15551801025867462,
				0.1770080029964447,
				0.1661146581172943,
				0.1576264351606369,
				0.1886156052350998,
				0.20861516892910004,
				0.17477725446224213,
				0.06939969211816788,
				0.0641380324959755,
				0.1493283361196518,
				0.23668508231639862,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 315209422,
			"isDeleted": false,
			"id": "s0oWQ9F4Y8vR8f_umdJit",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 607.3644106304877,
			"y": 230.0930493826955,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1194245591050276,
			"height": 0.5597122795525138,
			"seed": 205182208,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5597122795525138,
					0
				],
				[
					-1.1194245591050276,
					0.5597122795525138
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
				0.044421784579753876,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 552363282,
			"isDeleted": false,
			"id": "lAnFmRwrpLJy1EimHwM-2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 613.5212457055652,
			"y": 220.57794063030283,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.6791368386575414,
			"height": 19.589929784337926,
			"seed": 1230443776,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5597122795525138,
					0
				],
				[
					-0.5597122795525138,
					0.5597122795525138
				],
				[
					0.5597122795525138,
					6.716547354630109
				],
				[
					1.1194245591050276,
					15.67194382747033
				],
				[
					1.1194245591050276,
					19.589929784337926
				],
				[
					0.5597122795525138,
					19.589929784337926
				],
				[
					0,
					19.030217504785412
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09312082082033157,
				0.10446975380182266,
				0.23227624595165253,
				0.2804170548915863,
				0.21386444568634033,
				0.02491900697350502,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 2118495502,
			"isDeleted": false,
			"id": "e7KYUOM30r0HmerXerEUr",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 608.4838351895927,
			"y": 236.24988445777316,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.276259634182566,
			"height": 0,
			"seed": 2082960640,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5597122795525138,
					0
				],
				[
					1.6791368386575414,
					0
				],
				[
					6.716547354630052,
					0
				],
				[
					7.276259634182566,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13030999898910522,
				0.19912999868392944,
				0.08108276128768921,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 872542930,
			"isDeleted": false,
			"id": "qZcXqIcjaHIMbvQjyGmIT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 620.2377930601954,
			"y": 232.89161078045808,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.9179859568675965,
			"height": 5.037410515972624,
			"seed": 1196143872,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5597122795525138,
					1.6791368386575414
				],
				[
					3.3582736773150828,
					4.47769823642011
				],
				[
					3.9179859568675965,
					5.037410515972624
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.21029400825500488,
				0.0820450708270073,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 2070469454,
			"isDeleted": false,
			"id": "g2NLQnEStFUV3hz1BqTCm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 626.394628135273,
			"y": 232.89161078045808,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.597122795525138,
			"height": 17.351080666127928,
			"seed": 1482331392,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5597122795525138
				],
				[
					-0.5597122795525138,
					1.6791368386575414
				],
				[
					-2.798561397762569,
					7.276259634182679
				],
				[
					-5.597122795525138,
					15.112231547917872
				],
				[
					-5.597122795525138,
					17.351080666127928
				],
				[
					-5.037410515972624,
					17.351080666127928
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16102798283100128,
				0.30088597536087036,
				0.29376959800720215,
				0.07338931411504745,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1889519762,
			"isDeleted": false,
			"id": "qUuXv2aYdZs0gCG_jfE1X",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 632.5514632103507,
			"y": 225.0556388667229,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 15.112231547917872,
			"seed": 347444480,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5597122795525138
				],
				[
					0,
					8.395684193287707
				],
				[
					0,
					15.112231547917872
				],
				[
					0,
					13.433094709260331
				],
				[
					0,
					12.873382429707817
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.21158798038959503,
				0.2964300215244293,
				0.2913804054260254,
				0.02257818542420864,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1082933646,
			"isDeleted": false,
			"id": "6Ysl5rYXxbRRwgFp7sPno",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 625.275203576168,
			"y": 222.25707746896032,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.074821031945248,
			"height": 10.07482103194522,
			"seed": 968832256,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5597122795525138,
					-0.5597122795525138
				],
				[
					3.3582736773150828,
					-3.9179859568675397
				],
				[
					6.156835075077652,
					-7.276259634182651
				],
				[
					7.835971913735193,
					-5.5971227955251095
				],
				[
					8.95539647284022,
					-0.5597122795525138
				],
				[
					9.515108752392734,
					2.798561397762569
				],
				[
					10.074821031945248,
					2.798561397762569
				],
				[
					10.074821031945248,
					2.798561397762569
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13899798691272736,
				0.16675861179828644,
				0.17564724385738373,
				0.22958773374557495,
				0.32325947284698486,
				0.3265392482280731,
				0.1568363904953003,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 243066450,
			"isDeleted": false,
			"id": "L6Lx7jiJBwCFwWPDOVtZJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 581.7232732952086,
			"y": 280.67602138850935,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.165635318505565,
			"height": 9.632632016583727,
			"seed": 607188224,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5666254127402226,
					0
				],
				[
					1.6998762382206678,
					-0.5666254127402226
				],
				[
					2.833127063701113,
					-1.6998762382206678
				],
				[
					4.533003301921781,
					-3.966377889181558
				],
				[
					4.533003301921781,
					-5.666254127402226
				],
				[
					2.833127063701113,
					-6.232879540142449
				],
				[
					1.1332508254804452,
					-5.099628714662003
				],
				[
					-0.5666254127402226,
					-2.2665016509608904
				],
				[
					-1.1332508254804452,
					1.1332508254804452
				],
				[
					0.5666254127402226,
					3.3997524764412788
				],
				[
					3.966377889181558,
					3.3997524764412788
				],
				[
					6.799504952882671,
					1.6998762382206678
				],
				[
					6.799504952882671,
					0
				],
				[
					6.799504952882671,
					0.5666254127402226
				],
				[
					7.366130365622894,
					2.2665016509608336
				],
				[
					9.066006603843562,
					2.833127063701056
				],
				[
					11.899133667544675,
					1.1332508254804452
				],
				[
					13.03238449302512,
					-1.6998762382206678
				],
				[
					12.465759080284897,
					-3.966377889181558
				],
				[
					10.199257429324007,
					-5.099628714662003
				],
				[
					6.799504952882671,
					-2.2665016509608904
				],
				[
					6.799504952882671,
					-2.2665016509608904
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07280062884092331,
				0.09526290744543076,
				0.09823285043239594,
				0.11195654422044754,
				0.12013158947229385,
				0.1288815587759018,
				0.1324644237756729,
				0.13237524032592773,
				0.14445705711841583,
				0.15149161219596863,
				0.13904553651809692,
				0.09959899634122849,
				0.09770776331424713,
				0.12142208963632584,
				0.14254269003868103,
				0.13489016890525818,
				0.13412310183048248,
				0.14374643564224243,
				0.15414591133594513,
				0.17117737233638763,
				0.0056091309525072575,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1357438926,
			"isDeleted": false,
			"id": "w34q6O0LOLRN4ZnesiPZ5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 593.0557815500131,
			"y": 280.67602138850935,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.099628714662003,
			"height": 0.5666254127402226,
			"seed": 186774784,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5666254127402226,
					0.5666254127402226
				],
				[
					1.6998762382206678,
					0.5666254127402226
				],
				[
					4.533003301921781,
					0.5666254127402226
				],
				[
					5.099628714662003,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1145159900188446,
				0.07388800382614136,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 913329170,
			"isDeleted": false,
			"id": "ho94BDUcxsrECYDXv7Oco",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 602.1217881538565,
			"y": 274.4431418483669,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.533003301921667,
			"height": 7.932755778363116,
			"seed": 2019964160,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5666254127402226,
					0
				],
				[
					-1.1332508254804452,
					0
				],
				[
					-1.6998762382205541,
					0
				],
				[
					-2.8331270637009993,
					0.5666254127402226
				],
				[
					-2.2665016509607767,
					1.6998762382206678
				],
				[
					0,
					3.966377889181558
				],
				[
					1.1332508254804452,
					6.232879540142449
				],
				[
					0,
					7.932755778363116
				],
				[
					-2.8331270637009993,
					6.799504952882671
				],
				[
					-3.399752476441222,
					6.799504952882671
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08370999246835709,
				0.1251019835472107,
				0.16095322370529175,
				0.16231301426887512,
				0.13205066323280334,
				0.14710479974746704,
				0.16006451845169067,
				0.011527160182595253,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1620555278,
			"isDeleted": false,
			"id": "dbCuvOySeCH8LJXv3lliv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 607.2214168685185,
			"y": 275.57639267384735,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.232879540142449,
			"height": 4.533003301921781,
			"seed": 643740928,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5666254127402226
				],
				[
					2.2665016509608904,
					2.2665016509608904
				],
				[
					5.666254127402226,
					3.966377889181558
				],
				[
					6.232879540142449,
					4.533003301921781
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12622500956058502,
				0.1508522629737854,
				0.05473104864358902,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1584462290,
			"isDeleted": false,
			"id": "amqLYW5HR58lap8FffVVy",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 615.7207980596219,
			"y": 275.57639267384735,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.666254127402226,
			"height": 15.298886143985953,
			"seed": 789771520,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5666254127402226,
					0.5666254127402226
				],
				[
					-2.833127063701113,
					4.533003301921781
				],
				[
					-5.666254127402226,
					13.032384493025063
				],
				[
					-5.099628714662003,
					15.298886143985953
				],
				[
					-4.533003301921781,
					14.73226073124573
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13386498391628265,
				0.2650440037250519,
				0.3017919957637787,
				0.03683023154735565,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 949077070,
			"isDeleted": false,
			"id": "H2vfOxI6Le0kNDWNP0SMt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 632.1529350290882,
			"y": 268.2102623082245,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.599009905765342,
			"height": 14.73226073124573,
			"seed": 82351360,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.6998762382206678
				],
				[
					1.6998762382206678,
					7.366130365622837
				],
				[
					2.833127063701113,
					10.765882842064173
				],
				[
					1.1332508254804452,
					7.366130365622837
				],
				[
					-0.5666254127402226,
					2.833127063701113
				],
				[
					-1.6998762382206678,
					-0.5666254127402226
				],
				[
					-2.2665016509608904,
					-2.833127063701113
				],
				[
					-1.6998762382206678,
					-3.3997524764413356
				],
				[
					1.1332508254804452,
					-3.3997524764413356
				],
				[
					5.666254127402226,
					-2.2665016509608904
				],
				[
					7.932755778363116,
					0
				],
				[
					7.932755778363116,
					2.2665016509608904
				],
				[
					6.232879540142449,
					3.3997524764412788
				],
				[
					5.099628714662003,
					3.3997524764412788
				],
				[
					5.666254127402226,
					3.3997524764412788
				],
				[
					8.499381191103339,
					4.533003301921724
				],
				[
					10.76588284206423,
					6.799504952882614
				],
				[
					11.332508254804452,
					9.066006603843505
				],
				[
					9.066006603843562,
					10.765882842064173
				],
				[
					5.099628714662003,
					11.332508254804395
				],
				[
					2.833127063701113,
					9.632632016583727
				],
				[
					3.3997524764413356,
					9.066006603843505
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09564346075057983,
				0.11150936782360077,
				0.11578042805194855,
				0.04238760471343994,
				0.032192811369895935,
				0.04501467943191528,
				0.07913943380117416,
				0.11518976092338562,
				0.1493251621723175,
				0.1777612566947937,
				0.18101122975349426,
				0.17035043239593506,
				0.15408608317375183,
				0.13565954566001892,
				0.1203986182808876,
				0.13792037963867188,
				0.16275176405906677,
				0.19736908376216888,
				0.21651144325733185,
				0.19578155875205994,
				0.016169250011444092,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 630583186,
			"isDeleted": false,
			"id": "Ao98gUmN9b2Ipv01pht0w",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 645.7519449348536,
			"y": 272.74326561014624,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.7995049528825575,
			"height": 6.799504952882614,
			"seed": 251237632,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5666254127402226,
					0.5666254127402226
				],
				[
					-1.1332508254804452,
					0.5666254127402226
				],
				[
					-1.6998762382206678,
					1.1332508254804452
				],
				[
					-1.6998762382206678,
					3.3997524764413356
				],
				[
					-0.5666254127402226,
					5.099628714662003
				],
				[
					2.2665016509607767,
					5.099628714662003
				],
				[
					5.09962871466189,
					2.2665016509608904
				],
				[
					5.09962871466189,
					-0.5666254127402226
				],
				[
					2.8331270637009993,
					-1.699876238220611
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
				0.07765600830316544,
				0.0899219959974289,
				0.11616799980401993,
				0.18438400328159332,
				0.22658562660217285,
				0.234726682305336,
				0.2082466185092926,
				0.19291095435619354,
				0.15886938571929932,
				0.005630004685372114,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 447744654,
			"isDeleted": false,
			"id": "yijcbvOqk57g12hgczhTD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 648.0184465858143,
			"y": 275.57639267384735,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.533003301921781,
			"height": 0.5666254127402226,
			"seed": 1260442880,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5666254127402226,
					0
				],
				[
					1.6998762382206678,
					0.5666254127402226
				],
				[
					3.966377889181558,
					0.5666254127402226
				],
				[
					4.533003301921781,
					0.5666254127402226
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11052200198173523,
				0.06680916994810104,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 806759762,
			"isDeleted": false,
			"id": "tHhoRYzFv1MBu9OjZSCk8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 656.5178277769177,
			"y": 271.0433893719256,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.799504952882671,
			"height": 6.232879540142392,
			"seed": 599594240,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5666254127402226,
					0
				],
				[
					-2.2665016509608904,
					1.699876238220611
				],
				[
					-3.3997524764413356,
					4.533003301921724
				],
				[
					-1.1332508254804452,
					6.232879540142392
				],
				[
					2.2665016509608904,
					5.666254127402169
				],
				[
					3.3997524764413356,
					5.099628714661947
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11505978554487228,
				0.18149951100349426,
				0.23586858808994293,
				0.17808876931667328,
				0.014698456041514874,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 631998670,
			"isDeleted": false,
			"id": "cvKpssVO6pptSwHi9yHJ9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 660.4842056660992,
			"y": 261.97738276808207,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.232879540142449,
			"height": 14.73226073124573,
			"seed": 1972901120,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5666254127402226,
					0
				],
				[
					-0.5666254127402226,
					0.5666254127402226
				],
				[
					0.5666254127402226,
					4.533003301921781
				],
				[
					1.1332508254804452,
					9.632632016583727
				],
				[
					1.1332508254804452,
					14.165635318505508
				],
				[
					0.5666254127402226,
					14.73226073124573
				],
				[
					1.1332508254804452,
					11.899133667544618
				],
				[
					2.833127063701113,
					7.932755778363116
				],
				[
					5.099628714662003,
					6.232879540142449
				],
				[
					5.666254127402226,
					6.232879540142449
				],
				[
					5.666254127402226,
					7.932755778363116
				],
				[
					5.666254127402226,
					7.932755778363116
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.14938226342201233,
				0.16732625663280487,
				0.18450497090816498,
				0.17706643044948578,
				0.1575118452310562,
				0.11497613787651062,
				0.12391424924135208,
				0.13601885735988617,
				0.11609844863414764,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 55096082,
			"isDeleted": false,
			"id": "8dQ5I0Cf02pVgv53cPdwz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 662.1840819043199,
			"y": 274.4431418483669,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.533003301921781,
			"height": 2.833127063701113,
			"seed": 1113543936,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5666254127402226,
					1.1332508254804452
				],
				[
					1.1332508254804452,
					1.6998762382206678
				],
				[
					3.966377889181558,
					2.833127063701113
				],
				[
					4.533003301921781,
					2.833127063701113
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09310067445039749,
				0.15170998871326447,
				0.04795370623469353,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 958217998,
			"isDeleted": false,
			"id": "Kgdcs_FvEpGUUfqL6SCjR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 670.116837682683,
			"y": 259.144255704381,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.932755778363003,
			"height": 16.43213696946634,
			"seed": 974886144,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5666254127402226,
					0
				],
				[
					1.6998762382205541,
					5.666254127402169
				],
				[
					2.8331270637009993,
					13.032384493025006
				],
				[
					2.8331270637009993,
					15.298886143985897
				],
				[
					2.8331270637009993,
					13.599009905765229
				],
				[
					4.533003301921667,
					9.066006603843505
				],
				[
					6.7995049528825575,
					7.366130365622837
				],
				[
					7.36613036562278,
					10.765882842064173
				],
				[
					6.7995049528825575,
					15.86551155672612
				],
				[
					6.232879540142335,
					16.43213696946634
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15215304493904114,
				0.19164666533470154,
				0.17777639627456665,
				0.08031878620386124,
				0.028642425313591957,
				0.09225451946258545,
				0.19184307754039764,
				0.023821135982871056,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1638170834,
			"isDeleted": false,
			"id": "ydYPx_FGJ6uZsixr52_sr",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 679.7494696992667,
			"y": 272.176640197406,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.232879540142449,
			"height": 6.232879540142392,
			"seed": 1325667584,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5666254127402226,
					0.5666254127402226
				],
				[
					-1.1332508254804452,
					2.2665016509608904
				],
				[
					-1.1332508254804452,
					2.833127063701113
				],
				[
					0,
					2.833127063701113
				],
				[
					2.2665016509608904,
					2.833127063701113
				],
				[
					3.966377889181558,
					0.5666254127402226
				],
				[
					4.533003301921781,
					-2.2665016509608336
				],
				[
					2.2665016509608904,
					-3.3997524764412788
				],
				[
					-1.6998762382206678,
					-1.699876238220611
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
				0.08442343026399612,
				0.1384952962398529,
				0.13333916664123535,
				0.13122957944869995,
				0.15681158006191254,
				0.2106291800737381,
				0.22802932560443878,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1501441358,
			"isDeleted": false,
			"id": "LJBPXOZJKxScOFGN0-t8J",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 682.0159713502276,
			"y": 273.30989102288646,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.533003301921781,
			"height": 1.1332508254804452,
			"seed": 1389491456,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5666254127402226,
					0
				],
				[
					1.1332508254804452,
					0.5666254127402226
				],
				[
					2.2665016509608904,
					0.5666254127402226
				],
				[
					3.966377889181558,
					1.1332508254804452
				],
				[
					4.533003301921781,
					1.1332508254804452
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.009999999776482582,
				0.1398412436246872,
				0.10923019051551819,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 650155666,
			"isDeleted": false,
			"id": "Gd_uWk_CdKC5cJXr622JC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 688.8154763031102,
			"y": 269.34351313370496,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.666254127402226,
			"height": 7.366130365622837,
			"seed": 629642496,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5666254127402226,
					0.5666254127402226
				],
				[
					-0.5666254127402226,
					1.6998762382206678
				],
				[
					0.5666254127402226,
					3.9663778891815014
				],
				[
					3.966377889181558,
					3.9663778891815014
				],
				[
					5.099628714662003,
					0
				],
				[
					3.966377889181558,
					-2.833127063701113
				],
				[
					3.3997524764413356,
					-3.3997524764413356
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08273544162511826,
				0.17380797863006592,
				0.23238399624824524,
				0.23842786252498627,
				0.2074301391839981,
				0.052863892167806625,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 338121614,
			"isDeleted": false,
			"id": "erl8D2NvYbrIugu-n8RAg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 699.5813591451744,
			"y": 254.61125240245923,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.5666254127402226,
			"height": 20.965140271388123,
			"seed": 1976038656,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5666254127402226
				],
				[
					0,
					1.1332508254804452
				],
				[
					0.5666254127402226,
					9.632632016583727
				],
				[
					0.5666254127402226,
					18.698638620427232
				],
				[
					0.5666254127402226,
					20.3985148586479
				],
				[
					0.5666254127402226,
					19.831889445907677
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12593600153923035,
				0.19948400557041168,
				0.2911180257797241,
				0.341158002614975,
				0.1312226504087448,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 592704594,
			"isDeleted": false,
			"id": "4S5K984N0W_FFbMCNH895",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 718.8466231783418,
			"y": 254.044626989719,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.932755778363003,
			"height": 28.331270637011016,
			"seed": 1724052736,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5666254127402226
				],
				[
					-1.1332508254803315,
					2.833127063701113
				],
				[
					-1.6998762382205541,
					5.666254127402169
				],
				[
					-4.533003301921667,
					14.73226073124573
				],
				[
					-7.932755778363003,
					24.93151816056968
				],
				[
					-7.36613036562278,
					28.331270637011016
				],
				[
					-7.36613036562278,
					27.764645224270794
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08621899783611298,
				0.19933700561523438,
				0.26559150218963623,
				0.3260819911956787,
				0.3408762216567993,
				0.0839872732758522,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1666298318,
			"isDeleted": false,
			"id": "cpIGnQ3mPYTECaooeU6kS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 719.413248591082,
			"y": 269.34351313370496,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.366130365622894,
			"height": 16.998762382206564,
			"seed": 1798788352,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5666254127402226,
					0.5666254127402226
				],
				[
					1.6998762382206678,
					2.833127063701056
				],
				[
					3.966377889181558,
					10.19925742932395
				],
				[
					3.966377889181558,
					15.86551155672612
				],
				[
					2.2665016509608904,
					16.998762382206564
				],
				[
					-0.5666254127402226,
					13.032384493025063
				],
				[
					0,
					5.099628714661947
				],
				[
					4.533003301921781,
					0
				],
				[
					6.799504952882671,
					1.6998762382206678
				],
				[
					6.232879540142449,
					5.666254127402169
				],
				[
					4.533003301921781,
					8.499381191103282
				],
				[
					4.533003301921781,
					8.499381191103282
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09150848537683487,
				0.13710173964500427,
				0.16599297523498535,
				0.163511261343956,
				0.09524652361869812,
				0.020919494330883026,
				0.06469375640153885,
				0.16749945282936096,
				0.1965557187795639,
				0.037561796605587006,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 2033555986,
			"isDeleted": false,
			"id": "QUjUokEY47Pz7aB5y0xuN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 728.4792551949256,
			"y": 270.4767639591854,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.366130365622894,
			"height": 7.366130365622837,
			"seed": 877565184,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5666254127402226,
					0
				],
				[
					-0.5666254127402226,
					1.1332508254803884
				],
				[
					-1.1332508254804452,
					2.2665016509608336
				],
				[
					0.5666254127402226,
					5.099628714661947
				],
				[
					3.966377889181558,
					5.666254127402169
				],
				[
					5.666254127402226,
					2.833127063701056
				],
				[
					4.533003301921781,
					-1.1332508254804452
				],
				[
					0.5666254127402226,
					-1.6998762382206678
				],
				[
					-1.6998762382206678,
					2.2665016509608336
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
				0.09885397553443909,
				0.13727599382400513,
				0.17904825508594513,
				0.17547735571861267,
				0.1561451405286789,
				0.11404617130756378,
				0.1283712536096573,
				0.007523376494646072,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 303450126,
			"isDeleted": false,
			"id": "wXuYZ2PHNYqHqEOhncQUd",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 735.2787601478083,
			"y": 269.34351313370496,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.199257429323893,
			"height": 6.232879540142392,
			"seed": 1460434176,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5666254127402226,
					0
				],
				[
					-1.1332508254804452,
					0
				],
				[
					-1.6998762382206678,
					1.6998762382206678
				],
				[
					-0.5666254127402226,
					4.533003301921724
				],
				[
					1.1332508254804452,
					4.533003301921724
				],
				[
					2.833127063701113,
					1.1332508254804452
				],
				[
					2.833127063701113,
					-0.5666254127402226
				],
				[
					2.2665016509608904,
					1.1332508254804452
				],
				[
					2.833127063701113,
					4.533003301921724
				],
				[
					5.666254127402226,
					5.666254127402169
				],
				[
					7.932755778363003,
					2.833127063701056
				],
				[
					8.499381191103225,
					-0.5666254127402226
				],
				[
					6.7995049528825575,
					-0.5666254127402226
				],
				[
					6.7995049528825575,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11327999830245972,
				0.15798956155776978,
				0.1724323183298111,
				0.15968042612075806,
				0.11200512945652008,
				0.1055111363530159,
				0.12548208236694336,
				0.14253011345863342,
				0.15706607699394226,
				0.17350171506404877,
				0.12466790527105331,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 2002552786,
			"isDeleted": false,
			"id": "LJ_tTx1v6HzHVswputCm1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 747.1778938153528,
			"y": 269.9101385464452,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.099628714662003,
			"height": 7.366130365622837,
			"seed": 1963095296,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5666254127402226
				],
				[
					0.5666254127402226,
					-1.1332508254804452
				],
				[
					0.5666254127402226,
					-2.833127063701113
				],
				[
					-0.5666254127402226,
					-3.3997524764413356
				],
				[
					-2.833127063701113,
					-1.1332508254804452
				],
				[
					-3.3997524764413356,
					2.833127063701056
				],
				[
					1.6998762382206678,
					3.9663778891815014
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
				0.059521421790122986,
				0.09164437651634216,
				0.11940295249223709,
				0.14515405893325806,
				0.18311111629009247,
				0.20713765919208527,
				0.015709534287452698,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 544085582,
			"isDeleted": false,
			"id": "AWCHfZTLXM_SIix-to34Y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 750.5776462917942,
			"y": 267.07701148274407,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.499381191103339,
			"height": 8.499381191103282,
			"seed": 1880462592,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5666254127402226
				],
				[
					0,
					1.1332508254804452
				],
				[
					0,
					2.2665016509608904
				],
				[
					0.5666254127402226,
					6.232879540142392
				],
				[
					1.6998762382206678,
					7.366130365622837
				],
				[
					2.2665016509608904,
					5.666254127402169
				],
				[
					3.3997524764413356,
					2.2665016509608904
				],
				[
					5.666254127402226,
					-0.5666254127402226
				],
				[
					7.932755778363116,
					-1.1332508254804452
				],
				[
					8.499381191103339,
					-1.1332508254804452
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10644937306642532,
				0.12510095536708832,
				0.19824370741844177,
				0.18833334743976593,
				0.15357434749603271,
				0.13903217017650604,
				0.18962012231349945,
				0.10491671413183212,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 1977597330,
			"isDeleted": false,
			"id": "NkP-obyBrqMHih1KR259H",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 684.2481108363705,
			"y": 226.71314427791384,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 29.445699097974284,
			"height": 3.0672603227056356,
			"seed": 503190784,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.613452064541093,
					-0.6134520645411214
				],
				[
					4.2941644517878785,
					-0.6134520645411214
				],
				[
					14.109397484446049,
					-1.8403561936233928
				],
				[
					23.924630517104106,
					-3.0672603227056356
				],
				[
					28.218794968891984,
					-3.0672603227056356
				],
				[
					28.218794968891984,
					-2.453808258164514
				],
				[
					28.83224703343319,
					-1.8403561936233928
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08327841013669968,
				0.2123088389635086,
				0.2557052671909332,
				0.26231756806373596,
				0.21908187866210938,
				0.03420398011803627,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 657595534,
			"isDeleted": false,
			"id": "9GvrLBLdMRRxaAclPCGkr",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 729.6435636124141,
			"y": 221.1920756970437,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.42868509719915,
			"height": 6.747972709952421,
			"seed": 753825024,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.613452064541093,
					0
				],
				[
					-1.2269041290822997,
					0
				],
				[
					-1.840356193623279,
					0
				],
				[
					2.453808258164486,
					0.6134520645411214
				],
				[
					6.747972709952478,
					1.8403561936233928
				],
				[
					8.58832890357587,
					3.680712387246757
				],
				[
					6.747972709952478,
					4.907616516329028
				],
				[
					2.453808258164486,
					6.1345206454113
				],
				[
					0,
					6.747972709952421
				],
				[
					1.2269041290822997,
					6.1345206454113
				],
				[
					2.453808258164486,
					6.1345206454113
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.04520193487405777,
				0.16473068296909332,
				0.21052449941635132,
				0.22023709118366241,
				0.2229168713092804,
				0.2450360357761383,
				0.27153223752975464,
				0.25994086265563965,
				0.06426800787448883,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 838220626,
			"isDeleted": false,
			"id": "GxSJoQDnKbpdugm0bhQkI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 775.6524684529988,
			"y": 208.30958234167994,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.226904129082186,
			"height": 12.88249335536372,
			"seed": 903894272,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1.226904129082243
				],
				[
					-0.6134520645409793,
					-1.8403561936233643
				],
				[
					0,
					2.4538082581645426
				],
				[
					0.6134520645412067,
					7.9748768390346925
				],
				[
					0,
					11.042137161740357
				],
				[
					0,
					10.428685097199207
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09525223076343536,
				0.2570800185203552,
				0.2692417502403259,
				0.048669006675481796,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1008425678,
			"isDeleted": false,
			"id": "3f9sWDXbudpeB6Mpu95hq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 770.7448519366699,
			"y": 223.6458839552082,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.361424774493571,
			"height": 6.747972709952421,
			"seed": 1081824512,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6134520645411214
				],
				[
					0.6134520645412067,
					0.6134520645411214
				],
				[
					2.4538082581645995,
					4.294164451787907
				],
				[
					4.907616516328972,
					6.1345206454113
				],
				[
					6.134520645411271,
					3.6807123872467855
				],
				[
					6.747972709952364,
					0.6134520645411214
				],
				[
					6.747972709952364,
					0
				],
				[
					7.361424774493571,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.052626799792051315,
				0.15807199478149414,
				0.21628998219966888,
				0.2084612399339676,
				0.1758592575788498,
				0.1159178763628006,
				0.02514004521071911,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 704053522,
			"isDeleted": false,
			"id": "IPI6CNdbKTI3ngY1Sml-g",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 789.1484138729038,
			"y": 213.217198858009,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.58832890357587,
			"height": 15.949753678069385,
			"seed": 1950684416,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6134520645411499
				],
				[
					0.613452064541093,
					0
				],
				[
					0.613452064541093,
					1.226904129082243
				],
				[
					1.226904129082186,
					7.9748768390346925
				],
				[
					1.226904129082186,
					11.65558922628145
				],
				[
					-0.6134520645412067,
					9.815233032658085
				],
				[
					-3.0672603227056925,
					8.588328903575814
				],
				[
					-5.521068580870178,
					9.815233032658085
				],
				[
					-6.747972709952478,
					12.88249335536372
				],
				[
					-4.907616516329085,
					15.336301613528235
				],
				[
					-1.8403561936233928,
					15.336301613528235
				],
				[
					1.8403561936233928,
					14.722849548987114
				],
				[
					1.8403561936233928,
					14.722849548987114
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06776068359613419,
				0.10130584985017776,
				0.149187371134758,
				0.19603554904460907,
				0.1887543648481369,
				0.09329507499933243,
				0.08785833418369293,
				0.1446102261543274,
				0.16978341341018677,
				0.17386868596076965,
				0.12822988629341125,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1438830862,
			"isDeleted": false,
			"id": "AHw9S-vms2JjZaHMKhtvm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 793.4425783246917,
			"y": 226.09969221337272,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.815233032658057,
			"height": 7.9748768390346925,
			"seed": 469349632,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.613452064541093,
					0
				],
				[
					1.2269041290822997,
					-0.6134520645411214
				],
				[
					2.453808258164486,
					-1.2269041290822713
				],
				[
					2.453808258164486,
					-2.453808258164514
				],
				[
					-1.2269041290822997,
					-2.453808258164514
				],
				[
					-3.6807123872467855,
					0
				],
				[
					-3.0672603227056925,
					3.067260322705664
				],
				[
					-0.613452064541093,
					4.294164451787907
				],
				[
					2.453808258164486,
					2.453808258164514
				],
				[
					4.907616516329085,
					-0.6134520645411214
				],
				[
					6.134520645411271,
					-1.8403561936233928
				],
				[
					6.134520645411271,
					1.8403561936233928
				],
				[
					4.907616516329085,
					4.907616516329028
				],
				[
					4.907616516329085,
					5.521068580870178
				],
				[
					4.907616516329085,
					5.521068580870178
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.05643194541335106,
				0.11103210598230362,
				0.12787975370883942,
				0.13635452091693878,
				0.19038128852844238,
				0.24102075397968292,
				0.21771767735481262,
				0.14644427597522736,
				0.1141224056482315,
				0.15826064348220825,
				0.22230325639247894,
				0.20021721720695496,
				0.02904769964516163,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 2035879634,
			"isDeleted": false,
			"id": "ALsbxvmKWN1LKZVLXASQC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 806.3250716800554,
			"y": 225.4862401488316,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.6807123872467855,
			"height": 8.588328903575814,
			"seed": 1504777472,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6134520645411499
				],
				[
					-1.2269041290822997,
					-1.2269041290822713
				],
				[
					-1.8403561936233928,
					-1.8403561936233928
				],
				[
					-3.0672603227056925,
					-1.2269041290822713
				],
				[
					-3.0672603227056925,
					1.226904129082243
				],
				[
					-1.8403561936233928,
					3.6807123872467855
				],
				[
					-1.8403561936233928,
					5.52106858087015
				],
				[
					-3.0672603227056925,
					6.747972709952421
				],
				[
					-3.6807123872467855,
					6.747972709952421
				],
				[
					-3.6807123872467855,
					5.52106858087015
				],
				[
					-2.453808258164486,
					4.294164451787907
				],
				[
					-0.613452064541093,
					3.6807123872467855
				],
				[
					0,
					3.0672603227056356
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
				0.08831054717302322,
				0.13978418707847595,
				0.18688097596168518,
				0.18093957006931305,
				0.17490997910499573,
				0.17322222888469696,
				0.19508673250675201,
				0.19747231900691986,
				0.11676779389381409,
				0.06449850648641586,
				0.04136260971426964,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 799113038,
			"isDeleted": false,
			"id": "val7ahTz5y5aghkMeoCsW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 811.2326881963845,
			"y": 224.87278808429045,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6134520645409793,
			"height": 6.74797270995245,
			"seed": 1992062208,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					3.067260322705664
				],
				[
					0,
					6.74797270995245
				],
				[
					0.6134520645409793,
					6.74797270995245
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2189599871635437,
				0.04153900220990181,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 884171922,
			"isDeleted": false,
			"id": "yk178AtakZM8cdkNXoT9r",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 811.2326881963845,
			"y": 219.96517156796142,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6134520645412067,
			"height": 1.2269041290822713,
			"seed": 156456192,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6134520645412067,
					-0.6134520645411214
				],
				[
					-0.6134520645412067,
					-1.2269041290822713
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
				0.10888299345970154,
				0.15576599538326263,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 772826510,
			"isDeleted": false,
			"id": "MGmy_2Z1VLuhnS5GvE-rQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 816.7537567772547,
			"y": 213.217198858009,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.8403561936233928,
			"height": 19.63046606531617,
			"seed": 974099712,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6134520645411499
				],
				[
					0,
					-1.2269041290822713
				],
				[
					1.226904129082186,
					3.0672603227056356
				],
				[
					1.8403561936233928,
					11.042137161740328
				],
				[
					0.6134520645409793,
					17.79010987169275
				],
				[
					0,
					18.4035619362339
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.035508543252944946,
				0.1798017919063568,
				0.1963777393102646,
				0.04875592142343521,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1170014802,
			"isDeleted": false,
			"id": "UXpOUmJITfirlfUuZgGPm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 812.4595923254667,
			"y": 225.4862401488316,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.747972709952364,
			"height": 1.8403561936233928,
			"seed": 829068544,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6134520645412067,
					0
				],
				[
					1.8403561936233928,
					0
				],
				[
					6.134520645411385,
					1.226904129082243
				],
				[
					6.747972709952364,
					1.8403561936233928
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09938998520374298,
				0.06310214102268219,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1112048590,
			"isDeleted": false,
			"id": "ESAG3bhFRR3wfAJ_Vcb0u",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 822.8882774226659,
			"y": 226.71314427791384,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.361424774493571,
			"height": 1.8403561936233928,
			"seed": 934728960,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6134520645412067,
					0
				],
				[
					1.8403561936233928,
					1.2269041290822713
				],
				[
					6.747972709952592,
					1.8403561936233928
				],
				[
					7.361424774493571,
					1.2269041290822713
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.049514494836330414,
				0.01669485494494438,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1196222482,
			"isDeleted": false,
			"id": "-j_MmIc1_reMjtcL3eSx0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 831.4766063262418,
			"y": 225.4862401488316,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.88249335536375,
			"height": 19.630466065316142,
			"seed": 668144896,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6134520645412067,
					0
				],
				[
					-1.2269041290824134,
					0.6134520645411214
				],
				[
					-4.294164451787992,
					4.907616516329028
				],
				[
					-12.26904129082277,
					19.01701400077502
				],
				[
					-12.88249335536375,
					19.630466065316142
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.028359223157167435,
				0.11166799813508987,
				0.22706198692321777,
				0.14544840157032013,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1315101198,
			"isDeleted": false,
			"id": "jNzsIuuG4SEZHo81LQ0YV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 759.7027147749295,
			"y": 278.8565697639099,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.42868509719915,
			"height": 0,
			"seed": 2097984768,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6134520645412067,
					0
				],
				[
					1.8403561936233928,
					0
				],
				[
					4.907616516328972,
					0
				],
				[
					10.42868509719915,
					0
				],
				[
					10.42868509719915,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09707171469926834,
				0.15724971890449524,
				0.2064480036497116,
				0.05079611390829086,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1633293778,
			"isDeleted": false,
			"id": "g1RnHNYlj2iWRA-8QrxVO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 773.8121122593755,
			"y": 274.562405312122,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.201780968116964,
			"height": 7.974876839034721,
			"seed": 1633309952,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6134520645411499
				],
				[
					2.4538082581645995,
					0
				],
				[
					6.747972709952478,
					1.8403561936233928
				],
				[
					9.201780968116964,
					4.2941644517878785
				],
				[
					8.58832890357587,
					6.134520645411271
				],
				[
					6.134520645411385,
					6.747972709952421
				],
				[
					3.6807123872467855,
					6.747972709952421
				],
				[
					3.0672603227056925,
					6.747972709952421
				],
				[
					3.0672603227056925,
					7.361424774493571
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07664819061756134,
				0.2494799792766571,
				0.2889559864997864,
				0.2518884837627411,
				0.2661890685558319,
				0.32647836208343506,
				0.33740198612213135,
				0.1392190009355545,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 156788814,
			"isDeleted": false,
			"id": "nWlOkt8jnpq35scP1wcXq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 789.7514442989182,
			"y": 272.16024691553,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.973932464303402,
			"height": 10.777895626650775,
			"seed": 2132374784,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.2679877207824575
				],
				[
					0.6339938603912287,
					3.1699693019561437
				],
				[
					1.9019815811736862,
					8.875914045477145
				],
				[
					1.9019815811736862,
					9.509907905868374
				],
				[
					2.535975441564915,
					5.071950883129773
				],
				[
					3.8039631623473724,
					1.2679877207824575
				],
				[
					5.705944743521059,
					1.9019815811736862
				],
				[
					6.339938603912174,
					6.973932464303459
				],
				[
					6.973932464303402,
					10.777895626650775
				],
				[
					6.339938603912174,
					10.777895626650775
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14046569168567657,
				0.14870037138462067,
				0.1341637223958969,
				0.10301586985588074,
				0.05744924768805504,
				0.060823243111371994,
				0.12292837351560593,
				0.1668730229139328,
				0.15314559638500214,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 620465042,
			"isDeleted": false,
			"id": "uS2_iSbLM52nxWz9HghGo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 787.8494627177445,
			"y": 262.0163451492705,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.1699693019561437,
			"height": 24.091766694866465,
			"seed": 1647441152,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.2679877207824575
				],
				[
					1.9019815811736862,
					9.509907905868317
				],
				[
					2.535975441564915,
					20.287803532519092
				],
				[
					3.1699693019561437,
					24.091766694866465
				],
				[
					3.1699693019561437,
					24.091766694866465
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08630401641130447,
				0.15804651379585266,
				0.19348666071891785,
				0.03987365588545799,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1661087374,
			"isDeleted": false,
			"id": "m_mhTzpT2YwbUzZG9vY0M",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 796.7253767632216,
			"y": 275.33021621748617,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.973932464303402,
			"height": 8.875914045477089,
			"seed": 1088918784,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6339938603912287,
					0
				],
				[
					-0.6339938603912287,
					1.9019815811736294
				],
				[
					0.6339938603912287,
					5.705944743521002
				],
				[
					4.437957022738601,
					8.24192018508586
				],
				[
					6.339938603912174,
					6.3399386039122305
				],
				[
					6.339938603912174,
					1.9019815811736294
				],
				[
					3.8039631623473724,
					-0.6339938603912287
				],
				[
					0,
					0.6339938603911719
				],
				[
					0,
					5.705944743521002
				],
				[
					0.6339938603912287,
					5.705944743521002
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07380294799804688,
				0.13951458036899567,
				0.18695205450057983,
				0.1959814429283142,
				0.18433886766433716,
				0.1762576848268509,
				0.179071843624115,
				0.16578301787376404,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1751664978,
			"isDeleted": false,
			"id": "kyET3QvV381S0n770D8Yb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 803.0653153671337,
			"y": 278.50018551944225,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.07195088312983,
			"height": 3.1699693019561437,
			"seed": 63968512,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6339938603912287,
					0
				],
				[
					-0.6339938603912287,
					1.2679877207824575
				],
				[
					3.8039631623473724,
					3.1699693019561437
				],
				[
					4.437957022738601,
					3.1699693019561437
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07700400054454803,
				0.10147564858198166,
				0.05840035900473595,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1746480334,
			"isDeleted": false,
			"id": "lkuOuufYIYg_oJVx8P8aa",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 808.1372662502636,
			"y": 274.69622235709494,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.705944743521059,
			"height": 10.143901766259546,
			"seed": 1610372352,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6339938603912287
				],
				[
					0,
					1.2679877207824006
				],
				[
					0,
					3.8039631623473156
				],
				[
					1.2679877207824575,
					7.607926324694631
				],
				[
					1.9019815811736862,
					6.973932464303459
				],
				[
					3.8039631623473724,
					1.9019815811736294
				],
				[
					5.07195088312983,
					-1.9019815811736862
				],
				[
					5.705944743521059,
					-2.535975441564915
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.07345764338970184,
				0.12173043936491013,
				0.10899313539266586,
				0.09548486024141312,
				0.04722997918725014,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 586632978,
			"isDeleted": false,
			"id": "mn5rmlnZ_uxmb6Fpugblw",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 822.0851311788705,
			"y": 265.8203083116178,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.875914045476975,
			"height": 16.483840370171833,
			"seed": 1451627776,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6339938603912287
				],
				[
					0.6339938603912287,
					-1.2679877207824575
				],
				[
					0.6339938603912287,
					0.6339938603912287
				],
				[
					1.2679877207824575,
					3.8039631623473724
				],
				[
					1.2679877207824575,
					9.509907905868374
				],
				[
					1.9019815811736862,
					10.777895626650775
				],
				[
					0,
					10.143901766259546
				],
				[
					-3.16996930195603,
					9.509907905868374
				],
				[
					-5.071950883129716,
					12.045883347433232
				],
				[
					-3.8039631623472587,
					14.581858788998147
				],
				[
					0,
					15.215852649389376
				],
				[
					3.1699693019561437,
					14.581858788998147
				],
				[
					3.8039631623472587,
					13.947864928606919
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13257598876953125,
				0.16961801052093506,
				0.20136599242687225,
				0.21205191314220428,
				0.1708562970161438,
				0.10857705771923065,
				0.10872433334589005,
				0.1563078910112381,
				0.22540079057216644,
				0.23007138073444366,
				0.05623861774802208,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 64,
			"versionNonce": 641098510,
			"isDeleted": false,
			"id": "7gQ7aTz60n05HsNAp1n9R",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 844.2749162925633,
			"y": 211.93083017836386,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.215852649389376,
			"height": 72.27530008459937,
			"seed": 274380032,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6339938603912287
				],
				[
					1.2679877207824575,
					-1.9019815811736578
				],
				[
					5.705944743520945,
					0.6339938603912287
				],
				[
					9.509907905868317,
					5.705944743521002
				],
				[
					11.411889487042004,
					12.045883347433232
				],
				[
					10.777895626650775,
					18.385821951345463
				],
				[
					8.24192018508586,
					24.091766694866465
				],
				[
					5.071950883129716,
					29.797711438387466
				],
				[
					3.8039631623473724,
					34.86966232151724
				],
				[
					3.8039631623473724,
					36.771643902690926
				],
				[
					6.973932464303402,
					38.039631623473355
				],
				[
					10.143901766259546,
					38.039631623473355
				],
				[
					10.777895626650775,
					38.039631623473355
				],
				[
					8.875914045477089,
					38.67362548386458
				],
				[
					6.339938603912174,
					40.57560706503824
				],
				[
					5.705944743520945,
					43.74557636699436
				],
				[
					7.607926324694631,
					47.5495395293417
				],
				[
					10.143901766259546,
					51.35350269168907
				],
				[
					12.679877207824461,
					55.79145971442762
				],
				[
					14.581858788998147,
					60.86341059755739
				],
				[
					14.581858788998147,
					65.30136762029593
				],
				[
					12.045883347433232,
					69.1053307826433
				],
				[
					6.973932464303402,
					70.37331850342571
				],
				[
					1.2679877207824575,
					69.1053307826433
				],
				[
					-0.6339938603912287,
					68.47133692225208
				],
				[
					0,
					68.47133692225208
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10456686466932297,
				0.18149837851524353,
				0.24205224215984344,
				0.27985477447509766,
				0.28594687581062317,
				0.2940951883792877,
				0.30377525091171265,
				0.30658450722694397,
				0.30544236302375793,
				0.3099833130836487,
				0.29900890588760376,
				0.30086585879325867,
				0.316422700881958,
				0.3130624294281006,
				0.3207007944583893,
				0.3427276015281677,
				0.36020684242248535,
				0.3818667531013489,
				0.41384297609329224,
				0.43759095668792725,
				0.444636732339859,
				0.40769320726394653,
				0.29684364795684814,
				0.07627792656421661,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1226808530,
			"isDeleted": false,
			"id": "LoBHWmBQij25IA0xlE2Qn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 861.3927505231263,
			"y": 243.630523197925,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.24192018508586,
			"height": 11.411889487042004,
			"seed": 1544107264,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6339938603912003
				],
				[
					0,
					0.6339938603912287
				],
				[
					0.6339938603912287,
					5.705944743521002
				],
				[
					1.2679877207824575,
					10.777895626650803
				],
				[
					1.9019815811736862,
					6.3399386039122305
				],
				[
					4.437957022738601,
					1.2679877207824575
				],
				[
					8.24192018508586,
					0
				],
				[
					8.24192018508586,
					0.6339938603912287
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0570109561085701,
				0.09998355060815811,
				0.12335900962352753,
				0.13320715725421906,
				0.09599529951810837,
				0.12340081483125687,
				0.04753460735082626,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 265474382,
			"isDeleted": false,
			"id": "f2ehgXZbpdwuwd-8p_b8T",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 871.5366522893859,
			"y": 244.89851091870744,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.24192018508586,
			"height": 8.241920185085888,
			"seed": 1375401216,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6339938603912287,
					0.6339938603912287
				],
				[
					-1.2679877207824575,
					3.803963162347344
				],
				[
					-1.2679877207824575,
					5.705944743521002
				],
				[
					2.5359754415648013,
					8.241920185085888
				],
				[
					5.705944743520945,
					6.3399386039122305
				],
				[
					6.973932464303402,
					2.5359754415648865
				],
				[
					6.339938603912174,
					1.2679877207824575
				],
				[
					6.339938603912174,
					1.2679877207824575
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0561399832367897,
				0.08115749806165695,
				0.11783154308795929,
				0.12956854701042175,
				0.13718023896217346,
				0.14064590632915497,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 678965906,
			"isDeleted": false,
			"id": "sQHfkcyMMYzuNjnGhqydM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 881.0465601952542,
			"y": 243.630523197925,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.607926324694745,
			"height": 11.411889487042004,
			"seed": 1488762112,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6339938603912287
				],
				[
					0.6339938603912287,
					1.9019815811736862
				],
				[
					1.9019815811736862,
					6.973932464303459
				],
				[
					1.9019815811736862,
					10.143901766259575
				],
				[
					1.9019815811736862,
					7.607926324694688
				],
				[
					3.1699693019561437,
					1.9019815811736862
				],
				[
					6.973932464303516,
					-1.267987720782429
				],
				[
					7.607926324694745,
					-0.6339938603912003
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08917791396379471,
				0.12146227806806564,
				0.1445179134607315,
				0.15556804835796356,
				0.1267908364534378,
				0.13466638326644897,
				0.0669696033000946,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1615296398,
			"isDeleted": false,
			"id": "dv6ycFya4RdL7SqvyB-je",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 889.9224742407314,
			"y": 245.53250477909867,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.607926324694631,
			"height": 7.60792632469466,
			"seed": 743339264,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6339938603912287,
					1.9019815811736578
				],
				[
					-0.6339938603912287,
					3.1699693019561153
				],
				[
					-0.6339938603912287,
					4.437957022738544
				],
				[
					1.9019815811735725,
					5.071950883129773
				],
				[
					5.071950883129716,
					3.8039631623473156
				],
				[
					6.339938603912174,
					0.6339938603912287
				],
				[
					4.4379570227384875,
					-2.5359754415648865
				],
				[
					0,
					-2.5359754415648865
				],
				[
					-1.2679877207824575,
					-0.6339938603912287
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
				0.05197698995471001,
				0.08271017670631409,
				0.14650198817253113,
				0.1632850021123886,
				0.16270004212856293,
				0.20265011489391327,
				0.22139862179756165,
				0.13190233707427979,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1136136274,
			"isDeleted": false,
			"id": "Y4w9mtvRlKNpUMNPkMcVN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 894.3604312634699,
			"y": 248.7024740810548,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.607926324694631,
			"height": 3.1699693019561153,
			"seed": 960517376,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6339938603912287,
					0
				],
				[
					1.9019815811736862,
					0.6339938603912003
				],
				[
					5.071950883129716,
					1.267987720782429
				],
				[
					6.973932464303402,
					-1.2679877207824575
				],
				[
					7.607926324694631,
					-1.9019815811736862
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10940399020910263,
				0.15994711220264435,
				0.02839834615588188,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 2144163278,
			"isDeleted": false,
			"id": "tREEb5XmMfaMIQsXqASHi",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 903.236345308947,
			"y": 230.95064599010055,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.9019815811736862,
			"height": 22.823778974084007,
			"seed": 702674176,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6339938603912003
				],
				[
					-0.6339938603912287,
					1.9019815811736578
				],
				[
					-0.6339938603912287,
					8.241920185085888
				],
				[
					0,
					17.751828090954234
				],
				[
					1.2679877207824575,
					22.823778974084007
				],
				[
					1.2679877207824575,
					22.823778974084007
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08589398115873337,
				0.11385885626077652,
				0.2581459879875183,
				0.34862202405929565,
				0.13485360145568848,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 783693330,
			"isDeleted": false,
			"id": "4qe8G-SsP3ItOT4zz4tKD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 574.9123689245333,
			"y": 223.4238173888376,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.465362545513813,
			"height": 77.32681272756932,
			"seed": 1625093376,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1.0310241697009133
				],
				[
					0,
					-2.0620483394018265
				],
				[
					-1.0310241697009133,
					-4.124096678803653
				],
				[
					-6.186145018205593,
					-3.09307250910274
				],
				[
					-11.34126586671016,
					4.12409667880371
				],
				[
					-12.372290036411073,
					12.37229003641113
				],
				[
					-10.310241697009246,
					20.620483394018493
				],
				[
					-6.186145018205593,
					26.80662841222403
				],
				[
					-4.124096678803653,
					31.961749260728652
				],
				[
					-5.15512084850468,
					35.05482176983142
				],
				[
					-8.24819335760742,
					37.11687010923325
				],
				[
					-9.279217527308333,
					38.14789427893416
				],
				[
					-8.24819335760742,
					39.17891844863519
				],
				[
					-5.15512084850468,
					42.27199095773793
				],
				[
					-5.15512084850468,
					48.45813597594341
				],
				[
					-7.2171691879065065,
					55.67530516384991
				],
				[
					-8.24819335760742,
					62.89247435175642
				],
				[
					-6.186145018205593,
					69.0786193699619
				],
				[
					1.0310241697009133,
					72.17169187906475
				],
				[
					3.09307250910274,
					73.20271604876567
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.025175994262099266,
				0.10468258708715439,
				0.15868863463401794,
				0.19522155821323395,
				0.19807137548923492,
				0.21237915754318237,
				0.22204379737377167,
				0.2142297327518463,
				0.21913741528987885,
				0.23117254674434662,
				0.23745419085025787,
				0.2227737158536911,
				0.21579739451408386,
				0.2450847178697586,
				0.27126437425613403,
				0.29148900508880615,
				0.30476224422454834,
				0.2960914075374603,
				0.11399484425783157,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 66,
			"versionNonce": 1736272910,
			"isDeleted": false,
			"id": "26EFDVWfkkevICMsjPVyS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 611.551964517081,
			"y": 304.1227721366327,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 218.49312830791848,
			"height": 19.553859731837008,
			"seed": 39269632,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8501678144276639,
					0.8501678144276639
				],
				[
					-0.8501678144276639,
					3.400671257710769
				],
				[
					-0.8501678144276639,
					5.101006886566154
				],
				[
					0.8501678144276639,
					11.052181587560028
				],
				[
					4.250839072138433,
					17.00335628855396
				],
				[
					11.052181587560085,
					19.553859731837008
				],
				[
					19.553859731837065,
					18.703691917409344
				],
				[
					29.755873504969372,
					15.303020659698518
				],
				[
					41.658222906957235,
					11.902349401987749
				],
				[
					56.11107575222809,
					6.801342515421538
				],
				[
					68.01342515421584,
					4.25083907213849
				],
				[
					79.91577455620359,
					3.400671257710769
				],
				[
					90.96795614376367,
					4.25083907213849
				],
				[
					97.76929865918532,
					7.651510329849259
				],
				[
					102.02013773132376,
					10.202013773132364
				],
				[
					104.57064117460686,
					10.202013773132364
				],
				[
					107.12114461788997,
					7.651510329849259
				],
				[
					111.37198369002851,
					5.101006886566154
				],
				[
					120.72382964873316,
					3.400671257710769
				],
				[
					132.6261790507209,
					4.25083907213849
				],
				[
					143.678360638281,
					7.651510329849259
				],
				[
					154.73054222584108,
					12.75251721641547
				],
				[
					168.33322725668427,
					17.853524102981623
				],
				[
					185.33658354523823,
					19.553859731837008
				],
				[
					204.04027546264763,
					15.303020659698518
				],
				[
					215.94262486463538,
					5.9511747009938745
				],
				[
					217.64296049349082,
					2.5505034432830485
				],
				[
					216.79279267906304,
					2.5505034432830485
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0638163760304451,
				0.0842490866780281,
				0.11462243646383286,
				0.1328507363796234,
				0.136646568775177,
				0.13944031298160553,
				0.14195440709590912,
				0.16282619535923004,
				0.17820806801319122,
				0.19625970721244812,
				0.2160184383392334,
				0.22353698313236237,
				0.23138992488384247,
				0.23393948376178741,
				0.2109527587890625,
				0.19674991071224213,
				0.21027420461177826,
				0.23256899416446686,
				0.25025659799575806,
				0.26410192251205444,
				0.2737182676792145,
				0.29112836718559265,
				0.33252182602882385,
				0.3768424987792969,
				0.3386508822441101,
				0.07056313753128052,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1785308114,
			"isDeleted": false,
			"id": "QWv-Rp_6L3zg6_yE0HoSj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 704.4605154656381,
			"y": 333.0045526266292,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.882385035299421,
			"height": 15.152990387459226,
			"seed": 1939921664,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6588256690199614,
					0
				],
				[
					-2.6353026760798457,
					0.6588256690199614
				],
				[
					-3.9529540141197685,
					1.3176513380399797
				],
				[
					-5.929431021179653,
					4.611779683139787
				],
				[
					-7.247082359219576,
					9.882385035299535
				],
				[
					-5.270605352159691,
					14.494164718439265
				],
				[
					-1.3176513380399228,
					15.152990387459226
				],
				[
					1.9764770070598843,
					13.176513380399342
				],
				[
					2.6353026760798457,
					12.51768771137938
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10225533694028854,
				0.11979324370622635,
				0.17076687514781952,
				0.23488415777683258,
				0.2832237184047699,
				0.25448524951934814,
				0.07948599010705948,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 89176654,
			"isDeleted": false,
			"id": "DPrTe4Gqgqd1t2ouHe2tU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 711.7075978248578,
			"y": 343.5457633309487,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.9294310211797665,
			"height": 12.51768771137938,
			"seed": 1866447616,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6588256690199614,
					-1.3176513380399797
				],
				[
					1.9764770070598843,
					-4.611779683139787
				],
				[
					4.611779683139844,
					-10.541210704319496
				],
				[
					5.270605352159805,
					-5.270605352159748
				],
				[
					5.9294310211797665,
					0
				],
				[
					5.9294310211797665,
					1.9764770070598843
				],
				[
					5.270605352159805,
					1.3176513380399228
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16507400572299957,
				0.1778852790594101,
				0.1829572468996048,
				0.2447213977575302,
				0.2492597997188568,
				0.013818695209920406,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 40,
			"versionNonce": 1089034642,
			"isDeleted": false,
			"id": "d3Bm64U22IGRjouqhaCfK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 711.7075978248578,
			"y": 340.25163498584885,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.588256690199728,
			"height": 0,
			"seed": 2068142848,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6588256690199614,
					0
				],
				[
					5.270605352159805,
					0
				],
				[
					6.588256690199728,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1296519786119461,
				0.09779635816812515,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 538984590,
			"isDeleted": false,
			"id": "6D51xmu6i05IbaenZ4X_U",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 722.9076341981972,
			"y": 336.2986809717291,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3176513380399228,
			"height": 11.200036373339401,
			"seed": 1569487616,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6588256690199614
				],
				[
					0,
					1.9764770070598843
				],
				[
					0.6588256690199614,
					8.564733697259555
				],
				[
					1.3176513380399228,
					11.200036373339401
				],
				[
					1.3176513380399228,
					10.54121070431944
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08840981870889664,
				0.14123132824897766,
				0.018528686836361885,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 560748370,
			"isDeleted": false,
			"id": "2ELWEfJB-A-N62Cq5IaxJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 721.5899828601573,
			"y": 334.3222039646692,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.22355936627946,
			"height": 7.2470823592196325,
			"seed": 1249172224,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6588256690200183
				],
				[
					1.9764770070598843,
					-0.6588256690200183
				],
				[
					7.247082359219576,
					0
				],
				[
					9.22355936627946,
					2.6353026760798457
				],
				[
					5.929431021179653,
					5.270605352159691
				],
				[
					1.9764770070598843,
					6.588256690199614
				],
				[
					1.9764770070598843,
					6.588256690199614
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09908667206764221,
				0.20135800540447235,
				0.23831383883953094,
				0.24010363221168518,
				0.24608935415744781,
				0.07264990359544754,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1000668878,
			"isDeleted": false,
			"id": "SLVFqoEHYuep5zaqNNcfW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 735.4253219095765,
			"y": 336.2986809717291,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.564733697259499,
			"height": 12.517687711379324,
			"seed": 2008447744,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6588256690199614
				],
				[
					-0.6588256690199614,
					-0.6588256690199614
				],
				[
					-1.3176513380399228,
					0
				],
				[
					-3.294128345099807,
					5.270605352159691
				],
				[
					-3.294128345099807,
					9.882385035299478
				],
				[
					0,
					11.858862042359362
				],
				[
					3.9529540141197685,
					9.882385035299478
				],
				[
					5.270605352159691,
					6.588256690199671
				],
				[
					4.61177968313973,
					5.929431021179653
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1799039989709854,
				0.2302599847316742,
				0.26955127716064453,
				0.3244752585887909,
				0.31979691982269287,
				0.24474547803401947,
				0.014459991827607155,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 2085199122,
			"isDeleted": false,
			"id": "ll2wyCwxkhCZP3mbLOVj-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 735.4253219095765,
			"y": 339.5928093168289,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.9294310211797665,
			"height": 1.3176513380399228,
			"seed": 538532608,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6588256690199614
				],
				[
					0.6588256690199614,
					0.6588256690199614
				],
				[
					3.294128345099807,
					1.3176513380399228
				],
				[
					5.270605352159691,
					0.6588256690199614
				],
				[
					5.9294310211797665,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1764100044965744,
				0.23528149724006653,
				0.11464108526706696,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 2088236302,
			"isDeleted": false,
			"id": "hAYf-62T5bZarfH21UIDI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 734.7664962405565,
			"y": 336.2986809717291,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.223559366279574,
			"height": 0.6588256690199614,
			"seed": 910015232,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6588256690199614,
					0
				],
				[
					1.3176513380399228,
					0
				],
				[
					7.905908028239651,
					0
				],
				[
					9.223559366279574,
					0.6588256690199614
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17139798402786255,
				0.22523599863052368,
				0.14705684781074524,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 519580370,
			"isDeleted": false,
			"id": "6R8Rmo_opU4p5PIxiTEKT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 745.966532613896,
			"y": 333.6633782956492,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.247082359219689,
			"height": 7.905908028239594,
			"seed": 158694144,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6588256690199614,
					0
				],
				[
					1.3176513380399228,
					0.6588256690200183
				],
				[
					2.6353026760798457,
					2.6353026760799025
				],
				[
					7.247082359219689,
					7.2470823592196325
				],
				[
					7.247082359219689,
					7.905908028239594
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12064898759126663,
				0.18938998878002167,
				0.24984100461006165,
				0.06902270764112473,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 202515278,
			"isDeleted": false,
			"id": "Drf8U34LnHloTTWQ9zC8d",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 753.8724406421356,
			"y": 334.98102963368916,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.541210704319496,
			"height": 13.176513380399285,
			"seed": 645782272,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6588256690199614,
					0.6588256690199614
				],
				[
					-1.3176513380399228,
					0.6588256690199614
				],
				[
					-5.270605352159805,
					5.270605352159691
				],
				[
					-9.882385035299535,
					11.858862042359362
				],
				[
					-10.541210704319496,
					13.176513380399285
				],
				[
					-10.541210704319496,
					13.176513380399285
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16331076622009277,
				0.28612399101257324,
				0.326291024684906,
				0.10158737003803253,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 269418642,
			"isDeleted": false,
			"id": "NB9mjpS3norv8hQNIgqpl",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 743.9900556068361,
			"y": 169.6157867096777,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.905908028239651,
			"height": 11.858862042359362,
			"seed": 917691136,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6588256690199614,
					0
				],
				[
					1.3176513380399228,
					0
				],
				[
					2.6353026760798457,
					-1.3176513380399228
				],
				[
					3.9529540141197685,
					-1.9764770070599127
				],
				[
					5.9294310211797665,
					-3.952954014119797
				],
				[
					4.61177968313973,
					-5.27060535215972
				],
				[
					1.3176513380399228,
					-4.611779683139758
				],
				[
					-0.6588256690199614,
					-0.6588256690199614
				],
				[
					0,
					4.611779683139758
				],
				[
					3.9529540141197685,
					6.588256690199643
				],
				[
					7.247082359219689,
					5.27060535215972
				],
				[
					7.247082359219689,
					4.611779683139758
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07991598546504974,
				0.1163959950208664,
				0.15620800852775574,
				0.17395098507404327,
				0.16363488137722015,
				0.13333164155483246,
				0.1281251758337021,
				0.1524372547864914,
				0.19056610763072968,
				0.1454743593931198,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 2093779342,
			"isDeleted": false,
			"id": "VZOPpEAlhM-6uWHnLVqnJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 753.2136149731157,
			"y": 158.41575033633828,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.6353026760798457,
			"height": 15.811816056479188,
			"seed": 1460116224,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6588256690199614
				],
				[
					0,
					2.635302676079874
				],
				[
					0.6588256690199614,
					7.2470823592196325
				],
				[
					1.9764770070598843,
					15.152990387459226
				],
				[
					2.6353026760798457,
					15.811816056479188
				],
				[
					2.6353026760798457,
					15.152990387459226
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12255600094795227,
				0.17248299717903137,
				0.2051299810409546,
				0.23189978301525116,
				0.020113129168748856,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 1799691858,
			"isDeleted": false,
			"id": "ZHzPpddFXS40d1hVT6Hy7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 757.8253946562554,
			"y": 168.95696104065775,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.22355936627946,
			"height": 7.905908028239594,
			"seed": 1903991552,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6588256690199614,
					0
				],
				[
					1.3176513380399228,
					0
				],
				[
					2.6353026760798457,
					0
				],
				[
					5.270605352159691,
					-1.3176513380399513
				],
				[
					5.270605352159691,
					-2.635302676079874
				],
				[
					2.6353026760798457,
					-1.9764770070599127
				],
				[
					0.6588256690199614,
					1.3176513380399228
				],
				[
					1.9764770070598843,
					5.27060535215972
				],
				[
					8.564733697259499,
					4.611779683139758
				],
				[
					9.22355936627946,
					3.952954014119797
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06949929893016815,
				0.08455795049667358,
				0.11980029195547104,
				0.13628485798835754,
				0.09693588316440582,
				0.09532296657562256,
				0.14778882265090942,
				0.19401241838932037,
				0.011078765615820885,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 769664974,
			"isDeleted": false,
			"id": "ZtoCU_422Xh65Y6j15_I9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 771.6607337056746,
			"y": 165.6628326955579,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.247082359219689,
			"height": 7.2470823592196325,
			"seed": 1338776320,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6588256690199614,
					0
				],
				[
					-1.9764770070598843,
					0.6588256690199614
				],
				[
					-2.6353026760798457,
					1.9764770070598843
				],
				[
					-3.294128345099807,
					3.2941283450998355
				],
				[
					-1.3176513380399228,
					7.2470823592196325
				],
				[
					3.294128345099921,
					7.2470823592196325
				],
				[
					3.9529540141198822,
					6.588256690199643
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11366342008113861,
				0.1741980016231537,
				0.2001979947090149,
				0.21045257151126862,
				0.06912808120250702,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1030849554,
			"isDeleted": false,
			"id": "t_wRmZdYZlr2KWyalcDfK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 779.5666417339143,
			"y": 153.14514498417856,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.9764770070598843,
			"height": 21.082421408638908,
			"seed": 2095430400,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6588256690199614,
					0
				],
				[
					-0.6588256690199614,
					0.6588256690199614
				],
				[
					-0.6588256690199614,
					4.611779683139758
				],
				[
					0.6588256690199614,
					10.54121070431944
				],
				[
					0.6588256690199614,
					17.788293063539072
				],
				[
					-0.6588256690199614,
					20.423595739618946
				],
				[
					-1.3176513380399228,
					21.082421408638908
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09660501033067703,
				0.2043839991092682,
				0.23118539154529572,
				0.17268191277980804,
				0.010965545661747456,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 795213326,
			"isDeleted": false,
			"id": "ewXWLtPBzTyZBlAMKM2fF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 776.2725133888144,
			"y": 166.98048403359783,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.905908028239651,
			"height": 1.9764770070598843,
			"seed": 506157824,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.3176513380399228,
					-0.6588256690199614
				],
				[
					2.6353026760798457,
					-0.6588256690199614
				],
				[
					7.905908028239651,
					-1.9764770070598843
				],
				[
					7.905908028239651,
					-1.9764770070598843
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08613842725753784,
				0.09506027400493622,
				0.10432787984609604,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1619734994,
			"isDeleted": false,
			"id": "NZXNs5Wrfcfawvp9M2TsV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 786.154898424114,
			"y": 165.6628326955579,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3176513380399228,
			"height": 7.905908028239594,
			"seed": 1252727552,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6588256690199614
				],
				[
					0,
					1.3176513380399228
				],
				[
					0.6588256690199614,
					3.2941283450998355
				],
				[
					0.6588256690199614,
					6.588256690199643
				],
				[
					1.3176513380399228,
					7.905908028239594
				],
				[
					1.3176513380399228,
					7.2470823592196325
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.1127919927239418,
				0.1429985612630844,
				0.03343624994158745,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 643238990,
			"isDeleted": false,
			"id": "ks6xyn0TWOUlaujJaGeF3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 787.4725497621539,
			"y": 168.29813537163778,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.588256690199614,
			"height": 5.270605352159748,
			"seed": 1772100352,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6588256690199614,
					-0.6588256690199898
				],
				[
					1.3176513380399228,
					-0.6588256690199898
				],
				[
					2.6353026760798457,
					-2.635302676079874
				],
				[
					5.929431021179653,
					-5.270605352159748
				],
				[
					6.588256690199614,
					-5.270605352159748
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0908251628279686,
				0.10798672586679459,
				0.12448440492153168,
				0.016249634325504303,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 1470703506,
			"isDeleted": false,
			"id": "M34kZiJq0q0tyGYwDsLih",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 794.7196321213735,
			"y": 168.29813537163778,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6588256690199614,
			"height": 5.27060535215972,
			"seed": 2128378624,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6588256690199614
				],
				[
					0,
					2.6353026760798457
				],
				[
					0.6588256690199614,
					5.27060535215972
				],
				[
					0.6588256690199614,
					5.27060535215972
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09452731162309647,
				0.07167871296405792,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 40,
			"versionNonce": 814502542,
			"isDeleted": false,
			"id": "viQaInPdYPMpGx0fMw-YS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 794.7196321213735,
			"y": 161.7098786814381,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 0.6588256690199614,
			"seed": 2080652032,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6588256690199614
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
				0.007572997827082872,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 721577298,
			"isDeleted": false,
			"id": "viNQh-CouFQ3v0maRPyvq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 803.9431914876529,
			"y": 165.00400702653795,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.541210704319496,
			"height": 9.223559366279517,
			"seed": 721378048,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.3176513380399228,
					0
				],
				[
					-1.9764770070598843,
					0.6588256690199614
				],
				[
					-3.294128345099807,
					2.6353026760798457
				],
				[
					-3.9529540141197685,
					4.611779683139758
				],
				[
					-3.294128345099807,
					8.564733697259555
				],
				[
					0.6588256690199614,
					9.223559366279517
				],
				[
					3.294128345099807,
					6.588256690199643
				],
				[
					4.611779683139844,
					5.929431021179681
				],
				[
					5.270605352159805,
					7.247082359219604
				],
				[
					5.9294310211797665,
					7.247082359219604
				],
				[
					6.588256690199728,
					7.247082359219604
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05914398282766342,
				0.11451031267642975,
				0.16893599927425385,
				0.19647997617721558,
				0.22744931280612946,
				0.19025348126888275,
				0.11870800703763962,
				0.14200304448604584,
				0.20228160917758942,
				0.03798428177833557,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 40,
			"versionNonce": 1220464846,
			"isDeleted": false,
			"id": "MxgT_dnitiOabXCENfI9j",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 809.8726225088327,
			"y": 163.02753001947804,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6588256690199614,
			"height": 0,
			"seed": 2124118784,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6588256690199614,
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
				0.1332695037126541,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1139665682,
			"isDeleted": false,
			"id": "_rjOMzopJcpeAYiToH-aA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 815.8020535300124,
			"y": 151.16866797711864,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.3176513380400365,
			"height": 21.082421408638908,
			"seed": 1729010432,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.3176513380399513
				],
				[
					1.3176513380400365,
					9.223559366279545
				],
				[
					1.3176513380400365,
					17.12946739451914
				],
				[
					0.6588256690199614,
					21.082421408638908
				],
				[
					0,
					21.082421408638908
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17951001226902008,
				0.2770960032939911,
				0.27074095606803894,
				0.025396117940545082,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 713525006,
			"isDeleted": false,
			"id": "Q09te8U6iUjKcS3QWDCku",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 811.8490995158926,
			"y": 166.32165836457787,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.564733697259612,
			"height": 0.6588256690199614,
			"seed": 563804928,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.3176513380399228,
					-0.6588256690199614
				],
				[
					3.294128345099807,
					-0.6588256690199614
				],
				[
					7.905908028239651,
					-0.6588256690199614
				],
				[
					8.564733697259612,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1040157750248909,
				0.14753836393356323,
				0.18860653042793274,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1222818002,
			"isDeleted": false,
			"id": "fS4rWpiGOmA9ZsfJtLlfh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 821.0726588821722,
			"y": 165.00400702653795,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.588256690199614,
			"height": 4.611779683139758,
			"seed": 501398272,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6588256690199614
				],
				[
					0.6588256690199614,
					1.3176513380399228
				],
				[
					1.9764770070598843,
					2.6353026760798457
				],
				[
					5.929431021179653,
					3.952954014119797
				],
				[
					6.588256690199614,
					4.611779683139758
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1592315137386322,
				0.1750296950340271,
				0.04244793578982353,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 912225614,
			"isDeleted": false,
			"id": "kKppsouANhlAabjYaxAVK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 831.6138695864915,
			"y": 163.686355688498,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.588256690199614,
			"height": 18.447118732559062,
			"seed": 911416064,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6588256690199898
				],
				[
					-0.6588256690199614,
					1.9764770070599127
				],
				[
					-3.294128345099807,
					8.564733697259555
				],
				[
					-6.588256690199614,
					17.7882930635391
				],
				[
					-6.588256690199614,
					18.447118732559062
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.18422000110149384,
				0.30504998564720154,
				0.16389136016368866,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 2037894802,
			"isDeleted": false,
			"id": "yMltjFVypW-t0ouRs4BzQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 847.4256856429708,
			"y": 153.14514498417856,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.564733697259726,
			"height": 27.01185242981859,
			"seed": 586119936,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6588256690199614
				],
				[
					-1.3176513380400365,
					3.952954014119797
				],
				[
					-5.92943102117988,
					17.12946739451911
				],
				[
					-8.564733697259726,
					27.01185242981859
				],
				[
					-8.564733697259726,
					26.353026760798627
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10374941676855087,
				0.2359899878501892,
				0.2982659935951233,
				0.1309790313243866,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1436523406,
			"isDeleted": false,
			"id": "U0nenNvceYsxSfH46XwYF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 848.7433369810108,
			"y": 165.6628326955579,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.929431021179653,
			"height": 9.882385035299478,
			"seed": 221764352,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.3176513380399228
				],
				[
					0,
					3.2941283450998355
				],
				[
					0.6588256690199614,
					6.588256690199643
				],
				[
					2.6353026760798457,
					1.3176513380399228
				],
				[
					5.929431021179653,
					-2.635302676079874
				],
				[
					5.929431021179653,
					-3.2941283450998355
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10522866994142532,
				0.14623799920082092,
				0.1687869280576706,
				0.10516797006130219,
				0.017383422702550888,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 174337106,
			"isDeleted": false,
			"id": "-y9d51U6lTwgvs5pYRS2P",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 857.9668963472902,
			"y": 166.98048403359783,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.22355936627946,
			"height": 6.588256690199643,
			"seed": 1131207424,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6588256690199614,
					0
				],
				[
					1.9764770070598843,
					-0.6588256690199614
				],
				[
					1.9764770070598843,
					-1.9764770070598843
				],
				[
					0,
					-2.6353026760798457
				],
				[
					-2.6353026760798457,
					0
				],
				[
					-3.294128345099807,
					3.2941283450998355
				],
				[
					-0.6588256690199614,
					3.952954014119797
				],
				[
					2.6353026760798457,
					0
				],
				[
					5.270605352159691,
					-1.3176513380399228
				],
				[
					5.270605352159691,
					1.3176513380399513
				],
				[
					5.270605352159691,
					3.952954014119797
				],
				[
					5.929431021179653,
					3.952954014119797
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10819799453020096,
				0.1350235641002655,
				0.13099853694438934,
				0.11116272211074829,
				0.15326562523841858,
				0.15519088506698608,
				0.09614361822605133,
				0.11307989805936813,
				0.22352130711078644,
				0.08848599344491959,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1585510862,
			"isDeleted": false,
			"id": "nXGHduylO05zmcrkPq6Ab",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 870.4845840586695,
			"y": 153.80397065319852,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 15.152990387459226,
			"seed": 910269184,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6588256690199614
				],
				[
					0,
					1.9764770070599127
				],
				[
					0,
					7.2470823592196325
				],
				[
					0,
					13.835339049419275
				],
				[
					0,
					15.152990387459226
				],
				[
					0,
					15.152990387459226
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13342200219631195,
				0.19023999571800232,
				0.2766540050506592,
				0.2682398557662964,
				0.028440125286579132,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 25088530,
			"isDeleted": false,
			"id": "E8_UWwBSk5etr9RpYE14C",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 864.5551530374898,
			"y": 163.02753001947804,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.905908028239537,
			"height": 1.3176513380399513,
			"seed": 1991678720,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6588256690199614,
					0
				],
				[
					1.3176513380399228,
					0
				],
				[
					3.294128345099807,
					0.6588256690199614
				],
				[
					7.247082359219576,
					1.3176513380399513
				],
				[
					7.905908028239537,
					1.3176513380399513
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15563876926898956,
				0.23115099966526031,
				0.10447494685649872,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 2015137806,
			"isDeleted": false,
			"id": "A3UVDJpVWN5Ek-bYqJVS1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 889.5905284602486,
			"y": 153.80397065319852,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.200036373339572,
			"height": 25.035375422758705,
			"seed": 1581447936,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6588256690199614
				],
				[
					-0.6588256690199614,
					0.6588256690199614
				],
				[
					-1.9764770070598843,
					3.952954014119797
				],
				[
					-7.247082359219576,
					13.835339049419275
				],
				[
					-11.200036373339572,
					23.717724084718782
				],
				[
					-10.54121070431961,
					25.035375422758705
				],
				[
					-9.882385035299649,
					24.376549753738743
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10649819672107697,
				0.1606917679309845,
				0.2429960072040558,
				0.28481200337409973,
				0.09729721397161484,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 297713618,
			"isDeleted": false,
			"id": "fCx3u-KfdgqrxanUmzeQX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 896.1787851504482,
			"y": 150.50984230809868,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 20.423595739618946,
			"seed": 1755355904,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					4.611779683139758
				],
				[
					0,
					17.12946739451911
				],
				[
					0,
					20.423595739618946
				],
				[
					0,
					19.764770070598985
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1811952143907547,
				0.24193526804447174,
				0.040627654641866684,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 2120965710,
			"isDeleted": false,
			"id": "Z9Q4xX0Se2Dckm_sEYK5Z",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 899.472913495548,
			"y": 165.00400702653795,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6588256690199614,
			"height": 7.247082359219604,
			"seed": 204495616,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.3176513380399228
				],
				[
					0,
					2.6353026760798457
				],
				[
					0,
					3.952954014119797
				],
				[
					0,
					7.247082359219604
				],
				[
					0.6588256690199614,
					7.247082359219604
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11553149670362473,
				0.17016199231147766,
				0.10318435728549957,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 2000352658,
			"isDeleted": false,
			"id": "OORUS_x3TEnR1JEGF_Ik1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 902.7670418406478,
			"y": 160.3922273433982,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 1.3176513380399513,
			"seed": 1916058368,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6588256690199898
				],
				[
					0,
					-1.3176513380399513
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
				0.011697479523718357,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1715889294,
			"isDeleted": false,
			"id": "Z6mZG7BIUsmGkFFGnmFBw",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 910.0141241998674,
			"y": 164.345181357518,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.588256690199614,
			"height": 7.247082359219604,
			"seed": 539785984,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.9764770070598843,
					0.6588256690199614
				],
				[
					-3.9529540141197685,
					3.952954014119797
				],
				[
					-3.294128345099807,
					7.247082359219604
				],
				[
					1.9764770070598843,
					5.27060535215972
				],
				[
					2.6353026760798457,
					4.611779683139758
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.18659362196922302,
				0.2229122370481491,
				0.22037191689014435,
				0.0076750791631639,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1395290962,
			"isDeleted": false,
			"id": "K73RJM1B6fVM7FosRZSym",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 915.9435552210473,
			"y": 165.6628326955579,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.22355936627946,
			"height": 7.2470823592196325,
			"seed": 1091885824,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6588256690199614,
					0.6588256690199614
				],
				[
					1.3176513380399228,
					0
				],
				[
					3.294128345099807,
					-1.3176513380399228
				],
				[
					3.294128345099807,
					-1.9764770070599127
				],
				[
					1.3176513380399228,
					-1.9764770070599127
				],
				[
					-1.3176513380399228,
					0.6588256690199614
				],
				[
					-1.9764770070598843,
					3.952954014119797
				],
				[
					0.6588256690199614,
					5.27060535215972
				],
				[
					3.9529540141197685,
					5.27060535215972
				],
				[
					6.588256690199614,
					3.2941283450998355
				],
				[
					7.247082359219576,
					2.635302676079874
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11327481269836426,
				0.18570776283740997,
				0.19986876845359802,
				0.1745508760213852,
				0.1850576549768448,
				0.22447679936885834,
				0.2362690418958664,
				0.16719281673431396,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 560374478,
			"isDeleted": false,
			"id": "4q8PBs6haO93s7GTzG1GE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 925.8259402563467,
			"y": 163.02753001947804,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.61177968313973,
			"height": 7.905908028239594,
			"seed": 2042690304,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6588256690199614,
					0
				],
				[
					-1.3176513380399228,
					0
				],
				[
					-1.9764770070598843,
					0
				],
				[
					-0.6588256690199614,
					1.3176513380399513
				],
				[
					1.9764770070598843,
					3.952954014119797
				],
				[
					2.6353026760798457,
					5.92943102117971
				],
				[
					0,
					7.905908028239594
				],
				[
					-1.3176513380399228,
					7.905908028239594
				],
				[
					-1.3176513380399228,
					7.2470823592196325
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0457339771091938,
				0.13747000694274902,
				0.1604679822921753,
				0.157131165266037,
				0.14289841055870056,
				0.20004498958587646,
				0.22272250056266785,
				0.009988861158490181,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 132397330,
			"isDeleted": false,
			"id": "hncmQo-ZgIwaTDCE1CN5U",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 936.3671509606661,
			"y": 162.36870435045807,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.905908028239537,
			"height": 7.2470823592196325,
			"seed": 1303632640,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6588256690199614,
					0
				],
				[
					-1.3176513380399228,
					0
				],
				[
					-1.9764770070598843,
					0
				],
				[
					-3.294128345099807,
					0.6588256690199614
				],
				[
					-5.270605352159691,
					4.611779683139758
				],
				[
					-4.61177968313973,
					6.588256690199671
				],
				[
					-1.3176513380399228,
					7.2470823592196325
				],
				[
					1.9764770070598843,
					6.588256690199671
				],
				[
					2.6353026760798457,
					5.92943102117971
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08552999794483185,
				0.11803597956895828,
				0.171097993850708,
				0.2466059923171997,
				0.2522435188293457,
				0.14169012010097504,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 40179982,
			"isDeleted": false,
			"id": "CGHUEsdWD6IUMBvdMbxbQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 939.0024536367459,
			"y": 166.98048403359783,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.54121070431961,
			"height": 8.564733697259555,
			"seed": 456309504,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6588256690199614,
					0
				],
				[
					0.6588256690199614,
					0.6588256690199614
				],
				[
					1.9764770070598843,
					1.3176513380399513
				],
				[
					4.61177968313973,
					1.3176513380399513
				],
				[
					7.247082359219576,
					-0.6588256690199614
				],
				[
					7.247082359219576,
					-1.9764770070598843
				],
				[
					4.61177968313973,
					-1.9764770070598843
				],
				[
					1.3176513380399228,
					1.3176513380399513
				],
				[
					2.6353026760798457,
					5.27060535215972
				],
				[
					9.882385035299649,
					6.588256690199671
				],
				[
					10.54121070431961,
					6.588256690199671
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.03999999910593033,
				0.034019988030195236,
				0.09888198971748352,
				0.14560241997241974,
				0.15743304789066315,
				0.1588868945837021,
				0.16938626766204834,
				0.21120120584964752,
				0.27852627635002136,
				0.07774380594491959,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 350176978,
			"isDeleted": false,
			"id": "RmlqwNv3ORgVKm6fgsYX1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 678.7663143738595,
			"y": 176.20404339987735,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 20.423595739618918,
			"height": 0.6588256690199898,
			"seed": 1834146560,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6588256690199614,
					0
				],
				[
					1.9764770070598843,
					0
				],
				[
					5.270605352159805,
					0
				],
				[
					13.176513380399342,
					0.6588256690199898
				],
				[
					18.447118732559034,
					0.6588256690199898
				],
				[
					19.764770070598956,
					0.6588256690199898
				],
				[
					20.423595739618918,
					0.6588256690199898
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08904598653316498,
				0.16978274285793304,
				0.2265699803829193,
				0.3365109860897064,
				0.3066483736038208,
				0.1403089314699173,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 549111630,
			"isDeleted": false,
			"id": "_ctHCypcumeMcL4rNyU2c",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 715.6605518389775,
			"y": 166.98048403359783,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.223559366279574,
			"height": 7.905908028239594,
			"seed": 282360576,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.3176513380400365,
					0.6588256690199614
				],
				[
					6.588256690199728,
					1.9764770070599127
				],
				[
					9.223559366279574,
					4.611779683139758
				],
				[
					7.247082359219689,
					6.588256690199671
				],
				[
					4.611779683139844,
					7.905908028239594
				],
				[
					3.294128345099921,
					7.905908028239594
				],
				[
					4.611779683139844,
					7.905908028239594
				],
				[
					5.270605352159805,
					7.2470823592196325
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.24839800596237183,
				0.32409802079200745,
				0.34113654494285583,
				0.3607737421989441,
				0.37883853912353516,
				0.3372616469860077,
				0.13020123541355133,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1924308114,
			"isDeleted": false,
			"id": "9u2od-7dhAF2dhscX3fUx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 744.6488812758561,
			"y": 189.3805567802767,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.9764770070598843,
			"height": 15.152990387459198,
			"seed": 1384561408,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6588256690199614,
					1.9764770070598843
				],
				[
					-0.6588256690199614,
					5.27060535215972
				],
				[
					-0.6588256690199614,
					12.517687711379352
				],
				[
					-0.6588256690199614,
					15.152990387459198
				],
				[
					-1.3176513380399228,
					13.835339049419275
				],
				[
					-1.9764770070598843,
					13.176513380399314
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2143615186214447,
				0.2563300132751465,
				0.3088260293006897,
				0.29459303617477417,
				0.019503997638821602,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1019260302,
			"isDeleted": false,
			"id": "qAIYTNANRnVmqfWx9Ysct",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 736.7429732476164,
			"y": 197.94529047753625,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.51768771137938,
			"height": 0,
			"seed": 601602816,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6588256690199614,
					0
				],
				[
					2.6353026760798457,
					0
				],
				[
					9.223559366279574,
					0
				],
				[
					11.85886204235942,
					0
				],
				[
					11.85886204235942,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0837838426232338,
				0.26219549775123596,
				0.3728000223636627,
				0.3724519908428192,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1863662162,
			"isDeleted": false,
			"id": "pQhBV1fo7X-I-CCr7XXRD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 769.0254310295948,
			"y": 178.18052040693726,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.517687711379267,
			"height": 12.517687711379352,
			"seed": 1584143104,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6588256690199614
				],
				[
					0,
					1.9764770070598843
				],
				[
					-2.6353026760798457,
					6.588256690199643
				],
				[
					-7.905908028239537,
					11.20003637333943
				],
				[
					-11.858862042359306,
					12.517687711379352
				],
				[
					-12.517687711379267,
					12.517687711379352
				],
				[
					-11.858862042359306,
					12.517687711379352
				],
				[
					-11.200036373339344,
					12.517687711379352
				],
				[
					-11.200036373339344,
					12.517687711379352
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09178250283002853,
				0.1805659830570221,
				0.27902600169181824,
				0.3409999907016754,
				0.3697645366191864,
				0.3097797632217407,
				0.15909482538700104,
				0.02243923954665661,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 598723534,
			"isDeleted": false,
			"id": "f18WG9SufJTKijBsb6dCI",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 734.7664962405565,
			"y": 206.5100241747958,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.905908028239651,
			"height": 11.200036373339401,
			"seed": 395508480,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6588256690199614
				],
				[
					1.9764770070598843,
					4.611779683139758
				],
				[
					5.270605352159691,
					9.223559366279517
				],
				[
					7.247082359219689,
					11.200036373339401
				],
				[
					7.905908028239651,
					11.200036373339401
				],
				[
					7.905908028239651,
					10.54121070431944
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12101180851459503,
				0.24855199456214905,
				0.32560399174690247,
				0.32775378227233887,
				0.0700562447309494,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 148774930,
			"isDeleted": false,
			"id": "tpOKV3yh9FA5xt5fWLmlW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 740.6959272617362,
			"y": 223.6394915693149,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.223559366279687,
			"height": 11.858862042359362,
			"seed": 1755839232,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6588256690199614
				],
				[
					0.6588256690200751,
					3.952954014119797
				],
				[
					1.976477007059998,
					8.564733697259555
				],
				[
					2.6353026760799594,
					11.200036373339401
				],
				[
					3.294128345099921,
					8.564733697259555
				],
				[
					5.9294310211797665,
					3.952954014119797
				],
				[
					8.564733697259612,
					-0.6588256690199614
				],
				[
					9.223559366279687,
					-0.6588256690199614
				],
				[
					9.223559366279687,
					-0.6588256690199614
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09871600568294525,
				0.21379397809505463,
				0.24417035281658173,
				0.2564772367477417,
				0.2747032344341278,
				0.34336304664611816,
				0.3755195438861847,
				0.2808564007282257,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 329327118,
			"isDeleted": false,
			"id": "hNAs7adKA-AagFh1TgdDT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -63.156800411088284,
			"y": 245.09486824234887,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.502200003857922,
			"height": 30.64694286430756,
			"seed": 989518592,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5893642858520707,
					-0.5893642858520707
				],
				[
					-5.304278572668636,
					0.5893642858520707
				],
				[
					-10.019192859485202,
					4.714914286816509
				],
				[
					-10.608557145337272,
					8.840464287781003
				],
				[
					-8.25110000192899,
					14.14474286044964
				],
				[
					-3.536185715112424,
					20.038385718970346
				],
				[
					-1.1787285717041414,
					24.163935719934784
				],
				[
					-1.768092857556212,
					27.70012143504721
				],
				[
					-6.4830071443727775,
					30.05757857845549
				],
				[
					-13.555378574597569,
					30.05757857845549
				],
				[
					-16.502200003857922,
					30.05757857845549
				],
				[
					-14.14474286044964,
					28.87885000675135
				],
				[
					-13.555378574597569,
					28.28948572089928
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1711546629667282,
				0.24747997522354126,
				0.26189327239990234,
				0.23077014088630676,
				0.21556740999221802,
				0.21357983350753784,
				0.2525709569454193,
				0.31513646245002747,
				0.2808718979358673,
				0.1633535474538803,
				0.017341887578368187,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1275350482,
			"isDeleted": false,
			"id": "lyErjOOTaMAw2GRGaQcee",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -59.62061469597586,
			"y": 268.6694396764316,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.019192859485145,
			"height": 24.163935719934784,
			"seed": 1185168128,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5893642858520707
				],
				[
					-0.5893642858520707,
					-1.1787285717041414
				],
				[
					-0.5893642858520707,
					-0.5893642858520707
				],
				[
					1.1787285717041414,
					5.304278572668636
				],
				[
					2.3574571434082827,
					14.734107146301767
				],
				[
					1.768092857556212,
					17.680928575562064
				],
				[
					-0.5893642858520707,
					14.144742860449696
				],
				[
					-1.768092857556212,
					5.893642858520707
				],
				[
					1.768092857556212,
					-2.9468214292603534
				],
				[
					7.072371430224848,
					-6.483007144372721
				],
				[
					8.251100001928933,
					-2.9468214292603534
				],
				[
					7.072371430224848,
					2.3574571434082827
				],
				[
					4.714914286816565,
					3.536185715112424
				],
				[
					4.714914286816565,
					2.9468214292603534
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09467599540948868,
				0.15924200415611267,
				0.1885901838541031,
				0.2062162458896637,
				0.18536169826984406,
				0.1262540966272354,
				0.09638439863920212,
				0.13036838173866272,
				0.160432830452919,
				0.19008773565292358,
				0.20145800709724426,
				0.015183105133473873,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 529379406,
			"isDeleted": false,
			"id": "GUMt7iz71FhSVU4eOLQFq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -46.06523612137829,
			"y": 265.7226182471712,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.608557145337272,
			"height": 9.429828573633074,
			"seed": 1498299136,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5893642858520707,
					0
				],
				[
					1.768092857556212,
					0.5893642858520707
				],
				[
					2.9468214292603534,
					0.5893642858520707
				],
				[
					4.125550000964495,
					0.5893642858520707
				],
				[
					5.304278572668636,
					-1.7680928575561552
				],
				[
					3.536185715112424,
					-3.5361857151123672
				],
				[
					-0.5893642858520707,
					-2.357457143408226
				],
				[
					-2.3574571434082827,
					2.3574571434082827
				],
				[
					0,
					5.893642858520707
				],
				[
					7.661735716076919,
					4.714914286816565
				],
				[
					8.25110000192899,
					4.125550000964495
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12240087985992432,
				0.16269198060035706,
				0.17148345708847046,
				0.16769936680793762,
				0.1518324315547943,
				0.17192202806472778,
				0.2590455114841461,
				0.3065979480743408,
				0.023296814411878586,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 765379474,
			"isDeleted": false,
			"id": "JVhOboqCilDNT_KQeuUpz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -34.27795040433688,
			"y": 263.95452538961507,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.197921431189286,
			"height": 8.840464287781003,
			"seed": 650009344,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5893642858520707
				],
				[
					-0.5893642858520707,
					-1.1787285717041414
				],
				[
					-1.768092857556212,
					0
				],
				[
					-2.9468214292603534,
					4.714914286816509
				],
				[
					-1.1787285717041414,
					7.072371430224791
				],
				[
					2.9468214292603534,
					5.304278572668579
				],
				[
					5.304278572668579,
					2.357457143408226
				],
				[
					5.89364285852065,
					3.5361857151123672
				],
				[
					6.483007144372721,
					6.483007144372721
				],
				[
					7.661735716076862,
					7.661735716076862
				],
				[
					8.251100001928933,
					7.661735716076862
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.10670999437570572,
				0.16964001953601837,
				0.24336600303649902,
				0.25831523537635803,
				0.14154000580310822,
				0.07583004981279373,
				0.1766732782125473,
				0.249619722366333,
				0.09942648559808731,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 323909262,
			"isDeleted": false,
			"id": "Y8IMSVxNkPRrhnN9SEBjR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -26.616214688260015,
			"y": 258.06088253109436,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1787285717041414,
			"height": 0.5893642858520707,
			"seed": 872053504,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5893642858520707,
					-0.5893642858520707
				],
				[
					-1.1787285717041414,
					-0.5893642858520707
				],
				[
					-1.1787285717041414,
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
				0.1601639986038208,
				0.16299834847450256,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1743028562,
			"isDeleted": false,
			"id": "gQ9OgpD9pxPXUCzwTz8Dr",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -21.31193611559138,
			"y": 264.54388967546714,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.25110000192899,
			"height": 9.429828573633074,
			"seed": 1218632448,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5893642858520707
				],
				[
					-1.1787285717041414,
					2.357457143408226
				],
				[
					-0.5893642858520707,
					5.89364285852065
				],
				[
					2.9468214292603534,
					7.072371430224791
				],
				[
					7.072371430224848,
					4.714914286816509
				],
				[
					7.072371430224848,
					0.5893642858520707
				],
				[
					1.768092857556212,
					-2.3574571434082827
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
				0.1489899903535843,
				0.2187419980764389,
				0.22747604548931122,
				0.22363094985485077,
				0.22296923398971558,
				0.03342672809958458,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1469871310,
			"isDeleted": false,
			"id": "bFJ04uH674FqgQXhGTagV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -16.007657542922743,
			"y": 268.6694396764316,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.304278572668636,
			"height": 1.768092857556212,
			"seed": 696367872,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5893642858520707,
					0.5893642858520707
				],
				[
					1.768092857556212,
					1.1787285717041414
				],
				[
					2.9468214292603534,
					1.768092857556212
				],
				[
					5.304278572668636,
					1.768092857556212
				],
				[
					5.304278572668636,
					1.768092857556212
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12006527930498123,
				0.1922810673713684,
				0.07420431822538376,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1445758738,
			"isDeleted": false,
			"id": "k_f4DFBa6lz1OC331RvA9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -5.399100397585528,
			"y": 244.5055039564968,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.3574571434082827,
			"height": 28.87885000675135,
			"seed": 1523718912,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5893642858520707,
					0.5893642858520707
				],
				[
					-0.5893642858520707,
					3.5361857151123672
				],
				[
					0.5893642858520707,
					16.502200003857922
				],
				[
					1.1787285717041414,
					28.87885000675135
				],
				[
					1.768092857556212,
					28.87885000675135
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.22853399813175201,
				0.2870060205459595,
				0.3758919835090637,
				0.2275640219449997,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1443932942,
			"isDeleted": false,
			"id": "JOOvBjutc-9r8yml_y1xZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 12.281828177976593,
			"y": 265.1332539613192,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1787285717041414,
			"height": 7.661735716076862,
			"seed": 474905344,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5893642858520138
				],
				[
					0,
					2.9468214292602966
				],
				[
					0.5893642858520707,
					6.483007144372721
				],
				[
					0.5893642858520707,
					7.661735716076862
				],
				[
					1.1787285717041414,
					7.661735716076862
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15300799906253815,
				0.20345599949359894,
				0.2113981395959854,
				0.009592438116669655,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1357763794,
			"isDeleted": false,
			"id": "LGE91wHSHcuRD4v45Q7-3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 11.692463892124522,
			"y": 254.52469681598194,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.357457143408226,
			"height": 22.9852071482307,
			"seed": 393665280,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5893642858520707
				],
				[
					0,
					1.1787285717041414
				],
				[
					1.1787285717041414,
					11.787285717041357
				],
				[
					1.768092857556212,
					21.217114290674488
				],
				[
					2.357457143408226,
					22.39584286237863
				],
				[
					2.357457143408226,
					17.091564289709993
				],
				[
					1.768092857556212,
					16.502200003857922
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.17438501119613647,
				0.26096200942993164,
				0.3170979917049408,
				0.2167978137731552,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1562646862,
			"isDeleted": false,
			"id": "pWdX4WsaHci_4ome6Wwt2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 5.209456747751744,
			"y": 253.93533253012987,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.912835718005852,
			"height": 2.9468214292603534,
			"seed": 1920498432,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5893642858520707,
					-0.5893642858520707
				],
				[
					2.3574571434082827,
					-1.768092857556212
				],
				[
					11.197921431189286,
					-2.9468214292603534
				],
				[
					15.32347143215378,
					-2.3574571434082827
				],
				[
					14.73410714630171,
					-0.5893642858520707
				],
				[
					14.14474286044964,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07871600240468979,
				0.21068911254405975,
				0.2821899950504303,
				0.21256090700626373,
				0.010049774311482906,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 163539602,
			"isDeleted": false,
			"id": "94JtfkyDHfBzXFZFsIm-b",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 8.745642462864168,
			"y": 275.15244682080436,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.966014288745498,
			"height": 2.9468214292603534,
			"seed": 1712159488,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.768092857556212,
					0
				],
				[
					4.125550000964495,
					0
				],
				[
					7.072371430224791,
					-0.5893642858520707
				],
				[
					12.376650002893427,
					-2.3574571434082827
				],
				[
					12.966014288745498,
					-2.9468214292603534
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12463348358869553,
				0.17310400307178497,
				0.2433362454175949,
				0.08893691748380661,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 47,
			"versionNonce": 70238094,
			"isDeleted": false,
			"id": "6uxfrNdDcf446XfEPkLsH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 29.373392467686585,
			"y": 268.6694396764316,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.072371430224848,
			"height": 7.661735716076919,
			"seed": 504748800,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.1787285717041414,
					1.768092857556212
				],
				[
					-1.768092857556212,
					2.3574571434082827
				],
				[
					-2.3574571434082827,
					4.714914286816565
				],
				[
					0,
					6.4830071443727775
				],
				[
					3.536185715112424,
					5.304278572668636
				],
				[
					4.714914286816565,
					0.5893642858520707
				],
				[
					1.1787285717041414,
					-1.1787285717041414
				],
				[
					-1.768092857556212,
					1.768092857556212
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
				0.14217397570610046,
				0.1965779960155487,
				0.21887829899787903,
				0.1511227786540985,
				0.1519513875246048,
				0.20197875797748566,
				0.016339203342795372,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1733838930,
			"isDeleted": false,
			"id": "8fv_5g1iJTWauZi1eqdUM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 41.16067818472794,
			"y": 252.16723967257366,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.768092857556212,
			"height": 21.217114290674488,
			"seed": 1216699136,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5893642858520707,
					1.1787285717041414
				],
				[
					-1.1787285717041414,
					2.9468214292603534
				],
				[
					-1.1787285717041414,
					5.304278572668636
				],
				[
					0,
					14.73410714630171
				],
				[
					0.5893642858520707,
					21.217114290674488
				],
				[
					0.5893642858520707,
					20.627750004822417
				],
				[
					0.5893642858520707,
					20.038385718970346
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16082000732421875,
				0.2088319957256317,
				0.246319979429245,
				0.21703705191612244,
				0.025914184749126434,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 258776526,
			"isDeleted": false,
			"id": "0FEMiGKxEcO1ZtcqRq214",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 34.67767104035522,
			"y": 260.41833967450265,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.555378574597569,
			"height": 1.768092857556212,
			"seed": 2000091904,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5893642858520707,
					0
				],
				[
					1.1787285717040845,
					0.5893642858520707
				],
				[
					8.251100001928933,
					0.5893642858520707
				],
				[
					13.555378574597569,
					-0.5893642858520707
				],
				[
					12.966014288745498,
					-1.1787285717041414
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08551281690597534,
				0.1314563900232315,
				0.2533760070800781,
				0.11576373130083084,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1636789778,
			"isDeleted": false,
			"id": "D81baGu6hcq3YiZIGHcgK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -43.11841469211794,
			"y": 287.5290968236978,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.661735716076919,
			"height": 11.787285717041414,
			"seed": 1693408000,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.768092857556212,
					5.893642858520707
				],
				[
					2.9468214292603534,
					11.787285717041414
				],
				[
					2.3574571434082827,
					10.608557145337272
				],
				[
					2.9468214292603534,
					5.893642858520707
				],
				[
					7.072371430224848,
					0.5893642858520707
				],
				[
					7.661735716076919,
					0.5893642858520707
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.18766039609909058,
				0.18610107898712158,
				0.15847329795360565,
				0.12809982895851135,
				0.02798553556203842,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1408480270,
			"isDeleted": false,
			"id": "CIu1aoKmHktyNdByhSUGX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -30.15240040337244,
			"y": 291.0652825388102,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.966014288745498,
			"height": 9.42982857363313,
			"seed": 1269062400,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5893642858520707,
					0.5893642858520707
				],
				[
					1.1787285717041414,
					0.5893642858520707
				],
				[
					2.3574571434082827,
					0.5893642858520707
				],
				[
					2.9468214292603534,
					0
				],
				[
					3.536185715112424,
					-1.768092857556212
				],
				[
					0.5893642858520707,
					-2.3574571434082827
				],
				[
					-2.357457143408226,
					1.1787285717041414
				],
				[
					-1.7680928575561552,
					5.893642858520707
				],
				[
					2.3574571434082827,
					7.072371430224848
				],
				[
					4.714914286816565,
					3.536185715112424
				],
				[
					5.304278572668636,
					2.3574571434082827
				],
				[
					4.714914286816565,
					3.536185715112424
				],
				[
					5.893642858520707,
					5.893642858520707
				],
				[
					8.25110000192899,
					5.893642858520707
				],
				[
					10.608557145337272,
					2.9468214292603534
				],
				[
					10.608557145337272,
					0
				],
				[
					7.661735716076919,
					-1.1787285717041414
				],
				[
					5.304278572668636,
					0.5893642858520707
				],
				[
					4.714914286816565,
					3.536185715112424
				],
				[
					4.714914286816565,
					3.536185715112424
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07582498341798782,
				0.0896499902009964,
				0.13131600618362427,
				0.15020199120044708,
				0.15405718982219696,
				0.12146466225385666,
				0.14851641654968262,
				0.17898941040039062,
				0.14354586601257324,
				0.06861846894025803,
				0.062156952917575836,
				0.12886138260364532,
				0.1544308215379715,
				0.15980230271816254,
				0.18531015515327454,
				0.2035258412361145,
				0.21545721590518951,
				0.16447268426418304,
				0.012631622143089771,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1566301138,
			"isDeleted": false,
			"id": "QmOqlPvbahb-XZ_XHho3c",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -19.543843258035167,
			"y": 290.47591825295814,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.768092857556212,
			"height": 17.680928575562064,
			"seed": 1884166912,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5893642858520707,
					1.1787285717041414
				],
				[
					-1.1787285717041414,
					3.536185715112424
				],
				[
					-1.1787285717041414,
					6.4830071443727775
				],
				[
					-1.1787285717041414,
					14.734107146301767
				],
				[
					-1.768092857556212,
					17.680928575562064
				],
				[
					-1.768092857556212,
					17.680928575562064
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.16776376962661743,
				0.2059289813041687,
				0.21038317680358887,
				0.02161172404885292,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 465437262,
			"isDeleted": false,
			"id": "ZID46ZWWReIwNGdP6VycC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -16.007657542922743,
			"y": 290.47591825295814,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.304278572668636,
			"height": 7.661735716076919,
			"seed": 2084772608,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5893642858520707,
					0
				],
				[
					-0.5893642858520707,
					1.1787285717041414
				],
				[
					-0.5893642858520707,
					4.125550000964495
				],
				[
					1.1787285717041414,
					6.4830071443727775
				],
				[
					4.125550000964495,
					4.714914286816565
				],
				[
					4.714914286816565,
					0.5893642858520707
				],
				[
					3.536185715112424,
					-1.1787285717041414
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
				0.11170950531959534,
				0.17501598596572876,
				0.18746328353881836,
				0.19370834529399872,
				0.18673770129680634,
				0.15474776923656464,
				0.027279693633317947,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 148148626,
			"isDeleted": false,
			"id": "hnP7DOK5oxqMJm6t9AxAK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -9.524650398549966,
			"y": 290.47591825295814,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.7680928575561552,
			"height": 6.4830071443727775,
			"seed": 1774844672,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5893642858520707
				],
				[
					0,
					2.3574571434082827
				],
				[
					0.5893642858520707,
					3.536185715112424
				],
				[
					1.1787285717041414,
					4.714914286816565
				],
				[
					1.7680928575561552,
					6.4830071443727775
				],
				[
					1.7680928575561552,
					6.4830071443727775
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1420726329088211,
				0.19194000959396362,
				0.19797347486019135,
				0.05614907667040825,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 40,
			"versionNonce": 161777806,
			"isDeleted": false,
			"id": "mxcuNuZ0kTlg2aOSrk3Qd",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -8.345921826845824,
			"y": 285.1716396802895,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 0.5893642858520707,
			"seed": 1407122176,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5893642858520707
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
				0.10028918087482452,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 925929298,
			"isDeleted": false,
			"id": "_EL4uz3W-0CIAfE6L2Rl2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -4.809736111733457,
			"y": 289.297189681254,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.25110000192899,
			"height": 10.608557145337272,
			"seed": 35789568,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5893642858520707,
					2.9468214292603534
				],
				[
					1.768092857556212,
					6.4830071443727775
				],
				[
					1.768092857556212,
					5.893642858520707
				],
				[
					4.125550000964495,
					0.5893642858520707
				],
				[
					7.661735716076919,
					-4.125550000964495
				],
				[
					8.25110000192899,
					-4.125550000964495
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16543258726596832,
				0.1503375619649887,
				0.12189718335866928,
				0.15115179121494293,
				0.07580123841762543,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 2103461582,
			"isDeleted": false,
			"id": "s8pv1kQim6oF6eu3pPFYE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 7.566913891160027,
			"y": 289.88655396710607,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.14474286044964,
			"height": 9.42982857363313,
			"seed": 2048334592,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5893642858520707,
					0
				],
				[
					2.3574571434082827,
					-0.5893642858520707
				],
				[
					2.9468214292603534,
					-1.768092857556212
				],
				[
					1.1787285717041414,
					-2.3574571434082827
				],
				[
					-1.768092857556212,
					0
				],
				[
					-2.3574571434082827,
					4.125550000964495
				],
				[
					1.1787285717041414,
					7.072371430224848
				],
				[
					10.608557145337215,
					2.3574571434082827
				],
				[
					11.787285717041357,
					1.768092857556212
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07986661046743393,
				0.15466278791427612,
				0.1597760021686554,
				0.12670446932315826,
				0.13865265250205994,
				0.2211979627609253,
				0.24498236179351807,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1019663634,
			"isDeleted": false,
			"id": "vPXofqiB7cfMYxviYvt4B",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 16.40737817894103,
			"y": 288.7078253954019,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.787285717041414,
			"height": 8.84046428778106,
			"seed": 874380032,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.5893642858520707
				],
				[
					0,
					-1.1787285717041414
				],
				[
					0.5893642858520707,
					-0.5893642858520707
				],
				[
					1.768092857556212,
					3.536185715112424
				],
				[
					2.9468214292603534,
					7.072371430224848
				],
				[
					2.9468214292603534,
					5.893642858520707
				],
				[
					3.536185715112424,
					1.1787285717041414
				],
				[
					5.304278572668636,
					0
				],
				[
					6.4830071443727775,
					2.9468214292603534
				],
				[
					6.4830071443727775,
					5.893642858520707
				],
				[
					7.072371430224848,
					4.714914286816565
				],
				[
					10.019192859485202,
					-0.5893642858520707
				],
				[
					11.787285717041414,
					-1.1787285717041414
				],
				[
					11.787285717041414,
					3.536185715112424
				],
				[
					10.608557145337272,
					7.661735716076919
				],
				[
					10.608557145337272,
					7.072371430224848
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.03279653936624527,
				0.15895141661167145,
				0.21792398393154144,
				0.21216653287410736,
				0.11323937773704529,
				0.07258773595094681,
				0.13287249207496643,
				0.17039614915847778,
				0.17569971084594727,
				0.09681784361600876,
				0.09214373677968979,
				0.17605838179588318,
				0.24191531538963318,
				0.0862453281879425,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 2005548302,
			"isDeleted": false,
			"id": "07ZTYHeq4W1yUjL5zXSGG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 34.67767104035522,
			"y": 289.297189681254,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.483007144372721,
			"height": 5.893642858520707,
			"seed": 1606761216,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5893642858520707,
					0
				],
				[
					1.1787285717040845,
					0
				],
				[
					1.7680928575561552,
					-0.5893642858520707
				],
				[
					1.7680928575561552,
					-1.768092857556212
				],
				[
					0,
					-1.768092857556212
				],
				[
					-1.768092857556212,
					0.5893642858520707
				],
				[
					-1.1787285717041414,
					4.125550000964495
				],
				[
					4.714914286816509,
					3.536185715112424
				],
				[
					4.714914286816509,
					2.9468214292603534
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09225161373615265,
				0.11260751634836197,
				0.14616434276103973,
				0.14460064470767975,
				0.16863314807415009,
				0.22732779383659363,
				0.04467758163809776,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 1259234002,
			"isDeleted": false,
			"id": "2Kabyc9As7FtMwIMS0Ket",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 39.39258532717173,
			"y": 287.5290968236978,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.714914286816565,
			"height": 7.661735716076919,
			"seed": 115350272,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5893642858520707
				],
				[
					0.5893642858520707,
					2.3574571434082827
				],
				[
					1.1787285717041414,
					4.714914286816565
				],
				[
					2.9468214292603534,
					2.9468214292603534
				],
				[
					4.714914286816565,
					-0.5893642858520707
				],
				[
					4.714914286816565,
					0
				],
				[
					4.714914286816565,
					6.4830071443727775
				],
				[
					4.125550000964495,
					7.072371430224848
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1279199868440628,
				0.1630839854478836,
				0.17506463825702667,
				0.09703433513641357,
				0.09589587152004242,
				0.1589079350233078,
				0.030862823128700256,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 2107337550,
			"isDeleted": false,
			"id": "4DAAzLZprAqZKXwcaWqGE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 54.71605675932557,
			"y": 278.0992682500647,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.1787285717041414,
			"height": 16.502200003857922,
			"seed": 478829312,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5893642858520707,
					0
				],
				[
					-1.1787285717041414,
					0.5893642858520707
				],
				[
					-0.5893642858520707,
					6.483007144372721
				],
				[
					-0.5893642858520707,
					15.912835718005852
				],
				[
					-0.5893642858520707,
					16.502200003857922
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.19723199307918549,
				0.23923800885677338,
				0.02800247259438038,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 1285437586,
			"isDeleted": false,
			"id": "c_O-JJIVsAEj94G8ypThP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 47.64368532910072,
			"y": 285.7610039661416,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.42982857363313,
			"height": 1.1787285717041414,
			"seed": 1271839488,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5893642858520707,
					0
				],
				[
					1.1787285717041414,
					0
				],
				[
					8.25110000192899,
					0.5893642858520707
				],
				[
					9.42982857363313,
					1.1787285717041414
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14192599058151245,
				0.1564679890871048,
				0.09132153540849686,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 2112672142,
			"isDeleted": false,
			"id": "sCu3jVLr1WVeBz-5AEe6n",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 65.91397819051485,
			"y": 285.1716396802895,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.072371430224848,
			"height": 10.019192859485202,
			"seed": 2118548224,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.768092857556212,
					0
				],
				[
					-2.9468214292603534,
					0
				],
				[
					-3.536185715112424,
					0.5893642858520707
				],
				[
					-2.9468214292603534,
					3.536185715112424
				],
				[
					0.5893642858520707,
					6.4830071443727775
				],
				[
					1.768092857556212,
					9.42982857363313
				],
				[
					-2.3574571434082827,
					10.019192859485202
				],
				[
					-5.304278572668636,
					8.84046428778106
				],
				[
					-5.304278572668636,
					8.84046428778106
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.019999999552965164,
				0,
				0.10406948626041412,
				0.16969875991344452,
				0.16032010316848755,
				0.1818266063928604,
				0.24179324507713318,
				0.0649208053946495,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1093490258,
			"isDeleted": false,
			"id": "AGH27A3KbYHlto44X6Ub_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -73.48550819950378,
			"y": 39.869088221145375,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 27.40128226749266,
			"height": 172.52659205458383,
			"seed": 1746975488,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1.0148623062034403
				],
				[
					0,
					0
				],
				[
					0,
					10.148623062034346
				],
				[
					3.044586918610321,
					31.46073149230645
				],
				[
					4.059449224813761,
					57.84715145359576
				],
				[
					5.074311531017202,
					87.27815833349536
				],
				[
					10.14862306203429,
					117.7240275195984
				],
				[
					18.267521511661812,
					143.09558517468423
				],
				[
					24.356695348882454,
					162.37796899254948
				],
				[
					27.40128226749266,
					170.49686744217695
				],
				[
					27.40128226749266,
					171.5117297483804
				],
				[
					26.38641996128922,
					170.49686744217695
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16845598816871643,
				0.22119399905204773,
				0.2846980094909668,
				0.2984141707420349,
				0.3419835567474365,
				0.43395349383354187,
				0.47887736558914185,
				0.49086058139801025,
				0.5020736455917358,
				0.42418423295021057,
				0.15665750205516815,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 867659726,
			"isDeleted": false,
			"id": "1BDc7sTArx4qgyqiWoEo4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -53.18826207543509,
			"y": 216.4551295005429,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.282383817865252,
			"height": 17.25265920545837,
			"seed": 145586944,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.0148623062034403
				],
				[
					3.044586918610321,
					5.074311531017202
				],
				[
					8.118898449627409,
					12.178347674441227
				],
				[
					12.17834767444117,
					14.208072286848108
				],
				[
					15.222934593051491,
					10.148623062034346
				],
				[
					17.25265920545837,
					3.044586918610321
				],
				[
					18.267521511661812,
					-1.0148623062033835
				],
				[
					19.282383817865252,
					-3.044586918610264
				],
				[
					19.282383817865252,
					-3.044586918610264
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1797415167093277,
				0.26952001452445984,
				0.3477360010147095,
				0.3403589427471161,
				0.3202950954437256,
				0.33399465680122375,
				0.2651418447494507,
				0.07259634137153625,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 74,
			"versionNonce": 429046802,
			"isDeleted": false,
			"id": "cbw5c84a_okE6X2eIycg9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 71.17911960370509,
			"y": 58.198871961592914,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 388.8222412403617,
			"height": 227.9302793477983,
			"seed": 2057198336,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.1173052909205126,
					0
				],
				[
					-2.234610581841139,
					2.2346105818411672
				],
				[
					-5.586526454602904,
					12.290358200126377
				],
				[
					-12.29035820012632,
					24.580716400252754
				],
				[
					-17.876884654729224,
					36.87107460037913
				],
				[
					-18.99418994564985,
					45.80951692774374
				],
				[
					-13.407663491046947,
					53.63065396418784
				],
				[
					-5.586526454602904,
					62.569096291552455
				],
				[
					3.351915872761765,
					70.3902333279965
				],
				[
					10.055747618285181,
					81.5632862372023
				],
				[
					13.407663491046947,
					91.61903385548754
				],
				[
					15.642274072888085,
					103.90939205561392
				],
				[
					16.75957936380871,
					116.1997502557403
				],
				[
					16.75957936380871,
					129.60741374678724
				],
				[
					17.876884654729338,
					141.89777194691362
				],
				[
					17.876884654729338,
					151.95351956519886
				],
				[
					17.876884654729338,
					156.42274072888114
				],
				[
					18.99418994564985,
					156.42274072888114
				],
				[
					23.46341110933224,
					150.83621427427823
				],
				[
					32.4018534366968,
					145.2496878196754
				],
				[
					45.80951692774374,
					140.78046665599305
				],
				[
					68.15562274615536,
					137.4285507832313
				],
				[
					92.73633914640811,
					137.4285507832313
				],
				[
					116.19975025574035,
					138.54585607415186
				],
				[
					140.7804666559931,
					143.0150772378342
				],
				[
					163.1265724744046,
					149.71890898335766
				],
				[
					186.58998358373685,
					157.54004601980176
				],
				[
					210.05339469306898,
					167.59579363808695
				],
				[
					232.3995005114806,
					181.0034571291339
				],
				[
					254.7456063298922,
					194.41112062018084
				],
				[
					278.20901743922434,
					206.7014788203072
				],
				[
					302.7897338394771,
					217.874531729513
				],
				[
					328.48775553065036,
					225.69566876595715
				],
				[
					351.9511666399827,
					227.9302793477983
				],
				[
					366.47613542195006,
					226.81297405687766
				],
				[
					369.8280512947118,
					224.57836347503653
				],
				[
					367.5934407128708,
					223.4610581841159
				],
				[
					366.47613542195006,
					223.4610581841159
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.051790282130241394,
				0.18666616082191467,
				0.22314374148845673,
				0.2534247040748596,
				0.28203508257865906,
				0.2857222855091095,
				0.2997835576534271,
				0.3065378963947296,
				0.3220682740211487,
				0.33219170570373535,
				0.34560540318489075,
				0.35795125365257263,
				0.3703506588935852,
				0.3780210018157959,
				0.39005720615386963,
				0.3767913579940796,
				0.3476335406303406,
				0.32306617498397827,
				0.30894529819488525,
				0.29106995463371277,
				0.29231101274490356,
				0.3088800311088562,
				0.32229000329971313,
				0.3323025703430176,
				0.3393242359161377,
				0.3550267517566681,
				0.3664512634277344,
				0.37089085578918457,
				0.3790118098258972,
				0.3786791265010834,
				0.39591464400291443,
				0.410190224647522,
				0.3960811495780945,
				0.3914836049079895,
				0.35432520508766174,
				0.2955825626850128,
				0.08938809484243393,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 185878030,
			"isDeleted": false,
			"id": "CNREi1BIDawkeV_I9MlC0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 220.82344525436747,
			"y": 348.97475888551986,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.192725982666957,
			"height": 10.4621468838792,
			"seed": 1864850176,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.6538841802424145
				],
				[
					-0.6538841802424713,
					-0.6538841802424145
				],
				[
					-1.3077683604849426,
					-0.6538841802424145
				],
				[
					-3.269420901212243,
					1.961652540727357
				],
				[
					-4.577189261697185,
					6.5388418024245425
				],
				[
					-3.923305081454714,
					9.808262703636785
				],
				[
					1.961652540727357,
					7.846610162909428
				],
				[
					2.6155367209697715,
					7.846610162909428
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.18219000101089478,
				0.23310400545597076,
				0.28911200165748596,
				0.33943966031074524,
				0.3897550106048584,
				0.1447075754404068,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 331704786,
			"isDeleted": false,
			"id": "JUgHMw8wzxTh8PQBx3Fi1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 225.4006345160646,
			"y": 337.8587278213982,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.154378523394314,
			"height": 22.885946308485757,
			"seed": 817994496,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6538841802424145,
					-1.3077683604848858
				],
				[
					-0.6538841802424145,
					-2.6155367209697715
				],
				[
					-0.6538841802424145,
					-1.961652540727357
				],
				[
					0.6538841802424713,
					2.6155367209698284
				],
				[
					1.961652540727357,
					11.769915244364142
				],
				[
					1.961652540727357,
					20.270409587515985
				],
				[
					2.6155367209698284,
					20.270409587515985
				],
				[
					3.269420901212243,
					14.38545196533397
				],
				[
					5.2310734419396,
					9.808262703636785
				],
				[
					7.846610162909428,
					9.808262703636785
				],
				[
					8.5004943431519,
					15.039336145576385
				],
				[
					7.192725982666957,
					19.61652540727357
				],
				[
					7.192725982666957,
					19.61652540727357
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12360396981239319,
				0.16807998716831207,
				0.2508779764175415,
				0.3018488883972168,
				0.28175806999206543,
				0.1821245402097702,
				0.09295599162578583,
				0.0945701003074646,
				0.1983909010887146,
				0.26474785804748535,
				0.13040612637996674,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 83645518,
			"isDeleted": false,
			"id": "TUKAkAH23N9sN_5iv9Fiq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 238.47831812091363,
			"y": 351.5902956064897,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.5004943431519,
			"height": 9.154378523394314,
			"seed": 558986496,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.3077683604848858,
					-0.6538841802424713
				],
				[
					3.269420901212243,
					-1.961652540727357
				],
				[
					3.923305081454714,
					-2.6155367209698284
				],
				[
					2.6155367209698284,
					-3.269420901212243
				],
				[
					-0.6538841802424713,
					-1.961652540727357
				],
				[
					-1.961652540727357,
					1.961652540727357
				],
				[
					0,
					5.2310734419396
				],
				[
					3.269420901212243,
					5.884957622182071
				],
				[
					6.5388418024245425,
					4.577189261697129
				],
				[
					6.5388418024245425,
					3.923305081454714
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15863744914531708,
				0.18133309483528137,
				0.1603359431028366,
				0.14484964311122894,
				0.14747470617294312,
				0.17144501209259033,
				0.20181888341903687,
				0.2018040120601654,
				0.06763824820518494,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 383541138,
			"isDeleted": false,
			"id": "H0Ioh5p1BbPkUe9VHzEAO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 248.94046500479283,
			"y": 351.5902956064897,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.846610162909428,
			"height": 9.154378523394314,
			"seed": 1885992192,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6538841802424145,
					0
				],
				[
					-1.961652540727357,
					0.6538841802424713
				],
				[
					-1.961652540727357,
					3.269420901212243
				],
				[
					1.3077683604849426,
					5.2310734419396
				],
				[
					4.577189261697185,
					4.577189261697129
				],
				[
					5.884957622182071,
					0.6538841802424713
				],
				[
					4.577189261697185,
					-3.269420901212243
				],
				[
					1.3077683604849426,
					-3.923305081454714
				],
				[
					-0.6538841802424145,
					-2.6155367209698284
				],
				[
					-0.6538841802424145,
					0.6538841802424713
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
				0.05831725895404816,
				0.13712182641029358,
				0.17419573664665222,
				0.1724376529455185,
				0.16905413568019867,
				0.18064504861831665,
				0.2053622156381607,
				0.17695742845535278,
				0.10161047428846359,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 39,
			"versionNonce": 457742990,
			"isDeleted": false,
			"id": "u4jLW6ZqNrd73LuYq6V1S",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 252.86377008624754,
			"y": 354.85971650770193,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.2310734419396,
			"height": 1.3077683604848858,
			"seed": 1047082240,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6538841802424713,
					0
				],
				[
					1.3077683604849426,
					0.6538841802424713
				],
				[
					2.6155367209698284,
					1.3077683604848858
				],
				[
					4.577189261697185,
					1.3077683604848858
				],
				[
					5.2310734419396,
					1.3077683604848858
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11499197036027908,
				0.1407640129327774,
				0.08375662565231323,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 252616018,
			"isDeleted": false,
			"id": "FTEXEZGI_e7tnR5HF4UE6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 260.0564960689145,
			"y": 348.32087470527745,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.500494343151843,
			"height": 21.57817794800087,
			"seed": 533124352,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405047,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6538841802424145
				],
				[
					0,
					3.269420901212243
				],
				[
					1.961652540727357,
					13.731567785091443
				],
				[
					1.961652540727357,
					21.57817794800087
				],
				[
					0.6538841802424713,
					21.57817794800087
				],
				[
					-0.6538841802424145,
					13.731567785091443
				],
				[
					0.6538841802424713,
					5.2310734419396
				],
				[
					5.884957622182071,
					1.961652540727357
				],
				[
					7.846610162909428,
					3.923305081454714
				],
				[
					5.2310734419396,
					9.808262703636728
				],
				[
					4.577189261697185,
					10.4621468838792
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07206152379512787,
				0.11273831129074097,
				0.15237344801425934,
				0.17310687899589539,
				0.16600994765758514,
				0.0698685273528099,
				0.06857995688915253,
				0.12569060921669006,
				0.1632087677717209,
				0.0406620167195797,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 615651534,
			"isDeleted": false,
			"id": "yClgfSjs9EOo-ZfvOmwBB",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 269.8647587725513,
			"y": 347.666990525035,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.154378523394314,
			"height": 8.500494343151843,
			"seed": 1260172544,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.3077683604848858,
					3.269420901212243
				],
				[
					2.6155367209698284,
					7.846610162909428
				],
				[
					2.6155367209698284,
					8.500494343151843
				],
				[
					2.6155367209698284,
					4.577189261697185
				],
				[
					5.884957622182071,
					0
				],
				[
					9.154378523394314,
					0.6538841802424713
				],
				[
					8.500494343151843,
					5.884957622182071
				],
				[
					6.538841802424486,
					8.500494343151843
				],
				[
					6.538841802424486,
					8.500494343151843
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16392764449119568,
				0.18103381991386414,
				0.12472842633724213,
				0.0737278163433075,
				0.09684042632579803,
				0.16355593502521515,
				0.16029541194438934,
				0.02977963164448738,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1236476690,
			"isDeleted": false,
			"id": "k7R5BWG9Y6X0_tzvpEkHF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 282.9424423774003,
			"y": 348.97475888551986,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.34710450606127,
			"height": 13.077683604849028,
			"seed": 320328960,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6538841802424145,
					0
				],
				[
					1.3077683604848858,
					-0.6538841802424145
				],
				[
					1.961652540727357,
					-0.6538841802424145
				],
				[
					2.6155367209697715,
					-1.3077683604848858
				],
				[
					3.269420901212243,
					-1.961652540727357
				],
				[
					0,
					-1.961652540727357
				],
				[
					-2.6155367209698284,
					0.6538841802424713
				],
				[
					-1.3077683604848858,
					5.231073441939657
				],
				[
					3.269420901212243,
					5.884957622182071
				],
				[
					7.192725982666957,
					3.923305081454714
				],
				[
					9.154378523394314,
					-0.6538841802424145
				],
				[
					9.154378523394314,
					-3.269420901212243
				],
				[
					7.192725982666957,
					-2.6155367209697715
				],
				[
					6.538841802424486,
					0
				],
				[
					7.846610162909428,
					3.923305081454714
				],
				[
					11.769915244364086,
					7.846610162909428
				],
				[
					13.731567785091443,
					9.808262703636785
				],
				[
					11.769915244364086,
					9.808262703636785
				],
				[
					5.884957622182071,
					8.5004943431519
				],
				[
					5.884957622182071,
					7.846610162909428
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.08085626363754272,
				0.14104604721069336,
				0.16791199147701263,
				0.1484317034482956,
				0.11342254281044006,
				0.14599566161632538,
				0.2139054536819458,
				0.21068881452083588,
				0.17587929964065552,
				0.17068633437156677,
				0.1938570886850357,
				0.21899323165416718,
				0.22716592252254486,
				0.23352843523025513,
				0.2431318610906601,
				0.26781153678894043,
				0.31417062878608704,
				0.07781091332435608,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 119,
			"versionNonce": 953274126,
			"isDeleted": false,
			"id": "fXKrGe8CSNcwvAFReEdcZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -190.09685784118605,
			"y": 411.8463002480334,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.37901629020152,
			"height": 21.68686569228629,
			"seed": 1361712384,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.4928833111883364
				],
				[
					0,
					2.9572998671299615
				],
				[
					0.9857666223766444,
					13.800732713273078
				],
				[
					0.9857666223766444,
					20.208215758721337
				],
				[
					0.9857666223766444,
					21.193982381097953
				],
				[
					0,
					18.729565825156328
				],
				[
					-1.4786499335649808,
					13.307849402084742
				],
				[
					-0.4928833111883364,
					6.407483045448203
				],
				[
					2.464416555941625,
					0.9857666223766159
				],
				[
					4.92883311188325,
					-0.4928833111883364
				],
				[
					6.900366356636539,
					1.4786499335649523
				],
				[
					6.900366356636539,
					4.92883311188325
				],
				[
					3.943066489506606,
					7.393249667824875
				],
				[
					3.4501831783182695,
					7.886132979013212
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.05234597623348236,
				0.1379210501909256,
				0.17176157236099243,
				0.19610504806041718,
				0.16180367767810822,
				0.11797335743904114,
				0.06878994405269623,
				0.07665105909109116,
				0.13169385492801666,
				0.18391937017440796,
				0.20634862780570984,
				0.18532733619213104,
				0.007467743009328842,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 116,
			"versionNonce": 1363210450,
			"isDeleted": false,
			"id": "fRFZM53PXX1lt3yXLI9yp",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -181.71784155098453,
			"y": 413.8178334927867,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.92883311188325,
			"height": 7.393249667824875,
			"seed": 803214592,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4928833111883364
				],
				[
					-0.9857666223766444,
					1.4786499335649523
				],
				[
					-1.4786499335649808,
					2.464416555941625
				],
				[
					-1.4786499335649808,
					3.450183178318298
				],
				[
					0.4928833111883364,
					5.421716423071587
				],
				[
					2.464416555941625,
					4.92883311188325
				],
				[
					3.4501831783182695,
					0.9857666223766728
				],
				[
					1.4786499335649808,
					-1.9715332447532887
				],
				[
					-0.9857666223766444,
					-1.4786499335649523
				],
				[
					-0.9857666223766444,
					3.9430664895065775
				],
				[
					-0.9857666223766444,
					3.9430664895065775
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0997919887304306,
				0.15153799951076508,
				0.18457800149917603,
				0.1910334825515747,
				0.18850155174732208,
				0.1647818237543106,
				0.16066785156726837,
				0.14891399443149567,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 119,
			"versionNonce": 337689934,
			"isDeleted": false,
			"id": "IGJ5Jq2bRs3pLOtPuV5AU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -176.29612512791294,
			"y": 412.33918355922174,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.900366356636539,
			"height": 7.393249667824875,
			"seed": 237892864,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4928833111883364,
					0.49288331118827955
				],
				[
					-0.4928833111883364,
					3.450183178318241
				],
				[
					0.9857666223766444,
					7.393249667824875
				],
				[
					2.464416555941625,
					7.393249667824875
				],
				[
					2.957299867129933,
					3.450183178318241
				],
				[
					3.4501831783182695,
					0.49288331118827955
				],
				[
					2.957299867129933,
					0.9857666223766159
				],
				[
					2.957299867129933,
					4.92883311188325
				],
				[
					3.9430664895065775,
					7.393249667824875
				],
				[
					5.421716423071558,
					6.407483045448203
				],
				[
					6.407483045448203,
					3.450183178318241
				],
				[
					6.407483045448203,
					0.9857666223766159
				],
				[
					5.914599734259895,
					0.9857666223766159
				],
				[
					5.421716423071558,
					0.9857666223766159
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12745797634124756,
				0.17085421085357666,
				0.18488070368766785,
				0.15977315604686737,
				0.13215124607086182,
				0.07481173425912857,
				0.055011048913002014,
				0.06929080188274384,
				0.10540127754211426,
				0.13194897770881653,
				0.14879901707172394,
				0.11756326258182526,
				0.016158416867256165,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 112,
			"versionNonce": 1229915794,
			"isDeleted": false,
			"id": "rblS_bvAm7BjJFTgUvaxC",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -166.43845890414647,
			"y": 415.29648342635164,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.435949800694914,
			"height": 7.393249667824875,
			"seed": 2032399616,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.9857666223766728,
					-0.49288331118827955
				],
				[
					1.4786499335649808,
					-2.464416555941625
				],
				[
					0,
					-3.450183178318241
				],
				[
					-2.4644165559415967,
					-1.9715332447532887
				],
				[
					-2.4644165559415967,
					1.4786499335650092
				],
				[
					1.4786499335649808,
					3.9430664895066343
				],
				[
					1.9715332447533171,
					3.450183178318298
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.09307842701673508,
				0.1466197818517685,
				0.13701801002025604,
				0.15614566206932068,
				0.171860009431839,
				0.03325604274868965,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 114,
			"versionNonce": 2079843214,
			"isDeleted": false,
			"id": "iTLAGpDHENX7riy6gxREX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -162.98827572582817,
			"y": 412.83206687041,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.421716423071587,
			"height": 9.364782912578107,
			"seed": 2021152000,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4928833111883364
				],
				[
					-0.4928833111883364,
					0.9857666223766728
				],
				[
					0,
					2.9572998671299615
				],
				[
					0.9857666223766444,
					6.407483045448259
				],
				[
					1.4786499335649523,
					7.393249667824875
				],
				[
					2.464416555941625,
					4.435949800694971
				],
				[
					3.9430664895065775,
					0
				],
				[
					4.92883311188325,
					-1.9715332447532319
				],
				[
					4.92883311188325,
					-1.9715332447532319
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06495599448680878,
				0.0499119870364666,
				0.13863332569599152,
				0.14785946905612946,
				0.14437726140022278,
				0.13065585494041443,
				0.11032983660697937,
				0.05791766196489334,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 110,
			"versionNonce": 1251238994,
			"isDeleted": false,
			"id": "TJ0CXesT7Hrjd6VH_ofj3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -148.69465970136676,
			"y": 405.93170051377354,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.407483045448231,
			"height": 21.193982381097953,
			"seed": 83326208,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.49288331118827955
				],
				[
					-1.9715332447532887,
					6.900366356636482
				],
				[
					-5.914599734259895,
					18.236682513967992
				],
				[
					-6.407483045448231,
					21.193982381097953
				],
				[
					-5.914599734259895,
					21.193982381097953
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16565798223018646,
				0.2250719964504242,
				0.27782142162323,
				0.09421686083078384,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 111,
			"versionNonce": 579879374,
			"isDeleted": false,
			"id": "EAekz87W0vpYwdkPZJr61",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -170.8744087048414,
			"y": 433.04028262913135,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.49288331118830797,
			"height": 13.307849402084798,
			"seed": 1088230656,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.4928833111883364
				],
				[
					0,
					2.9572998671299615
				],
				[
					-0.49288331118830797,
					9.364782912578164
				],
				[
					-0.49288331118830797,
					12.814966090896462
				],
				[
					0,
					12.322082779708126
				],
				[
					0,
					11.82919946851979
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13469000160694122,
				0.2285199910402298,
				0.23019467294216156,
				0.1373523622751236,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 111,
			"versionNonce": 1055394322,
			"isDeleted": false,
			"id": "VGOmnpzmpqLyHxA0em515",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -164.9598089705815,
			"y": 438.46199905220294,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4928833111883364,
			"height": 5.914599734259923,
			"seed": 1924666624,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.49288331118827955
				],
				[
					0,
					0.9857666223766728
				],
				[
					0,
					2.464416555941625
				],
				[
					0,
					3.450183178318298
				],
				[
					0.4928833111883364,
					5.42171642307153
				],
				[
					0.4928833111883364,
					5.914599734259923
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11331198364496231,
				0.1764100044965744,
				0.2024099975824356,
				0.04357327148318291,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 108,
			"versionNonce": 184735758,
			"isDeleted": false,
			"id": "4xmjSR7iXc1ORATGcmzXZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -162.98827572582817,
			"y": 435.01181587388464,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4928833111883364,
			"height": 0.49288331118827955,
			"seed": 1502811392,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4928833111883364,
					-0.49288331118827955
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
				0.09437979012727737,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 120,
			"versionNonce": 1027667922,
			"isDeleted": false,
			"id": "QusAL7XaATbqryuszfHmb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -159.0452092363216,
			"y": 440.92641560814457,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.8576662237665,
			"height": 32.03741522724113,
			"seed": 839251200,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4928833111883364,
					-0.4928833111883364
				],
				[
					5.421716423071587,
					-3.9430664895065775
				],
				[
					7.886132979013212,
					-10.350549534954837
				],
				[
					6.900366356636567,
					-13.800732713273078
				],
				[
					4.435949800694942,
					-14.78649933564975
				],
				[
					2.464416555941625,
					-12.322082779708126
				],
				[
					2.464416555941625,
					-7.393249667824875
				],
				[
					3.943066489506606,
					0.49288331118827955
				],
				[
					5.914599734259923,
					8.379016290201548
				],
				[
					5.914599734259923,
					14.78649933564975
				],
				[
					2.9572998671299615,
					17.250915891591376
				],
				[
					-0.9857666223766444,
					15.772265958026424
				],
				[
					-1.9715332447532887,
					10.843432846143173
				],
				[
					2.9572998671299615,
					4.435949800694914
				],
				[
					3.943066489506606,
					3.9430664895065775
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16052398085594177,
				0.22547799348831177,
				0.2344479113817215,
				0.1955292969942093,
				0.14362157881259918,
				0.14386697113513947,
				0.15985482931137085,
				0.17271196842193604,
				0.18303155899047852,
				0.18993911147117615,
				0.19795748591423035,
				0.18360888957977295,
				0.1437782347202301,
				0.03736431896686554,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 114,
			"versionNonce": 1833477710,
			"isDeleted": false,
			"id": "EbFV-mJgHG_zfEN5lFvHn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -145.7373598342368,
			"y": 440.92641560814457,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.871899601389828,
			"height": 5.914599734259866,
			"seed": 867521792,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.9857666223766444,
					-0.4928833111883364
				],
				[
					1.4786499335649523,
					-0.9857666223766728
				],
				[
					2.464416555941625,
					-1.4786499335649523
				],
				[
					1.9715332447532887,
					-2.9572998671299615
				],
				[
					-0.9857666223766728,
					-2.9572998671299615
				],
				[
					-2.9572998671299615,
					0
				],
				[
					-0.4928833111883364,
					2.9572998671299047
				],
				[
					5.421716423071587,
					2.9572998671299047
				],
				[
					5.914599734259866,
					2.464416555941625
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07575704902410507,
				0.13320069015026093,
				0.14450857043266296,
				0.1128658726811409,
				0.21636348962783813,
				0.30926600098609924,
				0.10485781729221344,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 202,
			"versionNonce": 1706438034,
			"isDeleted": false,
			"id": "cAvJpsdStU0Tlsxv174Ae",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 90.49409156741575,
			"y": 367.7046012188339,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.417782360693039,
			"height": 10.543499592567116,
			"seed": 1616147712,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.4584130257637753
				],
				[
					0,
					1.3752390772913259
				],
				[
					0.916826051527579,
					6.417782360692968
				],
				[
					0.916826051527579,
					9.168260515275733
				],
				[
					0.916826051527579,
					7.334608412220575
				],
				[
					1.833652103055158,
					2.2920651288188765
				],
				[
					5.959369334929249,
					-1.3752390772913827
				],
				[
					6.417782360693039,
					-0.9168260515276074
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06756293028593063,
				0.11738989502191544,
				0.14532659947872162,
				0.15315084159374237,
				0.11459802091121674,
				0.12697339057922363,
				0.0853668823838234,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 206,
			"versionNonce": 440052878,
			"isDeleted": false,
			"id": "m1TwSIGPlEj3uNpWE9hwq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 98.2871130054001,
			"y": 369.538253321889,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.500956309165446,
			"height": 7.793021437984407,
			"seed": 221656320,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4584130257637895,
					0
				],
				[
					-1.3752390772913543,
					0
				],
				[
					-1.8336521030551438,
					1.3752390772913827
				],
				[
					-2.2920651288189333,
					4.584130257637867
				],
				[
					0.4584130257637895,
					5.959369334929306
				],
				[
					2.750478154582737,
					4.125717231874091
				],
				[
					3.2088911803465123,
					0.9168260515276074
				],
				[
					0.916826051527579,
					-1.8336521030551012
				],
				[
					-1.3752390772913543,
					-1.3752390772913259
				],
				[
					-1.8336521030551438,
					1.8336521030552149
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
				0.08621770888566971,
				0.14157800376415253,
				0.18545684218406677,
				0.17991073429584503,
				0.1644883155822754,
				0.15711505711078644,
				0.1714552640914917,
				0.13497598469257355,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 199,
			"versionNonce": 1031711570,
			"isDeleted": false,
			"id": "eDxi7dO4mC6SyQfXoh50u",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 100.57917813421909,
			"y": 372.28873147647175,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.584130257637895,
			"height": 1.8336521030551012,
			"seed": 1422226688,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.9168260515275506
				],
				[
					0.4584130257638037,
					1.3752390772913259
				],
				[
					1.3752390772913827,
					1.8336521030551012
				],
				[
					4.125717231874091,
					1.3752390772913259
				],
				[
					4.584130257637895,
					0.9168260515275506
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11244198679924011,
				0.15083999931812286,
				0.10575387626886368,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 203,
			"versionNonce": 1603398350,
			"isDeleted": false,
			"id": "ieup-_8N_BjM_oW9x_Vju",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 106.08013444338451,
			"y": 367.7046012188339,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.500956309165474,
			"height": 7.334608412220575,
			"seed": 74126592,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4584130257637753
				],
				[
					0,
					2.2920651288188765
				],
				[
					1.3752390772913827,
					5.500956309165417
				],
				[
					2.2920651288189617,
					5.042543283401642
				],
				[
					3.667304206110316,
					0.4584130257637753
				],
				[
					5.500956309165474,
					-0.9168260515276074
				],
				[
					5.500956309165474,
					2.7504781545827086
				],
				[
					5.04254328340167,
					5.9593693349291925
				],
				[
					5.04254328340167,
					6.417782360692968
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1092739850282669,
				0.14298801124095917,
				0.1662905514240265,
				0.11002236604690552,
				0.06313171237707138,
				0.09645208716392517,
				0.1717642843723297,
				0.053350768983364105,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 198,
			"versionNonce": 183595282,
			"isDeleted": false,
			"id": "2DD4Zs6T1FYwjdMgId_WM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 115.24839495866024,
			"y": 367.7046012188339,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4584130257637753,
			"height": 0.4584130257637753,
			"seed": 1176646912,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4584130257637753
				],
				[
					-0.4584130257637753,
					0.4584130257637753
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
				0.00040478515438735485,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 204,
			"versionNonce": 1810325774,
			"isDeleted": false,
			"id": "0BpQ3GmJe1uSs4VwwCGBf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 115.24839495866024,
			"y": 367.7046012188339,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.04254328340167,
			"height": 9.168260515275733,
			"seed": 104232192,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4584130257637753,
					0
				],
				[
					-0.916826051527579,
					1.3752390772913259
				],
				[
					0.4584130257638037,
					5.042543283401642
				],
				[
					2.750478154582737,
					6.417782360692968
				],
				[
					4.125717231874091,
					3.667304206110316
				],
				[
					4.125717231874091,
					-0.9168260515276074
				],
				[
					1.833652103055158,
					-2.7504781545827655
				],
				[
					-0.916826051527579,
					-0.4584130257637753
				],
				[
					0,
					3.208891180346484
				],
				[
					0.4584130257638037,
					3.667304206110316
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13003164529800415,
				0.19525201618671417,
				0.19521456956863403,
				0.17596662044525146,
				0.15831796824932098,
				0.15410910546779633,
				0.17849627137184143,
				0.15366137027740479,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 204,
			"versionNonce": 830832338,
			"isDeleted": false,
			"id": "kRxt66IyUfvCdTw3gUrNx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 118.45728613900678,
			"y": 365.87094911577867,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.251434463748154,
			"height": 19.711760107842906,
			"seed": 1171191040,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4584130257637753,
					-0.4584130257637753
				],
				[
					-1.3752390772913543,
					-0.4584130257637753
				],
				[
					-1.833652103055158,
					0
				],
				[
					-1.3752390772913543,
					4.125717231874091
				],
				[
					1.3752390772913543,
					11.001912618330948
				],
				[
					0.916826051527579,
					16.96128195326014
				],
				[
					-2.2920651288189333,
					19.25334708207913
				],
				[
					-5.959369334929221,
					17.878108004787748
				],
				[
					-6.8761953864568,
					15.12762985020504
				],
				[
					-6.417782360693025,
					14.669216824441264
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.0916842669248581,
				0.15829598903656006,
				0.20012111961841583,
				0.2026037573814392,
				0.22586295008659363,
				0.2653479278087616,
				0.17962343990802765,
				0.026377106085419655,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 203,
			"versionNonce": 850661198,
			"isDeleted": false,
			"id": "HyngzPHAb7QyR4MqBGpoQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 123.9582424481722,
			"y": 367.2461881930701,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.709847489511958,
			"height": 6.4177823606930815,
			"seed": 1957131520,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4584130257638037,
					0
				],
				[
					1.3752390772913827,
					0
				],
				[
					2.750478154582737,
					-0.45841302576383214
				],
				[
					2.2920651288189617,
					-1.3752390772914396
				],
				[
					-0.4584130257637753,
					-0.9168260515276074
				],
				[
					-1.8336521030551296,
					2.2920651288188765
				],
				[
					1.3752390772913827,
					5.042543283401642
				],
				[
					6.417782360693025,
					4.125717231874091
				],
				[
					6.876195386456828,
					3.667304206110259
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07735400646924973,
				0.103737972676754,
				0.1802079826593399,
				0.20238710939884186,
				0.19875119626522064,
				0.27885815501213074,
				0.3058912456035614,
				0.15717773139476776,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 64,
			"versionNonce": 231855250,
			"isDeleted": false,
			"id": "6acr-YPA9EsAA5NXrRaku",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -341.9199875739583,
			"y": 387.48736376360114,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.751976923102404,
			"height": 8.358837362659187,
			"seed": 1524669184,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4643798534810344,
					0
				],
				[
					0.4643798534810344,
					0.4643798534810344
				],
				[
					1.3931395604432169,
					2.3218992674053425
				],
				[
					3.7150388278485025,
					7.430077655697005
				],
				[
					4.179418681329594,
					8.358837362659187
				],
				[
					3.250658974367468,
					6.501317948734936
				],
				[
					2.786279120886377,
					2.3218992674053425
				],
				[
					3.7150388278485025,
					0
				],
				[
					5.572558241772811,
					0.9287597069620688
				],
				[
					6.501317948734936,
					6.036938095253845
				],
				[
					6.501317948734936,
					7.430077655697005
				],
				[
					6.965697802215971,
					4.179418681329594
				],
				[
					7.894457509178096,
					0.9287597069620688
				],
				[
					9.287597069621313,
					0.4643798534810344
				],
				[
					9.751976923102404,
					3.7150388278485025
				],
				[
					9.287597069621313,
					7.430077655697005
				],
				[
					9.287597069621313,
					7.430077655697005
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06816799938678741,
				0.10286999493837357,
				0.14632000029087067,
				0.18095974624156952,
				0.16729870438575745,
				0.09974432736635208,
				0.061381105333566666,
				0.08646334707736969,
				0.1498582810163498,
				0.18207846581935883,
				0.13113903999328613,
				0.04642535373568535,
				0.06769659370183945,
				0.16476577520370483,
				0.2108408510684967,
				0.018760131672024727,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1347483022,
			"isDeleted": false,
			"id": "VxpY-ld8_2begjvgxYNG4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -328.4529718230074,
			"y": 388.8805033240443,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.036938095253845,
			"height": 6.965697802215971,
			"seed": 980187904,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.46437985348109123,
					0
				],
				[
					1.3931395604432169,
					0
				],
				[
					2.3218992674053425,
					0
				],
				[
					2.7862791208864337,
					-0.9287597069621256
				],
				[
					0.9287597069621256,
					-0.9287597069621256
				],
				[
					-1.39313956044316,
					1.8575194139242512
				],
				[
					-0.9287597069621256,
					5.108178388291776
				],
				[
					1.3931395604432169,
					6.036938095253845
				],
				[
					4.179418681329594,
					3.7150388278485025
				],
				[
					4.643798534810685,
					3.250658974367468
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07646319270133972,
				0.12091467529535294,
				0.1347104161977768,
				0.13989348709583282,
				0.151504248380661,
				0.19050106406211853,
				0.2046608328819275,
				0.06408755481243134,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1368224338,
			"isDeleted": false,
			"id": "XwM7f7T0dWkcIcsPEKQAn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -319.16537475338606,
			"y": 387.02298391012005,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.643798534810685,
			"height": 8.358837362659187,
			"seed": 1273756416,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.3931395604432169,
					-0.46437985348109123
				],
				[
					-2.786279120886377,
					0.9287597069621256
				],
				[
					-3.250658974367468,
					2.7862791208864337
				],
				[
					-0.9287597069621256,
					5.108178388291719
				],
				[
					0.46437985348109123,
					7.430077655697062
				],
				[
					-1.3931395604432169,
					7.894457509178096
				],
				[
					-3.7150388278485025,
					7.894457509178096
				],
				[
					-4.179418681329594,
					7.894457509178096
				],
				[
					-3.7150388278485025,
					7.894457509178096
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13225598633289337,
				0.1991419941186905,
				0.22159774601459503,
				0.1765201985836029,
				0.15642288327217102,
				0.20040863752365112,
				0.1480298787355423,
				0.007810119539499283,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 66,
			"versionNonce": 1844909006,
			"isDeleted": false,
			"id": "EmtyW-uz63M3-UO1vPGhP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -314.5215762185754,
			"y": 387.9517436170822,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.287597069621313,
			"height": 8.358837362659187,
			"seed": 817814272,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9287597069621256,
					0
				],
				[
					-1.8575194139242512,
					0
				],
				[
					-2.3218992674053425,
					0.9287597069621256
				],
				[
					0,
					3.7150388278485593
				],
				[
					1.8575194139242512,
					6.501317948734936
				],
				[
					0.9287597069621256,
					7.894457509178153
				],
				[
					-1.8575194139242512,
					6.965697802215971
				],
				[
					-2.3218992674053425,
					5.572558241772811
				],
				[
					0,
					4.179418681329594
				],
				[
					2.3218992674053425,
					5.108178388291719
				],
				[
					4.643798534810628,
					6.965697802215971
				],
				[
					5.572558241772811,
					7.430077655697062
				],
				[
					6.501317948734936,
					5.572558241772811
				],
				[
					6.965697802215971,
					2.786279120886377
				],
				[
					6.501317948734936,
					0.4643798534810344
				],
				[
					5.108178388291719,
					-0.4643798534810344
				],
				[
					2.786279120886377,
					0.9287597069621256
				],
				[
					3.250658974367468,
					3.7150388278485593
				],
				[
					3.7150388278485593,
					3.7150388278485593
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1271359920501709,
				0.19801199436187744,
				0.1955609768629074,
				0.16936294734477997,
				0.20230425894260406,
				0.2115415632724762,
				0.18315017223358154,
				0.12092932313680649,
				0.12093490362167358,
				0.1841883510351181,
				0.2313304990530014,
				0.23238760232925415,
				0.24696306884288788,
				0.2582899332046509,
				0.2594129741191864,
				0.18916472792625427,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1603229714,
			"isDeleted": false,
			"id": "fsPI_UGiLF_pYRKUOssfc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -305.69835900243515,
			"y": 389.8092630310065,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.7150388278485025,
			"height": 3.7150388278485025,
			"seed": 239074048,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4643798534810344,
					0
				],
				[
					-0.9287597069620688,
					0
				],
				[
					-0.9287597069620688,
					0.4643798534810344
				],
				[
					-1.39313956044316,
					1.8575194139242512
				],
				[
					1.857519413924308,
					3.7150388278485025
				],
				[
					2.3218992674053425,
					3.7150388278485025
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07992129772901535,
				0.13632336258888245,
				0.2874400019645691,
				0.2086278349161148,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 633301518,
			"isDeleted": false,
			"id": "NEkspQlRPdb5g04Xg6_3l",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -297.803901493257,
			"y": 388.4161234705632,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.501317948734936,
			"height": 6.965697802216027,
			"seed": 575994624,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.9287597069621256,
					0.46437985348109123
				],
				[
					-0.9287597069621256,
					1.3931395604432737
				],
				[
					-1.3931395604432169,
					2.7862791208864337
				],
				[
					0.9287597069621256,
					5.572558241772867
				],
				[
					4.179418681329594,
					5.108178388291776
				],
				[
					5.108178388291719,
					1.3931395604432737
				],
				[
					3.250658974367468,
					-1.39313956044316
				],
				[
					-0.4643798534810344,
					0
				],
				[
					0.46437985348109123,
					5.108178388291776
				],
				[
					0.9287597069621256,
					5.108178388291776
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11015133559703827,
				0.18611681461334229,
				0.2200859934091568,
				0.2874540090560913,
				0.28212079405784607,
				0.23451803624629974,
				0.2350013703107834,
				0.21777017414569855,
				0.00777597026899457,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 667846098,
			"isDeleted": false,
			"id": "7PgWZVtzpgwou3cKqCgG3",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -295.0176223723706,
			"y": 387.48736376360114,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.894457509178096,
			"height": 19.968333699685786,
			"seed": 722762496,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4643798534810344,
					0
				],
				[
					-0.9287597069621256,
					0
				],
				[
					-0.9287597069621256,
					0.4643798534810344
				],
				[
					0.9287597069621825,
					4.643798534810628
				],
				[
					3.250658974367468,
					11.145116483545564
				],
				[
					3.250658974367468,
					16.717674725318375
				],
				[
					0,
					19.968333699685786
				],
				[
					-4.643798534810628,
					15.324535164875158
				],
				[
					-4.643798534810628,
					14.395775457913032
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12228000164031982,
				0.14288458228111267,
				0.17374242842197418,
				0.19637225568294525,
				0.24889807403087616,
				0.31586065888404846,
				0.0190008245408535,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 1721956430,
			"isDeleted": false,
			"id": "NWUSTi3IqfbUhBRSJ7Owk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -286.65878500971144,
			"y": 389.8092630310065,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.68073663006453,
			"height": 6.965697802216027,
			"seed": 1782012672,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4643798534810628,
					0
				],
				[
					1.8575194139242797,
					-0.46437985348109123
				],
				[
					3.250658974367468,
					-0.9287597069621825
				],
				[
					3.715038827848531,
					-2.3218992674053425
				],
				[
					0.928759706962154,
					-2.7862791208864337
				],
				[
					-2.321899267405314,
					0
				],
				[
					0,
					4.179418681329594
				],
				[
					7.894457509178125,
					3.7150388278485025
				],
				[
					8.358837362659216,
					3.7150388278485025
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11997964233160019,
				0.18595676124095917,
				0.21533654630184174,
				0.15817639231681824,
				0.1997346729040146,
				0.3084355592727661,
				0.1554483324289322,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 61,
			"versionNonce": 56753042,
			"isDeleted": false,
			"id": "9Qi9xedO_Eje9h_19xAHZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -334.0255300647802,
			"y": 410.70635643765445,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.036938095253902,
			"height": 11.609496337026712,
			"seed": 15088384,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.4643798534810344,
					-0.46437985348109123
				],
				[
					-0.9287597069621256,
					-0.9287597069621825
				],
				[
					-1.8575194139242512,
					-0.46437985348109123
				],
				[
					-2.3218992674052856,
					0.4643798534810344
				],
				[
					-1.8575194139242512,
					2.3218992674053425
				],
				[
					0.46437985348109123,
					4.179418681329594
				],
				[
					2.3218992674053425,
					6.501317948734936
				],
				[
					2.7862791208864337,
					7.894457509178096
				],
				[
					2.3218992674053425,
					9.287597069621313
				],
				[
					0.46437985348109123,
					10.216356776583439
				],
				[
					-1.39313956044316,
					10.68073663006453
				],
				[
					-3.250658974367468,
					10.216356776583439
				],
				[
					-2.786279120886377,
					8.358837362659187
				],
				[
					-2.3218992674052856,
					7.894457509178096
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.025477996096014977,
				0.071540467441082,
				0.08903186023235321,
				0.08685608208179474,
				0.07822006195783615,
				0.0778098776936531,
				0.0887766107916832,
				0.10068108886480331,
				0.11187167465686798,
				0.1254432052373886,
				0.14447982609272003,
				0.15127533674240112,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 53,
			"versionNonce": 1484439182,
			"isDeleted": false,
			"id": "bepNz641VzIxS4Hurt5pZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -327.52421211604525,
			"y": 413.4926355585408,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.9287597069621256,
			"height": 5.572558241772811,
			"seed": 1334852352,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4643798534810344
				],
				[
					0,
					0.9287597069621256
				],
				[
					0,
					1.8575194139242512
				],
				[
					0.46437985348109123,
					4.643798534810628
				],
				[
					0.9287597069621256,
					5.572558241772811
				],
				[
					0.9287597069621256,
					5.572558241772811
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.062085479497909546,
				0.10105319321155548,
				0.16509398818016052,
				0.1817074865102768,
				0.042509276419878006,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 276871506,
			"isDeleted": false,
			"id": "SuV7rj8A_LsyDHjpphE1B",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -326.5954524090831,
			"y": 408.3844571702491,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4643798534810344,
			"height": 0.46437985348109123,
			"seed": 1600469760,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.46437985348109123
				],
				[
					-0.4643798534810344,
					-0.46437985348109123
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
				0.07301797717809677,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 57,
			"versionNonce": 1073724622,
			"isDeleted": false,
			"id": "z1IXfOVrOky6OZ1dv2StY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -322.41603372775353,
			"y": 412.5638758515787,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.68073663006453,
			"height": 9.751976923102461,
			"seed": 251460352,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.46437985348109123,
					-0.46437985348109123
				],
				[
					1.3931395604432169,
					-0.9287597069621825
				],
				[
					4.179418681329594,
					-0.46437985348109123
				],
				[
					5.108178388291776,
					0.9287597069621256
				],
				[
					4.179418681329594,
					3.2506589743674112
				],
				[
					2.3218992674053425,
					6.036938095253845
				],
				[
					2.3218992674053425,
					8.358837362659187
				],
				[
					5.572558241772811,
					8.823217216140279
				],
				[
					10.216356776583496,
					6.501317948734936
				],
				[
					10.68073663006453,
					6.036938095253845
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08962798863649368,
				0.1361999809741974,
				0.19875399768352509,
				0.19587057828903198,
				0.21410156786441803,
				0.22148855030536652,
				0.27091166377067566,
				0.27342891693115234,
				0.016531219705939293,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 243384082,
			"isDeleted": false,
			"id": "tw0iCFrPmF353qLxmlMcv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -308.48463812332153,
			"y": 415.8145348259461,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.358837362659187,
			"height": 6.965697802216027,
			"seed": 1539078912,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.46437985348109123,
					0
				],
				[
					1.857519413924308,
					-0.9287597069620688
				],
				[
					2.3218992674053425,
					-2.78627912088632
				],
				[
					1.3931395604432169,
					-3.7150388278485025
				],
				[
					-1.8575194139242512,
					-2.78627912088632
				],
				[
					-3.250658974367468,
					0.46437985348109123
				],
				[
					-0.9287597069621256,
					3.250658974367525
				],
				[
					4.643798534810685,
					3.250658974367525
				],
				[
					5.108178388291719,
					2.7862791208864337
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11735394597053528,
				0.1643863469362259,
				0.153399258852005,
				0.14852844178676605,
				0.2043052315711975,
				0.27173274755477905,
				0.042774200439453125,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1657467662,
			"isDeleted": false,
			"id": "fiV9q4Xo9OM8iTQMYK7sv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 314.22092711675486,
			"y": 336.26660966020427,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.638312111023652,
			"height": 16.89752173715101,
			"seed": 1407146752,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.603482919183989,
					0
				],
				[
					-3.0174145959198313,
					0.603482919183989
				],
				[
					-5.4313462726557304,
					1.2069658383679212
				],
				[
					-6.638312111023652,
					3.0174145959198313
				],
				[
					-3.6208975151038203,
					7.241795030207584
				],
				[
					-0.603482919183989,
					11.466175464495336
				],
				[
					-0.603482919183989,
					15.087072979599156
				],
				[
					-3.6208975151038203,
					16.89752173715101
				],
				[
					-6.034829191839663,
					16.89752173715101
				],
				[
					-4.2243804342877525,
					13.880107141231179
				],
				[
					-3.6208975151038203,
					13.276624222047246
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07999999821186066,
				0.14699804782867432,
				0.19164299964904785,
				0.18720385432243347,
				0.17115932703018188,
				0.2265997976064682,
				0.29851678013801575,
				0.26346153020858765,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 38,
			"versionNonce": 970722514,
			"isDeleted": false,
			"id": "Pueg07w2Ns2M6vYJ3tq2F",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 309.9965466824671,
			"y": 332.64571214510045,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.603482919183989,
			"height": 20.518419252254887,
			"seed": 997948160,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.603482919183989
				],
				[
					0,
					0
				],
				[
					0,
					7.241795030207641
				],
				[
					-0.603482919183989,
					19.311453413886966
				],
				[
					-0.603482919183989,
					19.914936333070898
				],
				[
					-0.603482919183989,
					19.311453413886966
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0956919863820076,
				0.13900399208068848,
				0.2338460087776184,
				0.27554401755332947,
				0.011607117019593716,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 38,
			"versionNonce": 1800757582,
			"isDeleted": false,
			"id": "I9cj5qmViMXgMI7_ApBAv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 313.6174441975709,
			"y": 332.04222922591646,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.4139316767358423,
			"height": 25.34628260572663,
			"seed": 1007713024,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.603482919183989
				],
				[
					0,
					3.0174145959198313
				],
				[
					-1.2069658383679212,
					13.880107141231292
				],
				[
					-2.4139316767358423,
					22.932350928990786
				],
				[
					-1.8104487575519101,
					25.34628260572663
				],
				[
					-1.8104487575519101,
					25.34628260572663
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15280550718307495,
				0.2720080018043518,
				0.3450259864330292,
				0.09769430756568909,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 101,
			"versionNonce": 673620626,
			"isDeleted": false,
			"id": "5duadPxxrVofvGTtHpsky",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -174.61755582277164,
			"y": 382.10377377921253,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.862692545311404,
			"height": 15.087072979599156,
			"seed": 396720896,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6034829191839606,
					0
				],
				[
					-0.6034829191839606,
					3.6208975151038203
				],
				[
					-1.2069658383679496,
					10.259209626127415
				],
				[
					-1.2069658383679496,
					12.069658383679382
				],
				[
					-1.2069658383679496,
					9.655726706943483
				],
				[
					-1.2069658383679496,
					4.8278633534717414
				],
				[
					-2.4139316767358707,
					0.603482919183989
				],
				[
					-2.4139316767358707,
					-1.2069658383679212
				],
				[
					-1.2069658383679496,
					-1.2069658383679212
				],
				[
					1.8104487575518817,
					0
				],
				[
					6.638312111023623,
					1.2069658383679212
				],
				[
					8.448760868575533,
					1.2069658383679212
				],
				[
					7.845277949391544,
					1.2069658383679212
				],
				[
					7.241795030207584,
					3.0174145959198313
				],
				[
					7.241795030207584,
					6.638312111023652
				],
				[
					7.241795030207584,
					10.862692545311404
				],
				[
					7.845277949391544,
					13.276624222047246
				],
				[
					7.845277949391544,
					13.880107141231235
				],
				[
					7.241795030207584,
					13.276624222047246
				],
				[
					6.034829191839663,
					13.276624222047246
				],
				[
					4.2243804342877525,
					13.276624222047246
				],
				[
					1.2069658383679212,
					13.880107141231235
				],
				[
					-1.8104487575519101,
					13.880107141231235
				],
				[
					-2.4139316767358707,
					13.880107141231235
				],
				[
					-1.8104487575519101,
					13.880107141231235
				],
				[
					-1.2069658383679496,
					13.880107141231235
				],
				[
					-1.2069658383679496,
					13.276624222047246
				],
				[
					-1.2069658383679496,
					12.673141302863314
				],
				[
					-1.2069658383679496,
					12.069658383679382
				],
				[
					-1.2069658383679496,
					10.862692545311404
				],
				[
					-1.2069658383679496,
					9.655726706943483
				],
				[
					-1.8104487575519101,
					9.05224378775955
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.19364599883556366,
				0.24283701181411743,
				0.20073294639587402,
				0.13379980623722076,
				0.0722413957118988,
				0.09653567522764206,
				0.14527834951877594,
				0.21684134006500244,
				0.27211830019950867,
				0.30480292439460754,
				0.27951115369796753,
				0.2640444338321686,
				0.2613818049430847,
				0.2682645320892334,
				0.2874809503555298,
				0.2923924922943115,
				0.27103275060653687,
				0.2804936170578003,
				0.2775011956691742,
				0.2840186059474945,
				0.31111860275268555,
				0.3393727242946625,
				0.35172247886657715,
				0.28300076723098755,
				0.2802276015281677,
				0.2560229003429413,
				0.24340283870697021,
				0.23439373075962067,
				0.18964117765426636,
				0.03931201249361038,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 90,
			"versionNonce": 1291323278,
			"isDeleted": false,
			"id": "4JJpdm3YqATseAuECYd8f",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -172.80710706521975,
			"y": 375.46546166818894,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.431346272655702,
			"height": 7.84527794939163,
			"seed": 1511439104,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.6034829191839322
				],
				[
					0,
					1.8104487575518533
				],
				[
					-0.6034829191839606,
					4.827863353471685
				],
				[
					-0.6034829191839606,
					6.034829191839663
				],
				[
					0,
					6.034829191839663
				],
				[
					0,
					3.6208975151037635
				],
				[
					0,
					0.6034829191839322
				],
				[
					0,
					-1.206965838367978
				],
				[
					0,
					-1.810448757551967
				],
				[
					0.603482919183989,
					-0.603482919183989
				],
				[
					2.4139316767358707,
					0
				],
				[
					4.224380434287781,
					0.6034829191839322
				],
				[
					4.8278633534717414,
					0.6034829191839322
				],
				[
					4.224380434287781,
					0.6034829191839322
				],
				[
					4.224380434287781,
					1.2069658383679212
				],
				[
					3.6208975151038203,
					1.8104487575518533
				],
				[
					3.6208975151038203,
					3.0174145959198313
				],
				[
					3.6208975151038203,
					3.6208975151037635
				],
				[
					3.6208975151038203,
					4.827863353471685
				],
				[
					3.6208975151038203,
					5.431346272655674
				],
				[
					3.0174145959198313,
					5.431346272655674
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.0594019778072834,
				0.13644906878471375,
				0.17785225808620453,
				0.17192557454109192,
				0.13117969036102295,
				0.09049996733665466,
				0.07840093970298767,
				0.1076558530330658,
				0.15693634748458862,
				0.20651806890964508,
				0.2230636030435562,
				0.21380499005317688,
				0.20261234045028687,
				0.21098965406417847,
				0.2098446935415268,
				0.2123144567012787,
				0.21794335544109344,
				0.2209479659795761,
				0.23198825120925903,
				0.2339697927236557,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 84,
			"versionNonce": 605585490,
			"isDeleted": false,
			"id": "9rGiQyaHs5_PlTc4EHphK",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -173.4105899844037,
			"y": 386.3281542135003,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.8278633534717414,
			"height": 6.638312111023652,
			"seed": 1978735360,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6034829191839606,
					0
				],
				[
					-0.6034829191839606,
					0.603482919183989
				],
				[
					1.2069658383679496,
					1.206965838367978
				],
				[
					3.0174145959198313,
					1.8104487575519101
				],
				[
					4.224380434287781,
					1.8104487575519101
				],
				[
					3.0174145959198313,
					1.8104487575519101
				],
				[
					1.8104487575519101,
					3.0174145959198313
				],
				[
					1.2069658383679496,
					4.224380434287809
				],
				[
					0.6034829191839606,
					5.4313462726557304
				],
				[
					0,
					6.034829191839663
				],
				[
					0.6034829191839606,
					6.034829191839663
				],
				[
					1.8104487575519101,
					6.638312111023652
				],
				[
					2.4139316767358707,
					6.638312111023652
				],
				[
					3.0174145959198313,
					6.638312111023652
				],
				[
					3.0174145959198313,
					6.638312111023652
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.172807976603508,
				0.2530899941921234,
				0.33066800236701965,
				0.33342960476875305,
				0.2889237105846405,
				0.27339935302734375,
				0.30920299887657166,
				0.34571772813796997,
				0.3494223654270172,
				0.34139904379844666,
				0.38508397340774536,
				0.3779740631580353,
				0.33893224596977234,
				0.1173408180475235,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 218,
			"versionNonce": 669771214,
			"isDeleted": false,
			"id": "SVCw_SC3VC_uhnelrjUtv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 90.98806464708451,
			"y": 345.2204978982138,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 29.036837246623776,
			"height": 12.58262947353694,
			"seed": 784317184,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4839472874437547
				],
				[
					0,
					1.4518418623311504
				],
				[
					0,
					6.29131473676847
				],
				[
					0,
					8.71105117398713
				],
				[
					0,
					7.743156599099677
				],
				[
					-0.4839472874437263,
					4.355525586993565
				],
				[
					-0.9678945748874526,
					0.9678945748874526
				],
				[
					-1.4518418623311788,
					-1.4518418623312073
				],
				[
					-1.4518418623311788,
					-2.41973643721866
				],
				[
					-0.9678945748874526,
					-1.935789149774962
				],
				[
					1.9357891497749335,
					-1.935789149774962
				],
				[
					6.2913147367684985,
					-1.935789149774962
				],
				[
					10.162893036318337,
					-1.935789149774962
				],
				[
					13.066576760980695,
					-1.4518418623312073
				],
				[
					16.938155060530534,
					-1.4518418623312073
				],
				[
					21.777627934967853,
					-2.9036837246623577
				],
				[
					25.649206234517663,
					-2.9036837246623577
				],
				[
					26.617100809405144,
					-2.41973643721866
				],
				[
					26.617100809405144,
					-1.935789149774962
				],
				[
					26.617100809405144,
					-0.9678945748874526
				],
				[
					26.617100809405144,
					1.4518418623311504
				],
				[
					26.617100809405144,
					5.3234201618810175
				],
				[
					27.10104809684887,
					8.227103886543375
				],
				[
					27.584995384292597,
					9.678945748874582
				],
				[
					26.617100809405144,
					9.194998461430885
				],
				[
					26.133153521961418,
					8.71105117398713
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12764200568199158,
				0.16099201142787933,
				0.20052960515022278,
				0.17528429627418518,
				0.17203909158706665,
				0.1421695202589035,
				0.1285887211561203,
				0.1359010636806488,
				0.1769646257162094,
				0.23015286028385162,
				0.2626977860927582,
				0.2946494221687317,
				0.29799559712409973,
				0.283142626285553,
				0.3239935040473938,
				0.3484236001968384,
				0.3359614312648773,
				0.3380800485610962,
				0.3408252000808716,
				0.38121557235717773,
				0.39302942156791687,
				0.3860219419002533,
				0.3770561218261719,
				0.34419527649879456,
				0.0828746035695076,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 198,
			"versionNonce": 159950354,
			"isDeleted": false,
			"id": "hxKlJqDAmXGWYu6dZY3a9",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 90.02017007219706,
			"y": 355.38339093453214,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 22.26157522241155,
			"height": 0.48394728744369786,
			"seed": 1107901184,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.41973643721866,
					0
				],
				[
					10.162893036318337,
					0
				],
				[
					16.938155060530534,
					-0.48394728744369786
				],
				[
					20.325786072636646,
					0
				],
				[
					22.26157522241155,
					0
				],
				[
					21.777627934967825,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17171399295330048,
				0.27844148874282837,
				0.34013599157333374,
				0.32194194197654724,
				0.2583569288253784,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 197,
			"versionNonce": 759823374,
			"isDeleted": false,
			"id": "f3J-o0sSxW5qNTGc6T9qU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 94.37569565919063,
			"y": 344.2526033233264,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 5.3234201618810175,
			"seed": 148781824,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.48394728744369786
				],
				[
					0,
					2.419736437218603
				],
				[
					0,
					4.839472874437263
				],
				[
					0,
					5.3234201618810175
				],
				[
					0,
					5.3234201618810175
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1936340034008026,
				0.18445727229118347,
				0.060590118169784546,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 196,
			"versionNonce": 560862162,
			"isDeleted": false,
			"id": "6q1oNxhG5HxwgUFh5zlTb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 98.2472739587405,
			"y": 344.7365506107701,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4839472874437263,
			"height": 3.8715782995498103,
			"seed": 2000591616,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4839472874437547
				],
				[
					0,
					2.41973643721866
				],
				[
					0,
					3.8715782995498103
				],
				[
					0.4839472874437263,
					3.8715782995498103
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13974051177501678,
				0.11534424126148224,
				0.005066711455583572,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 198,
			"versionNonce": 51071566,
			"isDeleted": false,
			"id": "Jm3iObOblhEzU6fOwXhhJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 100.1830631085154,
			"y": 344.7365506107701,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.9678945748874526,
			"height": 2.9036837246624145,
			"seed": 206461696,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.4839472874437547
				],
				[
					0.4839472874437263,
					0.9678945748875094
				],
				[
					0.4839472874437263,
					1.9357891497749051
				],
				[
					0.9678945748874526,
					2.9036837246624145
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
				0.05087899789214134,
				0.1465192586183548,
				0.12578769028186798,
				0.005814819131046534,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 198,
			"versionNonce": 2111818130,
			"isDeleted": false,
			"id": "b6znIyaIWg5fkCNlaKELu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 104.05464140806521,
			"y": 344.2526033233264,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4839472874437547,
			"height": 6.775262024212225,
			"seed": 1677941504,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.4839472874437547
				],
				[
					0,
					0.48394728744369786
				],
				[
					0,
					2.9036837246623577
				],
				[
					0,
					5.3234201618810175
				],
				[
					0.4839472874437547,
					6.29131473676847
				],
				[
					0.4839472874437547,
					5.807367449324715
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06388818472623825,
				0.17901629209518433,
				0.21973489224910736,
				0.2001924365758896,
				0.026673583313822746,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 196,
			"versionNonce": 671666318,
			"isDeleted": false,
			"id": "sjFWdkr0xaS0_fO8LYkWS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 107.44227242017132,
			"y": 344.7365506107701,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4839472874437263,
			"height": 2.41973643721866,
			"seed": 1991793408,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.4839472874437263,
					0.9678945748875094
				],
				[
					0.4839472874437263,
					2.41973643721866
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
				0.1718669980764389,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 193,
			"versionNonce": 1444202322,
			"isDeleted": false,
			"id": "YlRTEs1PBEhhZ55_0p8Je",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 109.37806156994623,
			"y": 344.7365506107701,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.0001,
			"height": 0.0001,
			"seed": 360192768,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
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
			"version": 195,
			"versionNonce": 1476103886,
			"isDeleted": false,
			"id": "Q4qGPiiQSS4L2-UZKOIZf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 112.76569258205234,
			"y": 343.7686560358827,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4839472874437263,
			"height": 7.743156599099677,
			"seed": 604633856,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.4518418623312073
				],
				[
					0.4839472874437263,
					7.2592093116559795
				],
				[
					0.4839472874437263,
					7.743156599099677
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2338380068540573,
				0.118950255215168,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 46,
			"versionNonce": 1650724114,
			"isDeleted": false,
			"id": "JA2Ld5jihBz-ctwEYI5Ea",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 318.2276237701024,
			"y": 382.28688730021156,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.886269267905789,
			"height": 14.40230094648291,
			"seed": 782491238,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7580158392885323
				],
				[
					2.2740475178657675,
					7.580158392885721
				],
				[
					3.790079196442889,
					14.40230094648291
				],
				[
					3.790079196442889,
					12.1282534286172
				],
				[
					3.790079196442889,
					5.3061108750200106
				],
				[
					4.548095035731478,
					1.5160316785771215
				],
				[
					6.822142553597189,
					5.3061108750200106
				],
				[
					7.580158392885778,
					10.612221750040021
				],
				[
					9.096190071462956,
					4.548095035731421
				],
				[
					11.370237589328667,
					0.7580158392885323
				],
				[
					12.886269267905789,
					3.0320633571543
				],
				[
					12.886269267905789,
					7.580158392885721
				],
				[
					12.128253428617256,
					11.37023758932861
				],
				[
					12.128253428617256,
					10.612221750040021
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14363718032836914,
				0.183318629860878,
				0.19353753328323364,
				0.13406409323215485,
				0.07434728741645813,
				0.11242678761482239,
				0.1717807650566101,
				0.1956070214509964,
				0.09020132571458817,
				0.10662195086479187,
				0.15941794216632843,
				0.19566568732261658,
				0.06706018000841141,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 1870431502,
			"isDeleted": false,
			"id": "d3w2pq9rscyzvk1Zl-5Hw",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 333.38794055587397,
			"y": 386.0769664966544,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.822142553597189,
			"height": 10.612221750040078,
			"seed": 921129574,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7580158392885892,
					0.7580158392885892
				],
				[
					-0.7580158392885892,
					1.5160316785771784
				],
				[
					-1.5160316785771784,
					5.306110875020067
				],
				[
					1.5160316785771215,
					8.338174232174367
				],
				[
					4.548095035731421,
					6.822142553597189
				],
				[
					5.3061108750200106,
					1.5160316785771784
				],
				[
					3.0320633571543,
					-2.2740475178657107
				],
				[
					0.7580158392885323,
					-2.2740475178657107
				],
				[
					-0.7580158392885892,
					0.7580158392885892
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
				0.07453970611095428,
				0.17078854143619537,
				0.18092046678066254,
				0.18105310201644897,
				0.1919025033712387,
				0.1783539056777954,
				0.14110055565834045,
				0.030379822477698326,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 37,
			"versionNonce": 944020178,
			"isDeleted": false,
			"id": "CwGlRRVknnRH1Hib6zuAE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 337.9360355916054,
			"y": 390.62506153238587,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.2740475178657675,
			"height": 2.2740475178657107,
			"seed": 925863078,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7580158392885892
				],
				[
					0.7580158392885892,
					1.5160316785771215
				],
				[
					2.2740475178657675,
					2.2740475178657107
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
				0.08926599472761154,
				0.11846493184566498,
				0.1516580432653427,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 1342485326,
			"isDeleted": false,
			"id": "_5IlczITSPBGNABQR04gP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 340.9680989487597,
			"y": 384.56093481807727,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.580158392885778,
			"height": 9.854205910751489,
			"seed": 150037350,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7580158392885892
				],
				[
					0,
					2.2740475178657107
				],
				[
					0.7580158392885892,
					4.548095035731421
				],
				[
					1.5160316785771784,
					6.0641267143086
				],
				[
					3.0320633571543,
					3.0320633571543
				],
				[
					5.306110875020067,
					0
				],
				[
					7.580158392885778,
					4.548095035731421
				],
				[
					7.580158392885778,
					9.854205910751489
				],
				[
					7.580158392885778,
					9.854205910751489
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07592330873012543,
				0.14998207986354828,
				0.1596091240644455,
				0.14961394667625427,
				0.0731368139386177,
				0.09075024724006653,
				0.16629211604595184,
				0.11651162803173065,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 36,
			"versionNonce": 642609298,
			"isDeleted": false,
			"id": "_vkiGIoRTPgHOBEM39MNc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 350.8223048595112,
			"y": 386.0769664966544,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.0641267143086,
			"height": 7.580158392885778,
			"seed": 727125798,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7580158392885892,
					0.7580158392885892
				],
				[
					2.2740475178657675,
					5.306110875020067
				],
				[
					5.306110875020067,
					7.580158392885778
				],
				[
					6.0641267143086,
					6.822142553597189
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.21498550474643707,
				0.14575891196727753,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 37,
			"versionNonce": 1139612046,
			"isDeleted": false,
			"id": "ttTSzvkgPKOZWWUKfUhwV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 361.43452660955126,
			"y": 385.31895065736586,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.790079196442889,
			"height": 26.53055437510011,
			"seed": 2143746726,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.5160316785771215
				],
				[
					-0.7580158392885892,
					3.790079196442832
				],
				[
					-2.2740475178657107,
					8.33817423217431
				],
				[
					-3.790079196442889,
					26.53055437510011
				],
				[
					-3.0320633571543,
					25.772538535811577
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1797814965248108,
				0.2894602417945862,
				0.1660357415676117,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 271945298,
			"isDeleted": false,
			"id": "Ag8gb4d_ozdhfmZ-wpaqN",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 384.93301762749707,
			"y": 371.6746655501715,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.33817423217431,
			"height": 20.466427660791567,
			"seed": 2026934630,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7580158392885892
				],
				[
					0,
					0.7580158392885892
				],
				[
					0,
					12.1282534286172
				],
				[
					0,
					15.1603167857715
				],
				[
					-0.7580158392885323,
					12.1282534286172
				],
				[
					-3.790079196442832,
					9.854205910751489
				],
				[
					-6.0641267143086,
					11.37023758932861
				],
				[
					-6.0641267143086,
					18.1923801429258
				],
				[
					-2.2740475178657107,
					19.708411821502978
				],
				[
					1.5160316785771784,
					17.43436430363721
				],
				[
					2.2740475178657107,
					17.43436430363721
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06323599070310593,
				0.1624850183725357,
				0.22113540768623352,
				0.21668420732021332,
				0.14522342383861542,
				0.08939352631568909,
				0.11753039807081223,
				0.1930738240480423,
				0.19503091275691986,
				0.033996276557445526,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 1651423182,
			"isDeleted": false,
			"id": "_up3G3tAB_tWY_OjPKtMY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 391.7551601810943,
			"y": 384.56093481807727,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.854205910751489,
			"height": 9.0961900714629,
			"seed": 224553894,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7580158392885323,
					0
				],
				[
					3.032063357154243,
					-0.7580158392885892
				],
				[
					3.032063357154243,
					-1.5160316785771784
				],
				[
					1.5160316785770647,
					-2.2740475178657107
				],
				[
					-2.2740475178657107,
					-0.7580158392885892
				],
				[
					-3.790079196442889,
					3.790079196442889
				],
				[
					0,
					6.822142553597189
				],
				[
					6.0641267143086,
					5.3061108750200106
				],
				[
					6.0641267143086,
					4.548095035731421
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07110763341188431,
				0.12424994260072708,
				0.14531274139881134,
				0.1360541433095932,
				0.18003390729427338,
				0.25296664237976074,
				0.2510601580142975,
				0.05364767462015152,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 39,
			"versionNonce": 1255404562,
			"isDeleted": false,
			"id": "gNi7-LEYCgNrHoVFa2LUc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 400.85135025255715,
			"y": 383.0449031395001,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.580158392885778,
			"height": 9.0961900714629,
			"seed": 1963310950,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7580158392885323,
					0.7580158392885892
				],
				[
					-0.7580158392885323,
					2.2740475178657675
				],
				[
					0,
					5.306110875020067
				],
				[
					3.0320633571543567,
					6.822142553597189
				],
				[
					6.0641267143086,
					2.2740475178657675
				],
				[
					6.822142553597246,
					-2.2740475178657107
				],
				[
					6.822142553597246,
					-2.2740475178657107
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08898855745792389,
				0.14645813405513763,
				0.19531604647636414,
				0.20439544320106506,
				0.1400422304868698,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 37,
			"versionNonce": 1940033038,
			"isDeleted": false,
			"id": "WYoVqOApugRQFNtRXAQ70",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 410.70555616330864,
			"y": 383.0449031395001,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.5160316785771784,
			"height": 6.822142553597189,
			"seed": 12278950,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7580158392885892
				],
				[
					0.758015839288646,
					2.2740475178657675
				],
				[
					0.758015839288646,
					3.790079196442889
				],
				[
					1.5160316785771784,
					6.0641267143086
				],
				[
					1.5160316785771784,
					6.822142553597189
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.04805899038910866,
				0.08610998839139938,
				0.19067849218845367,
				0.1970440000295639,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 35,
			"versionNonce": 2015338962,
			"isDeleted": false,
			"id": "acRYtPU2cfiST_u_549aU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 410.70555616330864,
			"y": 378.49680810376867,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7580158392885323,
			"height": 0.7580158392885323,
			"seed": 216478566,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7580158392885323,
					0.7580158392885323
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
				0.009601105004549026,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 39,
			"versionNonce": 1417780302,
			"isDeleted": false,
			"id": "9U4O5rx6kCmO_JAFI7E9A",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 420.55976207406013,
			"y": 380.0128397823458,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.096190071462843,
			"height": 9.0961900714629,
			"seed": 1488737190,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.5160316785771784,
					0.7580158392885892
				],
				[
					-3.032063357154243,
					0.7580158392885892
				],
				[
					-5.306110875019954,
					3.790079196442889
				],
				[
					-4.548095035731421,
					7.580158392885778
				],
				[
					-0.7580158392885323,
					9.0961900714629
				],
				[
					3.0320633571543567,
					8.338174232174367
				],
				[
					3.790079196442889,
					7.580158392885778
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09290163964033127,
				0.1785479485988617,
				0.2548210024833679,
				0.23236499726772308,
				0.047875791788101196,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1664063378,
			"isDeleted": false,
			"id": "dXBvNDFydEEKzOKYthofJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 425.10785710979155,
			"y": 384.56093481807727,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.612221750040021,
			"height": 11.370237589328667,
			"seed": 152381670,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.758015839288646,
					0
				],
				[
					1.5160316785771784,
					0
				],
				[
					3.790079196442889,
					-0.7580158392885892
				],
				[
					4.548095035731535,
					-3.790079196442889
				],
				[
					2.2740475178658244,
					-4.548095035731478
				],
				[
					-0.7580158392885323,
					-0.7580158392885892
				],
				[
					0.758015839288646,
					4.548095035731421
				],
				[
					4.548095035731535,
					6.822142553597189
				],
				[
					9.096190071462956,
					3.0320633571543
				],
				[
					9.854205910751489,
					2.2740475178657107
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10462597757577896,
				0.1375740021467209,
				0.18281427025794983,
				0.16575860977172852,
				0.12835296988487244,
				0.18009695410728455,
				0.2644428610801697,
				0.22026918828487396,
				0.050030212849378586,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 1524949646,
			"isDeleted": false,
			"id": "Tpy-Ghp0w_2nPrt3qqbfc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 441.02618973485164,
			"y": 382.28688730021156,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.822142553597246,
			"height": 14.40230094648291,
			"seed": 588103654,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7580158392885892
				],
				[
					-2.2740475178657107,
					-1.5160316785771784
				],
				[
					-3.032063357154243,
					-0.7580158392885892
				],
				[
					-3.7900791964427754,
					1.5160316785771215
				],
				[
					0,
					5.3061108750200106
				],
				[
					2.2740475178658244,
					11.37023758932861
				],
				[
					-0.7580158392885323,
					12.886269267905732
				],
				[
					-3.7900791964427754,
					11.37023758932861
				],
				[
					-4.548095035731421,
					11.37023758932861
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06976199150085449,
				0.10258181393146515,
				0.11135293543338776,
				0.12081161141395569,
				0.17538702487945557,
				0.24121133983135223,
				0.2844645380973816,
				0.09707504510879517,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 40,
			"versionNonce": 1547359570,
			"isDeleted": false,
			"id": "ZjlnWfOWQzzsGOXMNuny5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 329.5978613594311,
			"y": 432.31593269325754,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.580158392885778,
			"height": 19.708411821502978,
			"seed": 2054568870,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7580158392885892
				],
				[
					0,
					0
				],
				[
					3.790079196442889,
					-3.790079196442889
				],
				[
					5.3061108750200106,
					-7.580158392885778
				],
				[
					5.3061108750200106,
					-4.548095035731478
				],
				[
					4.548095035731421,
					6.0641267143086
				],
				[
					7.580158392885778,
					12.1282534286172
				],
				[
					7.580158392885778,
					11.37023758932861
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.12976627051830292,
				0.1994263231754303,
				0.2086874395608902,
				0.160109281539917,
				0.2055356800556183,
				0.28411924839019775,
				0.11355157196521759,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 965042382,
			"isDeleted": false,
			"id": "8M1LmPShxbCQlzDcuz651",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 348.54825734164547,
			"y": 426.25180597894894,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.0961900714629,
			"height": 18.1923801429258,
			"seed": 293798950,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7580158392885892
				],
				[
					-2.2740475178657107,
					-0.7580158392885892
				],
				[
					-3.790079196442889,
					-0.7580158392885892
				],
				[
					-6.0641267143086,
					0
				],
				[
					-6.0641267143086,
					2.2740475178657107
				],
				[
					-0.7580158392885892,
					6.822142553597189
				],
				[
					3.0320633571543,
					12.1282534286172
				],
				[
					1.5160316785771215,
					16.676348464348678
				],
				[
					-3.0320633571543,
					17.43436430363721
				],
				[
					-5.3061108750200106,
					15.1603167857715
				],
				[
					-5.3061108750200106,
					14.40230094648291
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.12599682807922363,
				0.16075469553470612,
				0.17745694518089294,
				0.17417627573013306,
				0.16932034492492676,
				0.19374896585941315,
				0.26014888286590576,
				0.3057202398777008,
				0.0264471136033535,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 38,
			"versionNonce": 345529106,
			"isDeleted": false,
			"id": "LPHdbI_y-XogCbNBwgkii",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 344.000162305914,
			"y": 418.67164758606316,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.790079196442832,
			"height": 25.772538535811577,
			"seed": 738092646,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7580158392885323,
					0.7580158392885892
				],
				[
					-0.7580158392885323,
					4.548095035731478
				],
				[
					0,
					12.886269267905789
				],
				[
					1.5160316785771784,
					25.772538535811577
				],
				[
					3.0320633571543,
					23.498491017945867
				],
				[
					3.0320633571543,
					21.98245933936869
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11180264502763748,
				0.19322000443935394,
				0.2471420019865036,
				0.2864070236682892,
				0.01608029194176197,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 38,
			"versionNonce": 1677465358,
			"isDeleted": false,
			"id": "rOjbSwxMfFBoqZJNd8gE1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 348.54825734164547,
			"y": 418.67164758606316,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.790079196442889,
			"height": 31.836665250120177,
			"seed": 1510285414,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.5160316785771784
				],
				[
					0,
					6.0641267143086
				],
				[
					1.5160316785771215,
					20.466427660791567
				],
				[
					3.0320633571543,
					30.320633571543055
				],
				[
					3.790079196442889,
					31.836665250120177
				],
				[
					3.790079196442889,
					31.078649410831588
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13121099770069122,
				0.1992420107126236,
				0.3128499984741211,
				0.32205909490585327,
				0.09493743628263474,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 2059348178,
			"isDeleted": false,
			"id": "BK6z9FMBztIMrVnUZUn0-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 370.53071668101416,
			"y": 416.39760006819745,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.096190071462956,
			"height": 25.014522696522988,
			"seed": 1781652070,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					2.2740475178657107
				],
				[
					-0.7580158392885892,
					6.0641267143086
				],
				[
					-0.7580158392885892,
					11.37023758932861
				],
				[
					0.7580158392885892,
					17.43436430363721
				],
				[
					0.7580158392885892,
					18.1923801429258
				],
				[
					-1.5160316785771215,
					15.918332625060089
				],
				[
					-5.3061108750200106,
					15.1603167857715
				],
				[
					-7.580158392885778,
					18.95039598221439
				],
				[
					-6.822142553597189,
					23.49849101794581
				],
				[
					-3.0320633571543,
					25.014522696522988
				],
				[
					0.7580158392885892,
					24.2565068572344
				],
				[
					1.5160316785771784,
					23.49849101794581
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07989398390054703,
				0.1156531348824501,
				0.1567138433456421,
				0.1867707222700119,
				0.1590961068868637,
				0.10546572506427765,
				0.09643896669149399,
				0.133880615234375,
				0.1634853184223175,
				0.1565290242433548,
				0.030385924503207207,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1925317966,
			"isDeleted": false,
			"id": "WjeZR-vfZkJX6oX44YwS-",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 377.35285923461134,
			"y": 434.58998021112325,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 18.192380142925742,
			"height": 13.644285107194378,
			"seed": 148869094,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7580158392885892,
					-0.7580158392885892
				],
				[
					1.5160316785771215,
					-1.5160316785771215
				],
				[
					3.0320633571543,
					-2.2740475178657107
				],
				[
					3.0320633571543,
					-3.790079196442889
				],
				[
					0.7580158392885892,
					-3.0320633571543
				],
				[
					-2.2740475178657107,
					0.7580158392885892
				],
				[
					-2.2740475178657107,
					3.790079196442889
				],
				[
					3.790079196442889,
					5.3061108750200106
				],
				[
					9.0961900714629,
					1.5160316785771784
				],
				[
					9.854205910751432,
					-2.2740475178657107
				],
				[
					8.338174232174367,
					-3.0320633571543
				],
				[
					8.338174232174367,
					-2.2740475178657107
				],
				[
					9.854205910751432,
					0.7580158392885892
				],
				[
					13.644285107194321,
					4.548095035731478
				],
				[
					15.918332625060032,
					9.0961900714629
				],
				[
					14.402300946482967,
					9.854205910751489
				],
				[
					9.854205910751432,
					7.580158392885778
				],
				[
					9.854205910751432,
					6.822142553597189
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06845797598361969,
				0.07543032616376877,
				0.13358426094055176,
				0.14696304500102997,
				0.13142791390419006,
				0.15684786438941956,
				0.19398842751979828,
				0.17805099487304688,
				0.1581810563802719,
				0.12430743128061295,
				0.12073541432619095,
				0.16495895385742188,
				0.18729110062122345,
				0.2118425965309143,
				0.2812920808792114,
				0.31109878420829773,
				0.07142025977373123,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 35,
			"versionNonce": 373702290,
			"isDeleted": false,
			"id": "SXtw7xGNY9eeE4D0U_9WG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 416.76968287761724,
			"y": 432.31593269325754,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.096190071462956,
			"height": 1.5160316785771784,
			"seed": 1119084774,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.758015839288646,
					0
				],
				[
					7.580158392885778,
					-1.5160316785771784
				],
				[
					9.096190071462956,
					-1.5160316785771784
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.2794239819049835,
				0.1547674536705017,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 120597390,
			"isDeleted": false,
			"id": "20Zk2aCDPyuceTC4AcJGu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 430.4139679848116,
			"y": 427.0098218182375,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.612221750040021,
			"height": 8.33817423217431,
			"seed": 1701613862,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7580158392885892
				],
				[
					-0.7580158392885323,
					-1.5160316785771784
				],
				[
					0.758015839288646,
					-1.5160316785771784
				],
				[
					6.0641267143086,
					0
				],
				[
					9.854205910751489,
					3.790079196442832
				],
				[
					8.33817423217431,
					6.822142553597132
				],
				[
					4.548095035731421,
					6.822142553597132
				],
				[
					3.0320633571543567,
					5.3061108750200106
				],
				[
					3.0320633571543567,
					5.3061108750200106
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.17457400262355804,
				0.23903000354766846,
				0.28577300906181335,
				0.2687135636806488,
				0.2865821123123169,
				0.32965004444122314,
				0.0735933855175972,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 37,
			"versionNonce": 1675926610,
			"isDeleted": false,
			"id": "6lYtC6nYyy_BjY_56QUg7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 452.3964273241803,
			"y": 423.21974262179464,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.5160316785771784,
			"height": 15.1603167857715,
			"seed": 1768051942,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7580158392885892
				],
				[
					0,
					1.5160316785771215
				],
				[
					0,
					11.37023758932861
				],
				[
					1.5160316785771784,
					14.40230094648291
				],
				[
					1.5160316785771784,
					13.644285107194321
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1974100023508072,
				0.24389199912548065,
				0.028438353911042213,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 796887502,
			"isDeleted": false,
			"id": "EY3KbY6Y2hW9vuzk6o1uj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 460.7346015563546,
			"y": 426.25180597894894,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.854205910751489,
			"height": 15.1603167857715,
			"seed": 1709437862,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7580158392885323,
					1.5160316785771215
				],
				[
					-2.2740475178657107,
					4.548095035731421
				],
				[
					-0.7580158392885323,
					9.854205910751489
				],
				[
					3.790079196442889,
					11.37023758932861
				],
				[
					6.822142553597246,
					7.580158392885721
				],
				[
					7.580158392885778,
					0
				],
				[
					6.0641267143086,
					-3.790079196442889
				],
				[
					0,
					2.2740475178657107
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
				0.09579199552536011,
				0.13440798223018646,
				0.19632598757743835,
				0.20229706168174744,
				0.1756662279367447,
				0.19760999083518982,
				0.1994207799434662,
				0.0547567754983902,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 35,
			"versionNonce": 829506066,
			"isDeleted": false,
			"id": "hQyYFLqZcFemiObxSA2Nk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 475.13690250283764,
			"y": 429.28386933610324,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.032063357154243,
			"height": 0,
			"seed": 765094566,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					3.032063357154243,
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
				0.1257876306772232,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 38,
			"versionNonce": 1254694926,
			"isDeleted": false,
			"id": "GwAipYBnFcVXAq-gQU2mS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 487.26515593145484,
			"y": 420.18767926464034,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.758015839288646,
			"height": 16.67634846434862,
			"seed": 373621478,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7580158392885323
				],
				[
					0,
					2.2740475178657107
				],
				[
					0,
					7.580158392885721
				],
				[
					-0.758015839288646,
					12.886269267905789
				],
				[
					0,
					16.67634846434862
				],
				[
					0,
					16.67634846434862
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.19426687061786652,
				0.2711170017719269,
				0.303617000579834,
				0.1297065168619156,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 2044932050,
			"isDeleted": false,
			"id": "owQeYlgmGRoqKnKVs2YRP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 504.6995202350921,
			"y": 419.42966342535175,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.096190071462843,
			"height": 15.918332625060089,
			"seed": 1451703526,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.5160316785771784,
					0
				],
				[
					-3.0320633571543567,
					0
				],
				[
					-6.822142553597246,
					2.2740475178657107
				],
				[
					-7.580158392885778,
					5.3061108750200106
				],
				[
					-4.548095035731535,
					7.580158392885778
				],
				[
					-0.758015839288646,
					9.854205910751489
				],
				[
					1.5160316785770647,
					12.1282534286172
				],
				[
					0,
					15.1603167857715
				],
				[
					-4.548095035731535,
					15.918332625060089
				],
				[
					-7.580158392885778,
					15.1603167857715
				],
				[
					-7.580158392885778,
					13.644285107194378
				],
				[
					-7.580158392885778,
					12.886269267905789
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06500168144702911,
				0.15076464414596558,
				0.14701712131500244,
				0.1319967359304428,
				0.1223798543214798,
				0.1894371658563614,
				0.28459909558296204,
				0.30720043182373047,
				0.2560461759567261,
				0.06473114341497421,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 39,
			"versionNonce": 1829105230,
			"isDeleted": false,
			"id": "_WncXosWVh_I5rEVpOIJj",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 472.86285498497193,
			"y": 429.28386933610324,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.0641267143086,
			"height": 0.7580158392885892,
			"seed": 199135846,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.758015839288646,
					0
				],
				[
					-0.758015839288646,
					-0.7580158392885892
				],
				[
					0.7580158392885323,
					-0.7580158392885892
				],
				[
					3.032063357154243,
					-0.7580158392885892
				],
				[
					5.306110875019954,
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
				0.09392355382442474,
				0.16852343082427979,
				0.25463998317718506,
				0.29430797696113586,
				0.10894772410392761,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 38,
			"versionNonce": 1095853458,
			"isDeleted": false,
			"id": "WTlIvZzyGJ_VPNQUeNLxM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 518.3438053422864,
			"y": 428.52585349681465,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.338174232174424,
			"height": 11.37023758932861,
			"seed": 1461637030,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.758015839288646,
					5.3061108750200106
				],
				[
					0.758015839288646,
					9.0961900714629
				],
				[
					2.2740475178658244,
					6.0641267143086
				],
				[
					6.0641267143086,
					-0.7580158392885892
				],
				[
					8.338174232174424,
					-2.2740475178657107
				],
				[
					8.338174232174424,
					-2.2740475178657107
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.19583648443222046,
				0.17262579500675201,
				0.14443160593509674,
				0.154866024851799,
				0.023418335244059563,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 49,
			"versionNonce": 1125053582,
			"isDeleted": false,
			"id": "b3MaK1qx548hqXF6AbERu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 528.9560270923265,
			"y": 430.79990101468036,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.676348464348735,
			"height": 9.854205910751489,
			"seed": 993544614,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7580158392885323,
					0
				],
				[
					2.2740475178657107,
					-0.7580158392885323
				],
				[
					3.032063357154243,
					-0.7580158392885323
				],
				[
					5.306110875019954,
					-2.2740475178657107
				],
				[
					4.548095035731421,
					-4.548095035731421
				],
				[
					0.7580158392885323,
					-2.2740475178657107
				],
				[
					-0.758015839288646,
					3.0320633571543
				],
				[
					2.2740475178657107,
					5.306110875020067
				],
				[
					6.0641267143086,
					3.0320633571543
				],
				[
					6.822142553597132,
					1.5160316785771784
				],
				[
					7.580158392885778,
					3.790079196442889
				],
				[
					9.854205910751489,
					5.306110875020067
				],
				[
					14.40230094648291,
					3.790079196442889
				],
				[
					15.918332625060089,
					-0.7580158392885323
				],
				[
					13.644285107194378,
					-3.790079196442832
				],
				[
					9.096190071462843,
					-2.2740475178657107
				],
				[
					8.33817423217431,
					-2.2740475178657107
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.09406072646379471,
				0.14082956314086914,
				0.18422533571720123,
				0.1532893031835556,
				0.10122671723365784,
				0.13970254361629486,
				0.13964389264583588,
				0.08032558858394623,
				0.07647198438644409,
				0.13772030174732208,
				0.18290124833583832,
				0.22758565843105316,
				0.2672518789768219,
				0.2397136241197586,
				0.019278930500149727,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 37,
			"versionNonce": 1894966098,
			"isDeleted": false,
			"id": "Ki5qUdswvbFD9d7EoMhGA",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 543.3583280388094,
			"y": 433.0739485325461,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.580158392885778,
			"height": 4.548095035731478,
			"seed": 358750054,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7580158392885323,
					0
				],
				[
					1.5160316785771784,
					0
				],
				[
					3.032063357154243,
					0
				],
				[
					6.822142553597132,
					-3.0320633571543
				],
				[
					7.580158392885778,
					-4.548095035731478
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08602999895811081,
				0.09205999970436096,
				0.16649581491947174,
				0.06178076192736626,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 37,
			"versionNonce": 1990013646,
			"isDeleted": false,
			"id": "BTGsOxp2P-Abw11tF8h_U",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 557.0026131460038,
			"y": 409.57545751460026,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.5160316785771784,
			"height": 28.804601892965877,
			"seed": 1445955110,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7580158392885892
				],
				[
					-1.5160316785771784,
					6.822142553597189
				],
				[
					-1.5160316785771784,
					21.2244435000801
				],
				[
					0,
					28.804601892965877
				],
				[
					0,
					28.046586053677288
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.17480498552322388,
				0.34125572443008423,
				0.16327856481075287,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 39,
			"versionNonce": 857647378,
			"isDeleted": false,
			"id": "aEv7FsL2pqk8I1E6e7Vaz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 331.0282892358057,
			"y": 485.4691243651253,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.29661886340682,
			"height": 15.084761569830619,
			"seed": 1878068454,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7542380784915395
				],
				[
					0.7542380784914826,
					6.788142706423798
				],
				[
					1.508476156983022,
					12.067809255864518
				],
				[
					1.508476156983022,
					11.313571177372978
				],
				[
					1.508476156983022,
					5.279666549440719
				],
				[
					7.542380784915281,
					-3.016952313966101
				],
				[
					8.29661886340682,
					-3.016952313966101
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1649632304906845,
				0.1867816150188446,
				0.15706034004688263,
				0.14140115678310394,
				0.17382201552391052,
				0.13937072455883026,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 40,
			"versionNonce": 306817294,
			"isDeleted": false,
			"id": "k6UukwC9WcKRabxFbtwx7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 343.09609849167015,
			"y": 486.9776005221084,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.788142706423741,
			"height": 9.05085694189836,
			"seed": 1582004774,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7542380784915395,
					0
				],
				[
					1.508476156983079,
					0
				],
				[
					2.2627142354746184,
					-1.508476156983079
				],
				[
					2.2627142354746184,
					-3.016952313966101
				],
				[
					-0.7542380784915395,
					-1.508476156983079
				],
				[
					-2.2627142354745615,
					3.7711903924576404
				],
				[
					3.7711903924576404,
					6.033904627932259
				],
				[
					4.52542847094918,
					4.52542847094918
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1058179959654808,
				0.17747101187705994,
				0.17525921761989594,
				0.15054373443126678,
				0.19545315206050873,
				0.1572495400905609,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1330362066,
			"isDeleted": false,
			"id": "UmhljGeEVN9K1387mKtE0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 349.88424119809395,
			"y": 484.7148862866338,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.8050950203899,
			"height": 26.398332747203597,
			"seed": 982786726,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7542380784914826,
					3.016952313966101
				],
				[
					3.7711903924576404,
					15.838999648322101
				],
				[
					3.7711903924576404,
					23.38138043323744
				],
				[
					1.508476156983022,
					21.11866619776282
				],
				[
					0,
					11.313571177372921
				],
				[
					2.2627142354745615,
					1.508476156983022
				],
				[
					7.542380784915281,
					-3.016952313966158
				],
				[
					9.8050950203899,
					-2.2627142354746184
				],
				[
					9.8050950203899,
					3.7711903924576404
				],
				[
					6.788142706423741,
					10.559333098881382
				],
				[
					6.033904627932202,
					9.05085694189836
				],
				[
					6.033904627932202,
					8.29661886340682
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.17687201499938965,
				0.1967482566833496,
				0.2188614159822464,
				0.22103235125541687,
				0.12264126539230347,
				0.13000188767910004,
				0.18601424992084503,
				0.2391456961631775,
				0.30873072147369385,
				0.2817838490009308,
				0.05964227393269539,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 39,
			"versionNonce": 1703761742,
			"isDeleted": false,
			"id": "6RfEb2o5fOBVQ9R3kTvtg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 363.4605266109415,
			"y": 471.13860087378623,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.52542847094918,
			"height": 25.644094668712057,
			"seed": 1353869350,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1.508476156983022
				],
				[
					0,
					-2.2627142354745615
				],
				[
					0,
					3.016952313966158
				],
				[
					1.508476156983079,
					15.084761569830619
				],
				[
					3.016952313966101,
					23.381380433237496
				],
				[
					3.7711903924576404,
					20.364428119271338
				],
				[
					4.52542847094918,
					19.6101900407798
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.11635800451040268,
				0.2387939989566803,
				0.3005240261554718,
				0.2921295464038849,
				0.021962860599160194,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 101780626,
			"isDeleted": false,
			"id": "K6UuSKxH3wTolMZJ2nOzt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 368.7401931603822,
			"y": 486.9776005221084,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.542380784915281,
			"height": 10.559333098881439,
			"seed": 254291302,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7542380784915395,
					0.7542380784915395
				],
				[
					-0.7542380784915395,
					3.016952313966158
				],
				[
					0.7542380784915395,
					5.279666549440719
				],
				[
					4.525428470949123,
					6.033904627932259
				],
				[
					6.788142706423741,
					3.016952313966158
				],
				[
					6.788142706423741,
					-1.508476156983079
				],
				[
					4.525428470949123,
					-4.52542847094918
				],
				[
					1.508476156983022,
					-3.016952313966101
				],
				[
					0,
					1.508476156983079
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
				0.12985000014305115,
				0.16603979468345642,
				0.19486822187900543,
				0.26188716292381287,
				0.2649003863334656,
				0.2234899252653122,
				0.16285230219364166,
				0.022655975073575974,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 36,
			"versionNonce": 1757494670,
			"isDeleted": false,
			"id": "mPECXUphHMTCH_vV9zjTv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 373.2656216313313,
			"y": 486.9776005221084,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.5423807849153945,
			"height": 4.52542847094918,
			"seed": 1620871078,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7542380784915395,
					1.508476156983079
				],
				[
					1.508476156983079,
					2.2627142354746184
				],
				[
					6.788142706423855,
					4.52542847094918
				],
				[
					7.5423807849153945,
					4.52542847094918
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1758967638015747,
				0.14285004138946533,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 39,
			"versionNonce": 1831184978,
			"isDeleted": false,
			"id": "ic1nmtWjRleJQarHtJor1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 384.5791928087043,
			"y": 482.4521720511592,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.559333098881439,
			"height": 9.05085694189836,
			"seed": 1706562342,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.508476156983079,
					0.7542380784915395
				],
				[
					-3.016952313966044,
					2.2627142354746184
				],
				[
					-3.7711903924575836,
					3.7711903924576404
				],
				[
					-3.016952313966044,
					7.542380784915338
				],
				[
					1.508476156983079,
					9.05085694189836
				],
				[
					6.033904627932316,
					7.542380784915338
				],
				[
					6.788142706423855,
					6.788142706423798
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.1239449754357338,
				0.18839599192142487,
				0.23622000217437744,
				0.3238679766654968,
				0.3425416350364685,
				0.19278189539909363,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 555637710,
			"isDeleted": false,
			"id": "VoPlN-DGlj43MjYnNfWmH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 391.36733551512816,
			"y": 484.7148862866338,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.822047334355943,
			"height": 10.559333098881382,
			"seed": 1728411750,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7542380784914258,
					0
				],
				[
					2.2627142354745047,
					-0.7542380784915395
				],
				[
					3.016952313966044,
					-3.016952313966158
				],
				[
					2.2627142354745047,
					-4.52542847094918
				],
				[
					0,
					-0.7542380784915395
				],
				[
					-0.7542380784915395,
					3.7711903924576404
				],
				[
					4.525428470949123,
					6.033904627932202
				],
				[
					11.313571177372864,
					1.508476156983022
				],
				[
					12.067809255864404,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13497400283813477,
				0.1815979927778244,
				0.13508501648902893,
				0.1647946536540985,
				0.24945712089538574,
				0.24354101717472076,
				0.03169317543506622,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 1264619538,
			"isDeleted": false,
			"id": "l2NzvCxJp8n9TeqA8OEwT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 404.1893828494841,
			"y": 464.3504581673625,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.8050950203899,
			"height": 27.90680890418662,
			"seed": 1187136550,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7542380784915395,
					-0.7542380784915395
				],
				[
					-0.7542380784915395,
					4.52542847094918
				],
				[
					0.7542380784915395,
					16.59323772681364
				],
				[
					0,
					23.38138043323744
				],
				[
					0,
					21.87290427625436
				],
				[
					1.508476156983079,
					17.34747580530518
				],
				[
					6.033904627932316,
					15.838999648322158
				],
				[
					9.05085694189836,
					20.364428119271338
				],
				[
					9.05085694189836,
					26.39833274720354
				],
				[
					5.279666549440776,
					27.15257082569508
				],
				[
					1.508476156983079,
					24.13561851172898
				],
				[
					2.2627142354746184,
					24.13561851172898
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08878307789564133,
				0.20014630258083344,
				0.25303319096565247,
				0.23214422166347504,
				0.20382638275623322,
				0.1488754004240036,
				0.1968935877084732,
				0.2709786891937256,
				0.34052032232284546,
				0.35872289538383484,
				0.06828460842370987,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 38,
			"versionNonce": 79540750,
			"isDeleted": false,
			"id": "82zsbIOhmyaE3kZiiOQ64",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 420.0283824978063,
			"y": 465.10469624585403,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7542380784914258,
			"height": 29.415285061169698,
			"seed": 1526720934,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-2.2627142354746184
				],
				[
					0,
					-1.508476156983079
				],
				[
					0.7542380784914258,
					8.29661886340682
				],
				[
					0.7542380784914258,
					24.13561851172898
				],
				[
					0.7542380784914258,
					27.15257082569508
				],
				[
					0.7542380784914258,
					26.39833274720354
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.06816799938678741,
				0.19524569809436798,
				0.2846370339393616,
				0.3488510251045227,
				0.09383651614189148,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1958264274,
			"isDeleted": false,
			"id": "j-wp33-TFsu9J0V0AHwZ_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 424.55381096875544,
			"y": 485.4691243651253,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.576285412847596,
			"height": 11.313571177372978,
			"seed": 1491035046,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7542380784915395,
					0
				],
				[
					3.016952313966158,
					0.7542380784915395
				],
				[
					6.788142706423741,
					0.7542380784915395
				],
				[
					7.542380784915281,
					-3.016952313966101
				],
				[
					4.525428470949237,
					-3.7711903924576404
				],
				[
					1.508476156983079,
					1.508476156983079
				],
				[
					3.7711903924576973,
					7.542380784915338
				],
				[
					11.313571177372978,
					7.542380784915338
				],
				[
					12.822047334356057,
					6.033904627932259
				],
				[
					13.576285412847596,
					5.279666549440719
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.13189397752285004,
				0.2345399707555771,
				0.21475443243980408,
				0.18304452300071716,
				0.24498847126960754,
				0.39594998955726624,
				0.30571287870407104,
				0.22292788326740265,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 108,
			"versionNonce": 1587036238,
			"isDeleted": false,
			"id": "kyJyCdpqzS_dgGp6GDewQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -135.65046495449553,
			"y": 471.6445976219974,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 9.607718632369597,
			"seed": 1089329830,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7390552794130372
				],
				[
					0,
					1.4781105588260743
				],
				[
					0,
					5.912442235304411
				],
				[
					0,
					8.86866335295656
				],
				[
					0,
					9.607718632369597
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.16079400479793549,
				0.1609259992837906,
				0.18571554124355316,
				0.01701556332409382,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 106,
			"versionNonce": 642069394,
			"isDeleted": false,
			"id": "znBoFtXDZD8Mc5ooNOvrF",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -137.1285755133216,
			"y": 463.51498954845385,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7390552794130372,
			"height": 0,
			"seed": 879980902,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7390552794130372,
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
				0.05722512677311897,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 112,
			"versionNonce": 847709838,
			"isDeleted": false,
			"id": "Dv6aCAqoWIbiaUMDb7v9z",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -132.69424383684333,
			"y": 471.6445976219974,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.390552794130485,
			"height": 8.86866335295656,
			"seed": 1256313254,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7390552794130372,
					1.4781105588260743
				],
				[
					2.2171658382391115,
					6.651497514717448
				],
				[
					2.9562211176522055,
					8.129608073543523
				],
				[
					3.6952763970652427,
					3.6952763970652427
				],
				[
					5.912442235304354,
					-0.7390552794130372
				],
				[
					7.390552794130485,
					0
				],
				[
					7.390552794130485,
					5.912442235304411
				],
				[
					6.651497514717391,
					7.390552794130485
				],
				[
					6.651497514717391,
					7.390552794130485
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.13421228528022766,
				0.1599254459142685,
				0.11714526265859604,
				0.06978271156549454,
				0.06241525337100029,
				0.11823642253875732,
				0.14847701787948608,
				0.05450695753097534,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 114,
			"versionNonce": 1648161106,
			"isDeleted": false,
			"id": "fWTj4GKx1goYIi5Hkv4jV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -121.60841464564766,
			"y": 471.6445976219974,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.390552794130485,
			"height": 9.607718632369597,
			"seed": 1638983014,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7390552794130372,
					0.7390552794130372
				],
				[
					-0.7390552794130372,
					2.2171658382391115
				],
				[
					-1.4781105588260743,
					5.912442235304411
				],
				[
					1.4781105588261312,
					7.390552794130485
				],
				[
					4.43433167647828,
					6.651497514717448
				],
				[
					5.912442235304411,
					2.9562211176522055
				],
				[
					5.173386955891317,
					-0.7390552794130372
				],
				[
					2.9562211176522055,
					-2.2171658382391115
				],
				[
					0,
					1.4781105588260743
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
				0.050736479461193085,
				0.06555423140525818,
				0.1641870141029358,
				0.14705535769462585,
				0.149673193693161,
				0.16135388612747192,
				0.15272562205791473,
				0.14930224418640137,
				0,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 107,
			"versionNonce": 558040270,
			"isDeleted": false,
			"id": "rhutU7n8x17oZd5bkg3T0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -116.43502768975634,
			"y": 475.3398740190626,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.43433167647828,
			"height": 2.2171658382391684,
			"seed": 863649702,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.739055279413094,
					1.4781105588260743
				],
				[
					4.43433167647828,
					2.2171658382391684
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
				0.0945986658334732,
				0.1577649563550949,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 111,
			"versionNonce": 1274476306,
			"isDeleted": false,
			"id": "hGOiKF6pnyircXCfh0pQV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -103.87108793973454,
			"y": 467.9493212249322,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.390552794130485,
			"height": 11.085829191195728,
			"seed": 350997286,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7390552794130372,
					0
				],
				[
					-2.2171658382391115,
					-0.739055279413094
				],
				[
					-2.9562211176521487,
					0
				],
				[
					-4.43433167647828,
					1.4781105588260743
				],
				[
					-4.43433167647828,
					7.3905527941304285
				],
				[
					-2.2171658382391115,
					10.346773911782634
				],
				[
					2.2171658382391684,
					8.868663352956503
				],
				[
					2.9562211176522055,
					8.129608073543466
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.06388448923826218,
				0.1298452466726303,
				0.1680220067501068,
				0.25479400157928467,
				0.289760023355484,
				0.09290701150894165,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 110,
			"versionNonce": 1281702670,
			"isDeleted": false,
			"id": "ygOwSso-qixTcitAOhamR",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -96.48053514560405,
			"y": 469.42743178375827,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.607718632369597,
			"height": 8.86866335295656,
			"seed": 842216358,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7390552794130372,
					0
				],
				[
					-2.2171658382391684,
					0.7390552794130372
				],
				[
					-2.9562211176522055,
					1.4781105588260743
				],
				[
					-3.6952763970652427,
					6.651497514717391
				],
				[
					-0.7390552794130372,
					8.86866335295656
				],
				[
					5.173386955891317,
					6.651497514717391
				],
				[
					5.912442235304354,
					5.912442235304354
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.07475659251213074,
				0.13632982969284058,
				0.2365259975194931,
				0.282010018825531,
				0.10299429297447205,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 112,
			"versionNonce": 65684690,
			"isDeleted": false,
			"id": "jFM4Yr102_91XUdK5K0js",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -85.39470595440838,
			"y": 470.1664870631713,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.86866335295656,
			"height": 8.86866335295656,
			"seed": 1607469286,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.739055279413094,
					0
				],
				[
					1.4781105588261312,
					0
				],
				[
					1.4781105588261312,
					-0.7390552794130372
				],
				[
					0,
					-1.4781105588260743
				],
				[
					-2.9562211176521487,
					1.4781105588260743
				],
				[
					-4.43433167647828,
					5.173386955891317
				],
				[
					-1.4781105588260743,
					7.390552794130485
				],
				[
					3.6952763970652427,
					5.912442235304354
				],
				[
					4.43433167647828,
					5.173386955891317
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11031130701303482,
				0.17385873198509216,
				0.22049188613891602,
				0.18391866981983185,
				0.19970138370990753,
				0.29521098732948303,
				0.2764135003089905,
				0.07953183352947235,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 113,
			"versionNonce": 979806542,
			"isDeleted": false,
			"id": "mKQP_YxUt0iKt8eZisZJL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -72.83076620438658,
			"y": 466.47121066610606,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.912442235304354,
			"height": 11.085829191195728,
			"seed": 475538598,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7390552794130372,
					0
				],
				[
					-1.4781105588260743,
					0.7390552794130372
				],
				[
					-2.9562211176522055,
					1.4781105588261312
				],
				[
					-4.43433167647828,
					3.6952763970652427
				],
				[
					-0.7390552794130372,
					6.651497514717391
				],
				[
					1.4781105588260743,
					8.86866335295656
				],
				[
					0.7390552794130372,
					11.085829191195728
				],
				[
					-2.9562211176522055,
					11.085829191195728
				],
				[
					-2.9562211176522055,
					10.346773911782634
				],
				[
					-2.9562211176522055,
					9.607718632369597
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07072900235652924,
				0.10305099189281464,
				0.17704598605632782,
				0.2152578979730606,
				0.19678470492362976,
				0.192118838429451,
				0.27269285917282104,
				0.3052021265029907,
				0.007580749690532684,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 116,
			"versionNonce": 61725330,
			"isDeleted": false,
			"id": "zhJo3USxOcFr6N3hg3n8r",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -66.17926868966913,
			"y": 470.1664870631713,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.607718632369597,
			"height": 8.86866335295656,
			"seed": 1617763238,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.739055279413094,
					0
				],
				[
					-1.4781105588261312,
					0
				],
				[
					-2.9562211176522055,
					0
				],
				[
					-3.6952763970652427,
					0.7390552794130372
				],
				[
					-0.739055279413094,
					3.695276397065186
				],
				[
					1.4781105588260743,
					7.390552794130485
				],
				[
					0.7390552794130372,
					8.86866335295656
				],
				[
					-1.4781105588261312,
					7.390552794130485
				],
				[
					-0.739055279413094,
					4.43433167647828
				],
				[
					2.2171658382391115,
					3.695276397065186
				],
				[
					4.43433167647828,
					7.390552794130485
				],
				[
					5.173386955891317,
					8.86866335295656
				],
				[
					5.912442235304354,
					8.129608073543523
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.05890197679400444,
				0.10239312797784805,
				0.19804000854492188,
				0.19484835863113403,
				0.19484299421310425,
				0.26547008752822876,
				0.21481060981750488,
				0.11439669877290726,
				0.11955349892377853,
				0.25814563035964966,
				0.12183499336242676,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 107,
			"versionNonce": 983584654,
			"isDeleted": false,
			"id": "RAicxeETf7F3Ka5zkO8W1",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -58.7887158955387,
			"y": 464.2540448278669,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4781105588260743,
			"height": 0.7390552794130372,
			"seed": 129010790,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7390552794130372,
					-0.7390552794130372
				],
				[
					-1.4781105588260743,
					-0.7390552794130372
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
				0.18999499082565308,
				0.15660831332206726,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 115,
			"versionNonce": 2046343250,
			"isDeleted": false,
			"id": "-3CvmrMOqAyMIe2VNMZUT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -54.35438421906042,
			"y": 449.472939239606,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.86866335295656,
			"height": 28.08410061769581,
			"seed": 380733414,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.739055279413094
				],
				[
					0.7390552794130372,
					2.9562211176522055
				],
				[
					1.4781105588261312,
					8.129608073543523
				],
				[
					2.2171658382391684,
					16.259216147087045
				],
				[
					0.7390552794130372,
					19.21543726473925
				],
				[
					2.9562211176522055,
					17.73732670591312
				],
				[
					7.390552794130485,
					18.476381985326213
				],
				[
					8.86866335295656,
					22.910713661804436
				],
				[
					6.651497514717448,
					27.345045338282716
				],
				[
					1.4781105588261312,
					28.08410061769581
				],
				[
					0.7390552794130372,
					25.127879500043605
				],
				[
					1.4781105588261312,
					24.38882422063051
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.10286913812160492,
				0.13814443349838257,
				0.1712474375963211,
				0.21372641623020172,
				0.20035113394260406,
				0.09626928716897964,
				0.1411580741405487,
				0.24361783266067505,
				0.3171980082988739,
				0.23480533063411713,
				0.028006255626678467,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 109,
			"versionNonce": 1229663694,
			"isDeleted": false,
			"id": "n9PzNSM0Gwm67q6Fv_tcd",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -42.529499748451656,
			"y": 449.472939239606,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4781105588260743,
			"height": 27.345045338282716,
			"seed": 966368614,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7390552794130372
				],
				[
					0,
					0.739055279413094
				],
				[
					0.7390552794130372,
					12.563939750021802
				],
				[
					1.4781105588260743,
					25.127879500043605
				],
				[
					1.4781105588260743,
					26.60599005886968
				],
				[
					1.4781105588260743,
					25.866934779456642
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.21061773598194122,
				0.32013097405433655,
				0.3691979944705963,
				0.027241790667176247,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 112,
			"versionNonce": 648142354,
			"isDeleted": false,
			"id": "kxhVkI7joIlQAhBD3Q2Qv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -38.83422335138641,
			"y": 472.3836529014104,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 14.042050308847877,
			"height": 11.085829191195671,
			"seed": 1069111142,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4781105588260743,
					1.4781105588260743
				],
				[
					2.9562211176521487,
					2.2171658382391684
				],
				[
					7.3905527941304285,
					1.4781105588260743
				],
				[
					8.129608073543466,
					-0.7390552794130372
				],
				[
					5.912442235304354,
					-2.9562211176521487
				],
				[
					2.9562211176521487,
					1.4781105588260743
				],
				[
					4.43433167647828,
					8.129608073543523
				],
				[
					14.042050308847877,
					8.129608073543523
				],
				[
					14.042050308847877,
					7.390552794130485
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.08625400066375732,
				0.11303365975618362,
				0.22156000137329102,
				0.18195010721683502,
				0.14891788363456726,
				0.2099451869726181,
				0.326192170381546,
				0.1120094284415245,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 108,
			"versionNonce": 1937785870,
			"isDeleted": false,
			"id": "MghAfqcqffXodisO-5WZl",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -115.69597241034324,
			"y": 471.6445976219974,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.173386955891374,
			"height": 7.390552794130485,
			"seed": 92242726,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.739055279413094,
					0
				],
				[
					-0.739055279413094,
					2.2171658382391115
				],
				[
					0,
					4.43433167647828
				],
				[
					3.695276397065186,
					7.390552794130485
				],
				[
					4.43433167647828,
					7.390552794130485
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.15140999853610992,
				0.1813259869813919,
				0.06318185478448868,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 109,
			"versionNonce": 916474834,
			"isDeleted": false,
			"id": "5MIffLb_soycltmIaZaa7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -135.65046495449553,
			"y": 507.1192510338236,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4781105588261312,
			"height": 16.998271426500082,
			"seed": 361736678,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					2.9562211176521487
				],
				[
					0,
					6.651497514717448
				],
				[
					0.7390552794130372,
					11.824884470608708
				],
				[
					0.7390552794130372,
					16.998271426500082
				],
				[
					1.4781105588261312,
					16.998271426500082
				],
				[
					1.4781105588261312,
					16.259216147087045
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14034900069236755,
				0.19392001628875732,
				0.22761398553848267,
				0.2535512149333954,
				0.05386636406183243,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 114,
			"versionNonce": 993563214,
			"isDeleted": false,
			"id": "vdSWmgFUkURF1zZmG1EHO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -128.25991216036505,
			"y": 512.292637989715,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.129608073543523,
			"height": 16.259216147087045,
			"seed": 1937433574,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7390552794130372,
					0.7390552794130372
				],
				[
					-1.4781105588260743,
					2.2171658382391115
				],
				[
					-2.2171658382391684,
					4.434331676478223
				],
				[
					-1.4781105588260743,
					10.346773911782634
				],
				[
					2.2171658382391115,
					11.824884470608708
				],
				[
					5.173386955891317,
					5.912442235304297
				],
				[
					5.912442235304354,
					-1.478110558826188
				],
				[
					2.9562211176522055,
					-4.434331676478337
				],
				[
					0,
					2.9562211176521487
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
				0.07193518429994583,
				0.1691739857196808,
				0.2385679930448532,
				0.2361873835325241,
				0.1915322244167328,
				0.1519668847322464,
				0.16431762278079987,
				0.04978674277663231,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 106,
			"versionNonce": 537592210,
			"isDeleted": false,
			"id": "RaO4OTixSm1rDeyKVvhlM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -115.69597241034324,
			"y": 515.2488591073671,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.912442235304354,
			"height": 6.651497514717448,
			"seed": 2046733862,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7390552794130372,
					1.4781105588260743
				],
				[
					5.912442235304354,
					6.651497514717448
				],
				[
					5.912442235304354,
					6.651497514717448
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.21162451803684235,
				0.07076333463191986,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 109,
			"versionNonce": 2068650126,
			"isDeleted": false,
			"id": "3U2p6A4QVlza4zvKBhcwZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -106.82730905738669,
			"y": 513.7707485485411,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.912442235304411,
			"height": 22.91071366180438,
			"seed": 2047809126,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.739055279413094,
					0.7390552794130372
				],
				[
					-0.739055279413094,
					2.2171658382391115
				],
				[
					-3.6952763970652427,
					11.824884470608708
				],
				[
					-5.173386955891374,
					21.432603102978305
				],
				[
					-5.912442235304411,
					22.91071366180438
				],
				[
					-5.173386955891374,
					22.171658382391342
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11987549066543579,
				0.2359953373670578,
				0.35006803274154663,
				0.3716049790382385,
				0.11515240371227264,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 121,
			"versionNonce": 2115567442,
			"isDeleted": false,
			"id": "YYz9whPxM0rkIRd7_Bt7D",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -102.3929773809084,
			"y": 515.9879143867802,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 15.520160867674008,
			"height": 9.607718632369597,
			"seed": 140890214,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.2171658382391115,
					-0.7390552794130372
				],
				[
					5.912442235304354,
					-2.9562211176521487
				],
				[
					6.651497514717391,
					-5.173386955891374
				],
				[
					2.2171658382391115,
					-4.434331676478337
				],
				[
					-1.4781105588261312,
					0
				],
				[
					0,
					2.9562211176521487
				],
				[
					3.695276397065186,
					2.9562211176521487
				],
				[
					7.3905527941304285,
					0
				],
				[
					7.3905527941304285,
					2.9562211176521487
				],
				[
					8.86866335295656,
					4.434331676478223
				],
				[
					11.824884470608708,
					3.695276397065186
				],
				[
					14.042050308847877,
					0.7390552794130372
				],
				[
					14.042050308847877,
					-2.9562211176521487
				],
				[
					11.824884470608708,
					-4.434331676478337
				],
				[
					8.86866335295656,
					-3.695276397065186
				],
				[
					5.912442235304354,
					-0.7390552794130372
				],
				[
					6.651497514717391,
					0.7390552794130372
				],
				[
					6.651497514717391,
					1.4781105588260743
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.20082001388072968,
				0.2541939914226532,
				0.18306522071361542,
				0.1410457193851471,
				0.1978379786014557,
				0.23006156086921692,
				0.189146026968956,
				0.11094497889280319,
				0.18606290221214294,
				0.23164664208889008,
				0.2511897385120392,
				0.2708522379398346,
				0.2596326768398285,
				0.28511562943458557,
				0.28452807664871216,
				0.19992907345294952,
				0.011893494054675102,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 108,
			"versionNonce": 1266079438,
			"isDeleted": false,
			"id": "QB32jbo4yqt8RS31xKWX0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -89.82903763088666,
			"y": 515.9879143867802,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 5.173386955891374,
			"height": 2.9562211176521487,
			"seed": 1921311078,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7390552794130372
				],
				[
					0.739055279413094,
					1.4781105588260743
				],
				[
					1.4781105588261312,
					2.2171658382391115
				],
				[
					5.173386955891374,
					2.9562211176521487
				],
				[
					5.173386955891374,
					2.9562211176521487
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.11412448436021805,
				0.17688800394535065,
				0.23335598409175873,
				0.11056075990200043,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 111,
			"versionNonce": 1830896914,
			"isDeleted": false,
			"id": "as0RMl1ogMp-FkkY-cbKs",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -83.91659539558225,
			"y": 513.031693269128,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.86866335295656,
			"height": 11.824884470608708,
			"seed": 1715048486,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7390552794130372
				],
				[
					0,
					1.4781105588260743
				],
				[
					1.4781105588260743,
					5.17338695589126
				],
				[
					2.2171658382391115,
					7.390552794130372
				],
				[
					2.2171658382391115,
					5.17338695589126
				],
				[
					3.6952763970652427,
					-0.7390552794130372
				],
				[
					8.129608073543466,
					-4.434331676478337
				],
				[
					8.86866335295656,
					-4.434331676478337
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07429897785186768,
				0.0865979939699173,
				0.1398012340068817,
				0.18092812597751617,
				0.1690315306186676,
				0.16297496855258942,
				0.12082324177026749,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 113,
			"versionNonce": 1682885902,
			"isDeleted": false,
			"id": "yFRfhm4Ti-IPGR5knb-sE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -67.65737924849526,
			"y": 510.07547215147576,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.129608073543523,
			"height": 10.346773911782634,
			"seed": 1744746662,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7390552794130372,
					-0.7390552794130372
				],
				[
					-1.4781105588260743,
					-1.4781105588260743
				],
				[
					-2.9562211176521487,
					-1.4781105588260743
				],
				[
					-4.43433167647828,
					0
				],
				[
					-1.4781105588260743,
					2.9562211176522624
				],
				[
					2.2171658382391684,
					7.390552794130485
				],
				[
					2.2171658382391684,
					8.86866335295656
				],
				[
					-3.6952763970652427,
					8.86866335295656
				],
				[
					-5.912442235304354,
					8.86866335295656
				],
				[
					-5.912442235304354,
					8.86866335295656
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07273361086845398,
				0.11674697697162628,
				0.16360799968242645,
				0.1887781023979187,
				0.19989939033985138,
				0.19187670946121216,
				0.31854474544525146,
				0.3589964807033539,
				0.15545471012592316,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 110,
			"versionNonce": 1721422546,
			"isDeleted": false,
			"id": "l3xYvU-7lvoTOSUDPMjSx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -137.1285755133216,
			"y": 564.0265075486282,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.651497514717391,
			"height": 11.085829191195785,
			"seed": 894807974,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7390552794130372
				],
				[
					0.7390552794130372,
					5.912442235304411
				],
				[
					2.9562211176522055,
					11.085829191195785
				],
				[
					5.173386955891317,
					8.86866335295656
				],
				[
					6.651497514717391,
					2.9562211176522624
				],
				[
					6.651497514717391,
					1.4781105588260743
				],
				[
					6.651497514717391,
					1.4781105588260743
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.15974600613117218,
				0.23196399211883545,
				0.29471200704574585,
				0.2656122148036957,
				0.20768018066883087,
				0.03937213122844696,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 80,
			"versionNonce": 55442254,
			"isDeleted": false,
			"id": "SBVCeYp-bixq9DBJ3UVmr",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -126.78180160153897,
			"y": 564.0265075486282,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.824884470608708,
			"height": 23.64976894121753,
			"seed": 830932198,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					4.434331676478337
				],
				[
					2.2171658382391684,
					15.520160867674008
				],
				[
					2.9562211176522055,
					23.64976894121753
				],
				[
					0,
					22.171658382391456
				],
				[
					-2.2171658382391115,
					12.56393975002186
				],
				[
					1.4781105588261312,
					4.434331676478337
				],
				[
					7.390552794130485,
					2.9562211176522624
				],
				[
					9.607718632369597,
					7.390552794130485
				],
				[
					8.129608073543523,
					10.346773911782634
				],
				[
					5.173386955891317,
					9.607718632369597
				],
				[
					4.43433167647828,
					8.86866335295656
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.18094198405742645,
				0.251116007566452,
				0.27363693714141846,
				0.2244807481765747,
				0.08709079027175903,
				0.06743991374969482,
				0.18472403287887573,
				0.24948202073574066,
				0.25070446729660034,
				0.06606051325798035,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 109,
			"versionNonce": 488417426,
			"isDeleted": false,
			"id": "Uc46oDe3orNdeD9ZBKPr5",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -112.7397512926911,
			"y": 549.2454019603673,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.9562211176522055,
			"height": 22.91071366180438,
			"seed": 1728392998,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.7390552794130372
				],
				[
					0,
					2.9562211176521487
				],
				[
					1.4781105588261312,
					14.04205030884782
				],
				[
					2.2171658382391684,
					22.171658382391342
				],
				[
					2.2171658382391684,
					20.693547823565268
				],
				[
					2.9562211176522055,
					19.95449254415223
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.24039599299430847,
				0.31351399421691895,
				0.34373319149017334,
				0.061904359608888626,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 108,
			"versionNonce": 1322082702,
			"isDeleted": false,
			"id": "icXrWZNJGWIUSr0J1U6bV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -106.82730905738669,
			"y": 565.5046181074542,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.4781105588260743,
			"height": 7.390552794130485,
			"seed": 1059531046,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7390552794131509
				],
				[
					0.7390552794130372,
					2.9562211176522624
				],
				[
					0.7390552794130372,
					5.173386955891374
				],
				[
					1.4781105588260743,
					7.390552794130485
				],
				[
					1.4781105588260743,
					7.390552794130485
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.18878726661205292,
				0.2608940005302429,
				0.19521133601665497,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 104,
			"versionNonce": 1482540626,
			"isDeleted": false,
			"id": "YoffmMkjoPrvonjDw3G5O",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -106.08825377797365,
			"y": 559.5921758721499,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7390552794130372,
			"height": 0.7390552794130372,
			"seed": 225316838,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7390552794130372,
					0.7390552794130372
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
			"version": 112,
			"versionNonce": 973471694,
			"isDeleted": false,
			"id": "XMaTa1gNY4zkJcPeO-Pyu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -100.91486682208233,
			"y": 564.0265075486282,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.390552794130485,
			"height": 8.129608073543523,
			"seed": 1869681062,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7390552794130372
				],
				[
					0,
					2.217165838239225
				],
				[
					2.2171658382391115,
					6.651497514717448
				],
				[
					3.6952763970652427,
					5.912442235304411
				],
				[
					4.43433167647828,
					0.7390552794130372
				],
				[
					6.651497514717391,
					0
				],
				[
					7.390552794130485,
					5.912442235304411
				],
				[
					7.390552794130485,
					8.129608073543523
				],
				[
					7.390552794130485,
					8.129608073543523
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.14834798872470856,
				0.19562000036239624,
				0.22898800671100616,
				0.1617880016565323,
				0.06354959309101105,
				0.1481819748878479,
				0.2658340036869049,
				0.11928176879882812,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 113,
			"versionNonce": 1362439186,
			"isDeleted": false,
			"id": "VnBQuZjDdMGzbCk7Ggyly",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -89.08998235147357,
			"y": 550.7235125191934,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.607718632369597,
			"height": 21.432603102978305,
			"seed": 1716004198,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7390552794130372
				],
				[
					0,
					2.9562211176521487
				],
				[
					1.4781105588260743,
					11.085829191195671
				],
				[
					2.2171658382391115,
					19.95449254415223
				],
				[
					1.4781105588260743,
					21.432603102978305
				],
				[
					2.2171658382391115,
					15.520160867674008
				],
				[
					6.651497514717391,
					8.129608073543523
				],
				[
					9.607718632369597,
					6.651497514717448
				],
				[
					9.607718632369597,
					8.129608073543523
				],
				[
					9.607718632369597,
					8.129608073543523
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.19333800673484802,
				0.2221427857875824,
				0.2653416395187378,
				0.2100290209054947,
				0.13808394968509674,
				0.17388449609279633,
				0.23647820949554443,
				0.017145447432994843,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 107,
			"versionNonce": 1762711054,
			"isDeleted": false,
			"id": "6ww1E8cFmTKayc-qMTMMS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -84.65565067499529,
			"y": 568.4608392251065,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 7.3905527941304285,
			"height": 2.9562211176521487,
			"seed": 414841958,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.4781105588260743
				],
				[
					1.4781105588260743,
					2.2171658382391115
				],
				[
					7.3905527941304285,
					2.9562211176521487
				],
				[
					7.3905527941304285,
					2.9562211176521487
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.1734504997730255,
				0.19887149333953857,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 113,
			"versionNonce": 228186578,
			"isDeleted": false,
			"id": "Hxcu3nLhLKwijDY6XfJYv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -69.13548980732133,
			"y": 560.331231151563,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.563939750021802,
			"height": 12.563939750021746,
			"seed": 233240550,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7390552794130372,
					0
				],
				[
					0.7390552794130372,
					0.7390552794130372
				],
				[
					5.173386955891317,
					3.695276397065186
				],
				[
					10.346773911782634,
					6.651497514717448
				],
				[
					11.824884470608765,
					7.390552794130485
				],
				[
					11.085829191195671,
					7.390552794130485
				],
				[
					8.86866335295656,
					8.129608073543523
				],
				[
					5.173386955891317,
					10.346773911782634
				],
				[
					2.2171658382391115,
					12.563939750021746
				],
				[
					2.9562211176522055,
					12.563939750021746
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": false,
			"pressures": [
				0.07999999821186066,
				0.07999999821186066,
				0.3266740143299103,
				0.39729800820350647,
				0.396546870470047,
				0.3249957263469696,
				0.30153748393058777,
				0.3244934678077698,
				0.3916698098182678,
				0.45402035117149353,
				0
			]
		},
		{
			"type": "freedraw",
			"version": 112,
			"versionNonce": 350676046,
			"isDeleted": false,
			"id": "OyhDCQXCVRbAqOGCWeCRx",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -56.57155005729953,
			"y": 558.8531205927369,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 9.607718632369597,
			"height": 12.563939750021746,
			"seed": 847318758,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709016405048,
			"link": null,
			"locked": false,
			"points": [
				[