import React from 'react';
import { useState } from 'react';
import { posts } from './posts';

const News = () => {
  const [show, setShow] = useState(false);
  const [color, setColor] = useState(false);


  return (
    <div className='container mt-5'>
      <div className='row justify-content-center mb-4'>
        <div className='col-12 col-md-3 mb-2'>
          <div className='btn btn-primary w-100' onClick={() => setShow(!show)}>
            {show ? 'Hide' : 'Show'}
          </div>
        </div>
        <div className='col-12 col-md-3 mb-2'>
          <div className='btn btn-primary w-100' onClick={() => setColor(!color)}>
            {color ? 'Black' : 'White'}
          </div>
        </div>
      </div>

      <div className='row'>
        {
          !show &&
          posts.map((p) => {
            const { id, titolo, descrizione } = p;
            return (
              <div className='col-3' key={id}>
                <div className='card' style={{ backgroundColor: color ? 'black' : 'white', borderColor: color ? 'darkgray' : 'gray' }}>
                  <div className='card-body'>
                    <h5 className='card-title' style={{ color: color ? 'white' : 'black' }}>{titolo}</h5>
                    <p className='card-text' style={{ color: color ? 'white' : 'black' }}>{descrizione}</p>
                  </div>
                </div>
              </div>
            );
          })}
      </div>
    </div>
  );
};

export default News;