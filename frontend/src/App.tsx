import './App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import AppLayout from './layout/AppLayout'
import AuthPage from './pages/AuthPage/AuthPage'
import MainPage from './pages/MainPage/MainPage'
import ViewLogsPage from './pages/ViewLogsPage/ViewLogsPage'

function App() {

  return (
    <BrowserRouter>

      <Routes>
        <Route path='/login' element={<AuthPage />} />

        <Route element={<AppLayout />}>
          <Route path='/' element={<MainPage />} />
          <Route path='/logs' element={<ViewLogsPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
