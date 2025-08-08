<?php

class Animal {
    protected $nome;
    protected $nome_cientifico;
    protected $coluna_vertebral;
    protected $reproduçao;
    protected $habitat;
    protected $tamanho;

    public function __construct($nome, $nome_cientifico, $coluna_vertebral, $reproduçao, $habitat, $tamanho){
        $this-> nome = $nome;
        $this-> nome_cientifico = $nome_cientifico;
        $this-> coluna_vertebral = $coluna_vertebral;
        $this-> reproduçao = $reproduçao;
        $this-> habitat = $habitat;
        $this-> tamanho = $tamanho;
    }

    public function getNome(){
        return $this->nome;
    }
} 

class Invertebrado extends Animal{
    public function __construct(){
        $this-> coluna_vertebral = false;  
    }
}
class Vertebrado extends Animal{
    public function __construct(){
        $this-> coluna_vertebral = true;
    }
}

class Mamífero extends Vertebrado{
    
}

class Insecta extends Invertebrado{

}

class Besouro_verde{

}

class Baleia extends Mamífero{
    public function esguichar(){
        echo "Esguinchou";
    }
}

class Onitorrinco extends Mamífero{
    public function oníparo(){
        echo "Botar ovo";
    }
}

class Morcego extends Mamífero{
    public function voar(){
        echo "Ele ta voando bixo";
    }
}

$nome_animal = new Onitorrinco("Onitorrinco", "	Ornithorhynchus", True, "onívoro", "floresta", 1.5);

$nome_animal -> oníparo();


