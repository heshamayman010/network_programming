## Overview
This repository contains multiple projects demonstrating different technologies and use cases. Each project is organized into its respective folder:

1. **Live Chat Application**: A live chat application built with ASP.NET Web API, Angular, and SignalR, featuring both admin and user functionalities.

2. **Chatroom in Python**: A simple chat room application using Python, Tkinter, and WebSockets.

3. **Games using Python and WebSockets**: Two interactive games with GUIs built using Python's Tkinter library and WebSockets for real-time communication.

## Projects

### 1. Live Chat Application

#### Overview
A  live chat application built with ASP.NET Web API, Angular, and SignalR for real-time communication. The application supports two types of users: Admins and regular users.

#### Features
- **Admin Features**:
  - Send messages to all users simultaneously.
  - Open private chats with individual users.
  - View all live users.
  
- **User Features**:
  - Engage in private chats with other live users.
  - View all live users.

#### Technologies Used
- **Backend**: ASP.NET Web API ,EntityFramework core ,sql server 
- **Frontend**: Angular
- **Real-time Communication**: SignalR

#### How to Run

##### Backend Setup
1. Navigate to the `livechat/backend` directory.
2. Restore the dependencies and build the project:
3. Update the database:
4. Run the backend server:

##### Frontend Setup
1. Navigate to the `livechat/frontend` directory.
2. Install the dependencies:
3. Start the frontend server:
4. Open your browser and navigate to `http://localhost:4200`  for the regular user .
5. Open your browser and navigate to `http://localhost:4200/admin`  for the Admin .


#### Usage
- **Admin**: Log in as an admin to send messages to all users, open private chats, and view live users.
- **User**: Log in as a user to open private chats with other live users and view the list of live users.




### 2. Chatroom in Python

#### Overview
A simple chatroom application using Python, Tkinter for the GUI, and WebSockets for real-time chat functionality.

#### Features
- **Real-time chat**: Communicate with other users in real-time using WebSockets.
- **Tkinter GUI**: A simple and intuitive user interface for chatting.

#### How to Run
1. Navigate to the `chatroom` directory.
2. Run the WebSocket server:
3. Run the chatroom client:


### 3. Games using Python and WebSockets

#### Overview
This folder contains two interactive games developed using Python and WebSockets for real-time communication. The GUI for these games is created using Tkinter.

#### Features
- **Real-time communication**: The games use WebSockets for real-time updates and interactions.
- **Tkinter GUI**: User-friendly graphical interface for a seamless gaming experience.
