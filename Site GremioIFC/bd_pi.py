from peewee import *

# conexão com o banco de dados do SQLLite
arq = 'cadastro.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

# declaração da classe herdando características da classe BaseModel

class Aluno(BaseModel):
    cod_matricula = IntegerField()
    nome_aluno = CharField()

class Usuario(BaseModel):
    tipo_usuario = CharField()
    nome_usuario = CharField()
    senha = CharField()
    email = CharField()
    cod_matricula = IntegerField()

class Noticia(BaseModel):
    num_noticia = IntegerField()
    titulo = CharField()
    texto_noticia = CharField()
    usuario = CharField()


if __name__ == "__main__":
    db.connect()
    db.create_tables([Aluno, Usuario, Noticia])

    aluno = Aluno.create(cod_matricula = 2017300294, nome_aluno = "GUSTAVO HENRIQUE KISTNER")
    aluno = Aluno.create(cod_matricula = 2019327724, nome_aluno = "ADRIAN VERGILIO FUMAGALI")
    aluno = Aluno.create(cod_matricula = 2019317460, nome_aluno = "ALEXANDRO DEBASTIANI AGUIAR")
    aluno = Aluno.create(cod_matricula = 2019305370, nome_aluno = "ALEX DIETER BLUNCK")
    aluno = Aluno.create(cod_matricula = 2017305568, nome_aluno = "ALINE MIRANDA ZANELLA")
    aluno = Aluno.create(cod_matricula = 2018306695, nome_aluno = "ALINE NILLES BIEGER")
    aluno = Aluno.create(cod_matricula = 2018308869, nome_aluno = "AMANDA HILLESHEIM SALM")
    aluno = Aluno.create(cod_matricula = 2017304749, nome_aluno = "ANA CAROLINA TOZATTI")
    aluno = Aluno.create(cod_matricula = 2018307932, nome_aluno = "ANA JÚLIA LOPES DA SILVEIRA")
    aluno = Aluno.create(cod_matricula = 2017305129, nome_aluno = "ANDRÉ MARCUS DE SOUZA MACHADO")
    aluno = Aluno.create(cod_matricula = 2018306837, nome_aluno = "ANDRESSA LUÍZA RATAJK")
    aluno = Aluno.create(cod_matricula = 2018317590, nome_aluno = "ANE KAROLINE HORONGOSO")
    aluno = Aluno.create(cod_matricula = 2018313081, nome_aluno = "ANTHONY MATHEUS GEBIEN SCHMITT")
    aluno = Aluno.create(cod_matricula = 2019300023, nome_aluno = "ARTUR CIMARDI")
    aluno = Aluno.create(cod_matricula = 2019315607, nome_aluno = "AUGUSTO WALTRICK DA SILVA")
    aluno = Aluno.create(cod_matricula = 2019303992, nome_aluno = "BRAYAN BONATTI")
    aluno = Aluno.create(cod_matricula = 2019306582, nome_aluno = "BRUNO EDUARDO HOLZ")
    aluno = Aluno.create(cod_matricula = 2017300365, nome_aluno = "BRUNO GABRIEL RONCHI")
    aluno = Aluno.create(cod_matricula = 2017307179, nome_aluno = "CAIO GUILHERME MACHADO")
    aluno = Aluno.create(cod_matricula = 2017307849, nome_aluno = "CÁSSIO ANTÔNIO FILIPPI")
    aluno = Aluno.create(cod_matricula = 2019309207, nome_aluno = "DÂMARYS HAMES DE LIMA")
    aluno = Aluno.create(cod_matricula = 2017306799, nome_aluno = "DANIEL CÂNDIDO VIEIRA")
    aluno = Aluno.create(cod_matricula = 2017306028, nome_aluno = "DAYANA DOS SANTOS")
    aluno = Aluno.create(cod_matricula = 2017307393, nome_aluno = "DAYANDRA NICOLE NAHIRNEI")
    aluno_gremio = Aluno.create(cod_matricula = 2018309202, nome_aluno = "DENNER LIAN PRADA RODRIGUES")
    aluno = Aluno.create(cod_matricula = 2017313318, nome_aluno = "DIOGO FISCHER DA SILVA")
    aluno = Aluno.create(cod_matricula = 2019301183, nome_aluno = "DIOVANA LEANDRO DA SILVA")
    aluno = Aluno.create(cod_matricula = 2018303826, nome_aluno = "DOUGLAS RINALDI MONTAGNA")
    aluno = Aluno.create(cod_matricula = 2018307736, nome_aluno = "EDUARDA NEUENFELD")
    aluno = Aluno.create(cod_matricula = 2018320630, nome_aluno = "EDUARDO CRISTOFOLINI SCHNEIDER")
    aluno = Aluno.create(cod_matricula = 2018304538, nome_aluno = "EDUARDO GEHRKE")
    aluno = Aluno.create(cod_matricula = 2017323092, nome_aluno = "EMANUEL DAVID BERTI")
    aluno = Aluno.create(cod_matricula = 2018309347, nome_aluno = "ENZO DE OLIVEIRA CORRÊA")
    aluno = Aluno.create(cod_matricula = 2018306793, nome_aluno = "ERIC CHRISTOFER KRUL")
    aluno = Aluno.create(cod_matricula = 2017323172, nome_aluno = "ERICK RICHARDSON SOUSA MACHADO")
    aluno = Aluno.create(cod_matricula = 2017307034, nome_aluno = "FELIPE KAZUYUKI SHIGIHARA")
    aluno = Aluno.create(cod_matricula = 2018306695, nome_aluno = "FERNANDA OLIVEIRA SAAD")
    aluno = Aluno.create(cod_matricula = 2019302215, nome_aluno = "FLÁVIO KÜHL")
    aluno = Aluno.create(cod_matricula = 2017304604, nome_aluno = "GABRIEL COSTA DE AQUINO")
    aluno = Aluno.create(cod_matricula = 2019304775, nome_aluno = "GABRIEL DIAS CUSTODIO")
    aluno = Aluno.create(cod_matricula = 2019309225, nome_aluno = "GABRIEL FELIPE DUWE")
    aluno = Aluno.create(cod_matricula = 2018307119, nome_aluno = "GABRIEL GIL SOARES")
    aluno = Aluno.create(cod_matricula = 2017306645, nome_aluno = "GABRIEL JUSWIAKI TERNES")
    aluno = Aluno.create(cod_matricula = 2019301728, nome_aluno = "GABRIEL MARQUES")
    aluno = Aluno.create(cod_matricula = 2018306980, nome_aluno = "GABRIEL WENDLAND SEIFERT")
    aluno = Aluno.create(cod_matricula = 2019302494, nome_aluno = "GUILHERME AUGUSTO GOEDE")
    aluno = Aluno.create(cod_matricula = 2018309104, nome_aluno = "GUILHERME CESAR VENDRAMI")
    aluno = Aluno.create(cod_matricula = 2019307051, nome_aluno = "GUILHERME DA SILVEIRA")
    aluno = Aluno.create(cod_matricula = 2019302636, nome_aluno = "GUILHERME EDUARDO OECHSLER")
    aluno = Aluno.create(cod_matricula = 2019309987, nome_aluno = "GUILHERME LETTMANN PENHA")
    aluno = Aluno.create(cod_matricula = 2018304064, nome_aluno = "GUILHERME RAMOS BROLLO")
    aluno = Aluno.create(cod_matricula = 2018300216, nome_aluno = "GUSTAVO JÚLIO HOFFMANN")
    aluno = Aluno.create(cod_matricula = 2018316065, nome_aluno = "GUSTAVO SCHÜTZ WOLLICK")
    aluno = Aluno.create(cod_matricula = 2019303544, nome_aluno = "HALLYFE OBERDAM BOMBASSARO DOS ANJOS")
    aluno = Aluno.create(cod_matricula = 2019303796, nome_aluno = "HARLEY CONRADO SCHUSTER")
    aluno = Aluno.create(cod_matricula = 2017304453, nome_aluno = "HENRIQUE BLAU")
    aluno = Aluno.create(cod_matricula = 2019301236, nome_aluno = "HENRIQUE CUCO")
    aluno = Aluno.create(cod_matricula = 2019320474, nome_aluno = "IGOR AMORIM DE ALMEIDA")
    aluno = Aluno.create(cod_matricula = 2017300712, nome_aluno = "IGOR DE ARAUJO MARQUES")
    aluno = Aluno.create(cod_matricula = 2018302195, nome_aluno = "IGOR UEDA")
    aluno = Aluno.create(cod_matricula = 2018307487, nome_aluno = "JAIR FRANCISCO GARCIA")
    aluno = Aluno.create(cod_matricula = 2018303880, nome_aluno = "JASSIARA RAÍSA SCHMITT")
    aluno = Aluno.create(cod_matricula = 2019301460, nome_aluno = "JOÃO PEDRO DE ARRUDA ROCHA")
    aluno = Aluno.create(cod_matricula = 2019307730, nome_aluno = "JOÃO VÍTOR BECHTOLD")
    aluno = Aluno.create(cod_matricula = 2017305316, nome_aluno = "JOÃO VITOR LAZZAROTTO")
    aluno = Aluno.create(cod_matricula = 2019319910, nome_aluno = "JOÃO VITOR MALINSKI SCHAFER")
    aluno = Aluno.create(cod_matricula = 2018306514, nome_aluno = "JOÃO VITOR PITZ")
    aluno = Aluno.create(cod_matricula = 2019300506, nome_aluno = "JONATHAS AFONSO PISKE")
    aluno = Aluno.create(cod_matricula = 2018306953, nome_aluno = "JOSÉ EDUARDO ROLIM BARON")
    aluno = Aluno.create(cod_matricula = 2019302350, nome_aluno = "JOSÉ VALENTIM RAMPELOTTI")
    aluno = Aluno.create(cod_matricula = 2017305989, nome_aluno = "JOYCE THAYS MOSER")
    aluno = Aluno.create(cod_matricula = 2019314708, nome_aluno = "JULIANA BERTELLI")
    aluno = Aluno.create(cod_matricula = 2018304645, nome_aluno = "JÚLIA NAYARA PEREIRA")
    aluno = Aluno.create(cod_matricula = 2018307360, nome_aluno = "JULIA RAMLOW")
    aluno = Aluno.create(cod_matricula = 2019311045, nome_aluno = "KAIO HARUTA")
    aluno = Aluno.create(cod_matricula = 2018304609, nome_aluno = "KAROLINE SCHNEIDER DO AMARAL")
    aluno = Aluno.create(cod_matricula = 2018306111, nome_aluno = "KAUANE ADRIELLI TABORDA")
    aluno = Aluno.create(cod_matricula = 2019309762, nome_aluno = "KREICA PALOMA KALESKI PRESTES DA ROCHA")
    aluno = Aluno.create(cod_matricula = 2018303746, nome_aluno = "LARA SILVINO SCHNEIDER")
    aluno = Aluno.create(cod_matricula = 2018309150, nome_aluno = "LARISSA CAROLINE CUNHA")
    aluno = Aluno.create(cod_matricula = 2019302716, nome_aluno = "LARISSA WARMELING")
    aluno = Aluno.create(cod_matricula = 2019308059, nome_aluno = "LAURA CILENE ZIMMERMANN DIAS")
    aluno = Aluno.create(cod_matricula = 2017306224, nome_aluno = "LEONARDO AUGUSTO DE SOUZA")
    aluno = Aluno.create(cod_matricula = 2019300257, nome_aluno = "LEONARDO DALOLMO")
    aluno = Aluno.create(cod_matricula = 2018315513, nome_aluno = "LEONARDO MATHEUS EICHELBERGER")
    aluno = Aluno.create(cod_matricula = 2017306082, nome_aluno = "LEONARDO SCHMOELLER MAY")
    aluno = Aluno.create(cod_matricula = 2017301273, nome_aluno = "LEONARDO SIEVES NORT")
    aluno = Aluno.create(cod_matricula = 2018304734, nome_aluno = "LEONARDO YOSHIOKA LOPES DA SILVA")
    aluno = Aluno.create(cod_matricula = 2019310979, nome_aluno = "LUANA WERNER")
    aluno = Aluno.create(cod_matricula = 2018302426, nome_aluno = "LUCAS DANIEL CORDEIRO")
    aluno = Aluno.create(cod_matricula = 2017301540, nome_aluno = "LUCAS GORGES")
    aluno = Aluno.create(cod_matricula = 2019309038, nome_aluno = "LUCAS HEERDT")
    aluno = Aluno.create(cod_matricula = 2018306480, nome_aluno = "LUCAS HENRIQUE FALK")
    aluno = Aluno.create(cod_matricula = 2017311805, nome_aluno = "LUCAS RICARDO MACEDO")
    aluno = Aluno.create(cod_matricula = 2017303465, nome_aluno = "LUCAS TAVEIRA DE SENA")
    aluno = Aluno.create(cod_matricula = 2019315705, nome_aluno = "LUÍS FELIPE CRISTOVÃO")
    aluno = Aluno.create(cod_matricula = 2019304701, nome_aluno = "LUIZA GABRIELA BUSNARDO")
    aluno = Aluno.create(cod_matricula = 2018315818, nome_aluno = "LUIZ FELIPE DOMINGO")
    aluno = Aluno.create(cod_matricula = 2019331020, nome_aluno = "MANOELA BARTH WALTRICK")
    aluno = Aluno.create(cod_matricula = 2019302073, nome_aluno = "MARCELO KASUO SHINIKI FILHO")
    aluno = Aluno.create(cod_matricula = 2018308798, nome_aluno = "MARCOS EDUARDO DOS SANTOS")
    aluno = Aluno.create(cod_matricula = 2018302631, nome_aluno = "MARCUS VINICIUS DE SOUZA")
    aluno = Aluno.create(cod_matricula = 2018302079, nome_aluno = "MARIA EDUARDA GARLINI")
    aluno = Aluno.create(cod_matricula = 2019306760, nome_aluno = "MARIA EDUARDA PEREIRA")
    aluno = Aluno.create(cod_matricula = 2017301872, nome_aluno = "MARINA PEREIRA DUARTE")
    aluno = Aluno.create(cod_matricula = 2018309033, nome_aluno = "MATEUS LEOPOLDO HADLICH")
    aluno = Aluno.create(cod_matricula = 2017303705, nome_aluno = "MATEUS ROLIM BARON")
    aluno = Aluno.create(cod_matricula = 2019327958, nome_aluno = "MATHEUS BISSOLOTI BUENO")
    aluno = Aluno.create(cod_matricula = 2017300150, nome_aluno = "MATHEUS ELIAS DIONISIO")
    aluno = Aluno.create(cod_matricula = 2018313653, nome_aluno = "MATHEUS GABRIEL SOUZA")
    aluno = Aluno.create(cod_matricula = 2019303740, nome_aluno = "MATHEUS GUSTAVO DALCASTAGNE")
    aluno = Aluno.create(cod_matricula = 2017302000, nome_aluno = "MATHEUS MIRANDA")
    aluno = Aluno.create(cod_matricula = 2017306378, nome_aluno = "MILENA ANTUNES VELHO")
    aluno = Aluno.create(cod_matricula = 2018304350, nome_aluno = "MIRÍCIA BAEHR BORGES")
    aluno = Aluno.create(cod_matricula = 2018311990, nome_aluno = "MORGANA RIBEIRO SCHROR")
    aluno = Aluno.create(cod_matricula = 2019309270, nome_aluno = "NATHALIA MORAES DE SOUZA")
    aluno = Aluno.create(cod_matricula = 2018302140, nome_aluno = "NATHALY BEUTING PAZ")
    aluno = Aluno.create(cod_matricula = 2019302251, nome_aluno = "NATHAN GABRIEL FERREIRA GARBI")
    aluno = Aluno.create(cod_matricula = 2017306458, nome_aluno = "OTTO RIMES GRAMKOW")
    aluno = Aluno.create(cod_matricula = 2018300753, nome_aluno = "PÂMELLA SUÊVA GESSNER")
    aluno = Aluno.create(cod_matricula = 2017301676, nome_aluno = "PEDRO HENRIQUE FONTOURA DE SOUZA")
    aluno = Aluno.create(cod_matricula = 2017317442, nome_aluno = "PEDRO MANOEL DUWE BORBA")
    aluno = Aluno.create(cod_matricula = 2017302673, nome_aluno = "PEDRO PAULO AUGUST FRANÇA")
    aluno = Aluno.create(cod_matricula = 2017323109, nome_aluno = "PEDRO PAULO DA CRUZ FRANCO")
    aluno = Aluno.create(cod_matricula = 2017305067, nome_aluno = "PEDRO PEGORINI KLUGE")
    aluno = Aluno.create(cod_matricula = 2019301325, nome_aluno = "PEDRO ROMERO RODRIGUES")
    aluno = Aluno.create(cod_matricula = 2019322951, nome_aluno = "RAFAEL BAIENSE LOPES")
    aluno = Aluno.create(cod_matricula = 2019320080, nome_aluno = "RAFAEL DORN FERNANDES")
    aluno = Aluno.create(cod_matricula = 2019300730, nome_aluno = "RAFAEL GOULART SPIESS")
    aluno = Aluno.create(cod_matricula = 2019300471, nome_aluno = "RAFAEL VOGEL FERNANDES")
    aluno = Aluno.create(cod_matricula = 2017308050, nome_aluno = "RAFAEL ZANCANELLA")
    aluno = Aluno.create(cod_matricula = 2019301049, nome_aluno = "RENAN VIEIRA TORRES")
    aluno = Aluno.create(cod_matricula = 2019308451, nome_aluno = "RITA KAMILE FERREIRA DOMINGES")
    aluno = Aluno.create(cod_matricula = 2017323190, nome_aluno = "ROBSON DA SILVA VIANA JUNIOR")
    aluno = Aluno.create(cod_matricula = 2017307992, nome_aluno = "RODRIGO AUGUSTO SPIESS")
    aluno = Aluno.create(cod_matricula = 2019304292, nome_aluno = "ROGER HENRIQUE MALDANER")
    aluno = Aluno.create(cod_matricula = 2019304550, nome_aluno = "RYAN CARL HOCHLEITNER")
    aluno = Aluno.create(cod_matricula = 2017302922, nome_aluno = "SAMARA TALITA BECKER")
    aluno = Aluno.create(cod_matricula = 2019309539, nome_aluno = "SAMIRA MABILE CIPRIANI")
    aluno = Aluno.create(cod_matricula = 2018312235, nome_aluno = "SAMUEL FELIPE RONCHI")
    aluno = Aluno.create(cod_matricula = 2019301586, nome_aluno = "SAMUEL SEVERO HOSTERT")
    aluno = Aluno.create(cod_matricula = 2018307084, nome_aluno = "SAMUEL WILLIAM DO NASCIMENTO")
    aluno = Aluno.create(cod_matricula = 2017307061, nome_aluno = "SANTHIAGO DEGENHARDT")
    aluno = Aluno.create(cod_matricula = 2019304004, nome_aluno = "SCARLET KLABUNDE GEORG")
    aluno = Aluno.create(cod_matricula = 2017306805, nome_aluno = "SENA HARUTA")
    aluno = Aluno.create(cod_matricula = 2018302266, nome_aluno = "SOFIA ANDRADE BUTZKE")
    aluno = Aluno.create(cod_matricula = 2019306493, nome_aluno = "STEFANIE LASCHEWITZ")
    aluno = Aluno.create(cod_matricula = 2019300480, nome_aluno = "TATIANA PASOLD")
    aluno = Aluno.create(cod_matricula = 2019305852, nome_aluno = "THAÍS SCHLEI")
    aluno = Aluno.create(cod_matricula = 2018316000, nome_aluno = "THAMIRES DE OLIVERA SEVERO")
    aluno = Aluno.create(cod_matricula = 2017305728, nome_aluno = "THIAGO AUGUSTO FLORES")
    aluno = Aluno.create(cod_matricula = 2018305633, nome_aluno = "THIAGO EZEQUIEL DALMORA")
    aluno = Aluno.create(cod_matricula = 2017301792, nome_aluno = "THIAGO GABRIEL LAURETH SCHMIDT")
    aluno = Aluno.create(cod_matricula = 2018314310, nome_aluno = "THIAGO SCHLOSSER")
    aluno = Aluno.create(cod_matricula = 2019302224, nome_aluno = "THIERRI LAURINDO")
    aluno = Aluno.create(cod_matricula = 2017301326, nome_aluno = "THOMAS ROCHI GOMES")
    aluno = Aluno.create(cod_matricula = 2018304879, nome_aluno = "TIAGO JOÃO PRESTES")
    aluno = Aluno.create(cod_matricula = 2018307549, nome_aluno = "TIAGO RAINAN BARÃO")
    aluno = Aluno.create(cod_matricula = 2018304369, nome_aluno = "VICTOR HAYATO ITO")
    aluno = Aluno.create(cod_matricula = 2017307240, nome_aluno = "VICTOR HENRIQUE DAVILA")
    aluno = Aluno.create(cod_matricula = 2018325046, nome_aluno = "VICTOR VINÍCIUS ALVES DA SILVA")
    aluno = Aluno.create(cod_matricula = 2017323181, nome_aluno = "VINICIUS GABRIEL DOS SANTOS")
    aluno = Aluno.create(cod_matricula = 2019304381, nome_aluno = "VINICIUS GABRIEL MACHADO")
    aluno = Aluno.create(cod_matricula = 2019309010, nome_aluno = "VINÍCIUS HEERDT")
    aluno = Aluno.create(cod_matricula = 2018301438, nome_aluno = "VINICIUS LEITE BORTOLON")
    aluno = Aluno.create(cod_matricula = 2017319984, nome_aluno = "VITOR FELIPE GANDA")
    aluno = Aluno.create(cod_matricula = 2017307615, nome_aluno = "VITOR GUSTAVO BEYER")
    aluno = Aluno.create(cod_matricula = 2019316220, nome_aluno = "VÍTOR HENRIQUE CORDEIRO DE SOUZA")
    aluno = Aluno.create(cod_matricula = 2019315410, nome_aluno = "VITÓRIA GABRIELE ARAGÃO")
    aluno = Aluno.create(cod_matricula = 2018315442, nome_aluno = "WANGADNER MAYCOLL DO NASCIMENTO COSTA")
    aluno = Aluno.create(cod_matricula = 2019331370, nome_aluno = "YAN MIQUEIAS DANTAS DE AZEVEDO")
    aluno = Aluno.create(cod_matricula = 2018307351, nome_aluno = "YASMIN JULIA EMMENDOERFER GOMES")
    aluno = Aluno.create(cod_matricula = 2017306897, nome_aluno = "YURI ALVISE WERNER")
    aluno = Aluno.create(cod_matricula = 2018308930, nome_aluno = "YURI GABRIEL LIMA DE SOUZA")
    aluno = Aluno.create(cod_matricula = 2019307418, nome_aluno = "ALEF LUCAS RESENDE FERREIRA")
    aluno = Aluno.create(cod_matricula = 2019301835, nome_aluno = "ALEXANDRE SILVA ZABEL")
    aluno = Aluno.create(cod_matricula = 2017303797, nome_aluno = "ALEXIA TAINÁ LUCINDO DOS SANTOS")
    aluno = Aluno.create(cod_matricula = 2018308063, nome_aluno = "ALISSON REINALDO FLORES")
    aluno = Aluno.create(cod_matricula = 2018313036, nome_aluno = "AMANDA DE OLIVEIRA STRUTZ")
    aluno = Aluno.create(cod_matricula = 2017306322, nome_aluno = "AMANDA DETOFOL CONSTANTE")
    aluno = Aluno.create(cod_matricula = 2019305790, nome_aluno = "ANA CAROLINA SANTOS")
    aluno = Aluno.create(cod_matricula = 2017304346, nome_aluno = "ANA CAROLINE CIPRIANI DOS SANTOS")
    aluno = Aluno.create(cod_matricula = 2017304542, nome_aluno = "ANA JÚLIA CISIELSKI DUARTE")
    aluno = Aluno.create(cod_matricula = 2019309548, nome_aluno = "ANA LAURA DE OLIVEIRA")
    aluno = Aluno.create(cod_matricula = 2014300011, nome_aluno = "ANDRÉ LUIZ FEUZER ALVES CARNEIRO")
    aluno = Aluno.create(cod_matricula = 2018314660, nome_aluno = "ANTHONY DE ZUTTER")
    aluno = Aluno.create(cod_matricula = 2018301133, nome_aluno = "ARTHUR BEZERRA PINOTTI")
    aluno = Aluno.create(cod_matricula = 2018309679, nome_aluno = "ARTHUR FRANCISCO CARUSO")
    aluno = Aluno.create(cod_matricula = 2019306241, nome_aluno = "ARTHUR HENRIQUE DE SÁ SILVA")
    aluno = Aluno.create(cod_matricula = 2019315026, nome_aluno = "ÁVILLA RYAN DA SILVA MOREIRA")
    aluno = Aluno.create(cod_matricula = 2019305422, nome_aluno = "BEATRIZ AMORIM DE OLIVEIRA")
    aluno = Aluno.create(cod_matricula = 2018301779, nome_aluno = "BEATRIZ BAUER")
    aluno = Aluno.create(cod_matricula = 2019322675, nome_aluno = "BEATRIZ ROBERTA BALDI")
    aluno = Aluno.create(cod_matricula = 2019315920, nome_aluno = "BENLOVE ANELUS")
    aluno = Aluno.create(cod_matricula = 2017304408, nome_aluno = "BERNARDO ZONTA LUCKMANN")
    aluno = Aluno.create(cod_matricula = 2019309305, nome_aluno = "BRAIAN WANDALEN")
    aluno = Aluno.create(cod_matricula = 2017302628, nome_aluno = "BRUNA MARCELA LIMA DOS SANTOS")
    aluno = Aluno.create(cod_matricula = 2019331100, nome_aluno = "BRUNO HENRIQUE CUNHA COTA")
    aluno = Aluno.create(cod_matricula = 2018300323, nome_aluno = "CAMILA APARECIDA KÜSTER")
    aluno = Aluno.create(cod_matricula = 2019304256, nome_aluno = "CAMILA ELOISA CLAUDIO")
    aluno = Aluno.create(cod_matricula = 2017304426, nome_aluno = "CAMILA MORETTO DALCANALE")
    aluno = Aluno.create(cod_matricula = 2018304298, nome_aluno = "CAMILA POOL DE LIMA")
    aluno = Aluno.create(cod_matricula = 2018305446, nome_aluno = "CAMILLE BEATRIZ UBER")
    aluno = Aluno.create(cod_matricula = 2017312114, nome_aluno = "CAMILLE VITORIA MESTRE VILACA")
    aluno = Aluno.create(cod_matricula = 2019304640, nome_aluno = "CARLA EDUARDA NOBRE")
    aluno = Aluno.create(cod_matricula = 2019308685, nome_aluno = "CARLOS EDUARDO LANDEIRA RIBEIRO")
    aluno = Aluno.create(cod_matricula = 2019321032, nome_aluno = "CARLOS GREIN DUFFECK SANTOS")
    aluno = Aluno.create(cod_matricula = 2017315878, nome_aluno = "CARLOS HENRIQUE DE MORAIS")
    aluno = Aluno.create(cod_matricula = 2019301530, nome_aluno = "CELIO LUDWIG SLOMP")
    aluno = Aluno.create(cod_matricula = 2017305503, nome_aluno = "CHRISTOPHER ANDREY PISKE")
    aluno = Aluno.create(cod_matricula = 2018304180, nome_aluno = "CRISTINA DE SOUZA E SILVA")
    aluno = Aluno.create(cod_matricula = 2019305164, nome_aluno = "CRISTINA PRIESTER")
    aluno = Aluno.create(cod_matricula = 2019300355, nome_aluno = "DANIEL KRÜGER")
    aluno = Aluno.create(cod_matricula = 2017303732, nome_aluno = "DAVID DAVI MARTINES")
    aluno = Aluno.create(cod_matricula = 2018301581, nome_aluno = "DAVID HILDEBRANDT")
    aluno = Aluno.create(cod_matricula = 2018306828, nome_aluno = "DELIANY STELLA DA SILVA BAUER")
    aluno = Aluno.create(cod_matricula = 2019309083, nome_aluno = "DIEGO DANIEL BORBA")
    aluno = Aluno.create(cod_matricula = 2018313911, nome_aluno = "DIÓGENES HONÓRIO MAÇANEIRO")
    aluno = Aluno.create(cod_matricula = 2019306822, nome_aluno = "DJENIFER KAIANE DE LIMA")
    aluno = Aluno.create(cod_matricula = 2019310576, nome_aluno = "EDUARDA CRISTINA PEREIRA")
    aluno = Aluno.create(cod_matricula = 2019309163, nome_aluno = "EDUARDA SCHMITT")
    aluno = Aluno.create(cod_matricula = 2018304322, nome_aluno = "EDUARDA VALLE")
    aluno = Aluno.create(cod_matricula = 2018302730, nome_aluno = "EDUARDO BRANDT SILVEIRA DA SILVA")
    aluno = Aluno.create(cod_matricula = 2017300249, nome_aluno = "EDUARDO MENEGHIM ALVES SILVA")
    aluno = Aluno.create(cod_matricula = 2019305066, nome_aluno = "ELOISA MARTINS")
    aluno = Aluno.create(cod_matricula = 2017308944, nome_aluno = "EMIZAEL LISBOA RIBAS")
    aluno = Aluno.create(cod_matricula = 2019314440, nome_aluno = "ENOLLA CRISTINE BRESSANIM")
    aluno = Aluno.create(cod_matricula = 2018319782, nome_aluno = "ERICK BENTO DE MORAES")
    aluno = Aluno.create(cod_matricula = 2018307683, nome_aluno = "ERICK JOSÉ HEILER")
    aluno = Aluno.create(cod_matricula = 2016300389, nome_aluno = "FELIPE AUGUSTO FIAMONCINI")
    aluno = Aluno.create(cod_matricula = 2018325073, nome_aluno = "FELIPE ISRAEL SILVA RUNGUE")
    aluno = Aluno.create(cod_matricula = 2019302396, nome_aluno = "FERNANDA BORGES")
    aluno = Aluno.create(cod_matricula = 2018312674, nome_aluno = "GABRIELA RAMOS PEDRO")
    aluno = Aluno.create(cod_matricula = 2017301694, nome_aluno = "GABRIEL EDUARDO GERMANO")
    aluno = Aluno.create(cod_matricula = 2017302430, nome_aluno = "GABRIEL EDUARDO LIMA")
    aluno = Aluno.create(cod_matricula = 2019301100, nome_aluno = "GABRIEL EILERS HIEBERT")
    aluno = Aluno.create(cod_matricula = 2017313443, nome_aluno = "GABRIEL GAHIO LUIZ")
    aluno = Aluno.create(cod_matricula = 2018315630, nome_aluno = "GABRIEL HARMEL")
    aluno = Aluno.create(cod_matricula = 2019310370, nome_aluno = "GABRIEL JOÃO ROSA")
    aluno = Aluno.create(cod_matricula = 2017312179, nome_aluno = "GABRIEL OTÁVIO ZIMMER")
    aluno = Aluno.create(cod_matricula = 2017304963, nome_aluno = "GABRIEL RAMOS DE AMORIM")
    aluno = Aluno.create(cod_matricula = 2017305361, nome_aluno = "GABRIEL ROSA SCHMIDT")
    aluno = Aluno.create(cod_matricula = 2019300990, nome_aluno = "GABRIEL SPECKART")
    aluno = Aluno.create(cod_matricula = 2019309969, nome_aluno = "GABRIEL STREESE BERLANDA")
    aluno = Aluno.create(cod_matricula = 2018316299, nome_aluno = "GABRIEL VINÍCIUS DE OLIVEIRA")
    aluno = Aluno.create(cod_matricula = 2017312740, nome_aluno = "GEÓRGIA BAUMANN BRANDÃO")
    aluno = Aluno.create(cod_matricula = 2019305048, nome_aluno = "GREGORY ANTUNES")
    aluno = Aluno.create(cod_matricula = 2017313372, nome_aluno = "GUILHERME EDUARDO KUGLIN")
    aluno = Aluno.create(cod_matricula = 2018302103, nome_aluno = "GUILHERME GEISLER THEINDL")
    aluno = Aluno.create(cod_matricula = 2017300490, nome_aluno = "GUILHERME PANOSSO")
    aluno = Aluno.create(cod_matricula = 2018312647, nome_aluno = "GUSTAVO ADRIEL MITTELMANN")
    aluno = Aluno.create(cod_matricula = 2018301634, nome_aluno = "GUSTAVO DANIELEVIG PEREIRA DIAS")
    aluno = Aluno.create(cod_matricula = 2019302055, nome_aluno = "GUSTAVO GUERREIRO")
    aluno = Aluno.create(cod_matricula = 2017308434, nome_aluno = "GUSTAVO JOÃO DE SÁ BOSCO")
    aluno = Aluno.create(cod_matricula = 2018312567, nome_aluno = "GUSTAVO LUIZ STAHNKE")
    aluno = Aluno.create(cod_matricula = 2016300398, nome_aluno = "GUSTAVO MARINO HEINZ SCHLEI")
    aluno = Aluno.create(cod_matricula = 2019307534, nome_aluno = "HANNELY THAYS MASKE")
    aluno = Aluno.create(cod_matricula = 2018305179, nome_aluno = "HELENA HELOISA HOFFMANN")
    aluno = Aluno.create(cod_matricula = 2019309824, nome_aluno = "HENRIQUE ARNICHESKI DALPOSSO")
    aluno = Aluno.create(cod_matricula = 2018301760, nome_aluno = "HENRIQUE HEIDERSCHEIDT")
    aluno = Aluno.create(cod_matricula = 2018301957, nome_aluno = "HENRIQUE OLIVEIRA DE LIZ")
    aluno = Aluno.create(cod_matricula = 2019300159, nome_aluno = "HURIAN GUSTAVO ZANATTA")
    aluno = Aluno.create(cod_matricula = 2019304480, nome_aluno = "IGOR ZAFRIEL SCHMIDT")
    aluno = Aluno.create(cod_matricula = 2019315581, nome_aluno = "INGRID DE CAMARGO PACHE DE FARIA")
    aluno = Aluno.create(cod_matricula = 2019305674, nome_aluno = "ISABELLA HENSCHEL")
    aluno = Aluno.create(cod_matricula = 2018316029, nome_aluno = "JACKSON RICARDO RIEBE")
    aluno = Aluno.create(cod_matricula = 2018309866, nome_aluno = "JEAN LOPES PENA")
    aluno = Aluno.create(cod_matricula = 2018300664, nome_aluno = "JENNIFER PIRES")
    aluno = Aluno.create(cod_matricula = 2018306891, nome_aluno = "JHONNATAN GIAN LEVANDOWSKI")
    aluno = Aluno.create(cod_matricula = 2019307169, nome_aluno = "JOÃO CARLOS KRAPP")
    aluno = Aluno.create(cod_matricula = 2019306608, nome_aluno = "JOÃO VITOR DE JESUS CASALI")
    aluno = Aluno.create(cod_matricula = 2019302592, nome_aluno = "JOHANNES WACHHOLZ JOSÉ")
    aluno = Aluno.create(cod_matricula = 2018309472, nome_aluno = "JOSEF MATHAUS BISCHOF")
    aluno = Aluno.create(cod_matricula = 2018305965, nome_aluno = "JÚLIA BALLEN HAERTEL")
    aluno = Aluno.create(cod_matricula = 2018319844, nome_aluno = "JÚLIA BORGES")
    aluno = Aluno.create(cod_matricula = 2018300987, nome_aluno = "JÚLIA DOS SANTOS")
    aluno = Aluno.create(cod_matricula = 2019305496, nome_aluno = "JULIA KATHERINE LADEVIG")
    aluno = Aluno.create(cod_matricula = 2017301710, nome_aluno = "JÚLIA LUIZA FRANÇA")
    aluno = Aluno.create(cod_matricula = 2018314060, nome_aluno = "KALEBE BOGNAR GONÇALVES")
    aluno = Aluno.create(cod_matricula = 2017303142, nome_aluno = "KAMILA ALEXANDRE")
    aluno = Aluno.create(cod_matricula = 2017300632, nome_aluno = "KAUAN CLAUDIO ELIAS")
    aluno = Aluno.create(cod_matricula = 2018300403, nome_aluno = "KAUE REBLIN")
    aluno = Aluno.create(cod_matricula = 2018302417, nome_aluno = "LARYSSA GABRIELA CARVALHO BERNARDO")
    aluno = Aluno.create(cod_matricula = 2018312610, nome_aluno = "LAURA SCHROEDER HAFFENSTEIN")
    aluno = Aluno.create(cod_matricula = 2018300851, nome_aluno = "LAURA ZIMERMAM DE SOUZA")
    aluno = Aluno.create(cod_matricula = 2019310880, nome_aluno = "LEANDRO RAFAEL SPECKORT")
    aluno = Aluno.create(cod_matricula = 2017302190, nome_aluno = "LETICE SILVERIO")
    aluno = Aluno.create(cod_matricula = 2019309673, nome_aluno = "LETICIA PETERS")
    aluno = Aluno.create(cod_matricula = 2017308621, nome_aluno = "LORENZO ZOBOLI")
    aluno = Aluno.create(cod_matricula = 2019304908, nome_aluno = "LUANA CHIODINI")
    aluno = Aluno.create(cod_matricula = 2017307437, nome_aluno = "LUCAS AUGUSTO CARDOSO")
    aluno = Aluno.create(cod_matricula = 2019307220, nome_aluno = "LUCAS EDUARDO CARLINI")
    aluno = Aluno.create(cod_matricula = 2019303590, nome_aluno = "LUCAS SCHWAEMMLE RUARO")
    aluno = Aluno.create(cod_matricula = 2017300991, nome_aluno = "LUCAS VARGAS")
    aluno = Aluno.create(cod_matricula = 2019310235, nome_aluno = "LUCAS VINICIUS MASKE")
    aluno = Aluno.create(cod_matricula = 2018301189, nome_aluno = "LUIZ ANTONIO DA SILVA LOPES")
    aluno = Aluno.create(cod_matricula = 2017305085, nome_aluno = "LUIZ GUSTAVO KLITZKE")
    aluno = Aluno.create(cod_matricula = 2018301803, nome_aluno = "MAB DE ALENCAR FRAGA")
    aluno = Aluno.create(cod_matricula = 2019308836, nome_aluno = "MAISA BORCHARDT")
    aluno = Aluno.create(cod_matricula = 2018304995, nome_aluno = "MANOELA EDUARDA ROEPCKE")
    aluno = Aluno.create(cod_matricula = 2018300889, nome_aluno = "MANUELA HELENA WEIDMANN")
    aluno = Aluno.create(cod_matricula = 2018316350, nome_aluno = "MARCOS JESSÉ DA SILVA CORREA")
    aluno = Aluno.create(cod_matricula = 2019321480, nome_aluno = "MARCOS VINICIOS BORGERT")
    aluno = Aluno.create(cod_matricula = 2019310843, nome_aluno = "MARIA EDUARDA ERBS PEREIRA")
    aluno = Aluno.create(cod_matricula = 2019301844, nome_aluno = "MARIA EDUARDA LEITE SPINDOLA LEÃO")
    aluno = Aluno.create(cod_matricula = 2019316936, nome_aluno = "MARIA EDUARDA MARCOS DE OLIVEIRA")
    aluno = Aluno.create(cod_matricula = 2019328276, nome_aluno = "MARIA FERNANDA SCABURRI DE ALMEIDA")
    aluno = Aluno.create(cod_matricula = 2019320527, nome_aluno = "MARIA LUISA MOGNON")
    aluno = Aluno.create(cod_matricula = 2017301498, nome_aluno = "MARTIN BARALDI LOBE")
    aluno = Aluno.create(cod_matricula = 2018301680, nome_aluno = "MATEUS HENRIQUE MAAS")
    aluno = Aluno.create(cod_matricula = 2018302257, nome_aluno = "MATHEUS BASTOS GABRIEL")
    aluno = Aluno.create(cod_matricula = 2019315465, nome_aluno = "MATHEUS CORREA BARTH")
    aluno = Aluno.create(cod_matricula = 2017307188, nome_aluno = "MATHEUS GABRIEL OGLIARI VENERA")
    aluno = Aluno.create(cod_matricula = 2018301910, nome_aluno = "MATHEUS HENRIQUE TESTONI DOS SANTOS")
    aluno = Aluno.create(cod_matricula = 2017302127, nome_aluno = "MATHEUS JULIANO TEIXEIRA GUAITANELE")
    aluno = Aluno.create(cod_matricula = 2018301410, nome_aluno = "MATHEUS KAUAN SUTIL STOPASSOLA")
    aluno = Aluno.create(cod_matricula = 2019305610, nome_aluno = "MATHEUS OLIVER ROTHENBURG")
    aluno = Aluno.create(cod_matricula = 2019329120, nome_aluno = "MATHEUS PIMENTEL BRACKMANN CARAMURU")
    aluno = Aluno.create(cod_matricula = 2018304654, nome_aluno = "MATHEUS SILVERIO")
    aluno = Aluno.create(cod_matricula = 2017306860, nome_aluno = "MELISSA RADATZ")
    aluno = Aluno.create(cod_matricula = 2019301648, nome_aluno = "MÚCIO BRANDÃO MADUREIRA JÚNIOR")
    aluno = Aluno.create(cod_matricula = 2017303652, nome_aluno = "NAIELLY ROPER CARDOSO")
    aluno = Aluno.create(cod_matricula = 2017312025, nome_aluno = "NATÁLIA SENS WEISE")
    aluno = Aluno.create(cod_matricula = 2017300356, nome_aluno = "DANIEL KRÜGER")
    aluno = Aluno.create(cod_matricula = 2019309029, nome_aluno = "NATALIA VIEIRA COELHO")
    aluno = Aluno.create(cod_matricula = 2017308710, nome_aluno = "NATHALIA LAIS DE SOUZA KANIS")
    aluno = Aluno.create(cod_matricula = 2019300300, nome_aluno = "NICKOLAS GUENTHER")
    aluno = Aluno.create(cod_matricula = 2019310431, nome_aluno = "NICKOLAS LUIZ MALKIEWIEZ BUSARELLO")
    aluno = Aluno.create(cod_matricula = 2019328884, nome_aluno = "NICOLAS ZIMERMANN")
    aluno = Aluno.create(cod_matricula = 2017307464, nome_aluno = "NIKOLAS RUBENS STARKE")
    aluno = Aluno.create(cod_matricula = 2019308184, nome_aluno = "EDUARDA CRISTINA PEREIRA")
    aluno = Aluno.create(cod_matricula = 2017304239, nome_aluno = "PAULO ISMAEL SOUZA FRUTOS")
    aluno = Aluno.create(cod_matricula = 2018305778, nome_aluno = "PAULO RICARDO MACIEL")
    aluno = Aluno.create(cod_matricula = 2019302411, nome_aluno = "PEDRO HENRIQUE DOS SANTOS KUTNI")
    aluno = Aluno.create(cod_matricula = 2018300261, nome_aluno = "PEDRO ROMIG DE LIMA SOUZA")
    aluno = Aluno.create(cod_matricula = 2017300759, nome_aluno = "ELOISA MARTINS")
    aluno = Aluno.create(cod_matricula = 2018304019, nome_aluno = "PEDRO SCHUMANN")
    aluno = Aluno.create(cod_matricula = 2017300131, nome_aluno = "POLIANA ZALASIK")
    aluno = Aluno.create(cod_matricula = 2019302959, nome_aluno = "PRISCILA LEMKE")
    aluno = Aluno.create(cod_matricula = 2017319910, nome_aluno = "RAFAEL DAVINO MALON")
    aluno = Aluno.create(cod_matricula = 2018300790, nome_aluno = "RAÍSSA GUIMARÃES")
    aluno = Aluno.create(cod_matricula = 2018325073, nome_aluno = "RAVI BOHMANN TRIDAPALLI")
    aluno = Aluno.create(cod_matricula = 2019305576, nome_aluno = "RAYSSA TIFANY DE MOURA CASTILHOS")
    aluno = Aluno.create(cod_matricula = 2017300875, nome_aluno = "RENAN MIRANDA ZANELLA")
    aluno = Aluno.create(cod_matricula = 2018301367, nome_aluno = "RICHARD ROBERT DIAS CUSTODIO")
    aluno = Aluno.create(cod_matricula = 2019315812, nome_aluno = "SABRINA MARA RODRIGUES")
    aluno = Aluno.create(cod_matricula = 2018301170, nome_aluno = "SAMUEL PACHECO FERREIRA")
    aluno = Aluno.create(cod_matricula = 2019300032, nome_aluno = "SANDY HOFFMANN")
    aluno = Aluno.create(cod_matricula = 2016302294, nome_aluno = "SHAIANE KRAUS")
    aluno = Aluno.create(cod_matricula = 2018304743, nome_aluno = "SOFIA KATHERINE CIMARDI")
    aluno = Aluno.create(cod_matricula = 2018315890, nome_aluno = "STEFAN NOVASKY")
    aluno = Aluno.create(cod_matricula = 2019326370, nome_aluno = "TEODORO FREIBERGER")
    aluno = Aluno.create(cod_matricula = 2015300132, nome_aluno = "THAIS LETICIA JUNKES")
    aluno = Aluno.create(cod_matricula = 2017303634, nome_aluno = "THIAGO ALEXSANDER LUIZ")
    aluno = Aluno.create(cod_matricula = 2017300884, nome_aluno = "THIAGO VINICIUS DE OLIVEIRA HORNBURG")
    aluno = Aluno.create(cod_matricula = 2017304373, nome_aluno = "TIAGO STASAITIS")
    aluno = Aluno.create(cod_matricula = 2018301527, nome_aluno = "TIMÓTEO RAFAEL JANZEN")
    aluno = Aluno.create(cod_matricula = 2017301012, nome_aluno = "VANESSA DE SOUZA")
    aluno = Aluno.create(cod_matricula = 2019301414, nome_aluno = "VANESSA REGINA DA SILVA")
    aluno = Aluno.create(cod_matricula = 2017305405, nome_aluno = "VINÍCIUS BOING")
    aluno = Aluno.create(cod_matricula = 2018314786, nome_aluno = "VINICIUS DA SILVA")
    aluno = Aluno.create(cod_matricula = 2017307277, nome_aluno = "VINÍCIUS FELDHAUS GOBETTI")
    aluno = Aluno.create(cod_matricula = 2017300955, nome_aluno = "VINICIUS FISCHER")
    aluno = Aluno.create(cod_matricula = 2017305577, nome_aluno = "VINICIUS FRANKE DA SILVA")
    aluno = Aluno.create(cod_matricula = 2017300300, nome_aluno = "VINICIUS HEDLER")
    aluno = Aluno.create(cod_matricula = 2018300350, nome_aluno = "VINÍCIUS MANUEL MARTINS")
    aluno = Aluno.create(cod_matricula = 2019300758, nome_aluno = "VÍTOR AUGUSTO UENO OTTO")
    aluno = Aluno.create(cod_matricula = 2017308882, nome_aluno = "VÍTOR GUSTAVO HORNBURG")
    aluno = Aluno.create(cod_matricula = 2018315353, nome_aluno = "WAGNER HENRIQUE BORGES TORRIANI")
    aluno = Aluno.create(cod_matricula = 2018304986, nome_aluno = "WILLIAM MATEUS DE NOVAIS")
    aluno = Aluno.create(cod_matricula = 2018315694, nome_aluno = "YASMIN JANDRE PISKE")
 
    usuario_gremio = Usuario.create(tipo_usuario = "1", nome_usuario = "GrêmioIFCBlumenau", senha = "gremio123", email = "gremioifcblumenau@gmail.com", cod_matricula = 2018309202)
    n1 = Noticia.create(num_noticia = 1, titulo = "Teste", texto_noticia = "anderson <3", usuario = usuario_gremio.nome_usuario)

