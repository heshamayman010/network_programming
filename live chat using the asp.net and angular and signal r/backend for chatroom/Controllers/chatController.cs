using backend_for_chatroom.Services;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using backend_for_chatroom.Models;

namespace backend_for_chatroom.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class chatController : ControllerBase
    {
        private readonly Chatservice myservice;


        // here we will inject our chat service 
        public chatController(Chatservice myservice)
        {
            this.myservice = myservice;
        }




        [HttpPost("RegisterUser")]
        public IActionResult RegisterUser(UserDto theusertoregister)
        {


            if (myservice.AddUserTolist(theusertoregister.name))
            {

                return Ok();
            }
            else
            {

                return BadRequest("this user name is already taken ");
            }
        }

          

    }
}
