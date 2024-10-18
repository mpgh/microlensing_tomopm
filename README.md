# Observational Planning Manager (OPM) - A Target and Observation Manager Instance for the TVS microlensing subgroup

The OPM is an instance of the Target and Observation Manager (TOM) designed to track microlensing alerts over time, ingest targets with their alert priority, display corresponding light curves, and communicate with other TOM systems connected to observatories and proposals. This repository provides a system that can be installed locally by members of the TVS Microlensing Subgroup and eventually deployed in a suitable cloud environment.The OPM is an instance of the Target and Observation Manager (TOM) designed to track microlensing alerts over time, ingest targets with their alert priority, display corresponding light curves, and communicate with other TOM systems connected to observatories and proposals. This repository provides a system that can be installed locally by members of the TVS Microlensing Subgroup and eventually deployed in a suitable cloud environment.

## Usage
Once installed, you can access and interact with the OPM through its web interface. Here are some key features of the system:
* **Target Management**: Create, view, and update targets associated with microlensing alerts, subscribe to broker services
* **Light Curve Visualization**: View and analyze light curves associated with each target to monitor microlensing events over time.

## Planned Features
* **Communication with Other TOM Systems**: Interact with other TOM systems connected to observatories and proposals, enabling easy requesting of observations directly from the OPM interface.
* **Requesting and interacting with HPC systems to fit events**: Interact safely with HPC centers to fit complicated microlensing events, i.e. binary and triple lens events