def main():
    mensajecifrado=" RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
    diccionario={
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0,
    'K': 0,
    'L': 0,
    'M': 0,
    'N': 0,
    'Ñ': 0,
    'O': 0,
    'P': 0,
    'Q': 0,
    'R': 0,
    'S': 0,
    'T': 0,
    'U': 0,
    'V': 0,
    'W': 0,
    'X': 0,
    'Y': 0,
    'Z': 0,
    'v':0
    }
    for char in mensajecifrado:
         if char in diccionario:
             diccionario[char] += 1 
    print(diccionario)
    mensajedescifrado=mensajecifrado

   
    mensajedescifrado=mensajedescifrado.replace('V','Y') #bien
    mensajedescifrado=mensajedescifrado.replace('v','V') #bien
    mensajedescifrado=mensajedescifrado.replace('Q','B') #puede
    mensajedescifrado=mensajedescifrado.replace('S','Q') #puede
    mensajedescifrado=mensajedescifrado.replace('N','S') #bien
    mensajedescifrado=mensajedescifrado.replace('J','N') #bien
    mensajedescifrado=mensajedescifrado.replace('G','J') #bien
    mensajedescifrado=mensajedescifrado.replace('U','G') #puede
    mensajedescifrado=mensajedescifrado.replace('Z','U')#puede
    mensajedescifrado=mensajedescifrado.replace('L','Z')#puede
    mensajedescifrado=mensajedescifrado.replace('T','L') #bien
    mensajedescifrado=mensajedescifrado.replace('H','T') #bien
    mensajedescifrado=mensajedescifrado.replace('M','H') #puede
    mensajedescifrado=mensajedescifrado.replace('P','M') #bien
    mensajedescifrado=mensajedescifrado.replace('D','P') #puede
    mensajedescifrado=mensajedescifrado.replace('A','D') #bien
    mensajedescifrado=mensajedescifrado.replace('E','A') 
    mensajedescifrado=mensajedescifrado.replace('X','E') #bien
    mensajedescifrado=mensajedescifrado.replace('F','X') #puede
    mensajedescifrado=mensajedescifrado.replace('O','F') 
    mensajedescifrado=mensajedescifrado.replace('I','O') #bien
    mensajedescifrado=mensajedescifrado.replace('C','I') #bien
    mensajedescifrado=mensajedescifrado.replace('R','C') #puede
    mensajedescifrado=mensajedescifrado.replace('K','R') #bien
    
    print(mensajedescifrado)
main()