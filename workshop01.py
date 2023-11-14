def countWords(sentence):
    mywords = sentence.split()
    totalWords = len(mywords)
    
    uniqueWords = set(mywords)
    totalUnique = len(uniqueWords)
    
    duplicateWords = [word for word in uniqueWords if mywords.count(word) > 1]
    
    print(f'มีคำทั้งหมด {totalWords} คำ')
    print(f"มีคำที่ซ้ำกันรวม {len(duplicateWords)} คำ คือ {' '.join(duplicateWords)}")
    
    for word in duplicateWords:
        count = mywords.count(word)
        print(f'คำว่า {word} ซ้ำกัน {count} ครั้ง')

try:
    inputSentence = input('ป้อน : ')
    countWords(inputSentence)
except Exception as e:
    print(f'เกิดข้อผิดพลาด: {e}')


