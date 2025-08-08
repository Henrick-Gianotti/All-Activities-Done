<?php 

    abstract class veiculo
    {
        //atributos = são características que nossos objetos terão
        public $nome;
        public $ano;
        public $valor;        

        public function __construct($dados)
        {
            $this->nome = $dados;
            $this->ano = $dados;
            $this->valor = $dados;
        }

        public function getNome()
        {
            return $this->nome;
        }

        abstract protected function Acelerar();

        abstract protected function Freiar();
        // métodos = ações que nossos objetos poderão executar
        /*public function cadastrar(){
            if($this->nome == "Civic"){
            echo "O carro " . $this->nome . " foi cadastrado";
            }*/
    }

    class carro extends veiculo
    {
        /*
        public function abrirPorta(){
            echo "Abrir porta";
        }*/
        public function Acelerar()
        {
            echo "Vrom!";
        }

        public function Freiar()
        {
            echo "Tum!";
        }
    }

    class moto extends veiculo
    {
        /*public function darGrau(){
            echo "Empinar a moto";
        }*/
        public function Acelerar()
        {
            echo "Ron! Ron!";
        }
        
        public function Freiar()
        {
            echo "Tum!";
        }
    }

    class barco extends veiculo
    {
        public function Acelerar()
        {
            echo "Acelera aí";
        }
        public function Freiar()
        {
            echo "Só parar de acelerar";
        }
    }

    class bicicleta extends veiculo
    {
        public function Acelerar()
        {
            echo "Pedala!";
        }
        public function Freiar()
        {
            echo "Aperte o guidão";
        }
    }

    class skate extends veiculo
    {
        public function Acelerar()
        {
            echo "Empurre o solo com o pé";
        }
        public function Freiar()
        {
            echo "Só pular do skate pra freiar";
        }
    }

    class aviao extends veiculo
    {
        public function Acelerar()
        {
            echo "É igual mexer com linux para acelerar";
        }
        public function Freiar()
        {
            echo "Use a aerodinâmica para freiar";
        }
    }

    class elevador extends veiculo
    {
        public function Acelerar()
        {
            echo "Aperte o botão para locomover";
        }    
        public function Freiar()
        {
            echo "Só Deus freia isso aqui";
        }
    }

    

echo "<pre> ---Carro--- \n";
$carro = new carro("Civic", 2023, 105000);
$carro -> Acelerar();
$carro -> Freiar();

echo "<pre> ---Moto--- \n";
$moto = new moto("Pop 100", 2010, 10200);
$moto -> Acelerar();
$moto -> Freiar();

echo "<pre> ---Barco--- \n";

$barco = new barco("Astray", 2020, 600000);
$barco -> Acelerar();
$barco -> Freiar();

echo "<pre> ---Bicicleta--- \n";

$bicicleta = new bicicleta("BMX", 2022, 15000);
$bicicleta -> Acelerar();
$bicicleta -> Freiar();

echo "<pre> ---Skate--- \n";

$skate = new skate("Chorão", 2018, 1500000);
$skate -> Acelerar();
$skate -> Freiar();

echo "<pre> ---Avião--- \n";

$aviao = new aviao("Flying-V", 2020, 2000000);
$aviao -> Acelerar();
$aviao -> Freiar();

echo "<pre> Vez do elevador \n";

$elevador = new elevador("Elevador", 2010, 400000);
$elevador -> Acelerar();
$elevador -> Freiar();
