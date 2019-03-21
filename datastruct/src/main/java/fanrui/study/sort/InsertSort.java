package fanrui.study.sort;

/**
 * 插入排序实现
 * @author fanrui
 * @time 2019-03-21 15:27:46
 */
public class InsertSort implements ISort {

	public void sort(int[] array) {

		if (array.length <= 1) return;

		for (int i = 1; i < array.length; ++i) {
			int value = array[i];
			int j = i - 1;
			// 查找插入的位置
			for (; j >= 0; --j) {
				if (array[j] > value) {
					array[j+1] = array[j];  // 数据移动
				} else {
					break;
				}
			}
			array[j+1] = value; // 插入数据
		}
	}

}
