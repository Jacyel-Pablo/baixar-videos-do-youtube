import './App.css'

function App() {

  return (
    <div className='corpo'>
      <h1 className='container__titulo'>Baixar vidéos do YouTube</h1>

      <p className='texto'>Insira um link de um video e click em download</p>

      <form className='campo__buscar' action="http://localhost:3000/download">
        <input className='campo__buscar__input' placeholder='Insira um link aqui:' type="text" name='url'/>
        <input className='campo__buscar__submit' type="submit" value="Download" />
      </form>
    </div>
  )
}

export default App
