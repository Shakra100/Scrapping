import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';
import './App.css';
import Smartphones from './Smartphones/Smartphones.js';
import Headphones from './Headphones/Headphones.js';
import Shoes from './Shoes/shoes.js'
import Jackets from './Jackets/jackets.js'
import Bags from './Bags/bags.js'
import Laptops from './Laptops/laptops.js'
import Books from './Books/books.js'
import Novels from './Novels/novels.js'

function HomePage() {
  const navigate = useNavigate();

  return (
    <div className="App">
      <div className="flex flex-col min-h-screen">
      <h1 className="text-black bg-black bg-opacity-0 px-10 py-2 text-3xl font-bold">Amazon Products Search</h1>
      <p className="text-black  px-10 py-2 text-xl font-bold">
            "Click any Button to View Products"
          </p>
      <div h-screen flex items-center justify-center>
      <button className="border border-gray-300 bg-blue_500 p-4 w-64 text-blue-500 underline" onClick={() => navigate('/smartphones')}>Smartphones</button>
      <button className="border border-gray-300 p-4 w-64 text-blue-500 underline" onClick={() => navigate('/headphones')}>Headphones</button>
      <button className="border border-gray-300 p-4 w-64 text-blue-500 underline" onClick={() => navigate('/nike_shoes')}>Nike Shoes</button>
      <button className="border border-gray-300 p-4 w-64 text-blue-500 underline" onClick={() => navigate('/nike_jackets')}>Nike Jackets</button>
      <button className="border border-gray-300 p-4 w-64 text-blue-500 underline" onClick={() => navigate('/books')}>NoteBooks</button>
      <button className="border border-gray-300 p-4 w-64 text-blue-500 underline" onClick={() => navigate('/bags')}>Bags</button>
      <button className="border border-gray-300 p-4 w-64 text-blue-500 underline" onClick={() => navigate('/novels')}>Novels</button>
      <button className="border border-gray-300 p-4 w-64 text-blue-500 underline" onClick={() => navigate('/laptops')}>Laptops</button>
          </div>
          </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/smartphones" element={<Smartphones />} />
        <Route path="/headphones" element={<Headphones />} />
        <Route path="/nike_shoes" element={<Shoes />} />
        <Route path="/nike_jackets" element={<Jackets />} />
        <Route path="/books" element={<Books />} />
        <Route path="/laptops" element={<Laptops />} />
        <Route path="/bags" element={<Bags />} />
        <Route path="/novels" element={<Novels />} />
      </Routes>
    </Router>
  );
}

export default App;