def topStudents(positive_feedback, negative_feedback, report, student_id, k) :

    def count_student_point(report):
        count = 0
        words = report.split()
        for word in words:
            if word in positive_feedback:
                count += 3
            elif word in negative_feedback:
                count -= 1
        return count
    map = {}
    for i in range(len(student_id)):
        if student_id[i] not in map:
            map[student_id[i]] = count_student_point(report[i])

    sorted_map = sorted(map.items(), key= lambda x:x[1],reverse=True)
    result = [x[0] for x in sorted_map[:k]]
    return result
print(topStudents(["smart","brilliant","studious"],["not"],["this student is not studious","the student is smart"],[1,2],2))