def listar_alunos():
    lista_a = Aluno.select()
    return lista_a

def listar_usuarios_nome():
    lista_u = Usuario.select()
    lista_nome_u = []
    for nome_u in lista_u:
        lista_nome_u.append(nome_u.nome_usuario)
    return lista_nome_u

def listar_usuarios_senha():
    lista_u = Usuario.select()
    lista_senha_u = []
    for senha_u in lista_u:
        lista_senha_u.append(senha_u.senha)
    return lista_senha_u

def listar_noticia():
    lista_noticia = Noticia.select()
    return lista_noticia

def listar_noticia_tit():
    lista_n = Noticia.select()
    lista_tit = []
    for titulo_n in lista_n:
        lista_tit.append(titulo_n.titulo)
    return lista_tit

def listar_noticia_text():
    lista_n = Noticia.select()
    lista_text = []
    for text in lista_n:
        lista_text.append(text.texto_noticia)
    return lista_text

def listar_noticia_autor():
    lista_n = Noticia.select()
    lista_autor = []
    for autor in lista_n:
        lista_autor.append(autor.usuario)
    return lista_autor

def inserir_usuario(tipo, nome, senha, email, novo_usuario):
    db.connect()
    usuario = Usuario.create(tipo_usuario = tipo, nome_usuario = nome, senha = senha, email = email, cod_matricula = novo_usuario)
    return True

def inserir_noticia(tit, text_not, autor):
    db.connect()
    noticia = Noticia.create(num_noticia = (len(listar_noticia()) + 1), titulo = tit, texto_noticia = text_not, usuario = autor)
    return True