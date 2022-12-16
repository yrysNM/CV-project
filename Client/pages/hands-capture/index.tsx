import React from 'react';
import useLogic from './hooks/index';

function HandsCapture() {
  const { videoElement, maxVideoWidth, maxVideoHeight, canvasEl, initCamara } = useLogic();

  const handlePause = () => {
    let stream = videoElement.current.srcObject;
    const tracks = stream.getTracks();

    tracks.forEach(track => track.stop());
    videoElement.current.srcObject = null;
  }

  const handlePlay = () => {
    initCamara();
  }

  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        flexDirection: 'column',
      }}
    >
      <video
        style={{ display: 'none' }}
        className='video'
        playsInline
        ref={videoElement}
      />

      <canvas ref={canvasEl} width={maxVideoWidth} height={maxVideoHeight} />
      <button onClick={handlePause}>Stop</button>
      <button onClick={handlePlay}>Start</button>
    </div>
  );
}

export default HandsCapture;
