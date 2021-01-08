import React from 'react';
import calendar from './calendar.svg';
import person from './person.svg';

const ButtonBase = ({ img_source }) => (
  <div style={{
    width: 100,
    height: 100,
    borderRadius: 50,
    backgroundColor: 'white',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center'
  }}>
    <img src={img_source} style={{ height: '80%' }} />
  </div>
)

const CalendarButton = () => <ButtonBase img_source={calendar} />
const PersonButton = () => <ButtonBase img_source={person} />
export { CalendarButton, PersonButton };