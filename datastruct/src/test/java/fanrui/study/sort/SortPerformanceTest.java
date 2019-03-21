package fanrui.study.sort;

import junit.framework.Assert;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.omg.PortableInterceptor.SYSTEM_EXCEPTION;

/**
 * 排序测试
 * @author fanrui
 * @time 2019-03-21 15:50:13
 * @see ISort
 * @see BubbleSort
 * @see SelectionSort
 * @see MergeSort
 * @see QuickSort
 */
public class SortPerformanceTest {
    private int arrayCount = 10000;
    private int arrayLength = 500;
    private int[][] array;
    private ISort sort;
    private long startTime;
    private long endTime;

    @Before
    public void before() {
        array = new int[arrayCount][arrayLength];

        for (int i=0; i<arrayCount; i++ ){
            for ( int j = 0; j < arrayLength; j++ ) {
                array[i][j] = (int)(100 * Math.random());
            }
        }

        startTime = System.currentTimeMillis();
    }

    @After
    public void after(){
        endTime = System.currentTimeMillis();
        System.out.println( (endTime - startTime) + "ms" );
    }
	
	@Test
	public void testBubbleSort(){
        sort = new BubbleSort();

        for (int i=0; i<arrayCount; i++ ) {
            sort.sort(array[i]);
        }
	}

	@Test
	public void testInsertSort(){
        // 插入排序性能要比冒泡排序快5倍以上
		sort = new InsertSort();
        for (int i=0; i<arrayCount; i++ ) {
            sort.sort(array[i]);
        }
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
	
	private void validate(int[] array){
		for(int i = 0; i < array.length - 1; i++){
			Assert.assertTrue(array[i] <= array[i + 1]);
		}
	}
}
