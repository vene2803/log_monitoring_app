## Author

© 2025 Vladut Ene | enevlad28@gmail.com

## log_monitoring_app
This is a Repository created for a Log Monitoring application written in Python.

This Python script parses a `logs.log` file and calculates the runtime duration of jobs based on their `START` and `END` timestamps. It flags any job that exceeds a defined threshold with a `WARNING` or `ERROR` level, outputing them in the CLI and a separate TXT file.

If there is a delay in generating the outputs, it can be because the flush() is not used; It can be added as feature but only if the buffer needs this feature.

More details can be found in the here: (<Log Monitoring Application 1.pdf>)