import './assets/css/style.css';
import Chat from './components/chat';
import SideBar from './components/side-bar';
import { SocketIO, SocketContext } from './socketio'

function App() {
    return (
        <SocketContext.Provider value={SocketIO}>
            <SideBar/>
            <Chat/>
        </SocketContext.Provider>
    );
}

export default App;
