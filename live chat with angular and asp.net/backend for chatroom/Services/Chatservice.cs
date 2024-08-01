namespace backend_for_chatroom.Services
{

    
    public class Chatservice
    {

        // here the dictionary key is the username and the value is the message 

        private static readonly Dictionary<string,string> Users=new Dictionary<string, string>();


        public bool AddUserTolist(string UserToAdd)
        {
            // here we used the lock to prevent the race conditioning 
            lock (Users)
            {
                foreach (var user in Users)
                {
                    // Check if user.Value is null before calling ToLower()
                    if (user.Value != null && user.Value.ToLower() == UserToAdd.ToLower())
                    {
                        return false;
                    }
                }

                Users.Add(UserToAdd, null);
                return true;
            }
        }




        // here is the function to give each user an id 
        public void AddUserId(string User,string ConnectionId)
        {

            lock (Users)
            {

                if(Users.ContainsKey(User))
                {

                    Users[User] = ConnectionId;

                }


            }



        }
    
    


        // then function to get back the username by his id 

        public string GetUserByConnectionId(string ConnectionId)
        {

            lock( Users)
            {

                return Users.Where(c => c.Value == ConnectionId).Select(x => x.Key).FirstOrDefault();

            }


        }


        public string GetConnectionIdByUser(string username)
        {

            lock (Users)
            {

                return Users.Where(c => c.Key == username).Select(x => x.Value).FirstOrDefault();

            }


        }



        public void RemoveUser(string Usertodelete)
        {

            lock (Users)
            {
                if (Users.ContainsKey(Usertodelete))
                {

                    Users.Remove(Usertodelete);

                }



            }

        }



        //then function to get all the online users Names

        public string[] GetLiveUsers()
        {

            return Users.Select(x=>x.Key).ToArray();


        }


    }
}
