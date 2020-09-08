# ActiveWorkflow Custom Agent Example in Python

This project implements a simple example agent for
[ActiveWorkflow](https://github.com/automaticmode/active_workflow). The agent
is implemented in Python and uses the [remote agent
API](https://github.com/automaticmode/active_workflow/blob/master/docs/remote_agent_api.md).

This Agent doesn't do anything useful but it does demonstrate the features of
ActiveWorkflow's Remote Agent API.

## Quick Start

This agent is intended to be used as part of
[ActiveWorkflow](https://github.com/automaticmode/active_workflow). To use it
please install ActiveWorkflow according to the instructions in its README
first.

Also, make sure you run this agent *before* starting ActiveWorkflow (you may
want to use [virtualenv](https://virtualenv.pypa.io/en/latest/)):

```sh
git clone https://github.com/automaticmode/aw_python_sample_agent
cd aw_python_sample_agent
#virtualenv .venv && source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Note the URL of the agent's server (usually it is `http://127.0.0.1:5000/`),
and set it as an environment variable for ActiveWorkflow:

```sh
export REMOTE_AGENT_URL="http://127.0.0.1:5000/"
```

Now start ActiveWorkflow. You should be able to create instances of this agent
(named "Python Test Agent"). Run it and send messages to it.

Please note that this project is just a minimal example. Consider using a
proper project structure when developing your own ActiveWorkflow agents.
