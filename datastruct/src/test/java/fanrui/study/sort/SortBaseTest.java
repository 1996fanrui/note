package fanrui.study.sort;

import junit.framework.Assert;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

/**
 * 排序测试
 * @author fanrui
 * @time 2019-03-21 15:17:25
 * @see ISort
 * @see BubbleSort
 * @see SelectionSort
 * @see MergeSort
 * @see QuickSort
 */
public class SortBaseTest {
	int[] array = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	ISort sort;

    @Before
    public void before(){
        int[] arrayIni = {10, 9, 8, 7, 6, 5, 4, 4, 1, -1};
        for(int i = 0; i < array.length; i++){
            array[i] = arrayIni[i];
        }
    }
	
	@Test
	public void testBubbleSort(){
		sort = new BubbleSort();
		sort.sort(array);
		printArray(array);
		validate();
	}

	@Test
	public void testInsertSort(){
		sort = new InsertSort();
		sort.sort(array);
		printArray(array);
		validate();
	}


//	@Test
//	public void testSelectionSort(){
//		sort = new SelectionSort();
//		sort.sort(array);
//		validate();
//	}
//
//	@Test
//	public void testMergeSort(){
//		sort = new MergeSort();
//		sort.sort(array);
//		validate();
//
//	}
//
//	@Test
//	public void testQuickSort(){
//		sort = new QuickSort();
//		sort.sort(array);
//		validate();
//	}
//	@Test
//	public void testInsertOptimizeSort(){
//		sort = new InsertOptimizeSort();
//		sort.sort(array);
//		validate();
//	}

	private void printArray(int[] printArray){
        System.out.print("[");
        for (int a:printArray){
			System.out.print(a + ",");
		}
        System.out.println("]");
	}
	
	private void validate(){
		for(int i = 0; i < array.length - 1; i++){
			Assert.assertTrue(array[i] <= array[i + 1]);
		}
	}
}
