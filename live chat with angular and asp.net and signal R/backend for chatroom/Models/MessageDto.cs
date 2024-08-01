using System.ComponentModel.DataAnnotations;

namespace backend_for_chatroom.Models
{
    public class MessageDto
    {
        [Required]
        public string From { get; set; }
        public string To { get; set; }
        [Required]
        public string content { get; set; }

    }
}
