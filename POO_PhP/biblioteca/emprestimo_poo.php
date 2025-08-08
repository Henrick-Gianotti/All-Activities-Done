<?php

interface Crud
{
    public function criar();
    public function ler();
    public function atualizar();
    public function deletar();
}

class Usuario implements Crud
{
    protected $nome;
    protected $cep;
    const max_emprestimo = 3;
    public $qtd_livros = [];

    public function criar()
    {
        return $query = 'insert into usuario(nome, cep) values("'.$this-titulo.'";"'.$this->nome.'","'.$this->cep.'"';
    }
    public function ler()
    {
        return "select * from usuario where nome = ".$this->nome.";";
    }
    public function atualizar()
    {
        #fazer o mesmo com o livro, criar um método de selecionar qual coluna eu quero alterar
        return "update usuario set";
    }
    public function deletar()
    {
        return "delete * from usuario where nome = ''";
    }
    public function emprestar($livro)
    {
        if($this->countLivro < self::max_emprestimo)
        {
            $this->countLivro++;
            array_push($this->qtd_livros, $livro);
        }
    }
    public function devolver()
    {
        if(in_array($livro, $this->livros_emprestados))
        {
            $postion = array_search($livro, $this->livros_emprestados)
            unset($this->livros_emprestados[$position]);
        }
    }
}

class Livro implements Crud
{

    protected $titulo;
    protected $autor;

    public function criar()
    {
        return $query = 'insert into livro(titulo, autor, genero,status_livro) values("'.$this->titulo.'","'.$this->autor.'","'.$this->genero.'","'.$this->status.'");';
    }
    public function ler()
    {
        return "select * from livro where titulo = ".$this->titulo.";";
    }
    public function atualizar()
    {
        return "update livro set genero = ".$genero_novo." where titulo = ".$this->tiutulo.";";

        /*
        $query = "update livro set ";

        foreach ($arrayColunas as $coluna) 
        {
        #pegar chave
            $chave;

        #pegar valor
            $valor;

            $query += .$chave.' = "'.$valor.'"';
        }
        return $query += "where titulo = "'.$this->titulo. '";';

        */
    }
    public function deletar()
    {
        return "delete * from livro where titulo = '';";
    }
}

class Biblioteca
{
    const servidor = 'localhost';
    const usuario = 'root';
    const senha = '';
    const banco_de_dados = 'biblioteca141';
    public statis function emprestar($livro, $usuario)
    {
        $livro->emprestar($usuario);
        $usuario->emprestar($livro);
    }
    public static function devolver($livro, $usuario)
    {
        $livro->devolver();
        $usuario->devolver($livro);
    }
    public static function conexao()
    {
        return $conexao = mysql_connect(self::servidor, self::usuario, self::senha, self:: banco_de_dados);
    }
    public static function cadastrar($livro)
    {
        self::conexao()->query($livro->criar());
        self::conexao()->close();
    }
}

