import { createContext } from 'react';
import socketio from 'socket.io-client';
import config from './config';


export const SocketIO = socketio.connect(config.socketServer);

export const SocketContext = createContext();
