const { Client, version } = require('discord.js');
const { token, serverID, roleID, interval } = require('./config.json')
const bot = new Client();

bot.on("ready", async() => {
    console.log(`[ Client ] ${bot.user.tag} conectado con éxito a DiscordAPI`);

    let guild = bot.guilds.cache.get(serverID) // Estamos buscando un servidor por id
    if(!guild) throw `[ Error ] No se encontró el bot en el servidor con id.: ${serverID}` // Si no hay servidor, lanza un error

    let role = guild.roles.cache.find(u => u.id === roleID) // Тоже самое.. Ищем роль
    if(!role) throw `[ Error ] No se encontró el rol en el servidor con el nombre ${guild.name}` // Si no hay rol, entonces un error...
    
    
    if(interval < 60000) console.log(`\n[!!!] Ha introducido muy poco tiempo. ¡Ten cuidado! Puede que tengas problemas..`) // Advertencia si el intervalo es inferior a un minuto.

    setInterval(() => {
        role.edit({color: 'RANDOM'}).catch(err => console.log(`[ Error ] Ocurrió un error al cambiar el rol.`));
    }, interval)

})

bot.login(token)