#fheMcontrol
*fheMcontrol* is a gateway server for integrating fhem to mediola aio-Remote.

###Installation:

	python setup.py install
	systemctl enable fheMcontrol

###Configuration files:
- /etc/fheMcontrol/fheMcontrol.cfg
- /etc/fheMcontrol/fheMcontrolServer.xml

the file **fheMcontrol.cfg** is the daemon configuration file, here you setup the behavier of the gateway daemon.

Possible Options are:

- **listenPort** - setup the listening port of the daemon
- **listenIP** - setup the IP where to listen
- **fhemIP** - ip address of fhem (f.e. 127.0.0.1)
- **fhemtelnetPort** - on which port fhems telnet interface ist listening (normally 7072)
- **DEBUG** - enable debug mode or not [0|1]
- **mctlDefFile** - where to find the definition file to translate mediola commands to fhem commands.

###Commandline Arguments:

	fheMcontrolServer -h
	
	fheMcontrolServer v. 0.1 -  mediola gateway for fhem  - (c) Tobias D. Oestreicher
	---------------------------------------------------------------------------------
	Usage:
	  fheMcontrolServer [options]
	
	Options:
	  -c <configfile>       : define the configurationfile for the daemon
	  -d                    : enable debug output to stdout
	  -h                    : shows this helpmessage
	
	Example:
	  fheMcontrolServer -c /etc/fheMcontrol/fheMcontrol.cfg
	---------------------------------------------------------------------------------


### Definition Configuration File:

The definition configuration file */etc/fheMcontrol/fheMcontrolServer.xml* is for translating incoming mediola commands to fhem commands.
After you have to setup the executable commands before, this is also a security feature.
The definiton file contains two main sections.

- ExecuteCommand
- GetStates

The *ExecuteCommand* section requires within the `<Command>` tag to define the same name as you have defined within mediola. The name to use is `<devicegroup>`.`<devicename>`.`<command>`.
In the `<fhemCmd>`you have to define the command to execute in fhem.

In the *GetStates* section you also have to define in the `<Command>` tag the name you've used in mediola. This name corresponds to `<devicegroup>`.`<devicename>`.
Here are required to set `<fhemDev>`with the devicename used in fhem, the `<Reading>` which should be set to the requested information and the `<Type>` which can be either be

- Reading
- Internal
- Attribute
 

### Example definitions:

	<mctl>
		<ExecuteCommand>
			<Command name="Test.Wohnzimmer_Lampe.toggle">
				<fhemCmd>set Wohnzimmer_Lampe_Tisch toggle</fhemCmd>
			</Command>
			<Command name="Test.Wohnzimmer_Lampe2.toggle">
				<fhemCmd>set Wohnzimmer_Lampe_Couch toggle</fhemCmd>
			</Command>
		</ExecuteCommand>

		<GetStates>
			<Command name="Test.Wohnzimmer_Lampe">
				<Type>Reading</Type>
				<fhemDev>Wohnzimmer_Lampe_Tisch</fhemDev>
				<Reading>state</Reading>
			</Command>
		</GetStates>
	</mctl>
	
	
### Debugging:

For debugging purposese start fheMcontrolServer in the foregroud with the **-d** argument:

	fheMcontrolServer -c /etc/fheMcontrol/fheMcontrol.cfg -d
	
For every incomming request there will be an output of:

- IncomingMessage (XML)
- fhem device definition (JSON)
- OutgoingMessage (XML)

All Outputs will also include timestamps.
Also you can activate debug within your aioCreator, there should be after test to connect to the mcontrol gateway messages in the log.
 
