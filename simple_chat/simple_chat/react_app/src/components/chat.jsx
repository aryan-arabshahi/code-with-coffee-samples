import React, { Fragment, useContext, useEffect, useState } from 'react';
import { SocketContext } from '../socketio';
import { animateScroll } from 'react-scroll';
import sendImage from '../assets/images/send.png';


const Sender = {
    me: 'me',
    others: 'others',
}


function MessageData({ sender, message }) {

    return {
        sender: sender,
        message: message,
    }
}


export default function Chat() {

    const [message, setMessage] = useState(null);
    const [receivedMessage, setReceivedMessage] = useState(null);
    const [messagesList, setMessagesList] = useState([]);
    const socketio = useContext(SocketContext);


    const scrollToBottom = () => {
        animateScroll.scrollToBottom({
            containerId: 'scroll-to-bottom',
        });
    }

    const onSubmit = (e) => {
        e.preventDefault();

        if (message !== null) {
            sendMessage(message);
        }

    }

    const sendMessage = (message) => {

        setMessagesList(messagesList.concat([
            MessageData({
                sender: Sender.me,
                message: message,
            })
        ]));

    }

    const onMessageChangeHandler = (e) => {
        setMessage(e.target.value);
    }

    const onMessageReceived = (data) => {

        setReceivedMessage(
            MessageData({
                sender: Sender[data.sender],
                message: data.message,
            })
        );

    }


    useEffect(() => {
        socketio.on('receive_message', onMessageReceived);
        return () => {
            socketio.off('receive_message', onMessageReceived);
        };
    }, [socketio]);

    useEffect(() => {

        /*
        * Get the last inserted message and send it if it's from me
        */
        const messagesCount = messagesList.length;
        if (messagesCount && messagesList[messagesCount -1].sender === Sender.me) {
            socketio.emit('send_message', message);
            setMessage(null);
        }

        scrollToBottom();

    }, [messagesList]);

    useEffect(() => {

        if (receivedMessage !== null) {
            setMessagesList(messagesList.concat(receivedMessage));
        }

    }, [receivedMessage]);


    return (
        <Fragment>
            <div id="main-container" className="scroll-to-bottom">
                <div className="p-5 px-8 pb-10">
                    <MessagesList data={messagesList}/>
                </div>
            </div>

            <div id="input-container">
                <div className="px-10">
                    <form id="input-parent" className="border-t-2 p-2 px-0 relative" onSubmit={onSubmit}>
                        <input
                            type="text"
                            name="message"
                            placeholder="Send Message"
                            className="block w-full bg-transparent text-lg"
                            onChange={onMessageChangeHandler}
                            value={message || ''}
                            autoComplete="off"/>

                        <button className="block absolute cursor-pointer">
                            <img src={sendImage} alt="Send Message"/>
                        </button>

                    </form>
                </div>
            </div>
        </Fragment>
    );
}

function Message({ data }) {

    return (
        <div className={`msg-container msg-${data.sender}`}>
            <div className="msg-body">
                {data.message}
            </div>
        </div>
    );
}

function MessagesList({ data }) {

    return (
        <Fragment>
            {data.map(function(value, index) {
                return <Message data={value} key={index}/>
            })}
        </Fragment>
    );
}
