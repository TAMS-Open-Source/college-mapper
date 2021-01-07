import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, ZoomControl } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

const DEFAULT_LOCATION = { lat: 38.0, lon: -97.7548 }

function MapView() {
  const [currentLoc, setCurrentLoc] = useState(DEFAULT_LOCATION)
  const [zoom, setZoom] = useState(5);

  return (
    <MapContainer zoom={zoom} center={currentLoc} style={{ height: '100%', width: '100%' }} zoomControl={false} >
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&copy; <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
      />
      <ZoomControl position="bottomleft" />
    </MapContainer>
  )
}

export default MapView;