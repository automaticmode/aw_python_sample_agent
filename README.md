# ActiveWorkflow Agent Example in Python

This project implements a simple example agent for [ActiveWorkflow](https://github.com/automaticmode/active_workflow).
The agent is implemented in Python and uses the [remote agent API](https://docs.activeworkflow.org/remote-agent-api).

This agent doesn't do anything useful but it does demonstrate the features of ActiveWorkflow's Remote Agent API.

## Quick Start

This agent is intended to be used as part of [ActiveWorkflow](https://github.com/automaticmode/active_workflow).
To get started with ActiveWorkflow please see the [ActiveWorkflow documentation](https://docs.activeworkflow.org/).

Also, please make sure you run this agent *before* starting ActiveWorkflow (you may want to use [virtualenv](https://virtualenv.pypa.io/en/latest/)):

```sh
git clone https://github.com/automaticmode/aw_python_sample_agent
cd aw_python_sample_agent
#virtualenv .venv && source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Note the URL of the agent's server (usually it is `http://127.0.0.1:5000/`), and set it as an environment variable for ActiveWorkflow:

```sh
export REMOTE_AGENT_URL="http://127.0.0.1:5000/"
```

If using [Docker to run ActiveWorkflow](https://docs.activeworkflow.org/#running-locally-with-docker),
you'll need to use the `-e` parameter to `docker run` to pass `REMOTE_AGENT_URL` through
to ActiveWorkflow. The address in the URL will also have to be updated to match where the agent
is running (`127.0.0.1` is unlikely to be correct). Docker provides `host.docker.internal` for the host IP.
Thus, you could run:
```sh
docker run -e REMOTE_AGENT_URL="http://host.docker.internal:5000/" -p 3000:3000 --rm automaticmode/active_workflow
```

Now you can start ActiveWorkflow. You should be able to create instances of this agent (named "Python Test Agent"). Run it and send messages to it.

Please note that this project is just a minimal example. Consider using a proper project structure when developing your own ActiveWorkflow agents.
