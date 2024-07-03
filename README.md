# qa-test

**Kubernetes Deployment:**

Deploy the services to a local Kubernetes cluster (e.g., Minikube or Kind).

**Verification:**

- Ensure the frontend service can successfully communicate with the backend service.
- Verify that accessing the frontend URL displays the greeting message fetched from the backend.

**Automated Testing:**

- Write a simple test script (using a tool of your choice) to verify the integration between the frontend and backend services.
- The test should check that the frontend correctly displays the message returned by the backend.

**Documentation:**

- Provide a README file with instructions on how to set up and run the automated tests script.

**Deliverables:**
- Test script for automated testing.
- README file with setup and execution instructions.

**Github repo should be Public**


 Setup Instructions

1. Set Up Minikube
   - Install Minikube
   - Start Minikube:
     
    

2. Deploy Services and Verify
   - Clone the repository:
     git clone https://github.com/username/qa-test
     cd qa-test/kubernetes
   - Deploy backend and frontend services:
     kubectl apply -f backend-deployment.yaml
     kubectl apply -f frontend-deployment.yaml

     get the minikube ip using  minikube "service frontend-service --url" and launch in browser : result would be 'Hello from the     Backend!'

## Testing Instructions
- Create the automated test Script to verify the results using the same minikube ip as  frontend url
- Run the automated test script to verify integration:
  python backendmessage.py



