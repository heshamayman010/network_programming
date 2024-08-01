using backend_for_chatroom.MyHubs;
using backend_for_chatroom.Services;

namespace backend_for_chatroom
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            // Add services to the container.
            builder.Services.AddControllers();
            builder.Services.AddEndpointsApiExplorer();
            builder.Services.AddSwaggerGen();

            // Register services
            builder.Services.AddSingleton<Chatservice>();
            builder.Services.AddSignalR();

            // Configure CORS
            builder.Services.AddCors(options =>
            {
                options.AddPolicy("mypolicy", builder =>
                {
                    builder
                           .AllowAnyMethod()
                          .AllowAnyHeader().
                          AllowCredentials().WithOrigins("http://localhost:4200"); // the origin for my angular project 
                });
            });

            var app = builder.Build();

            // Configure the HTTP request pipeline.
            if (app.Environment.IsDevelopment())
            {
                app.UseSwagger();
                app.UseSwaggerUI();
            }

            // Apply CORS policy
            app.UseCors("mypolicy");

            app.UseAuthorization();

            app.MapControllers();
            app.MapHub<ChatHubs>("/hubs/chat");

            app.Run();
        }
    }
}
