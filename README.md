# FileTransfer
File Transfer using multi-threading

The main idea is having a star-shaped architecture with several remote servers and a central client-repo which allows us to centralize the reception of files from remote sites.

Bitacora of versions.

The first version were just for testing the client/server connectivity where the client can ask the server for the files which are stored in, then request one of them. After that multithreading support in the server side was added, so, several client could request a content to the server.

The current version includes the multi-thread support in the server side and I've changed completely the functionality, it's not now the client requesting for a contenct, it's basically the server pushing everything stored in a folder to the client. By the way, multiple remote sites could be added and a central store could keep all the content.

