import 'bulma/css/bulma.css'
import './App.css'
import axios from 'axios'
import { useState } from 'react'
import Block from './block';
import { findStringsContainingSubstring } from './search'

const App=()=>{

    const days=['MON','TUE','WED','THU','FRI'];
    const times=['8-9AM','9-10AM','10-11AM','11-12PM','12-1PM','2-3PM','3-4PM','4-5PM','5-6PM'];

    const [freeRooms,setFreeRooms]=useState([]);
    const [filteredFreeRooms,setFilteredFreeRooms]=useState([]);
    const [selectedDay,setSelectedDay]=useState('');
    const [selectedTimeIndex,setSelectedTimeIndex]=useState(0);
    const [selectedTime,setSelectedTime]=useState('8-9PM');
    const [roomName,setRoomName]=useState('')

    const Rooms=filteredFreeRooms.map((room)=>{
        return(<Block value={room}/>)
    })

    // const pos=filteredFreeRooms.length>42?'relative':'absolute'

    const handleSelectChangeDay =async (event) => {
        setSelectedDay(event.target.value);

        const response=await axios.get(`https://sdrawkcabdear.github.io/FreeRooms/db.json`)

        const rdata=response.data[event.target.value][selectedTimeIndex];
        setFreeRooms(rdata.time)
        setFilteredFreeRooms(rdata.time)
        setRoomName('');
      };

    const handleSelectChangeTime =async (event) => {
        setSelectedTimeIndex(event.target.selectedIndex);
        setSelectedTime(event.target.value);

        const response=await axios.get(`https://sdrawkcabdear.github.io/FreeRooms/db.json`)

        const rdata=response.data[selectedDay][event.target.selectedIndex];
        setFreeRooms(rdata.time)
        setFilteredFreeRooms(rdata.time)
        setRoomName('');
    };

    const handleSelectChangeRoom=(event)=>{
        setRoomName(event.target.value);
        if(event.target.value)
        setFilteredFreeRooms(findStringsContainingSubstring(freeRooms,event.target.value));
        else
        setFilteredFreeRooms(freeRooms);
    }

    const dayOption=days.map((day)=>{
        return (<option value={day}>{day}</option>)
    })
    const timeOption=times.map((time)=>{
        return (<option value={time}>{time}</option>)
    })

    return(<div className="everything">
        <div className="topbar">
            <div className="header">
                <div className='freerooms'>
                    <h1>freerooms</h1>
                    <p className='iitkgp'>IIT_KGP</p>
                </div>
                <input className='input is-rounded' placeholder='Search Room' onChange={handleSelectChangeRoom} value={roomName}/>
            </div>
            <div className='filter'>
                    <select className="select" onChange={handleSelectChangeDay} value={selectedDay}>
                    <option value="" disabled selected>DAY</option>
                        {dayOption}
                    </select>
                    <select className="select" onChange={handleSelectChangeTime} value={selectedTime}>
                        {timeOption}
                    </select>
                </div>
        </div>
        
        <div className="rooms"> 
            {Rooms}
        </div>
        <div className='footer' >
            "This website will tell you the free rooms available in nalanda as per the day and time"
        </div>
    </div>)
}

export default App

//end of code