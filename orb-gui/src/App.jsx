import { useEffect, useState } from 'react';
import Orb from './Orb';

export default function App() {
  const [hue, setHue] = useState(330); // idle = blue

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8765');

    ws.onopen = () => {
      console.log('Connected to Nina');
    };

    ws.onmessage = (event) => {
      const state = event.data; // 👈 STRING, NOT JSON
      console.log('State from Nina:', state);

      switch (state) {
        case 'idle':
          setHue(330); // blue
          break;
        case 'listening':
          setHue(120); // green
          break;
        case 'thinking':
          setHue(60); // yellow
          break;
        case 'speaking':
          setHue(0); // red
          break;
        default:
          console.warn('Unknown state:', state);
      }
    };

    ws.onerror = (e) => {
      console.error('WebSocket error', e);
    };

    return () => ws.close();
  }, []);

  return (
    <div
      style={{
        width: '100vw',
        height: '100vh',
        background: 'black',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center'
      }}
    >
      <div style={{ width: '600px', height: '600px' }}>
        <Orb
          hue={hue}
          hoverIntensity={0.4}
          rotateOnHover={true}
          forceHoverState={false}
        />
      </div>
    </div>
  );
}
