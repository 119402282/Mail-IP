# Mail IP

## Description

This is a simple script that sends an email with the public IP of the machine it is running on. It is intended to be run as a cron job to send the IP address of a machine to a specified email address at regular intervals. It is useful for keeping track of the public IP address of a machine that does not have a static IP address. This way you can always know the IP address of the machine and access it remotely if needed.

## Installation

1. Clone the repository
2. Create a virtual environment with `python -m venv venv`
3. Activate the virtual environment with `source venv/bin/activate`
4. Install the required packages with `pip install -r requirements.txt`
5. Get a gmail account and an app password for the account. Instructions can be found [here](https://support.google.com/accounts/answer/185833?hl=en)
6. Configure the script with your email settings in a `.env` file (see the `.env.example` file for an example).
7. Run the script with `python mail_ip.py`

## Usage with Windows Task Scheduler

1. Open Task Scheduler
2. Click on `Create Basic Task...`
3. Name the task and give it a description
4. Choose the trigger for the task (e.g. `Daily`)
5. Choose the start date and time for the task
6. Choose the action for the task (e.g. `Start a program`)
<!-- we are using virtual environment  -->
7. In the `Program/script` field, enter the path to the Python executable in the virtual environment (e.g. `C:\path\to\venv\Scripts\python.exe`)
8. In the `Add arguments (optional)` field, enter the path to the script (e.g. `C:\path\to\mail_ip.py`)
9. Click `Finish`

## Credits

This script was created by Henry Cullen an enjoyer of all things tech ✌️.


