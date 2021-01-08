import React, { useEffect, useState, useRef } from 'react';
import { MapContainer, TileLayer, ZoomControl, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import Marker from 'react-leaflet-enhanced-marker';
import styled from 'styled-components';

const DEFAULT_LOCATION = { lat: 38.0, lon: -97.7548 }
const TESTING_LOC = { lat: 33.2101, lon: -97.7548 }

function MapView() {
  const [currentLoc, setCurrentLoc] = useState(DEFAULT_LOCATION)
  const [zoom, setZoom] = useState(5);
  const [showPopup, setShowPopup] = useState(false)
  const [map, setMap] = useState()
  const [bounds, setBounds] = useState()

  useEffect(() => {
    if (map) {
      map.on('moveend', handleMove);
      // by returning this, we ensure we don't get much more movement
      // actions than necessary.
      return () => map.removeEventListener("moveend", handleMove)
    }
  }, [map]);

  // this is where we'll continually update which markers can be shown
  const handleMove = () => {
    console.log("I done been moved!")
    setBounds(map.getBounds())
  }

  useEffect(() => {
    console.log("Got new bounds!");
    console.log(bounds)
  }, [bounds])
  
  return (
    <>
    <MapContainer 
      zoom={zoom} center={currentLoc} 
      whenCreated={map => setMap(map)}
      style={{ height: '100%', width: '100%', position: 'absolute', top: 0, left: 0, zIndex: 0 }} 
      zoomControl={false}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&copy; <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
      />
      <ZoomControl position="bottomleft" />
      <Marker
        icon={<div>I am a Marker!</div>}
        position={[
          TESTING_LOC.lat,
          TESTING_LOC.lon
      ]}
        eventHandlers={{
          mouseover: (e) => {
            console.log('Hoovering!')
            e.target.openPopup();
          },
        }}
      >
        <Popup>
            <div style={{
              height: '30vh',
              width: '20vw',
              backgroundColor: 'white',
              boxShadow: 'none'
          }}>
          </div>
        </Popup>
      </Marker>
    </MapContainer>
    <div style={{
      width: 100,
      height: 100,
      borderRadius: 50,
      position: 'absolute',
      top: 10,
      right: 10,
      backgroundColor: 'white',
      zIndex: 1
    }}></div>
    </>
  )
}


export default MapView;