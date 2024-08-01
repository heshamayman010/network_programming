using backend_for_chatroom.Models;
using backend_for_chatroom.Services;
using Microsoft.AspNetCore.SignalR;

namespace backend_for_chatroom.MyHubs
{
    public class ChatHubs : Hub
    {
        private readonly Chatservice myservice;

        public ChatHubs(Chatservice myservice)
        {
            this.myservice = myservice;
        }


        // this is the function inside the hub that will be triagerd when new user is connected to the hub 
        public override async Task OnConnectedAsync()
        {

            await Groups.AddToGroupAsync(Context.ConnectionId, "mychatroom");
            // here after the function befroe is done the next function is called in the angular 
            await Clients.Caller.SendAsync("userconnected");

        }


        // this is the method trigrared when the user disconnect from the hub and we used it now for the handling of any exception  
        public override async Task OnDisconnectedAsync(Exception exception)
        {
            await Groups.RemoveFromGroupAsync(Context.ConnectionId, "mychatroom");

            //after the user disconnect we must remove him from the liveusers list 

            var disconnecteduser = myservice.GetUserByConnectionId(Context.ConnectionId);
            //then remove him from the list 
            myservice.RemoveUser(disconnecteduser);
            await getliveusersprivatemethod();
            await base.OnDisconnectedAsync(exception);
        }

        public async Task Adduserconnectionid(string myname)
        {

            myservice.AddUserId(myname, Context.ConnectionId);

            // and to get the online users to send them to the angular 

            await getliveusersprivatemethod();
        }
        // you can access Context.ConnectionId to get the unique identifier for the connection that is currently executing the method.
        //as When a client connects to a SignalR hub, SignalR creates a unique ConnectionId for that connection.




        // for simplicity here is function to get the liveusrs
        private async Task getliveusersprivatemethod()
        {

            var liveusers = myservice.GetLiveUsers();
            // now we will call method to be excuted in the angular using the sendasync and send with it the parameter 

            await Clients.Group("mychatroom").SendAsync("liveusers", liveusers);

        }


        public async Task RecieveMessage(MessageDto message)
        {

            Clients.Group("mychatroom").SendAsync("Newmessage", message);
        }


        // now the part of the private chat 

        public async Task CreatePrivateChat(MessageDto message)
        {
            // we first get the unique name for the group 
            string privateGroupname=GetprivateNameForGroup(message.From,message.To);

            // then we generate the group using the group name and the connection id 
            await Groups.AddToGroupAsync(Context.ConnectionId, privateGroupname);

            // now get the connection id of the user you are going to connect to using the function in the service 

            var toconnectionid = myservice.GetConnectionIdByUser(message.To);
            await Groups.AddToGroupAsync(toconnectionid, privateGroupname);


            // now we will call method in the angular for the clien who wants to be connected in the to in the chat 
            // and here we will open the private chate dialog at the other end user 
            await Clients.Client(toconnectionid).SendAsync("openprivatechat", message);



        }


        // and the message to recieve the private message 

        public async Task RecievePrivateMessage(MessageDto message)
        {
            string privateGroupname = GetprivateNameForGroup(message.From, message.To);

            await Clients.Group(privateGroupname).SendAsync("newprivatemessage", message);

        }


        // and the next function is to close the private chat between the to and the from 

        public async Task RemovePrivateChat(string to ,string from)
        {
            string privateGroupname = GetprivateNameForGroup(from,to);

            await Clients.Group(privateGroupname).SendAsync("closeprivatechat");


            // now we want to remove the both users from the group so 

            await Groups.RemoveFromGroupAsync(Context.ConnectionId, privateGroupname);

            // and for the second user

            var toconnectionid=myservice.GetConnectionIdByUser(to);
            await Groups.RemoveFromGroupAsync(toconnectionid, privateGroupname);

            // now we had removed both users and also sent message to close the connection on the angular 
        }


        // and for the private chat we need to create private group name with method to be called 

        private string GetprivateNameForGroup(string from ,string to)
        {
            // here This compares the two strings from and to using their ordinal (binary) values
            var stringcomapre =string.CompareOrdinal(from,to) < 0;


            return stringcomapre?$"{from}-{to}":$"{to}-{from}";

            // different way to get the unique name 
            //// Create an array of the two strings
            //string[] users = new string[] { from, to };

            //// Sort the array
            //Array.Sort(users);

            //// Concatenate the sorted strings with a hyphen
            //return $"{users[0]}-{users[1]}";
        }

    }
}
