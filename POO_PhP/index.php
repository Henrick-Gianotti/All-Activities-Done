<?php 

    class usuario{
        //atributos = são características que nossos objetos terão
        public $nome;
        public $idade;
        public $email;
        public $senha;
        

        public function __construct($nome, $idade, $email, $senha){
            $this->nome = $nome;
            $this->idade = $idade;
            $this->email = $email;
            $this->senha = $senha;
        }

        public function setNome($n){
            $this->nome = $n;
        }

        public function getNome(){
            return $this->nome;
        }
        // métodos = ações que nossos objetos poderão executar
        public function cadastrar(){
            if($this->nome == "Teste"){
            echo $this->nome . " cadastrou";
            }
            /*if($this->email == "jorisvaldo@gmail.com" && $this->senha == "1234"){
                echo "Cadastrado com sucesso";
            }
            else{
                echo "Erro ao cadastrar";
            }
        }*/
    }
    }
    $usuario = new usuario("Teste", 25, "jorisvaldo@gmail.com", "1234");

    $usuario -> cadastrar();




    /*
    $usuario -> nome = "Jorisvaldo Valdes";
    $usuario -> idade = 52;
    $usuario -> email = "jorisvaldo@gmail.com";
    $usuario -> senha = "1234";
    */


    #$usuario -> cadastrar();