import books from '../notebooks.json'

import { useState } from 'react';

  function Books() {
    const [data, setData] = useState(books); // Directly set imported data
    
  
    return (
      <div className="App">
      <h1  className="text-black  px-10 py-2 text-xl font-bold">Smartphones List</h1>
      <table className="min-w-full bg-white shadow-md rounded-lg overflow-hidden">
        <thead>
          <tr className='bg-gray-200'>
            <th className='border border-gray-300 p-2 text-left'>#</th>
            <th className='border border-gray-300 p-2 text-left'>Title</th>
            <th className='border border-gray-300 p-2 text-left'>Rating</th>
            <th className='border border-gray-300 p-2 text-left'>Price</th>
            <th className='border border-gray-300 p-2 text-left'>Sales</th>
            <th className='border border-gray-300 p-2 text-left'>Image</th>
          </tr>
        </thead>
        <tbody>
          {data.map((books, i) => (
            <tr key={i}>
              <td className='border border-gray-300 p-2'>{i + 1}</td>
              <td className='border border-gray-300 p-2'>{books.title}</td>
              <td className='border border-gray-300 p-2'>{books.rating}</td>
              <td className='border border-gray-300 p-2'>{books.price}</td>
              <td className='border border-gray-300 p-2'>{books.sales}</td>
              <td className='border border-gray-300 p-2'> <a
        href={books.image_url}
        target="_blank"
        className="text-blue-500 underline"
      >
        Open Image
      </a></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Books;