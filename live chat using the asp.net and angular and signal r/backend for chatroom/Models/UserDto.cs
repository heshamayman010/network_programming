using System.ComponentModel.DataAnnotations;

namespace backend_for_chatroom.Models
{
    public class UserDto
    {
        [Required]
        [StringLength(maximumLength:20,ErrorMessage ="the length of the user name must be between 3 to 20  ", MinimumLength =3)]
        public string name { get; set; }

    }
}
