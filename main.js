const electron = require('electron');
const url = require('url');
const path = require('path');


const {app, BrowserWindow, Menu} = electron;

let mainWindow;

// Listen for app to be ready
app.on('ready', function(){
    // Create new window
    refocus = new BrowserWindow({});
    // Load html into window
    refocus.loadURL(url.format({
        pathname: path.join(__dirname, 'refocus.html'),
        protocol: 'file:',
        slashes: true
    }));

    // Build menu from template
    const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
    // Insert Menu
    Menu.setApplicationMenu(mainMenu);
    //refocus.webContents.openDevTools()
});

//create menu template
const mainMenuTemplate = [
    {
        label:'File',
        submenu: [
            {
                label: 'Add Item'
            },
            {
                label: 'Clear Items'
            },
            {
                label: 'Quit',
                click(){
                    app.quit();
                }
            }
        ]
    }
];
