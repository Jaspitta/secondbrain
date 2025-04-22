# þÿTopic 8   Services and Daemons: View as Single Page | OU Online

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/289998595/kUdvP3vj6hEWN9uQ2EN5_JwbAxx_Phd51N28cZYZG-0-cove_Th2VAIB.png)

## Metadata
- Author: [[readwise.io]]
- Full Title: þÿTopic 8   Services and Daemons: View as Single Page | OU Online
- Category: #articles
- Summary: This topic discusses background processes in operating systems, known as jobs, services, or daemons. It explains how to manage these processes using the command line, including starting, stopping, and killing them when necessary. Additionally, it highlights the importance of signals in controlling processes and the use of commands like `kill` to handle out-of-control programs.
- URL: https://readwise.io/reader/document_raw_content/289998595

## Highlights
- When you enter a command, that command will execute but you have to wait until the program finishes
- The Linux shell provides features that treat long-running programs as ‘jobs’
- The bg command will restart the job in the background, so you can continue to enter further commands
- they run in the background, they are not under a user’s direct control and have no interactive interface, but in other respects they are normal programs. These are usually termed services, but in the Unix/Linux world they were traditionally called daemons and have program names ending with a ‘d’
- Most of these daemons are managed by systemd
- systemd is itself a daemon and is started during the boot process;
- systemd in turn will start other daemon processes running
- d controlled indirectly at boot time through a cluster of configuration files
- In systemd terminology, daemons are a type of service, and services are a type of unit.
- services and daemons are used for core functions of the operating system,
- the cron daemon, which is used to schedule background jobs at regular intervals
- The cron daemon relies on a configuration file that lists which commands to run and when they should be repeated
- the crontab command should be used: t
- all mainstream OSs have a similar organisation and provide similar tools both through the command line and through GUI tools.
- the kill command you saw earlier in the context of background jobs
- use an underlying OS mechanism based on the idea of signals that are sent to a process which is given the chance to handle them itself
- There are a number of such signals defined in the POSIX standard, which are therefore common to all Unix- like operating systems.
- Ctrl+C to interrupt a program running in a terminal: this sends the sigint signal.
- Ctrl+Z (sigstp) used to stop a program in such a way that it can be restarted
- sigterm signal is normally handled in the same way as the quit/exit/close
- sigkill signal is not passed to the application but immediately causes the operating system to delete the process
- unlike an interrupt they are normally then passed to the program to handle in user mode.
- The kill command can be used to send signals from the command line. The command is not well named since it can be used to send any signal to a process
